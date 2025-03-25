# Ryan Zartman
#Module2CaseStudyIfElseWhile.py 
#This app will accept a first and last name of a student and a gpa as an input
#if the gpa is greater than or equal to 3.5 it will announce the student making the deans list
#if the gpa is greater than or equal to 3.25 it will annount the student making the honor roll

# Instructions
# Complete the following steps:
# Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
# ask for and accept a student's last name.
# quit processing student records if the last name entered is 'ZZZ'.
# ask for and accept a student's first name.
# ask for and accept the student's GPA as a float.
# test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
# test if the student's GPA is 3.25 or greater and, if so, print a message saying that the student has made the Honor Roll.
# Test your app using at least five students.
# Your header comments need to contain:
# Your name
# The file name for your app
# A brief description of what your app will do


while True:
    lastName = input("Enter the Student\'s Last Name: ")
    print(f'Last Name is : {lastName}')
    if lastName == 'ZZZ':
        print('You\'ve entered ZZZ - we will exit now')
        break
    firstName = input('Enter the First Name of the Student: ')
    print(f'You entered {firstName} as the First Name')
    GPA = float(input("Enter the GPA of the student: "))
    print(f'You entered {GPA} as the GPA')
    if GPA >= 3.5:
        print(f'With a GPA of {GPA}, {firstName} {lastName} has satisfied the requirement of 3.5 to make the Dean\'s List')
    if GPA >= 3.25:
        print(f'With a GPA of {GPA}, {firstName} {lastName} has satisfied the requirement of 3.25 to make the Honor Roll')


