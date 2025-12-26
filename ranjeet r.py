import pandas as pd
import matplotlib.pyplot as plt
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
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())
df["Utilization_Percentage"] = (df["Allocated_Students"] / df["Room_Capacity"]) * 100
print(df[["Room_No", "Utilization_Percentage"]])
overcrowded = df[df["Allocated_Students"] > df["Room_Capacity"]]
underutilized = df[df["Utilization_Percentage"] < 70]

print("\nUnderutilized Rooms:")
print(underutilized[["Room_No", "Utilization_Percentage"]])
block_count = df.groupby("Hostel_Block")["Allocated_Students"].sum()

plt.figure()
block_count.plot(kind="bar")
plt.title("Students Distribution by Hostel Block")
plt.xlabel("Hostel Block")
plt.ylabel("Number of Students")
plt.show()
plt.figure()
plt.bar(df["Room_No"], df["Utilization_Percentage"])
plt.axhline(100, linestyle='--')
plt.title("Room Utilization Percentage")
plt.xlabel("Room Number")
plt.ylabel("Utilization (%)")
plt.show()
