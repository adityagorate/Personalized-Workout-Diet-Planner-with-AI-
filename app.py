from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import os

app = Flask(__name__)

# Load dataset
data = pd.read_csv("meals.csv")

# ---------------- HEIGHT CONVERSION ----------------

def convert_height_to_cm(height_input):
    parts = height_input.split(".")
    feet = int(parts[0])
    inches = int(parts[1]) if len(parts) > 1 else 0
    total_inches = (feet * 12) + inches
    cm = total_inches * 2.54
    return cm

# ---------------- BMI ----------------

def calculate_bmi(weight, height_input):
    height_cm = convert_height_to_cm(height_input)
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

# ---------------- BMR ----------------

def calculate_bmr(gender, weight, height_cm, age):
    if gender == "male":
        return 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height_cm - 5 * age - 161

def adjust_calories(calories, goal):
    if goal == "weight_loss":
        return calories - 400
    elif goal == "muscle_gain":
        return calories + 400
    return calories

# ---------------- ML Meal Recommendation ----------------

def recommend_meals(target_calories, preference):

    if preference == "veg":
        filtered = data[data['type'] == "veg"]

    elif preference == "nonveg":
        filtered = data[data['type'] == "nonveg"]

    else:
        veg_items = data[data['type'] == "veg"].sample(2)
        nonveg_items = data[data['type'] == "nonveg"].sample(2)
        filtered = pd.concat([veg_items, nonveg_items])

    model = NearestNeighbors(n_neighbors=min(3, len(filtered)))
    X = filtered[['calories', 'protein']]
    model.fit(X)

    target = np.array([[target_calories/4, 25]])
    distances, indices = model.kneighbors(target)

    return filtered.iloc[indices[0]]

# ---------------- WORKOUT PLAN ----------------

def generate_workout(goal):

    if goal == "weight_loss":
        return {
            "Monday": "30 min Cardio + Abs",
            "Tuesday": "Full Body HIIT",
            "Wednesday": "Cycling / Running",
            "Thursday": "Upper Body Strength",
            "Friday": "Lower Body + Core",
            "Saturday": "Yoga / Stretching",
            "Sunday": "Rest"
        }

    elif goal == "muscle_gain":
        return {
            "Monday": "Chest + Triceps",
            "Tuesday": "Back + Biceps",
            "Wednesday": "Legs",
            "Thursday": "Shoulders",
            "Friday": "Core + Abs",
            "Saturday": "Light Cardio",
            "Sunday": "Rest"
        }

    else:
        return {
            "Monday": "Full Body Workout",
            "Tuesday": "Light Cardio",
            "Wednesday": "Upper Body",
            "Thursday": "Lower Body",
            "Friday": "Core",
            "Saturday": "Outdoor Activity",
            "Sunday": "Rest"
        }

# ---------------- ROUTE ----------------

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height_input = request.form["height"]
        gender = request.form["gender"]
        goal = request.form["goal"]
        preference = request.form["preference"]

        bmi = calculate_bmi(weight, height_input)

        height_cm = convert_height_to_cm(height_input)
        bmr = calculate_bmr(gender, weight, height_cm, age)

        base_calories = round(bmr * 1.3)
        target_calories = adjust_calories(base_calories, goal)

        meals = recommend_meals(target_calories, preference)
        workout_plan = generate_workout(goal)

        # -------- FIXED CHART GENERATION --------
        plt.figure()
        plt.bar(meals['name'], meals['protein'])
        plt.xlabel("Meals")
        plt.ylabel("Protein (g)")
        plt.title("Protein Comparison")
        plt.xticks(rotation=30)
        plt.tight_layout()

        if os.path.exists("static/chart.png"):
            os.remove("static/chart.png")

        plt.savefig("static/chart.png")
        plt.close()

        return render_template("result.html",
                               bmi=bmi,
                               calories=target_calories,
                               meals=meals,
                               workout=workout_plan)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)