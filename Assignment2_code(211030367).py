#Question 1
str1=("Python is a case sensitive language")                                                                              
print(len(str1))                                               # len is a built in function for find lenght of string      (part a) 
print(str1[::-1])                                              # by[::-1] it reverse the string                            (part b)
print(str1[10::])                                                                                                        # (part c)
print(str1.replace("case sensitive","object oriented"))                                                                  # (part d)
print(str1.find('a'))                                                                                                    # (part e)
print(str1.replace(" ",""))                                                                                              # (part f)

 
#Question 2
Name=input("enter your name")
S_I_D=int(input("enter your sid"))
Department=input("enter your department")
CGPA=float(input("enter your cgpa"))
print("Hey %s,"%Name,"Here!")
print("My SID is %d" %S_I_D)
print("I am from %s"%Department,"and my CGPA is %f"%CGPA)


#Question 3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print("left sift a with 2 bits:",a<<2)
print("left shift b with 2 bits:",b<<2)
print("right shift a with 2 bits:",a>>2)
print("right shift b with 4 bits:",b>>4)


#Question 4
first_num=float(input("enter 1st number"))
second_num=float(input("enter 2nd number"))
third_num=float(input("enter 3rd number"))
if first_num>second_num:
    if first_num>third_num:
        print("greater number is:",first_num)
    else:
        print("greater number is:",third_num)
elif second_num>third_num:
    if second_num>first_num:
        print("greater number is:",second_num)
    else:
        print("greater number is:",first_num)
elif third_num>first_num:
    if third_num>second_num:
        print("greater number is:",third_num)
    else:
        print("greater number is:",second_num)
elif first_num>third_num:
    if first_num>second_num:
        print("greater number is:",first_num)
    else:
        print("greater number is:",second_num)
else:
    print("all three are equal and also largest value is:",first_num)



#Question 5
str_2=input("enter a string")
if "name" in str_2:
    print("Yes")
else:
    print("No")
              

#Question 6
first_side=int(input("enter first side of triangle"))
second_side=int(input("enter second side of triangle"))
third_side=int(input("enter third side of triangle"))
first_side,second_side,third_side>0
if (first_side+second_side)<=(third_side):
    print("NO")
elif (first_side+third_side)<=(second_side):
     print("NO")
elif (second_side+third_side)<=(first_side):
     print("NO")
else:
     print("YES")
     
