#QUESTION 1
print("---------OUTPUT-1---------")
def Tower(n , selected_rod, destination_rod, centeral_rod):
	if n == 0:
		return
	Tower(n-1, selected_rod, centeral_rod, destination_rod)
	print("shifted disk",n,"selected the rod",selected_rod,"destination of rod",destination_rod)
	Tower(n-1, centeral_rod, destination_rod, selected_rod)
n = 3
Tower(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2
print("---------OUTPUT-2---------")
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle you want: '))

print("PASCAL TRIANGLE USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for giving spacing in triangle

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("PASCAL TRIANGLE USING RECURSSIONS")

def pascal_triangle(n,original_length=n):
    if n == 0:
        return
    pascal_triangle(n-1,original_length)
    print(' '*(original_length-n), end=' ')   #for print the spaces(" ")
    begin = 1                                #first number is always 1
    for i in range(1, n+1):

        print(begin, end =' ')
        
        begin = begin * (n - i) // i         #using Binomial Coefficient
    print()
pascal_triangle(n)
print("\n")




#QUESTION 3
print("---------OUTPUT-3---------")
int_1=int(input("enter first no.:"))
int_2=int(input("enter second no.:"))
Quotient = int_1 // int_2
Remainder = int_1 % int_2

#part (a)
print("part-(a):Checking whether the quotient and remainder is a callable value or not")
print(callable(Quotient))
print(callable(Remainder))

#part (b)
if (Quotient == 0):
    print("(b) The quotient is zero")
if (Remainder == 0):
    print("(b) The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(b) All the values are non zero")

#part (c)
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"(c) Filtered out numbers that are greater than 4 are : {result}")

#part (d)
set_result = set(result)
print("(d) Set:",set_result)

#part (e)
immutable_Set = frozenset(set_result) #frozen Set is used to make the set immutable
print("(e) Immutable set:",immutable_Set)

#part (f)
print("(f) Hash value of the maximum value from the above set:", hash(max(immutable_Set)))
print("\n")

#QUESTION 4
print("---------OUTPUT-4---------")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

#creating object
student_1 = Student("LOVENEET", 21103067)
print("Object created")                  #printing the assigned values
print(f"The name of the student it {student_1.name} and SID is {student_1.roll_no}.")
del student_1                             #deleting object
print("\n")

#QUESTION 5
print("---------OUTPUT-5---------")
class Employ:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employ_1 = Employ("Mehak", 40000)
employ_2 = Employ("Ashok", 50000)
employ_3 = Employ("Viren", 60000)

#part (a) updating salary
employ_1.salary = 70000
print(f"(a)The updated salary of {employ_1.name} is {employ_1.salary} ")
#part (b) deleting a record
print("(b)Record of Viren deleted", end='')
del employ_3
print("\n")

#QUESTION 6
print("---------OUTPUT-6---------")
#inputting a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting a meaningful word with the exact same letters
test_word = input("Enter a word using the exact same letters to test your friendship: ")
test_word=test_word.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
