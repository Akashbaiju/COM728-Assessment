#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from tabulate import tabulate

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the file path and try again.")
        return None

def top_mother_education_by_race(df, race, parental_involvement_level, top_n=3):
    # Filter the data by the specified race and parental involvement level
    filtered_df = df[(df['Race'].str.lower() == race.lower()) & 
                     (df['Parental_involvement'].str.lower() == parental_involvement_level.lower())]

    # Group by mother's education level and count occurrences
    education_counts = filtered_df['Mother_education_level '].value_counts().head(top_n)
    
    return education_counts

def calculate_average_absences(df, parental_involvement_level):
    # Filter the data by the specified parental involvement level
    filtered_df = df[df['Parental_involvement'].str.lower() == parental_involvement_level.lower()]

    if not filtered_df.empty:
        # Calculate the average number of absences
        average_absences = filtered_df['Absences'].mean()
        return average_absences
    else:
        return None

def analyze_math_scores_by_race(df):
    # Prompt the user to input the race
    input_race = input("Enter the race to analyze (as it appears in the data): ").strip()

    # Filter the data for students with an attendance rate greater than 80% and the specified race
    filtered_data = df[(df['Attendance_rate'] > 80) & (df['Race'].str.lower() == input_race.lower())]

    # Calculate the average math score for the specified race
    average_math_score = filtered_data['Math_score'].mean()

    # Display the result
    print("===================================================================================================================")
    if pd.notna(average_math_score):
        print(f"Average Math Score for students with attendance rate > 80% in race '{input_race}': {average_math_score}")
    else:
        print(f"No data available for race '{input_race}' with attendance rate > 80%")
    print("===================================================================================================================")

def analyze_studytime_by_sex(df):
    # Prompt the user to input the sex
    input_sex = input("Enter the sex to analyze (as it appears in the data): ").strip()

    # Define the study time threshold
    study_time_threshold = 2  # Adjust the threshold as needed

    # Filter the data for students who study more than the defined threshold hours and the specified sex
    filtered_data = df[(df['Studytime'] > study_time_threshold) & (df['Sex'].str.lower() == input_sex.lower())]

    # Calculate the average math score for the specified sex
    average_math_score = filtered_data['Math_score'].mean()

    # Calculate the correlation between study time and math score for the specified sex
    correlation = filtered_data['Studytime'].corr(filtered_data['Math_score'])

    # Display the results
    print("===================================================================================================================")
    if not filtered_data.empty:
        print(f"Average Math Score for {input_sex} students who study more than {study_time_threshold} hours: {average_math_score}")
        print(f"Correlation between Studytime and Math Score for {input_sex} students: {correlation}")
    else:
        print(f"No data available for sex '{input_sex}' with study time > {study_time_threshold} hours")
    print("===================================================================================================================")

def main():
    # Specify the path to your CSV file
    file_path = 'students_data.csv'  # replace with your actual file path
    
    # Load the data
    df = load_data(file_path)
    
    # Exit if the data could not be loaded
    if df is None:
        return
    
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Identify the top 3 levels of mother’s education for a specific race of students based on parental involvement levels.")
        print("2. Analyze the average number of absences among students with a particular level of parental involvement.")
        print("3. Analyze average math scores for students with attendance rate > 80% based on race.")
        print("4. Analyze study time and math scores by sex.")
        print("5. Exit")
        
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ").strip()

        if choice == '1':
            # Query 1: Identify top 3 levels of mother's education
            race = input("Enter the race you're interested in: ").strip().lower()
            parental_involvement_level = input("Enter the parental involvement level (e.g., high, medium, low): ").strip()
            
            # Validate race input
            valid_races = df['Race'].str.lower().unique()
            if race not in valid_races:
                print(f"'{race}' is not a valid race. Please enter a valid race.")
                continue
            
            top_education_levels = top_mother_education_by_race(df, race, parental_involvement_level)
            
            # Display the results
            print("===================================================================================================================")
            if not top_education_levels.empty:
                print(f"Top 3 Mother's Education Levels for race '{race}' with '{parental_involvement_level}' parental involvement:")
                print(top_education_levels)
            else:
                print(f"No data available for race '{race}' with '{parental_involvement_level}' parental involvement.")
            print("===================================================================================================================")

        elif choice == '2':
            # Query 2: Analyze average absences
            parental_involvement_level = input("Enter the parental involvement level (e.g., high, medium, low): ").strip()
            average_absences = calculate_average_absences(df, parental_involvement_level)
            
            # Display the result
            print("===================================================================================================================")
            if average_absences is not None:
                print(f"The average number of absences for students with '{parental_involvement_level}' parental involvement is: {average_absences:.2f}")
            else:
                print(f"No data available for parental involvement level '{parental_involvement_level}'.")
            print("===================================================================================================================")

        elif choice == '3':
            # Query 3: Analyze average math scores for students with attendance rate > 80% based on race
            analyze_math_scores_by_race(df)

        elif choice == '4':
            # Query 4: Analyze study time and math scores by sex
            analyze_studytime_by_sex(df)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




