import json
import os

DATA_FILE = "data.json"

def _load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

students = _load_data()

def add_student(name, score):
    students.append({"name": name, "score": score})
    _save_data(students)
    print(f"已添加学生：{name}，成绩：{score}")

def show_all_students():
    if not students:
        print("暂无学生信息。")
        return
    print("\n当前学生列表：")
    for i, stu in enumerate(students, 1):
        print(f"{i}. 姓名：{stu['name']}，成绩：{stu['score']}")

def calculate_average():
    if not students:
        return 0
    total = sum(stu["score"] for stu in students)
    return total / len(students)
