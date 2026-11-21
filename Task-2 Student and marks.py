"'build a student performance system totals, toppers, percentage, grades, rank list using reusable function with error handling for invalid marks and missing data in python"'

def validate_marks(marks, subjects):
    if not marks:
        raise ValueError("Missing marks")
    cleaned = {}
    for sub in subjects:
        if sub not in marks or marks[sub] is None or marks[sub] == "":
            raise ValueError(f"Missing marks for {sub}")
        try:
            m = float(marks[sub])
        except:
            raise ValueError(f"Invalid marks for {sub}")
        if m < 0 or m > 100:
            raise ValueError(f"Invalid marks for {sub}: {m}")
        cleaned[sub] = m
    return cleaned

def calculate_total(marks):
    return sum(marks.values())

def calculate_percentage(total, n):
    return round(total / n, 2)

def get_grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B+"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "F"

def process_student(student, subjects):
    try:
        name = student.get("name")
        if not name:
            raise ValueError("Missing name")
        marks = validate_marks(student.get("marks"), subjects)
        total = calculate_total(marks)
        percentage = calculate_percentage(total, len(subjects))
        grade = get_grade(percentage)
        return {"name": name, "total": total, "percentage": percentage, "grade": grade, "status": "Pass" if grade != "F" else "Fail"}
    except ValueError as e:
        return {"name": student.get("name", "Unknown"), "error": str(e)}

def get_rank_list(results):
    valid = [r for r in results if "error" not in r]
    valid = sorted(valid, key=lambda x: (-x["total"], x["name"]))
    rank = 1
    for i, r in enumerate(valid):
        if i > 0 and r["total"] < valid[i-1]["total"]:
            rank = i + 1
        r["rank"] = rank
    return valid

def get_toppers(rank_list, top_n=3):
    return rank_list[:top_n]

subjects = ["Tamil", "English", "Maths", "Science", "Social"]

students = [
    {"name": "Arun", "marks": {"Tamil": 92, "English": 88, "Maths": 95, "Science": 90, "Social": 85}},
    {"name": "Priya", "marks": {"Tamil": 98, "English": 95, "Maths": 99, "Science": 97, "Social": 96}},
    {"name": "Kumar", "marks": {"Tamil": 45, "English": 50, "Maths": 120, "Science": 40, "Social": 55}},
    {"name": "Divya", "marks": {"Tamil": 78, "English": 82, "Maths": 75, "Science": None, "Social": 80}},
    {"name": "Ravi", "marks": {"Tamil": 70, "English": 65, "Maths": 72, "Science": 68, "Social": 71}},
]

results = [process_student(s, subjects) for s in students]
rank_list = get_rank_list(results)

print("RANK LIST")
for r in rank_list:
    print(r["rank"], r["name"], r["total"], r["percentage"], r["grade"], r["status"])

print("\nTOPPERS")
for r in get_toppers(rank_list):
    print(r["rank"], r["name"], r["total"])

print("\nERRORS")
for r in results:
    if "error" in r:
        print(r["name"], ":", r["error"])