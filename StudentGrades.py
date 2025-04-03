student= {}
n=int(input("enter no of students"))

for i in range(0,n):
    tuple=()
    list=[]
    name=input("enter name")
    for i in range (0,4):
        list.append(int(input()))
    tuple=list
    student[name]=tuple

def average_grade(name_of_student):
    list=student[name_of_student]
    sum=0
    for i in range(0,len(list)):
        sum=sum+list[i]
    return float(sum/len(list))

def highest_avg_grade():
    top_student=""
    high_grade=0
    for i in student.keys():
        if(high_grade<average_grade(i)):
            top_student=i
    return top_student

def no_of_students_passed():
    no_of_students=0
    for i in student.keys():
        if(average_grade(i)>=50):
            no_of_students+=1
    return no_of_students

print(student)
name_of_student=input("enter name of student to know average")
print(average_grade(name_of_student))

print(highest_avg_grade())

print(no_of_students_passed())
