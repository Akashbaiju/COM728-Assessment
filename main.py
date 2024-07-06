{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a14a38d1-e18f-4c5e-8952-99bb79159adc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "    =================================================\n",
      "    Welcome to the Student Data Management System\n",
      "    =================================================\n",
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
      "Choose the correct menu:\n",
      "1. Retrieving the students data\n",
      "2. Advanced Student Data Analysis Using Pandas\n",
      "3. Visualization of the students Data\n",
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
      "Retrieving the students data\n"
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
      "Advanced Student Data Analysis Using Pandas\n"
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
      "Visualization of the students data...\n"
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
    "    =================================================\n",
    "    Welcome to the Student Data Management System\n",
    "    =================================================\n",
    "'''\n",
    "\n",
    "print(welcome_message)\n",
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
    "\n",
    "            # Display the menu options\n",
    "            def display_menu():\n",
    "                print(\"\\nChoose the correct menu:\")\n",
    "                print(\"1. Retrieving the students data\")\n",
    "                print(\"2. Advanced Student Data Analysis Using Pandas\")\n",
    "                print(\"3. Visualization of the students Data\")\n",
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
    "                        print(\"Retrieving the students data\")\n",
    "                        # Add code to add new student data to the CSV file\n",
    "                    elif choice == 2:\n",
    "                        print(\"Advanced Student Data Analysis Using Pandas\")\n",
    "                        # Add code to display the data from the CSV file\n",
    "                    elif choice == 3:\n",
    "                        print(\"Visualization of the students data...\")\n",
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
   "id": "5b42adfa-64c9-45bb-85d0-041b14a666d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "        "
   ]
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
