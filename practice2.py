#variables
name="Beau" #string
age=39
name1="Abril"
heightName1=5.7

#keywords: for, if, while, import. do not use as a variable name

#expressions and statements
1+1
"Beau"

#statement
name3="Carter"; print(name3)

#indentation matters in python

print(type(name)==str) #returns true
print(isinstance(name,str)) #returns whether an object is an instance of a class or of a subclass thereof.

age=2
print(isinstance(age,int)) #returns true
print(isinstance(age,float)) #returns false

#class constructor
age2=float(3)
print(isinstance(age2,float)) #returns true

#casting
age4=int("20") #only works with numbers not with letters or words
print(isinstance(age,int)) #returns true

#operators
1+1 #2
1+-1 #0
2-1 #1
2*2 #4
4/2 #2
4%3 #1
4**2 #16
4//2 #2 rounds down to the nearst whole number

print("Scamp" + "is a good dog")

age6=8
age6+=8 #age6=age6+8 --> 16
print(age6)

#comparasion operators
a=1
b=2

a==b
a!=b
a<b
a>=b

condition1=True
condition2=False

not condition1 #false
condition1 and condition2 #false
condition1 or condition2 #true 

print(0 or 1)
print(False or "Hey")
print("hi" or "hey")
print([] or False)
print(False or [])
