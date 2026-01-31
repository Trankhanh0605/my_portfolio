# Django Personal Portfolio Project

This project is a personal portfolio website built using **Django (Python)** and **Bootstrap**. It allows for dynamic content management (adding projects, achievements, and profile info) via the Django Admin panel without editing HTML code.

---

## 1. Project Structure & File Explanations

In Django's **MVT (Model-View-Template)** architecture, each file has a specific role. Here is how the files in the `cv` app interact:

### 📂 The Data Layer (Database & Management)
* **`models.py` (The Architect):**
    * **Function:** Defines the structure of the database. Each class represents a table in the database.
    * **In this project:** We created models like `HoSo` (Profile), `DuAn` (Project), and `ThanhTich` (Achievement).
* **`admin.py` (The Manager):**
    * **Function:** Registers the models with the Django Admin interface.
    * **Purpose:** Allows you to add, edit, or delete data (text, images) via a graphical interface (`/admin`) instead of using SQL commands.
* **`apps.py`:** Configuration file for the app itself (usually left as default).

### 📂 The Logic & Routing Layer
* **`views.py` (The Chef/Logic):**
    * **Function:** Handles the logic. It receives a request, fetches the necessary data from the Database (using Models), bundles it into a context, and sends it to the Template.
    * **Example:** The `home()` function fetches `HoSo.objects.first()` and sends it to `home.html`.
* **`urls.py` (The Receptionist/Map):**
    * **Function:** Defines the URL paths. It decides which function in `views.py` runs based on the web address the user types.
    * **Note:**
        * `my_portfolio/urls.py`: The main entry point (routes traffic to apps).
        * `cv/urls.py`: Specific routes for the portfolio app (e.g., Homepage, Project Detail).

### 📂 The Presentation Layer (Frontend)
* **`templates/cv/home.html`:**
    * **Function:** The HTML skeleton of the website. It uses **Django Template Language (DTL)** (e.g., `{{ variable }}`, `{% for %}`) to display dynamic data passed from the View.
* **`static/cv/`:**
    * **Function:** Stores static files that do not change based on database data, such as CSS (styling), JS (animations), and default assets (background images).

---

## 2. Development Workflow (Step-by-Step)

This is the order in which the project was built to ensure all components link together correctly.

### Step 1: Initialization
1.  Created a Virtual Environment (`venv`) to isolate dependencies.
2.  Installed Django (`pip install django pillow`).
3.  Created Project and App (`startproject`, `startapp cv`).
4.  **Crucial:** Registered `'cv'` in the `INSTALLED_APPS` list within `settings.py`.

### Step 2: Backend & Database (The Foundation)
1.  **Define Models:** Wrote classes in `models.py` to define what data to save.
2.  **Migrations:**
    * `python manage.py makemigrations` (Created the blueprint).
    * `python manage.py migrate` (Built the actual tables in the database).
3.  **Admin Setup:** Registered models in `admin.py`.
4.  **Data Entry:** Created a Superuser, logged into Admin, and added real data (Profile info, Projects, Awards).

### Step 3: Logic & Routing (The Brain)
1.  **Views:** Wrote the `home` function in `views.py` to query data (`objects.all()`) and pass it to the template via `context`.
2.  **URLs:** Connected the empty path `''` to the `home` view in `cv/urls.py`, and included `cv.urls` in the main `my_portfolio/urls.py`.

### Step 4: Frontend Integration (The Face)
1.  **Static Files:** Moved Bootstrap CSS/JS/Images into `static/cv/`.
2.  **Templates:**
    * Copied the Bootstrap HTML file to `templates/cv/`.
    * Added `{% load static %}`.
    * Updated CSS/JS links using the `{% static '...' %}` tag.
    * Replaced hardcoded text (e.g., "Clarence Taylor") with dynamic variables (e.g., `{{ nguoi_dung.ten_hien_thi }}`).

---

## 3. Data Flow Cycle

When a user visits the website, the data travels in this specific loop:

1.  **User:** Visits `http://127.0.0.1:8000/`.
2.  **URL Dispatcher (`urls.py`):** Sees the request matches the home path and calls `views.home`.
3.  **View (`views.py`):**
    * Asks **Models** (`models.py`) for data.
    * **Models** query the **Database**.
    * **Database** returns the data (e.g., your name, projects).
4.  **View:** Sends this data + the HTML file (`home.html`) to the browser.
5.  **Template:** The HTML renders the data using `{{ }}` tags and loads styles from `static`.
6.  **User:** Sees the final Portfolio website.

---

## 4. How to Run This Project locally

If you need to restart the server or move to a new computer:

1.  **Activate Virtual Environment:**
    * Windows: `venv\Scripts\activate`
    * Mac/Linux: `source venv/bin/activate`
2.  **Install Dependencies (if moving to new PC):**
    * `pip install django pillow`
3.  **Run Server:**
    * `python manage.py runserver`
4.  **Access:**
    * Website: `http://127.0.0.1:8000/`
    * Admin: `http://127.0.0.1:8000/admin/`