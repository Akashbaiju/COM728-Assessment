{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c1577a13-9c7d-4321-8665-ab0ebdaff76e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1986129697.py, line 30)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[29], line 30\u001b[1;36m\u001b[0m\n\u001b[1;33m    except ValueError:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "# File name for the CSV file\n",
    "csv_file = 'data.csv'\n",
    "\n",
    "# Function to display the menu\n",
    "def display_menu():\n",
    "    print(\"Menu:\")\n",
    "    print(\"1. Add Data\")\n",
    "    print(\"2. Display Data\")\n",
    "    print(\"3. Search Data\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    " # Get user input for the chosen option\n",
    "choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "    # Handle the user's choice\n",
    "if choice == 1:\n",
    "    print(\"Viewing student records...\")\n",
    "elif choice == 2:\n",
    "    print(\"Adding a new student...\")\n",
    "elif choice == 3:\n",
    "    print(\"Updating a student record...\")\n",
    "elif choice == 4:\n",
    "    print(\"Exiting the application...\")\n",
    "    sys.exit(0)\n",
    "else:\n",
    "    print(\"Invalid choice. Please try again.\")\n",
    "    \n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter a valid number (1-4).\")\n",
    "    except KeyboardInterrupt:\n",
    "print(\"\\nApplication interrupted. Exiting...\")\n",
    "sys.exit(0)\n",
    "except Exception as e:\n",
    "    print(f\"An error occurred: {e}\")\n",
    "    print(\"Please try again later.\")\n",
    "    sys.exit(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "69448aa1-4966-4960-b323-c1e97ecc6139",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected 'except' or 'finally' block (34297589.py, line 19)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[17], line 19\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(f\"{welcome_message}\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected 'except' or 'finally' block\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "try:\n",
    "    # Define the welcome message\n",
    "    welcome_message = '''\n",
    "    ===============================\n",
    "    Welcome to the Student Management System\n",
    "    ===============================\n",
    "\n",
    "    This application allows you to manage student records.\n",
    "    \n",
    "    Please select an option to get started:\n",
    "    1. Student data retrieval\n",
    "    2. Add a new student\n",
    "    3. Update a student record\n",
    "    4. Exit the application\n",
    "    '''\n",
    "\n",
    "print(f\"{welcome_message}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9582b932-4146-4ad6-80a0-a0cdeca35b52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adding a new student...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying student records...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching for student data...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the application...\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "0",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AKASH\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "# File name for the CSV file\n",
    "csv_file = 'data.csv'\n",
    "\n",
    "# Function to display the menu\n",
    "def display_menu():\n",
    "    print(\"Menu:\")\n",
    "    print(\"1. Add Data\")\n",
    "    print(\"2. Display Data\")\n",
    "    print(\"3. Search Data\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        # Get user input for the chosen option\n",
    "        choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "        # Handle the user's choice\n",
    "        if choice == 1:\n",
    "            print(\"Adding a new student...\")\n",
    "            # Add code to add new student data to the CSV file\n",
    "        elif choice == 2:\n",
    "            print(\"Displaying student records...\")\n",
    "            # Add code to display the data from the CSV file\n",
    "        elif choice == 3:\n",
    "            print(\"Searching for student data...\")\n",
    "            # Add code to search and display the data from the CSV file\n",
    "        elif choice == 4:\n",
    "            print(\"Exiting the application...\")\n",
    "            sys.exit(0)\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter a valid number (1-4).\")\n",
    "    except KeyboardInterrupt:\n",
    "        print(\"\\nApplication interrupted. Exiting...\")\n",
    "        sys.exit(0)\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")\n",
    "        sys.exit(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "802e6ee5-da11-49db-8865-396c7dbca342",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  hhv\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Please enter a valid number (1-4).\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the application...\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "# File name for the CSV file\n",
    "csv_file = 'data.csv'\n",
    "\n",
    "# Function to display the menu\n",
    "def display_menu():\n",
    "    print(\"Menu:\")\n",
    "    print(\"1. Add Data\")\n",
    "    print(\"2. Display Data\")\n",
    "    print(\"3. Search Data\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        # Get user input for the chosen option\n",
    "        choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "        # Handle the user's choice\n",
    "        if choice == 1:\n",
    "            print(\"Adding a new student...\")\n",
    "            # Add code to add new student data to the CSV file\n",
    "        elif choice == 2:\n",
    "            print(\"Displaying student records...\")\n",
    "            # Add code to display the data from the CSV file\n",
    "        elif choice == 3:\n",
    "            print(\"Searching for student data...\")\n",
    "            # Add code to search and display the data from the CSV file\n",
    "        elif choice == 4:\n",
    "            print(\"Exiting the application...\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter a valid number (1-4).\")\n",
    "    except KeyboardInterrupt:\n",
    "        print(\"\\nApplication interrupted. Exiting...\")\n",
    "        break\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "cbde3d3c-07a1-4b9d-a962-6de66095e364",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'path_to_your_students_data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[44], line 36\u001b[0m\n\u001b[0;32m     33\u001b[0m     students \u001b[38;5;241m=\u001b[39m read_students_from_csv(students_data)\n\u001b[0;32m     35\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m---> 36\u001b[0m     main()\n",
      "Cell \u001b[1;32mIn[44], line 33\u001b[0m, in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     31\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmain\u001b[39m():\n\u001b[0;32m     32\u001b[0m     students_data \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mpath_to_your_students_data.csv\u001b[39m\u001b[38;5;124m'\u001b[39m  \u001b[38;5;66;03m# Update with your file path\u001b[39;00m\n\u001b[1;32m---> 33\u001b[0m     students \u001b[38;5;241m=\u001b[39m read_students_from_csv(students_data)\n",
      "Cell \u001b[1;32mIn[44], line 3\u001b[0m, in \u001b[0;36mread_students_from_csv\u001b[1;34m(students_data)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mread_students_from_csv\u001b[39m(students_data):\n\u001b[0;32m      2\u001b[0m     students \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m----> 3\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(students_data, mode\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[0;32m      4\u001b[0m         csv_reader \u001b[38;5;241m=\u001b[39m csv\u001b[38;5;241m.\u001b[39mDictReader(file)\n\u001b[0;32m      5\u001b[0m         \u001b[38;5;28;01mfor\u001b[39;00m row \u001b[38;5;129;01min\u001b[39;00m csv_reader:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:310\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    303\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    304\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    305\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    306\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    307\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    308\u001b[0m     )\n\u001b[1;32m--> 310\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'path_to_your_students_data.csv'"
     ]
    }
   ],
   "source": [
    "def read_students_from_csv(students_data):\n",
    "    students = []\n",
    "    with open(students_data, mode='r') as file:\n",
    "        csv_reader = csv.DictReader(file)\n",
    "        for row in csv_reader:\n",
    "            students.append(row)\n",
    "    return students\n",
    "\n",
    "# Function to display the first few rows of the CSV file\n",
    "def head(students_data, num_rows=5):\n",
    "    with open(students_data, mode='r') as file:\n",
    "        csv_reader = csv.reader(file)\n",
    "        headers = next(csv_reader)  # Read the header row\n",
    "        print(headers)\n",
    "        for i, row in enumerate(csv_reader):\n",
    "            if i >= num_rows:\n",
    "                break\n",
    "            print(row)\n",
    "def query_a1(students, student_id):\n",
    "    for student in students:\n",
    "        if student['ID'] == student_id:\n",
    "            return {\n",
    "                'Sex': student.get('Sex', 'N/A'),\n",
    "                'Age': student.get('Age', 'N/A'),\n",
    "                'Number of relatives in family': student.get('Number of relatives in family', 'N/A'),\n",
    "                'State': student.get('State', 'N/A'),\n",
    "                'Race': student.get('Race', 'N/A')\n",
    "            }\n",
    "    return None\n",
    "# Main function to run the query a1\n",
    "def main():\n",
    "    students_data = 'path_to_your_students_data.csv'  # Update with your file path\n",
    "    students = read_students_from_csv(students_data)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "2a339d14-a290-4441-932b-de1ac1a7422e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Student Data Management System!\n",
      "CSV file 'studentS_data.csv' loaded successfully.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the application...\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "# Welcome message\n",
    "print(\"Welcome to the Student Data Management System!\")\n",
    "\n",
    "# Get the CSV file path\n",
    "csv_file = 'studentS_data.csv'\n",
    "\n",
    "try:\n",
    "    with open(csv_file, 'r') as file:\n",
    "        reader = csv.reader(file)\n",
    "        next(reader)  # Skip the header row\n",
    "        print(f\"CSV file '{csv_file}' loaded successfully.\")\n",
    "except FileNotFoundError:\n",
    "    print(f\"Error: File '{csv_file}' not found. Please check the file path and try again.\")\n",
    "    sys.exit(1)\n",
    "except Exception as e:\n",
    "    print(f\"An error occurred: {e}\")\n",
    "    print(\"Please try again later.\")\n",
    "    sys.exit(1)\n",
    "\n",
    "# Function to display the menu\n",
    "def display_menu():\n",
    "    print(\"\\nMenu:\")\n",
    "    print(\"1. Add Data\")\n",
    "    print(\"2. Display Data\")\n",
    "    print(\"3. Search Data\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        # Get user input for the chosen option\n",
    "        choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "        # Handle the user's choice\n",
    "        if choice == 1:\n",
    "            print(\"Adding a new student...\")\n",
    "            # Add code to add new student data to the CSV file\n",
    "        elif choice == 2:\n",
    "            print(\"Displaying student records...\")\n",
    "            # Add code to display the data from the CSV file\n",
    "        elif choice == 3:\n",
    "            print(\"Searching for student data...\")\n",
    "            # Add code to search and display the data from the CSV file\n",
    "        elif choice == 4:\n",
    "            print(\"Exiting the application...\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter a valid number (1-4).\")\n",
    "    except KeyboardInterrupt:\n",
    "        print(\"\\nApplication interrupted. Exiting...\")\n",
    "        break\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "4d3c5f37-4bc5-4758-98f2-f4279152d7a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Student Data Management System!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the path to the CSV file (or 'exit' to quit):  students_data\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: File not found. Please try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the path to the CSV file (or 'exit' to quit):  students_data\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: File not found. Please try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the path to the CSV file (or 'exit' to quit):  students_data.csv\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file 'students_data.csv' loaded successfully.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adding a new student...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the application...\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "# Welcome message\n",
    "print(\"Welcome to the Student Data Management System!\")\n",
    "\n",
    "# Get the CSV file path\n",
    "csv_file = 'students_data.csv'\n",
    "\n",
    "while True:\n",
    "    # Get the CSV file path from the user\n",
    "    csv_file = input(\"Please enter the path to the CSV file (or 'exit' to quit): \")\n",
    "    if csv_file.lower() == 'exit':\n",
    "        print(\"Exiting the application...\")\n",
    "        sys.exit(0)\n",
    "\n",
    "    try:\n",
    "        with open(csv_file, 'r') as file:\n",
    "            reader = csv.reader(file)\n",
    "            next(reader)  # Skip the header row\n",
    "            print(f\"CSV file '{csv_file}' loaded successfully.\")\n",
    "            break\n",
    "    except FileNotFoundError:\n",
    "        print(\"Error: File not found. Please try again.\")\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")\n",
    "\n",
    "# Function to display the menu\n",
    "def display_menu():\n",
    "    print(\"\\nMenu:\")\n",
    "    print(\"1. Add Data\")\n",
    "    print(\"2. Display Data\")\n",
    "    print(\"3. Search Data\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        # Get user input for the chosen option\n",
    "        choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "        # Handle the user's choice\n",
    "        if choice == 1:\n",
    "            print(\"Adding a new student...\")\n",
    "            # Add code to add new student data to the CSV file\n",
    "        elif choice == 2:\n",
    "            print(\"Displaying student records...\")\n",
    "            # Add code to display the data from the CSV file\n",
    "        elif choice == 3:\n",
    "            print(\"Searching for student data...\")\n",
    "            # Add code to search and display the data from the CSV file\n",
    "        elif choice == 4:\n",
    "            print(\"Exiting the application...\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter a valid number (1-4).\")\n",
    "    except KeyboardInterrupt:\n",
    "        print(\"\\nApplication interrupted. Exiting...\")\n",
    "        break\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "80169856-83f4-4797-b02e-5ab58205d901",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Student Data Management System!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the path to the CSV file (or 'exit' to quit):  students_data.csv\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file 'students_data.csv' loaded successfully.\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "# Welcome message\n",
    "print(\"Welcome to the Student Data Management System!\")\n",
    "\n",
    "# Get the CSV file path\n",
    "csv_file = 'students_data.csv'\n",
    "\n",
    "while True:\n",
    "    # Get the CSV file path from the user\n",
    "    csv_file = input(\"Please enter the path to the CSV file (or 'exit' to quit): \")\n",
    "    if csv_file.lower() == 'exit':\n",
    "        print(\"Exiting the application...\")\n",
    "        sys.exit(0)\n",
    "\n",
    "    try:\n",
    "        with open(csv_file, 'r') as file:\n",
    "            reader = csv.reader(file)\n",
    "            next(reader)  # Skip the header row\n",
    "            print(f\"CSV file '{csv_file}' loaded successfully.\")\n",
    "            break\n",
    "    except FileNotFoundError:\n",
    "        print(\"Error: File not found. Please try again.\")\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "c6e8a414-e2c0-4217-8ea6-3feb25b34a21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "    ===============================\n",
      "    Welcome to the Student Management System\n",
      "    ===============================\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the path to the CSV file (or 'exit' to quit):  students_data.csv\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file 'students_data.csv' loaded successfully.\n",
      "\n",
      "Menu:\n",
      "1. Add Data\n",
      "2. Display Data\n",
      "3. Search Data\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adding a new student...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying student records...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching for student data...\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  acas\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: Please enter a valid number (1-4).\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting the application...\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sys\n",
    "\n",
    "welcome_message = '''\n",
    "    ===============================\n",
    "    Welcome to the Student Management System\n",
    "    ===============================\n",
    "'''\n",
    "\n",
    "print(welcome_message)\n",
    "\n",
    "while True:\n",
    "    # Get the CSV file path from the user\n",
    "    csv_file = input(\"Please enter the path to the CSV file (or 'exit' to quit): \")\n",
    "    if csv_file.lower() == 'exit':\n",
    "        print(\"Exiting the application...\")\n",
    "        sys.exit(0)\n",
    "\n",
    "    try:\n",
    "        with open(csv_file, 'r') as file:\n",
    "            reader = csv.reader(file)\n",
    "            next(reader)  # Skip the header row\n",
    "            print(f\"CSV file '{csv_file}' loaded successfully.\")\n",
    "\n",
    "            # Display the menu options\n",
    "            def display_menu():\n",
    "                print(\"\\nMenu:\")\n",
    "                print(\"1. Add Data\")\n",
    "                print(\"2. Display Data\")\n",
    "                print(\"3. Search Data\")\n",
    "                print(\"4. Exit\")\n",
    "\n",
    "            display_menu()\n",
    "\n",
    "            # Get user input for the chosen option\n",
    "            while True:\n",
    "                try:\n",
    "                    choice = int(input(\"Enter your choice (1-4): \"))\n",
    "\n",
    "                    # Handle the user's choice\n",
    "                    if choice == 1:\n",
    "                        print(\"Adding a new student...\")\n",
    "                        # Add code to add new student data to the CSV file\n",
    "                    elif choice == 2:\n",
    "                        print(\"Displaying student records...\")\n",
    "                        # Add code to display the data from the CSV file\n",
    "                    elif choice == 3:\n",
    "                        print(\"Searching for student data...\")\n",
    "                        # Add code to search and display the data from the CSV file\n",
    "                    elif choice == 4:\n",
    "                        print(\"Exiting the application...\")\n",
    "                        break\n",
    "                    else:\n",
    "                        print(\"Invalid choice. Please try again.\")\n",
    "                except ValueError:\n",
    "                    print(\"Error: Please enter a valid number (1-4).\")\n",
    "                except KeyboardInterrupt:\n",
    "                        print(\"\\nApplication interrupted. Exiting...\")\n",
    "                        break\n",
    "                except Exception as e:\n",
    "                    print(f\"An error occurred: {e}\")\n",
    "                    print(\"Please try again later.\")\n",
    "                    continue\n",
    "\n",
    "            break\n",
    "\n",
    "    except FileNotFoundError:\n",
    "        print(\"Error: File not found. Please try again.\")\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "        print(\"Please try again later.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25913629-c789-48fa-982b-51ab89a99a42",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
