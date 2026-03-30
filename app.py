import students
import services
import files

print("\n Bienvenidos al Sistema de Gestión de Estudiantes")

option = 0

# Cycle while repeat the menu undefined until the user enters 8
while option != 8:
    print("\n1. Register new students")
    print("2. Consult list of students")
    print("3. Search student")
    print("4. Update data of a student")
    print("5. Delete student")
    print("6. Save in CSV file")
    print("7. Load from CSV file")
    print("8. Exit")

    # Using try/except to validate the inputs of the user
    try:
        # Variable 'option' chooses the option of the user
        option = int(input("\nEnter the option that you want: "))

        # Conditional that validate if the input is between (1-8)
        if option not in range(1, 9):
            print("\nPlease only enter a valid option")
            continue
    except ValueError:
        print("\nPlease only enter numbers")
        continue

    if option == 1:
        # Call the function 'add_students' from 'services.py' file, and pass list from 'students.py' file as an argument
        services.add_students(students.students)
    elif option == 2:
        # Call the function 'consult_list_students' from 'services.py' file, and pass list from 'students.py' file as an argument
        services.consult_list_students(students.students)
    elif option == 3:
        # Call the function 'search_student' from 'services.py' file, and pass list from 'students.py' file as an argument
        services.search_student(students.students)
    elif option == 4:
        # Call the function 'update_student_data' from 'services.py' file, and pass list from 'students.py' file as an argument
        services.update_student_data(students.students)
    elif option == 5:
        # Call the function 'delete_student' from 'services.py' file, and pass list from 'students.py' file as an argument
        services.delete_student(students.students)
    elif option == 6:
        # Call the function 'save_csv' from 'services.py' file, and pass list from 'students.py' file as an argument
        files.save_csv(students.students)
    elif option == 7:
        # Call the function 'load_csv' from 'services.py' file, and pass list from 'students.py' file as an argument
        files.load_csv(students.students)
    # If the user option is 8 the exit from cycle and terminate the program
    else:
        print("\nExiting...")