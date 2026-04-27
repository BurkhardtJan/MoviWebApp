# 🎬 MoviWebApp

MoviWeb is a full-stack web application designed to help users manage and curate their personal movie collections. This project was developed as part of the MSIT Masterschool program.

## 🚀 Features
* **User Profiles:** Manage multiple user accounts, each with their own movie library.
* **Movie Management:** Add, update, and delete movies.
* **API Enrichment:** Automatically fetches posters, release years, and directors using the **OMDb API**.
* **Dynamic Feedback:** Integrated Flask Flash messaging system for real-time user notifications.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BurkhardtJan/MoviWebApp.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory and add your OMDB-Key and a secret string for flask:
   ```text
   API_KEY=your_omdb_key_here
   FLASK_SECRET_KEY=your_secure_random_string
   ```

4. **Run the application:**
   ```bash
   python3 app.py
   ```

## 🗄️ Database & Security
* **Storage:** Uses **SQLite** with **SQLAlchemy ORM**.
* **Structure:** The database file is stored within the `/data` directory.
* **Security:** Sensitive keys and API credentials are managed via environment variables and `python-dotenv`.

## 🌐 Deployment
This application is deployed and accessible at:
[https://JanB.pythonanywhere.com](https://JanB.pythonanywhere.com)
