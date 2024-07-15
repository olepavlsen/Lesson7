grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
# print(grades)
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
students = sorted(students)
# print(students)
grades1 = grades[0]
import statistics
a1 = statistics.mean(grades1)
grades2 = grades[1]
import statistics
a2 = statistics.mean(grades2)
grades3 = grades[2]
import statistics
a3 = statistics.mean(grades3)
grades4 = grades[3]
import statistics
a4 = statistics.mean(grades4)
grades5 = grades[4]
import statistics
a5 = statistics.mean(grades5)
average_grades = [a1, a2, a3, a4, a5]
average_mark = dict(zip(students, average_grades))
print(average_mark)