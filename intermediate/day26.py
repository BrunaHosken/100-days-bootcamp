#day 26
#list comprehension

numbers = [1,2,3]
new_list = [ n+1 for n in numbers]
print(new_list)

name = "Bruna"
new_list = [letter for letter in name]
print(new_list)

new_list = [number*2 for number in range(1,5)]
print(new_list)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_list = [ name for name in names if len(name) < 5]
print(new_list)

new_list = [ name.upper() for name in names if len(name) > 5]
print(new_list)

#dictionary comprehension

import random

students_score= {student: random.randint(1,100) for student in names}
print(students_score)

passed_students= { student:score for (student,score) in students_score.items() if score>= 60}
print(passed_students)

#PandasFrame

import pandas

student_dict={
    "student":['Alex', 'Beth', 'Caroline'],
    "score": [ 56, 76, 98]
}

students_data_frame = pandas.DataFrame(student_dict)

for (index, row) in students_data_frame.iterrows():
    if row.student == "Alex":
        print(row)

