import csv

def save_csv(students, path="data/students_list.csv", include_header=True):
    """
    Save the list students in a CSV file, if the file already exist overwrite it.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student. (in memory).
        path: Path of the CSV file where the data will be saved, default: "students_list.csv".
        include_header: Boolean for the title data, default: True.

    Returns:
        None: If the data was saved correctly.
        None: If there were errors saving the file.
    """

    try:
        with open(path, "w", newline="", encoding="utf-8") as file:

            fieldnames = ["id", "name", "age", "course", "state"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if include_header:
                writer.writeheader()
            writer.writerows(students)
            print(f"\nStudents list saved in: {path}")
            return None
    except PermissionError:
        print("\nError you don't have writing permission")
        return None
    

def load_csv(students, path="data/students_list.csv"):
    """
    Load the list students from a CSV file, if there students with the same id only upload the id from CSV
    deleting the data from memory's terminal.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student. (in memory).
        path: Path of the CSV file where the data will be uploaded, default: "students_list.csv".

    Returns:
        None: If the data was uploaded correctly.
        List[]: If there were errors uploading the file.
    """

    new_list_students = []
    # Error counter
    error = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            header = ["id", "name", "age", "course", "state"]
            reader = csv.DictReader(file)

            if reader.fieldnames != header:
                print("\nInvalid titles, must be: 'id', 'name', 'age', 'course', 'state'")
                return []

            print(f"\nStudents list load from: {path}")

            for row in reader:
                if len(row) != 5 or None in row.values():
                    print(f"\nInvalid row, the quantity of columns are incorrect: {row}")
                    error += 1
                    continue
                try:
                    student_id = int(row["id"])
                    age = int(row["age"])
                    state = row["state"]

                    if student_id < 0 or age < 0:
                        print(f"\nInvalid row, negative values in the row: {row}")
                        error += 1
                        continue
                    if state != "active" and state != "inactive":
                        print(f"\nInvalid row, the state must be 'active' or 'inactive': {row}")
                        error += 1
                        continue
                except ValueError:
                    print(f"\nInvalid row, no numeric values: {row}")
                    error += 1
                    continue
               
                student = {
                    "id": student_id,
                    "name": row['name'],
                    "age": age,
                    "course": row['course'],
                    "state": row['state']
                }
                        
                new_list_students.append(student)

                for new_student in new_list_students:
                    for student_list_memory in students:
                        if new_student['id'] == student_list_memory['id']:
                            students.remove(student_list_memory)
                        
            students.extend(new_list_students)
            
            if students:
                if error > 0:
                    print(f"\n{error} Invalid rows omitted")
                    print("\nStudents list load successfully!!")
                else:
                    print("\nNo found invalid rows")
                    print("\nStudents list load successfully!!")
            return None

    except FileNotFoundError:
        print("\nError couldn't load due the file doesn't exist")
        return []

    except PermissionError:
        print("\nError you don't have permission to write in this loacation")
        return []

    except UnicodeDecodeError:
        print("\nError codification problem in the loading")
        return []