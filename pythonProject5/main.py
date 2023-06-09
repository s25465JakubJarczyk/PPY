import smtplib



def load_students_data():
    students_data = {}
    with open('students.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            email, first_name, last_name, points = data[0], data[1], data[2], int(data[3])
            grade, status = None, ''
            if len(data) > 4:
                grade, status = float(data[4]), data[5]
            students_data[email] = {'first_name': first_name, 'last_name': last_name,
                                    'points': points, 'grade': grade, 'status': status}
    return students_data



def save_students_data(students_data):
    with open('students.txt', 'w') as file:
        for email, data in students_data.items():
            line = f"{email},{data['first_name']},{data['last_name']},{data['points']}"
            if data['grade'] is not None:
                line += f",{data['grade']},{data['status']}"
            file.write(f"{line}\n")



def assign_grades(students_data):
    for email, data in students_data.items():
        if data['status'] not in ['GRADED', 'MAILED'] and data['grade'] is None:
            if data['points'] <= 50:
                data['grade'] = 2
            elif data['points'] <= 60:
                data['grade'] = 3
            elif data['points'] <= 70:
                data['grade'] = 3.5
            elif data['points'] <= 80:
                data['grade'] = 4
            elif data['points'] <= 90:
                data['grade'] = 4.5
            else:
                data['grade'] = 5
            data['status'] = 'GRADED'
    save_students_data(students_data)



def delete_student(students_data, email):
    if email in students_data:
        del students_data[email]
        save_students_data(students_data)
        print(f"Student with email {email} has been deleted.")
    else:
        print(f"Student with email {email} not found.")



def add_student(students_data, email, first_name, last_name, points):
    if email in students_data:
        print("Student with this email already exists.")
    else:
        students_data[email] = {'first_name': first_name, 'last_name': last_name,
                                'points': points, 'grade': None, 'status': ''}
        save_students_data(students_data)
        print("New student added.")



def send_emails(students_data):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'  # tutaj wpisz swój adres email
    sender_password = 'your_password'  # tutaj wpisz swoje hasło do konta email

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        for email, data in students_data.items():
            if data['status'] == 'GRADED' and data['grade'] is not None:
                subject = "Ocena z przedmiotu Podstawy Programowania Python"
                body = f"Cześć {data['first_name']},\nTwoja ocena z przedmiotu Podstawy Programowania Python wynosi {data['grade']}."
                message = f"Subject: {subject}\n\n{body}"
                smtp.sendmail(sender_email, email, message.encode('utf-8'))
                data['status'] = 'MAILED'
            save_students_data(students_data)
            print("Emails sent.")


            while True:
                print("Select an action:")
                print("1. Assign grades automatically")
                print("2. Delete a student")
                print("3. Add a student")
                print("4. Send emails")
                print("5. Quit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    assign_grades(students_data)
                elif choice == '2':
                    email = input("Enter email of the student you want to delete: ")
                    delete_student(students_data, email)
                elif choice == '3':
                    email = input("Enter email of the new student: ")
                    first_name = input("Enter first name of the new student: ")
                    last_name = input("Enter last name of the new student: ")
                    points = int(input("Enter points of the new student: "))
                    add_student(students_data, email, first_name, last_name, points)
                elif choice == '4':
                    send_emails(students_data)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice.")



      




