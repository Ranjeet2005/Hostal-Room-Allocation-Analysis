# 📊 College Hostel Room Allocation Analysis

*Difficulty:* Easy
*Tools:* Python, Pandas, Matplotlib
*Concept:* Exploratory Data Analysis (EDA)

---

## 🎯 Project Objective

The objective of this project is to analyze *college hostel room allocation efficiency* based on:

* Student year
* Room capacity
* Room occupancy
* Hostel blocks

Using EDA, we identify:

* Overcrowded rooms
* Underutilized rooms
* Allocation patterns

---

## 📁 Dataset Description (Real-life Based)

| Column Name        | Description                  |
| ------------------ | ---------------------------- |
| Student_ID         | Unique student number        |
| Year               | Year of study (1st–4th)      |
| Hostel_Block       | Block name (A, B, C)         |
| Room_No            | Room number                  |
| Room_Capacity      | Max students allowed         |
| Allocated_Students | Students currently allocated |

---

## 🧪 Python Code (EDA Project)

### 🔹 Step 1: Import Libraries

python
import pandas as pd
import matplotlib.pyplot as plt


---

### 🔹 Step 2: Create Realistic Hostel Dataset

python
data = {
    "Student_ID": range(101, 121),
    "Year": ["1st", "2nd", "3rd", "4th", "1st", "2nd", "3rd", "4th",
             "1st", "2nd", "3rd", "4th", "1st", "2nd", "3rd", "4th",
             "1st", "2nd", "3rd", "4th"],
    "Hostel_Block": ["A", "A", "A", "A", "B", "B", "B", "B",
                     "C", "C", "C", "C", "A", "A", "B", "B",
                     "C", "C", "A", "B"],
    "Room_No": [101,102,103,104,201,202,203,204,
                301,302,303,304,105,106,205,206,
                305,306,107,207],
    "Room_Capacity": [3,3,3,3,4,4,4,4,3,3,3,3,3,3,4,4,3,3,3,4],
    "Allocated_Students": [3,2,3,1,4,3,2,4,3,3,2,1,3,2,4,3,2,1,3,4]
}

df = pd.DataFrame(data)
print(df.head())


---

### 🔹 Step 3: Basic EDA

python
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


---

### 🔹 Step 4: Room Utilization Calculation

python
df["Utilization_Percentage"] = (df["Allocated_Students"] / df["Room_Capacity"]) * 100
print(df[["Room_No", "Utilization_Percentage"]])


---

### 🔹 Step 5: Identify Overcrowded & Underutilized Rooms

python
overcrowded = df[df["Allocated_Students"] > df["Room_Capacity"]]
underutilized = df[df["Utilization_Percentage"] < 70]

print("\nUnderutilized Rooms:")
print(underutilized[["Room_No", "Utilization_Percentage"]])


---

### 🔹 Step 6: Visualization – Students per Hostel Block

python
block_count = df.groupby("Hostel_Block")["Allocated_Students"].sum()

plt.figure()
block_count.plot(kind="bar")
plt.title("Students Distribution by Hostel Block")
plt.xlabel("Hostel Block")
plt.ylabel("Number of Students")
plt.show()


---

### 🔹 Step 7: Room Utilization Bar Chart

python
plt.figure()
plt.bar(df["Room_No"], df["Utilization_Percentage"])
plt.axhline(100, linestyle='--')
plt.title("Room Utilization Percentage")
plt.xlabel("Room Number")
plt.ylabel("Utilization (%)")
plt.show()


---

## 📈 Results & Insights

* Some rooms are *underutilized (<70%)*
* Block *B* has highest student load
* Allocation is *not evenly distributed*
* Reallocation can reduce congestion

---

## ✅ Conclusion

This EDA project successfully analyzes *hostel room allocation efficiency* using Pandas and Matplotlib.
The analysis helps hostel administration optimize room usage and improve student accommodation planning.

---
