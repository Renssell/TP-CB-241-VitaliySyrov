import csv
from student import Student

class FileUtils:

    @staticmethod
    def load_csv(filename: str, student_list):
        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student = Student(
                        row["name"],
                        row["phone"],
                        row["age"],
                        row["group"]
                    )
                    student_list.students.append(student)
        except FileNotFoundError:
            pass

    @staticmethod
    def save_csv(filename, student_list):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "age", "group"])
            writer.writeheader()
            for s in student_list.students:
                writer.writerow(s.to_dict())
