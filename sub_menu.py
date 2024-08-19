#!/usr/bin/env python
# coding: utf-8

# In[11]:




# In[6]:


import csv
from tabulate import tabulate

def query_1(records, student_id):
    for row in records:
        if row['ID'] == student_id:
            return {
                'Sex': row['Sex'],
                'Age': row['Age'],
                'Family_relative': row['Family_relative'],
                'State': row['State'],
                'Race': row['Race']
            }
    return None

def query_2(records, race):
    result = []
    for student in records:
        if student['Race'] == race:
            student_info = {
                'Sex': student['Sex'],
                'School_support': student['School_support'],
                'Access_internet': student['Access_internet'],
                'Attendance_rate': student['Attendance_rate'],
                'Parental_involvement': student['Parental_involvement']
            }
            result.append(student_info)
    return result

def query_3(records, parental_involvement):
    result = []
    for student in records:
        try:
            absences = int(student['Absences'])
            if absences < 50 and student['Parental_involvement'] == parental_involvement:
                result.append({
                    "ID": student['ID'],
                    "Free_Time": student['Free_Time'],
                    "Math_Score": student['Math_Score'],
                    "Reading_Score": student['Reading_Score'],
                    "Writing_Score": student['Writing_Score'],
                    "Parental_Involvement": student['Parental_involvement']
                })
        except ValueError:
            continue  # Skip rows with non-integer absences
    return result

def query_4(records, student_age):
    result = []
    for student in records:
        try:
            age = int(student['Age'])
            if age == student_age:
                result.append({
                    'ID': student['ID'],
                    'Family_size': student['Family_size'],
                    'Traveltime': student['Traveltime'],
                    'Health': student['Health']
                })
        except ValueError:
            continue  # Skip rows with non-integer age
    return result

def display_sub_menu(csv_file):
    records = []
    try:
        with open(csv_file, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            records = [line for line in csv_reader]
        print(f"Successfully loaded {len(records)} records from {csv_file}.")

        while True:
            print("Select an option:")
            print("1. Retrieve the sex, age, number of relatives in family, state, and race based on the ID.")
            print("2. Retrieve the sex, school support, access internet, attendance rate, and parental involvement associated with a specific race.")
            print("3. Retrieve the ID, free time, math score, reading score, and writing score of students whose absences are less than 50, based on parental involvement.")
            print("4. Retrieve information from your chosen columns and apply a specific condition.")
            print("5. Exit.... To the Main Menu !!!!!")
                  
            option = input("Enter option (1, 2, 3, 4, 5): ").strip().lower()

            if option == '1':
                student_id = input("Enter student ID for an option 1: ")
                result = query_1(records, student_id)
                print("===================================================================================================================")
                if result:
                    print("Option 1 result:")
                    print(tabulate([result.values()], headers=result.keys(), tablefmt="grid"))
                else:
                    print("No student found with the given ID.")
                print("===================================================================================================================")

            elif option == '2':
                race = input("Enter race for an option 2: ")
                result = query_2(records, race)
                print("===================================================================================================================")
                if result:
                    headers = ["Sex", "School Support", "Access Internet", "Attendance Rate", "Parental Involvement"]
                    table = [[student['Sex'], student['School_support'], student['Access_internet'], student['Attendance_rate'], student['Parental_involvement']] for student in result]
                    print(f"Option 2 result for race '{race}':")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found for race '{race}'.")
                print("===================================================================================================================")

            elif option == '3':
                parental_involvement = input("Enter parental involvement for an option 3: ")
                result = query_3(records, parental_involvement)
                print("===================================================================================================================")
                if result:
                    headers = ["ID", "Free Time", "Math Score", "Reading Score", "Writing Score"]
                    table = [[student['ID'], student['Free_Time'], student['Math_Score'], student['Reading_Score'], student['Writing_Score']] for student in result]
                    print(f"Option 3 result for parental involvement '{parental_involvement}':")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found with parental involvement '{parental_involvement}' and absences less than 50.")
                print("===================================================================================================================")

            elif option == '4':
                try:
                    student_age = int(input("Enter the student's age: "))
                except ValueError:
                    print("Invalid age. Please enter an integer.")
                    continue

                result = query_4(records, student_age)
                print("===================================================================================================================")
                if result:
                    headers = ["ID", "Family Size", "Travel Time", "Health"]
                    table = [[student['ID'], student['Family_size'], student['Traveltime'], student['Health']] for student in result]
                    print(f"Option 4 result for students with age {student_age}:")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found with age {student_age}.")
                print("===================================================================================================================")

            elif option == '5':
                print("Exiting the submenu...")
                break
            else:
                print("Invalid option. Please try again.")

            # Ask if the user wants to run another query
            another = input("Do you want to run another Option? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except FileNotFoundError:
        print("Error: CSV file not found. Please ensure the file is in the same directory as the script.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again later.")

if __name__ == "__main__":
    # Example usage:
    display_sub_menu('students_data.csv')


# In[11]:


import csv
from tabulate import tabulate

def query_1(records, student_id):
    for row in records:
        if row['ID'] == student_id:
            return {
                'Sex': row['Sex'],
                'Age': row['Age'],
                'Family_relative': row['Family_relative'],
                'State': row['State'],
                'Race': row['Race']
            }
    return None

def query_2(records, race):
    result = []
    for student in records:
        if student['Race'] == race:
            student_info = {
                'Sex': student['Sex'],
                'School_support': student['School_support'],
                'Access_internet': student['Access_internet'],
                'Attendance_rate': student['Attendance_rate'],
                'Parental_involvement': student['Parental_involvement']
            }
            result.append(student_info)
    return result

def query_3(records, parental_involvement):
    result = []
    for student in records:
        try:
            absences = int(student['Absences'])
            if absences < 50 and student['Parental_involvement'] == parental_involvement:
                result.append({
                    "ID": student['ID'],
                    "Freetime": student['Freetime'],
                    "Math_score": student['Math_score'],
                    "Reading_score": student['Reading_score'],
                    "Writing_score": student['Writing_score'],
                    "Parental_Involvement": student['Parental_involvement']
                })
        except ValueError:
            continue  # Skip rows with non-integer absences
    return result

def query_4(records, student_age):
    result = []
    for student in records:
        try:
            age = int(student['Age'])
            if age == student_age:
                result.append({
                    'ID': student['ID'],
                    'Family_size': student['Family_size'],
                    'Traveltime': student['Traveltime'],
                    'Health': student['Health']
                })
        except ValueError:
            continue  # Skip rows with non-integer age
    return result

def display_sub_menu(csv_file):
    records = []
    try:
        with open(csv_file, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            records = [line for line in csv_reader]
        print(f"Successfully loaded {len(records)} records from {csv_file}.")

        while True:
            print("Select an option:")
            print("1. Retrieve the sex, age, number of relatives in family, state, and race based on the ID.")
            print("2. Retrieve the sex, school support, access internet, attendance rate, and parental involvement associated with a specific race.")
            print("3. Retrieve the ID, free time, math score, reading score, and writing score of students whose absences are less than 50, based on parental involvement.")
            print("4. Retrieve information from your chosen columns and apply a specific condition.")
            print("5. Exit.... To the Main Menu !!!!!")
                  
            option = input("Enter option (1, 2, 3, 4, 5): ").strip().lower()

            if option == '1':
                student_id = input("Enter student ID for an option 1: ")
                result = query_1(records, student_id)
                print("===================================================================================================================")
                if result:
                    print("Option 1 result:")
                    print(tabulate([result.values()], headers=result.keys(), tablefmt="grid"))
                else:
                    print("No student found with the given ID.")
                print("===================================================================================================================")

            elif option == '2':
                race = input("Enter race for an option 2: ")
                result = query_2(records, race)
                print("===================================================================================================================")
                if result:
                    headers = ["Sex", "School Support", "Access Internet", "Attendance Rate", "Parental Involvement"]
                    table = [[student['Sex'], student['School_support'], student['Access_internet'], student['Attendance_rate'], student['Parental_involvement']] for student in result]
                    print(f"Option 2 result for race '{race}':")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found for race '{race}'.")
                print("===================================================================================================================")

            elif option == '3':
                parental_involvement = input("Enter parental involvement for an option 3: ")
                result = query_3(records, parental_involvement)
                print("===================================================================================================================")
                if result:
                    headers = ["ID", "Free Time", "Math Score", "Reading Score", "Writing Score"]
                    table = [[student['ID'], student['Freetime'], student['Math_score'], student['Reading_score'], student['Writing_score']] for student in result]
                    print(f"Option 3 result for parental involvement '{parental_involvement}':")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found with parental involvement '{parental_involvement}' and absences less than 50.")
                print("===================================================================================================================")

            elif option == '4':
                try:
                    student_age = int(input("Enter the student's age: "))
                except ValueError:
                    print("Invalid age. Please enter an integer.")
                    continue

                result = query_4(records, student_age)
                print("===================================================================================================================")
                if result:
                    headers = ["ID", "Family Size", "Travel Time", "Health"]
                    table = [[student['ID'], student['Family_size'], student['Traveltime'], student['Health']] for student in result]
                    print(f"Option 4 result for students with age {student_age}:")
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(f"No students found with age {student_age}.")
                print("===================================================================================================================")

            elif option == '5':
                print("Exiting the submenu...")
                break
            else:
                print("Invalid option. Please try again.")

            # Ask if the user wants to run another query
            another = input("Do you want to run another Option? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except FileNotFoundError:
        print("Error: CSV file not found. Please ensure the file is in the same directory as the script.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again later.")

if __name__ == "__main__":
    # Example usage:
    display_sub_menu('students_data.csv')


# In[ ]:




