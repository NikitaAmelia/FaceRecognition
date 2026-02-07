import cv2
import random
import time

animal_spirits = [
    "Kucing Sok Cool Padahal Laper",
    "Koala Pemalas Banget Tapi Baik",
    "Kodok Overthinking Jam 3 Pagi",
    "Anjing Terlalu Setia Sampai Lupa Diri",
    "Panda Rebahan Profesional",
    "Kelinci Panikan Level Tinggi",
    "Rubah Licik Tapi Hatinya Lembut",
    "Kura-kura Santai Anti Drama",
    "Burung Julid Pengamat Sekitar",
    "Ikan Cupang Gampang Tersinggung",
    "Bebek Ngeyel Tapi Ngangenin",
    "Kambing Random Tidak Bisa Diprediksi",
    "Ayam Panik Padahal Aman",
    "Ubur-ubur No Thoughts Head Empty",
    "Sloth Deadline Melekat",
    "Singa Percaya Diri Tanpa Alasan",
    "Kucing Liar Tapi Sensitif",
    "Burung Hantu Sok Bijak",
    "Capybara Paling Santai Sedunia",
    "Kucing Oren Energi Berlebihan"
]


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# timer
CHANGE_INTERVAL = 3  # detik
last_change = time.time()
current_spirit = random.choice(animal_spirits)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 🔁 GANTI ANIMAL SPIRIT TIAP 3 DETIK
    if time.time() - last_change >= CHANGE_INTERVAL:
        current_spirit = random.choice(animal_spirits)
        last_change = time.time()

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            current_spirit,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Animal Spirit Detector 🐾", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
