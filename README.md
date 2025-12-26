# 📌 **Project Title:**

## *College Hostel Room Allocation Analysis using Pandas*

---

### **1. Project Objective**

To analyze hostel room allotment data for students using Pandas and visualize meaningful insights such as room distribution, hostel capacity usage, gender-wise allocation, branch-wise allocation, year-wise allocation, vacant/filled room status, etc.

---

### **2. Real-World Dataset (Sample)**

Save as **hostel_data.csv**

```csv
Student_ID,Name,Gender,Branch,Year,Hostel_Name,Room_No,Bed_No,Room_Type,Mess_Opted,Fees_Paid
101,Rahul Verma,Male,CSE,2,Hostel-A,101,1,Double,Yes,45000
102,Neha Sharma,Female,IT,1,Hostel-B,203,2,Double,No,38000
103,Aman Gupta,Male,ME,3,Hostel-A,102,1,Single,Yes,50000
104,Pooja Yadav,Female,EE,2,Hostel-B,204,1,Double,Yes,42000
105,Ravi Kumar,Male,CSE,4,Hostel-C,301,2,Double,No,35000
106,Simran Kaur,Female,CSE,1,Hostel-B,205,1,Single,Yes,52000
107,Arjun Singh,Male,IT,3,Hostel-A,103,2,Double,Yes,41000
108,Kritika Mishra,Female,ME,2,Hostel-B,206,2,Double,No,36000
109,Rishi Raj,Male,EE,1,Hostel-C,302,1,Single,Yes,54000
110,Anjali Jain,Female,CSE,3,Hostel-B,207,2,Double,Yes,43000
```

---

### **3. Python Project Code**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("hostel_data.csv")

# Display first rows
print("Dataset Preview:\n", df.head())

# Basic Info
print("\nData Summary:")
print(df.describe(include='all'))

# 1. Gender-wise room allocation
gender_count = df['Gender'].value_counts()
print("\nGender-wise Allocation:\n", gender_count)

gender_count.plot(kind='bar')
plt.title("Gender-wise Hostel Room Allocation")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.show()

# 2. Hostel-wise room allocation
hostel_count = df['Hostel_Name'].value_counts()
print("\nHostel-wise Allocation:\n", hostel_count)

hostel_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Hostel-wise Student Distribution")
plt.ylabel("")
plt.show()

# 3. Branch-wise Analysis
branch_count = df['Branch'].value_counts()
print("\nBranch-wise Allocation:\n", branch_count)

branch_count.plot(kind='bar')
plt.title("Branch-wise Hostel Allocation")
plt.xlabel("Branch")
plt.ylabel("No. of Students")
plt.show()

# 4. Year-wise Distribution
year_count = df['Year'].value_counts()
print("\nYear-wise Room Allocation:\n", year_count)

year_count.plot(kind='bar')
plt.title("Year-wise Student Distribution")
plt.xlabel("Year")
plt.ylabel("Students Count")
plt.show()

# 5. Fee Analysis
print("\nFee Analysis:")
print("Total Fees Collected:", df['Fees_Paid'].sum())
print("Average Fee Paid:", df['Fees_Paid'].mean())

# Mess opted count
mess_count = df["Mess_Opted"].value_counts()
mess_count.plot(kind="bar")
plt.title("Mess Opted Distribution")
plt.xlabel("Mess Opted (Yes/No)")
plt.ylabel("Count")
plt.show()
```

---

### **4. Output Insights (Discussion for Report)**

| Metric                | Result   |
| --------------------- | -------- |
| Total Students        | 10       |
| Highest Fee Paid      | ₹54000   |
| Most allocated Hostel | Hostel-B |
| Popular Branch        | CSE      |
| Mess Opted Majority   | Yes      |

---

### **5. Conclusion**

This project analyzed student hostel allocation patterns using Pandas.
From the dataset:

* Hostel-B has the highest occupancy.
* CSE students are the most in count.
* Mess service is opted by most students.
* Fee distribution varies among room type & year.

Such analysis helps management optimize hostel space, track capacity, manage mess planning, and improve accommodation facilities.

---
END PROJECT
