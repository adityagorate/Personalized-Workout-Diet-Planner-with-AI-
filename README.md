# 🏋️ Personalized-Workout-Diet-Planner-with-AI

An intelligent Flask-based AI Fitness Planner that calculates BMI, estimates daily calorie needs, recommends meals using Machine Learning, and generates a personalized weekly workout plan.

---

## 🚀 Features

- BMI Calculation
- BMR & Daily Calorie Estimation
- Goal-based Calorie Adjustment (Weight Loss / Muscle Gain / Maintain)
- ML-Based Meal Recommendation (KNN Algorithm)
- Protein Comparison Chart (Matplotlib)
- Weekly Workout Plan Generator
- Modern Glassmorphism UI (Bootstrap 5)

---

## 🧠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Scikit-learn (Nearest Neighbors)
- Bootstrap 5
- HTML & CSS

---

## 📂 Project Structure

```text
AI-Fitness-Planner/
│
├── app.py
├── meals.csv
├── static/
│   └── chart.png (automatically get created)
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```
---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/adityagorate/Personalized-Workout-Diet-Planner-with-AI- 

cd ai-fitness-planner

2️⃣ Create Virtual Environment (Recommended)

3️⃣ Install Dependencies

pip install flask pandas numpy matplotlib scikit-learn

4️⃣ Run the Application

python app.py

Open browser and visit:

http://127.0.0.1:5000/

---

## 📊 How It Works

Step 1: User Input

- Age
- Weight
- Height (feet.inches format e.g., 5.8)
- Gender
- Fitness Goal
- Meal Preference

Step 2: Health Calculations

- BMI Calculation
- BMR Calculation
- Activity Multiplier Applied
- Goal-based Calorie Adjustment

Step 3: ML Meal Recommendation

- Uses K-Nearest Neighbors
- Filters based on diet preference
- Recommends meals closest to target calories & protein

Step 4: Visualization

- Protein comparison bar chart generated using Matplotlib

Step 5: Workout Plan

- Goal-based weekly workout routine generated

---

## Demo Screanshorts

<img width="597" height="558" alt="Image" src="https://github.com/user-attachments/assets/0acff8aa-f990-4869-bedf-f9288baee756" />

<img width="891" height="605" alt="Image" src="https://github.com/user-attachments/assets/e1bc2108-8adf-4237-8846-933a412ddd87" />

<img width="897" height="307" alt="Image" src="https://github.com/user-attachments/assets/73c2bce9-a7ce-44a0-8f3e-52ace297cdeb" />


