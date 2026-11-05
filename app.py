from flask import Flask, render_template, request, session, redirect, url_for
import os
import joblib
import numpy as np
import mysql.connector

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Load the trained ML model
model = joblib.load("student_performance_model.pkl")


# -----------------------------
# MySQL Database Connection
# -----------------------------

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="student_performance"
    )
    return connection


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# -----------------------------
# Logout
# -----------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# -----------------------------
# Prediction History
# -----------------------------

@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM predictions WHERE user_id = %s ORDER BY created_at DESC",
        (session["user_id"],)
    )

    predictions = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "history.html",
        predictions=predictions
    )


# -----------------------------
# Prediction Page
# -----------------------------

@app.route("/predict-page")
def predict_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")


# -----------------------------
# Registration
# -----------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )

            connection.commit()

            message = "Registration successful! You can now login."

        except mysql.connector.IntegrityError:

            message = "Email already registered."

        finally:

            cursor.close()
            connection.close()

        return render_template(
            "register.html",
            message=message
        )

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            session["user_id"] = user["id"]
            session["username"] = user["name"]

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "login.html",
                message="Invalid email or password."
            )

    return render_template("login.html")


# -----------------------------
# Machine Learning Prediction
# -----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    if "user_id" not in session:
        return redirect(url_for("login"))

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    assignment_score = float(request.form["assignment_score"])
    midterm_score = float(request.form["midterm_score"])
    sleep_hours = float(request.form["sleep_hours"])

    # Prepare input for ML model
    features = np.array([[
        study_hours,
        attendance,
        assignment_score,
        midterm_score,
        sleep_hours
    ]])

    # Make prediction
    prediction = model.predict(features)

    predicted_score = round(float(prediction[0]), 2)

    # Save prediction to MySQL
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (user_id, study_hours, attendance, assignment_score,
         midterm_score, sleep_hours, predicted_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            session["user_id"],
            study_hours,
            attendance,
            assignment_score,
            midterm_score,
            sleep_hours,
            predicted_score
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        prediction=predicted_score
    )


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)



