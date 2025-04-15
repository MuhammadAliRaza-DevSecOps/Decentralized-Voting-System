# 🗳️ Decentralized Voting System using Blockchain & Django

A secure, transparent, and modern online voting platform built with Django and integrated Blockchain technology to ensure trust, integrity, and auditability in democratic processes.

![Banner](https://raw.githubusercontent.com/MuhammadAliRaza-DevSecOps/Decentralized-Voting-System/main/static/img/banner.png) <!-- (Replace with actual path if available) -->

---

## 🔐 Features

- ✅ **User Authentication** (Register/Login/Logout)
- 🗳️ **Voting System** with one-vote-per-user rule
- 🔗 **Blockchain Integration** for immutable vote storage
- 📜 **Vote Receipts** with Block Hash & QR Code
- 📊 **Live Voting Results** with auto-updating Chart.js graphs
- 🌙 **Dark Mode** toggle support
- 📁 **Downloadable Vote Receipt (PDF)**
- 🧾 **Vote History (My Receipts)**
- 🔍 **Blockchain Explorer** to review each vote block
- ⏳ **Voting Deadline Countdown**
- 📉 **Admin Dashboard (Planned)**
- 📱 **Mobile Responsive Layout**
- 🔒 **Auto Logout after Inactivity**
- 🧬 **Face/Fingerprint Authentication (Optional/Future)**

---

## 💡 How it Works

1. **User registers and logs in.**
2. **Eligible users vote once for their preferred candidate.**
3. **Each vote is hashed and stored in a new block on a custom blockchain.**
4. **User receives a cryptographically signed vote receipt with a QR code.**
5. **Vote counts update live via a Chart.js graph every 5 seconds.**
6. **Users can view past receipts and inspect the blockchain for transparency.**

---

## 🛠️ Tech Stack

- 🐍 **Python 3.13**
- 🌐 **Django 5.1**
- 📦 **SQLite** (can be upgraded to PostgreSQL/MySQL)
- 🔗 **Custom Blockchain Implementation**
- 🧾 **xhtml2pdf** (PDF generation)
- 📊 **Chart.js** (Live vote visualization)
- 🎨 **Tailwind CSS + Dark Mode**
- 📸 **qrcode** (for encrypted vote receipt QR)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/MuhammadAliRaza-DevSecOps/Decentralized-Voting-System.git
cd Decentralized-Voting-System

2. Install Dependencies
pip install -r requirements.txt

3. Run Migration
python manage.py makemigrations
python manage.py migrate

4. Run the Development Server
python manage.py runserver
Visit: http://127.0.0.1:8000/

🧠 Future Enhancements
🔐 Fingerprint / Face Recognition Login

🗳️ QR Code-based Voting

📊 Admin Analytics Dashboard

🧾 Encrypted Blockchain Audit Logs

📲 Android / iOS App

📡 Voting API for Government Use

📫 Contact

Ali Raza
📧 infoman55.it@gmail.com
🌐 GitHub

📝 License
This project is licensed under the MIT License. Feel free to use and modify with credit.

“Building transparent and tamper-proof elections for the digital age.” — Ali Raza


---

Would you like me to generate a `requirements.txt` and `.gitignore` too?

