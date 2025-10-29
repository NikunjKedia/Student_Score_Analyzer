import pandas as pd
# We'll use print("-" * 50) for seperation in output for better readability.
print("-" * 50)

# Importing the CSV file.
df = pd.read_csv("Student_data.csv")

# EDA (Exploratory Data Analysis)
print("1. EDA (Exploratory Data Analysis):")
print(df.head())
print("-" * 50)
print(df.tail())
print("-" * 50)

# Per-student average marks
def average_marks():
    print("2. AVERAGE MARKS:")
    subject_columns = df.columns[1:]
    df["Average"] = df[subject_columns].mean(axis=1)
    print(df.head())
    print("-" * 50)
average_marks()

# Grade Assigning
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 55:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)
print("3. GRADE ASSIGNMENT:")
print(df.head())
print("-" * 50)

# Subject-wise Analysis
subject_cols = df.columns[1:-2]
print("4. SUBJECT-WISE STATISTICS:")
for i in subject_cols:
    mean = df[i].mean().round()
    maximum = df[i].max()
    minimum = df[i].min()
    std_dev = df[i].std().round()
    median = df[i].median()
    print(f"{i}: Mean = {mean} | Max = {maximum} | Min = {minimum} | Standard Deviation = {std_dev} | Median = {median}")
print("-" * 50) 

# Top scorers for each subject
print("5. TOP SCORERS IN EACH SUBJECT:")
for i in subject_cols:
    max_score = df[i].max()
    toppers = df.loc[df[i] == max_score, "Name"].tolist()
    print(f"{i}: Top Score = {max_score}, Topper(s) = {", ".join(toppers)}")
print("-" * 50) 

# Overall top performers (based on grades = A)
print("6. OVERALL TOP PERFORMERS:")
top_performers = df[df["Grade"] == "A"]
print(top_performers[["Name", "Average", "Grade"]])
print("-" * 50)

# Exporting summary
print(df)
df[['Name', 'Average', 'Grade']].to_csv('results_summary.csv', index=False)
print("-" * 50) 