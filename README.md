# Expiration Control System

A Django-based system designed to manage and control the expiration dates of registered products.
It allows users to perform full **CRUD operations** (Create, Read, Update, Delete) on product expiration records, ensuring proper monitoring and reducing risks of expired items in inventory.

---

## 🚀 Features

* 📌 Register products with expiration dates
* 📋 View and list expiration records
* ✏️ Update expiration dates
* ❌ Delete expired or unnecessary records
* 🔔 Keep track of product validity efficiently

---

## 🛠️ Technologies Used

* **Backend:** Django 4+ (Python 3.10+)
* **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
* **Frontend:** Django Templates / HTML / CSS / JS

---

## ⚙️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/expiration-control-system.git
   cd expiration-control-system
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   * Admin panel: `http://127.0.0.1:8000/admin`
   * Main app: `http://127.0.0.1:8000/`

---

## ✅ Usage

* Log in with the superuser account to manage products.
* Register products and their expiration dates.
* Use the interface to edit, view, or delete records.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute it.

