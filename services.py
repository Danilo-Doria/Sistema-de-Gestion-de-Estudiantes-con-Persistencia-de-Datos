def add_students(students):
    """
    Add student to the students list.

    Verify if an student id exists, if exists displays a message, if not then request id, name,
    age, course and state.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student.

    Returns:
        None: If the student id exists.
        None: If the student id doesn't exists, add student's data to the students list.
    """
    # Variable to verify the conditions and exit or retry the cycle
    valid = False
    
    while not valid:
        try:
            student_id = int(input("\nEnter the student's ID: "))
            if student_id < 0:
                print("\nPlease enter only positive numbers")
            else:
                valid = True
        except ValueError:
            print("\nPlease enter only numbers")
    
    for student in students:
        if student_id == student['id']:
            print("\nThis ID already exists!!")
            return None

    name = input("\nEnter the student's name: ").strip().lower()

    # Variable to verify the conditions and exit or retry the cycle
    valid = False

    while not valid:
        try:
            age = int(input("\nEnter the student's age: "))
            if age < 0:
                print("\nPlease enter only positive numbers")
            else:
                valid = True
        except ValueError:
            print("\nPlease enter only numbers")

    course = input("\nEnter the student's course name: ").strip().lower()

    # Variable to verify the conditions and exit or retry the cycle
    valid = False

    while not valid:
        state = input("\nEnter the student's current state (active or inactive): ").strip().lower()
        if state == "active" or state == "inactive":
            valid = True
        else:
            print("\nPlease enter (active or inactive)")
      
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "state": state
    }

    students.append(student)
    print(f"\nThe student {name} | id: {student_id} | Age: {age} | Course: {course} | State: {state} has been register successfully!!")
    return None


def consult_list_students(students):
    """
    Consults the students list.

    Verify if there students, if not displays a message, if there are then display the students.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student.

    Returns:
        None: If there no students.
        None: If there students, then display all of them.
    """
    
    if not students:
        print("\nThe list of students is empty!!")
        return None

    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']} | State: {student['state']}")
    return None


def search_student(students):
    """
    Search a student in the students list.

    Verify if the student id exist in the list and display the student data, if not exists displays a message.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student.

    Returns:
        None: If the student doesn't exists.
        None: If the student exist, then display the data of the student.
    """

    if not students:
        print("\nThe list of students is empty!!")
        return None
    
    # Variable to verify the conditions and exit or retry the cycle
    valid = False

    while not valid:
        try:
            student_id = int(input("\nEnter the student's ID: "))
            if student_id < 0:
                print("\nPlease enter only positive numbers")
            else:
                valid = True
        except ValueError:
            print("\nPlease enter only numbers")

    for student in students:
        if student_id == student['id']:
            print(f"\nStudent data -> ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']} | State: {student['state']}")
            return None
    else:
        print(f"\nThe ID {student_id} of the student doesn't exists")
    return None


def update_student_data(students):
    """
    Update the data of the student.

    Verify if the student id exist in the list and request the data again, if not exists displays a message.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student.

    Returns:
        None: If the student doesn't exists.
        None: If the student exist, then display the old data and the new data after the update.
    """

    if not students:
        print("\nThe list of students is empty!!")
        return None
    
    # Variable to verify the conditions and exit or retry the cycle
    valid = False
    while not valid:
        try:
            student_id = int(input("\nEnter the student's ID: "))
            if student_id < 0:
                print("\nPlease enter only positive numbers")
            else:
                valid = True
        except ValueError:
            print("\nPlease enter only numbers")

    for student in students:
        if student_id == student['id']:
            print(f"\nCurrent student data -> ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']} | State: {student['state']}")
            
            name = input("\nEnter the student's name: ").strip().lower()

            # Variable to verify the conditions and exit or retry the cycle
            valid = False

            while not valid:
                try:
                    age = int(input("\nEnter the student's age: "))
                    if age < 0:
                        print("\nPlease enter only positive numbers")
                    else:
                        valid = True
                except ValueError:
                    print("\nPlease enter only numbers")

            course = input("\nEnter the student's course name: ").strip().lower()

            # Variable to verify the conditions and exit or retry the cycle
            valid = False

            while not valid:
                state = input("\nEnter the student's current state (active or inactive): ").strip().lower()
                if state == "active" or state == "inactive":
                    valid = True
                else:
                    print("\nPlease enter (active or inactive)")

            student['name'] = name
            student['age'] = age
            student['course'] = course
            student['state'] = state

            print(f"\nNew student data -> ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']} | State: {student['state']}")
            return None
    else:
        print(f"\nThe ID {student_id} of the student doesn't exists")
    return None


def delete_student(students):
    """
    Delete a student in the students list.

    Verify if the student id exist in the list and remove all the student data, if not exists displays a message.

    Parameters:
        students (list[dict]): List of dictionaries, where each dictionary is a student.

    Returns:
        None: If the student doesn't exists.
        None: If the student exist, then remove the data of the student.
    """

    if not students:
        print("\nThe list of students is empty!!")
        return None
    
    # Variable to verify the conditions and exit or retry the cycle
    valid = False

    while not valid:
        try:
            student_id = int(input("\nEnter the student's ID: "))
            if student_id < 0:
                print("\nPlease enter only positive numbers")
            else:
                valid = True
        except ValueError:
            print("\nPlease enter only numbers")

    for student in students:
        if student_id == student['id']:
            students.remove(student)
            print("\nStudent deteled successfully!!")
            return None
    else:
        print(f"\nThe ID {student_id} of the student doesn't exists")
    return None