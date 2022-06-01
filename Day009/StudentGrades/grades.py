# Student Grades
# Author: Powell A. Mims
# This practice program takes a set of student scores and converts them to grades

from math import floor;

GRADES = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"];

def get_grade(score):
    if score < 0:
        return "F";
    score = floor(score / 10);
    try:
        return GRADES[score];
    except IndexError:
        return "A";

student_scores = {
    "Piddles" : -5,
    "Kevin" : 5,
    "Bob" : 15,
    "Tim" : 25,
    "Kelly" : 35,
    "Tina" : 45,
    "Julia" : 55,
    "Bilbo" : 65,
    "Frodo" : 75,
    "Steven" : 85,
    "Stan" : 95,
    "Felicia" : 105,
    "Chad" : 115
}

student_grades = {};

for student in student_scores:
    grade = get_grade(student_scores[student]);
    student_grades[student] = grade;

print(student_scores);
print(student_grades);
