# Question 1
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
avg=(a+b+c)/3
print("The average of three numbers is :",avg)



# Question 2
standard_deduction=10000
tax_rate=0.2
dependent_deduction=3000
gross_income=int(input("enter your gross income"))
No_of_dependents=int(input("Enter your number of dependents"))
taxable_income=gross_income-standard_deduction-(dependent_deduction*No_of_dependents)
tax=(float(taxable_income)*tax_rate)
print("Your income tax is :",tax)



# Question 3
SID=input("Enter your SID")
Name=input("Enter your name")
Gender=input("Enter your Gender ")
Course_name=input("Enter your course name")
CGPA=float(input("Enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)



# Question 4
Marks=[]
for i in range(5):                                  #for loop to take input 5 times
    Marks.append(input("Enter marks of students"))
Marks.sort()
print(Marks)  


  
# Question 5
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)                    #1st part of question
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Part b of question :",colour)                   #2nd part of question
