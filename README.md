## 📖 Table of Contents
1. [About The Project](#-about-the-project)
2. [Key Features](#-key-features)
3. [Tech Stack](#-tech-stack)
4. [Project Structure](#-project-structure)
5. [Installation & Setup](#-installation--setup)
6. [Contributing](#-contributing)
7. [Contact](#-contact)

---

## 🧐 About The Project

This project is a dynamic and fully functional Blog Application designed to provide users with a seamless platform to read, write, and manage blog posts. Built with a focus on clean code and architecture, it features a robust backend system developed using Python and Django, paired with an interactive and fully responsive frontend user interface.

---

## ✨ Key Features

* **User Management System:** Complete authentication workflow including user registration, secure login/logout, and profile management.
* **Blog Post Operations:** Full CRUD capabilities for managing articles, organizing content, and displaying posts dynamically.
* **Modular Infrastructure:** Built using independent Django apps (`users`, `blog`, `home`) to ensure high scalability and easy maintenance.
* **Responsive UI Design:** Clean layout tailored with CSS and JavaScript to ensure perfect display across mobile devices, tablets, and desktops.

---

## 🛠️ Tech Stack

* **Backend:** [Python](https://python.org) & [Django Framework](https://djangoproject.com)
* **Database:** SQLite3 (Default development database)
* **Frontend:** HTML5, CSS3, JavaScript

---

## 📂 Project Structure

The project follows standard Django architectural patterns, divided into modular components:
* `blog/` - Handles the models, views, and core logic for articles and blog posts.
* `users/` - Manages user profiles, custom user data, and authentication permissions.
* `home/` - Contains the logic and components for the main landing page.
* `static/` & `templates/` - Stores global frontend design files (CSS/JS) and HTML layouts.

---

## 🚀 Installation & Setup

Follow these steps to set up a local development copy of the project on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Mohsen-Sleman/Blog_App_Using_Django
cd Blog_App_Using_Django
```

### 2. Set Up a Virtual Environment
* **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Make sure you have your virtual environment active, then run:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Panel Access)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
Once the server starts, open your browser and navigate to: `http://127.0.0`

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📬 Contact

* **GitHub Profile:** [@Mohsen-Sleman](https://github.com)
* **Project Link:** [https://github.com/Blog_App_Using_Django](https://github.com/Blog_App_Using_Django)
