# To find the average of three numbers
num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
num3 = float(input('Enter the third number:'))
avg= (num1+num2+num3)/3
print('The average of the three numbers is %.2f'%avg )

# Computing income tax
gross_income=float(input("Enter the gross income: "))
n=int(input("Enter the number of dependents: "))
taxable_income= gross_income-10000-(3000*n)
print('Taxable income : %.2f' %taxable_income)

# Store different data types in a list
SID=int(input('Enter SID: '))
Name =input("Enter students' name: ")
Gender=input("Enter the students' gender: ")
Course_Name= input('Enter the course name opted: ')
CGPA =float(input("Enter the students' CGPA :"))
Student=[SID,Name,Gender,Course_Name,CGPA]
print(Student)

# Entering and displaying marks in a sorted manner
m1=float(input("Enter the marks obtained by the 1st student:"))
m2=float(input("Enter the marks obtained by the 2nd student:"))
m3=float(input("Enter the marks obtained by the 3rd student:"))
m4=float(input("Enter the marks obtained by the 4th student:"))
m5=float(input("Enter the marks obtained by the 5th student:"))
Marks=[m1,m2,m3,m4,m5]
Marks.sort()
print(Marks)

# Eliminating an element from a list
color = ['Red','Green','White','Black','Pink','Yellow']
print(color)
del color[3]
print("New list obtained after removing the 4th element : ",color)

# Replacing 'Black' and 'Pink' by 'Purple'
color = ['Red','Green','White','Black','Pink','Yellow']
color[3] = color[4]= 'Purple'
print("New list obtained after replacing 'Black' and 'Pink' with 'Purple': ",color)


