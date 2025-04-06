import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)


avg_marks = df.groupby('Subject')['Marks'].mean()
print("Average marks of students in each subject:\n",avg_marks)

stud = df[(df['Marks'] > 85) & (df['Attendance']<90)]
print("students have more than 85 marks and attendance less than 85:",stud)

def get_grade(marks):
    if marks>90:
        return 'A'
    elif marks>=80 & marks<90:
        return 'B'
    elif marks>=70 & marks<80:
        return 'C'
    else:
        return 'D'
    
df['Grade'] = df['Marks'].apply(get_grade)
print(df)

count_grade = df['Grade'].value_counts()
print("Number of students received each grade:",count_grade)

corre = df['Marks'].corr(df['Attendance'])
print("correlation between marks and attendance:",corre)