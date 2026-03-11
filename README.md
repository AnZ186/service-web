# 🚀 Django Project

Halo!  
Ini adalah project web yang dibuat menggunakan **Django**. Project ini dibuat untuk belajar, eksperimen, dan mengembangkan aplikasi backend menggunakan Python.

Struktur project dibuat sederhana supaya mudah dipahami dan gampang dikembangkan lagi ke depannya.

---

## ✨ Fitur

- Backend menggunakan **Django**
- Struktur project rapi dan modular
- Mendukung **database migration**
- Tersedia **Django Admin Panel**
- Mudah dijalankan di environment lokal

---

## 🧰 Teknologi yang Digunakan

| Teknologi | Keterangan |
|---|---|
| Python | Bahasa pemrograman utama |
| Django | Web framework backend |
| SQLite | Database default Django |

---

## ⚙️ Cara Menjalankan Project

Ikuti langkah berikut untuk menjalankan project di komputer kamu.

### 1. Clone repository

```bash
git clone https://github.com/anz186/service-web.git
cd nama-repository
```

---

### 2. Buat Virtual Environment

```bash
python -m venv venv
```

Aktifkan environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

---

### 4. Setup Database

Jalankan migration supaya database terbentuk.

```bash
python manage.py makemigrations
python manage.py migrate
```

Kalau ingin mengakses **admin panel**, buat akun admin:

```bash
python manage.py createsuperuser
```

---

### 5. Jalankan Server

```bash
python manage.py runserver
```

Buka di browser:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## 📁 Struktur Project

```
project/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── apps/
```


## 📌 Rencana Pengembangan

Beberapa hal yang mungkin akan ditambahkan ke depannya:

- [ ] Sistem autentikasi user
- [ ] API endpoint
- [ ] Integrasi frontend
- [ ] Deployment ke server / cloud

---

## 📜 Lisensi

Project ini bersifat **open-source** dan bebas digunakan untuk belajar maupun pengembangan lebih lanjut.

---

⭐ Kalau project ini membantu atau menarik buat kamu, jangan lupa kasih **star di repository** ya.