from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "123"   # Required for session


# ----------- Create DB & Table if not exists -----------
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ----------- Home route (login page) -----------
@app.route("/")
def home():
    return render_template("login.html")


# ----------- Login -----------
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        session["username"] = username
        return redirect("/profile")
    else:
        return "Invalid username or password"


# ----------- Signup page -----------
@app.route("/signup")
def signup_page():
    return render_template("signup.html")


# ----------- Signup logic -----------
@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect("/")
    except:
        conn.close()
        return "Username already exists!"


# ----------- Profile page -----------
@app.route("/profile")
def profile():
    if "username" in session:
        return render_template("profile.html", username=session["username"])
    else:
        return redirect("/")


# ----------- Logout -----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
