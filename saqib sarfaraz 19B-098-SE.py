#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


line1 = 'saqib'
line2 = 'sarfaraz'
print(line1 +" "+ line2 )


# In[7]:


first = input('Enter your first name: ') 
last = input('Enter your last name: ') 
line1 = 'Hello '+ first + ' ' + last + '...' 
print(line1) 
print('Welcome to the world of Python!')


# #3.1
# Implement a program that requests the current temperature in degrees Fahrenheit from the user and prints the temperature in degrees Celsius using the formula
# 

# In[11]:


c=eval(input("enter the current temperature in degree farhrenheit:"))
d= c-32
e=d*5/9
print("The current temperature in degree celsius:",e)


# #3.2

# (a) If age is greater 62,print 'You can get your pension benefits'.  

# In[17]:


age =eval(input("enter the age :"))
if age>62:
    print("you have pension beneifit ")
else:
    print("keep wait ")
print("good bye ")    
print("-------------------------------------------------------")
age =eval(input("enter the age :"))
if age>62:
    print("you have pension beneifit ")
else:
    print("keep wait ")
print("good bye ")


# (b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], print'One of the top 5 baseball players, ever!'. 

# In[24]:



lst=['Musial','Aaraon','William','gehrig','ruth']
if  'ruth' in lst:
    print("one of the the top 5 base ball players ")
print("thank you")    


# (c) If hits is greater than 10 and shield is 0, print'You are dead...'.

# In[1]:


hit=eval(input("enter the hits"))
sheild=eval(input("enter the shield"))  
if hit>10 or sheild<=0:
    print("you are dead")


# (d) If at least one of the Boolean variable snorth,south,east,and west is True,print 'I can escape.'.
# 

# #3.3
# (a) If year is divisible by 4,print'Could beal eapyear.';other wise print'Deﬁnitely not aleapyear.' 
# (b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck next time...'
# 

# In[4]:


year=eval(input("enter year"))
if year/4:
    print("could be eapyear")
else:
    print("could not be eapyer")
print("---------------------------------------------")
year=eval(input("enter year"))
if year/4:
    print("could be eapyear")
else:
    print("could not be eapyer")


# In[9]:


#(b)
l=eval(input("enter the ticket"))
t=eval(input("enter the lottery"))

if l==t:
    print("you won")
else:
    print("you lose")
print("----------------------------------------------------------")
l=eval(input("enter the ticket"))
t=eval(input("enter the lottery"))

if l==t:
    print("you won")
else:
    print("you lose")


# #3.4
# Implement a program that starts by asking the user to enter a login id (i.e., a string). The program then checks whether the id entered by the user is in the list ['joe', 'sue', 'hani', 'sophie'] of valid users. Depending on the outcome, an appropriate message should be printed. Regardless of the outcome, your function should print 'Done.' before terminating.Here is an example of a successful login: >>> 

# In[13]:


lst=['joe', 'sue', 'hani', 'sophie']
login=eval(input("your id "))
if login in lst:
    print("you are login in")
else:
    print("access failed")
print("------------------------------------")    
lst=['joe', 'sue', 'hani', 'sophie']
login=eval(input("your id "))
if login in lst:
    print("you are login in")
else:
    print("access failed")


# #3.5 Implement aprogram that requests from the user a list of words(i.e.,strings) and then prints on the screen,oneper line,all four-letter strings in the list. 

# In[18]:


lst: ['stop', 'desktop', 'top', 'post']
for char in lst:
    print(char)
print("--------------------------------------------------")
#by using loop

animals = ['fish', 'cat', 'dog',] 
for animal in animals: 
        print(animal)

 


# #3.6
# Write the for loop that will print these sequences of numbers,oneperline,intheinteractive shell. 

# In[20]:


for i in range(0,9):
    print(i)
    


# #3.7 
# Write the for loop that will print the following sequences of numbers, oneperline. (a) Integers from 3 upto and including 12 (b) Integers from 0 up to but not including 9, but with a step of 2 instead of the default of1(i.e.,0,2,4,6,8) (c) Integers from 0upto but not including 24 with a step of 3 (d) Integers from 3 up to but not including 12 with a step of 5
# 

# In[21]:


for i in range(3,12):
    print(i)


# In[23]:


for i in range (0,10,2):
    print(i)


# In[26]:


for i in range(0,24,3):
    print(i)


# In[27]:


for i in range(3,20,5):
    print(i)


# #3.8
# Deﬁne, directly in the interactive shell, function perimeter() that takes, as input, the radius of a circle (a nonnegative number) and returns the perimeter of the circle. A sample usageis:

# In[9]:


import math 
def perimeter(radius):
    return 2 * math.pi * radius

    
    


# #3.9 The function average() takes two inputs. We use variable names x and y to refer to theinputarguments.Theaverageofxandyis(x+y)/2: 

# In[11]:


def average(x, y): 
    return (x + y) / 2 
average(4,5)


# #3.10
# 3.10 Weneedtousea for loop to check whether or not each character of the input string is a vowel.If yes,we can return False immediately.Wecanreturn True only after all the characters have been checked,that is,when the for looph as complete dexecution. 

# In[18]:


def noVowel(s): 
    s=('saqib')
    for c in s:
        if c in 'aeiouAEIOU':
            return False 
        return True


# 3.11 A for loop is used to check whether or not each number in the list is even.If not,we can return False right away. We can return True only after the for loop has completed execution. 

# In[10]:


def even(s):
    'return True is all integers in numList are even, False otherwise' 
    for num in s:
        if num%2!=0:
            return false
    return true


# 3.12 The function should iterate over all numbers in the list and test each to determine whether it is negative ;if so,the number is printed. 

# In[3]:


lst=[1,2,3,-4]
for i in lst: 
    if i < 0: 
         print(i)
          


#  3.14
# Draw a diagram representing the state of names and objects after this execution

# In[3]:


a=[1,2,5]
b=a
a=3
print(a)


# 3.15 Suppose a nonempty list team has been assigned. Write a Python statement or statements that swap the ﬁrst and last value of the list.So,if the original list is: 

# In[13]:


a=['saqib','ali','sarah','sadia']
teams=['sadia','ali','sarah','saqib']
a,teams=teams,a
print(teams)
print(a)


# 3.16 Implement function swapFL() that takes a list as input and swaps the ﬁrst and last element softhe list. You may assume the list will be nonempty.The function should not return anything.

# In[17]:


ingredients = ['flour', 'sugar', 'butter', 'apples']
ingredients.sort()
print(ingredients)


# 3.17 Use the eval() function to evaluate these strings as Python expressions

# In[31]:


a= eval('2 * 3 + 1')
print(a)
c=eval("'hello' + ' ' + 'world!'")
print(c)
d=eval( "'ASCII'.count('I')")
print(d)
e=eval('x=5')
print(e)
b=eval('hello')
print(b)

#hello word is not defined
#X=5 integer not equal to str


# 3.18 Assumea,b,and c have been deﬁned in the interactive shell as shown: 

# In[38]:


a,b,c=4,5,6
print(a)
print(b)
print(c)
if a<b:
    print("okay")
if c<b:
    print("okay")

print("thanks")


# 3.19 Repeat the previous problem with the additional requirement that 'NOT OK' isprinted if the condition is false.
# 

# In[37]:


a,b,c=4,5,6
print(a)
print(b)
print(c)
if a<b:
    print("okay")
if c<b:
    print("okay")
else:
    print("not okay")


# 3.20 Write a for loop that iterate soveralist of strings lst and prints the ﬁrst three characters of every word. If lst is the list ['January', 'February', 'March'] then the following should be printed: 

# In[40]:


lst=['jan','feb','march']
for char in lst:
    print(char)


# 3.21 Write a for loop that iterates over a list of numbers lst and prints the even numbers in the list.For example,if lst is [2, 3, 4, 5, 6, 7, 8, 9],then the numbers 2,4,6, and 8 should be printed.
# 

# In[45]:


lst=[2,3,4,5,6,7,8,9]
for i in lst:
    if i%2==0:
        print("number",'even')
    else:
        print("number is odd ")


# 3.22 Write afor loop that iterates over a list of numbers lst and prints the number sin the list whose square is divisible by 8. For example, if lst is [2, 3, 4, 5, 6, 7, 8, 9], then then umbers 4 and 8 should be printed

# In[1]:


lst=[2,3,4,5,6,7,8,9]
for y in lst:
    if (y**2)%8==0:
        print(y)


# 3.23 Write for loops that use the function range() and print the following sequences: 

# In[2]:


for a in range(0,2):
    print(a)


# In[3]:


for b in range(0,1):
    print(b)


# In[4]:


for c in range(3,7):
    print(c)


# In[5]:


for d in range(1,2):
    print(d)


# In[6]:


for e in range(0,4,3):
    print(e)


# In[7]:


for  f in range(5,22,4):
    print(f)


# 3.24 Implement a program that requests a list of words from the user and then print seach word in the list that is not 'secret'. 

# In[8]:


words=['cia','mi6','secret','isi']
for i in words:
    if i!='secret':
        print(i)


# 3.25 Implement a program that requests a list of student names from the user and prints those names that start with letters Athrough M. 

# In[31]:


lst = ['saqib','Sarfaraz','Ahmed','muhammad']
for i in lst:
    if i[0] in "AaMm":
        print(i)


# 3.26 Implement a program that requests a nonempty list from the user and prints on the screen a message giving the ﬁrst and last element of the list. 

# In[10]:


a=[]
for x in range(0,4):
    num=input("Enter a number: ")
    a.append(num)
print('The first element is:',a[0])
print('The last element is:',a[3])


# 3.27 Implement a program that requests a positive integer n from the user and prints the ﬁrst four multiples of n. 

# In[11]:


n=eval(input('Enter a number: '))
for j in range(0,4):
        print(n*j)


# 3.28 Implement a program that requests an integer n from the user and prints on the screen the squares of all numbers from 0 upto,but not including, n. 

# In[12]:


n=eval(input('Enter a number: '))
for i in range(0,n):
    print(i**2)


# 3.29 Implement a program that requests a positive integer n and prints on the screen all the positive divisors of n.Note: 0 is not a divisor of any integer,and n divides itself

# n=eval(input('Enter a positive integer: '))
# for i in range(1,n+1):
#     if (n%i)==0:
#         print(i)

# 3.30 Implement a program that requests four numbers (integer or ﬂoating-point) from the user.Your program should compute the average of the ﬁrst three numbers and compare the average to the fourt hnumber.If they are equal,your program should print 'Equal'on  the screen. 

# In[14]:



n1=eval(input('Enter a number: '))
n2=eval(input('Enter a number: '))
n3=eval(input('Enter a number: '))
n4=eval(input('Enter a number: '))
av=(n1+n2+n3)/3
if av==n4:
    print('Equal')


# 3.31 Implement a program that requests the user to enter the x and y coordinates (each between − 10 and 10 ) of adart and computes whether the darthashit the dartboard,acircle withcenter (0,0) and radius 8.If so,string It is in!should  be printed on the screen. 

# In[15]:



x=eval(input('Enter the value of X: '))
y=eval(input('Enter the value of Y: '))
r=eval(input('Enter the radius of dartboard: '))
if (x**2)+(y**2) < (r**2):
    print('It is in!')


# 3.32 Write aprogram that requests a positive four-digit integer from the user and prints its digits. You are not allowed to use the string data type operations to do this task. Your program shoulds imply read the input as an integer and process it as an integer,using standard arithmeti coperations(+,*,-,/,%,etc). 

# In[16]:


n=int(input('Enter four integers: '))
x=n%10
y=x-3
for num in range(y,x+1):
    print(num)


# 3.33 Implement function reverse_string() that takes as input a three-letter string and returns the string with its characters reversed.

# In[17]:


def rev_string(x):
    s=''
    for char in x:
        s=char+s
    return s

word=input('Enter a word: ')
rev_string(word)


# 3.34 Implement n function pay() that takes as input two arguments:an hourly wage and the number of hours an employee worked in the last week. Your function should compute and return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at 1.5 times the regular hourly wage.

# In[18]:


def pay(wage_h,hours):
    wage=wage_h*hours
    if hours > 40:
        extra_pay=(wage_h*1.5)*hours
        print('Weekly pay(Included Overtime):',extra_pay)
    else:
        print('Weekly pay:',wage)
        
w=eval(input('Enter wage per hour: '))
h=eval(input('Enter working hours per week: '))
pay(w,h)


# 3.35 The probability of getting n heads in a row when tossing a fair coin n times is 2−n. Implement function prob() that takes a nonnegative integer n as input and returns the probability of n heads in arow when to ssingafair coin n times. 

# In[19]:


def prob(n):
    return 2**(-n)

prob(1)


# 3.36 Implement function reverse_int() that takes a three-digit integer as input and returns the integer obtained by reversing its digits. For example, if the input is 123, your function should return 321. You are not allowed to use the string data type operations to do this task. Your program should simply read the input as an integer and process it as an integer using operators such as // and %. You may assume that the input integer does not endwiththe 0 digit.

# In[20]:


def reverse_int(n):
    x=0
    while(n!=0):
        x*=10
        x+=n%10
        n=n//10
    return x


reverse_int(1234)


# 3.37 Implement function points() that takes as input four numbers x1, y1, x2, y2 that are the coordinates of two points (x1,y1) and (x2,y2) in the plane. Your function should compute: 

# In[21]:



import math
def points(x1,y1,x2,y2):
    d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if x1==0 and x2==0:
        print('The slope is infinity and the distance is',abs(d))
    else:
        m=(y1-y2)/(x1-x2)
        print('The slope is',m,'and the distance is',d)
        
points(0,0,0,1)


# 3.38 Implement function abbreviation() that takes a day of the week as input and returns its two-letter abbreviation. 

# In[22]:



def abbreviation(x):
    return x[0:2]

day=input('Enter the name of day: ')
abbreviation(day)


# 3.39 The computer game function collision() checks whether two circular objects collide;itreturns True if they do and False otherwise.Each circular object will be given by its radius and the (x,y) coordinates of its center. Thus the function will take six numbers as input:the coordinates x1 and y1 of the center and the radius r1 of the ﬁrst circle,and the coordinates x2 and y2 of the center and the radius r2 of these condcircle.

# In[23]:


import math
def collision(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x1-x2)**2+(y1-y2)**2) > (r1+r2):
        return False
    else:
        return True

collision(0,0,3,0,5,3)


# 3.40 Implement function partition() that splits a list of soccer players into two groups. More precisely,it takes a list of ﬁrst names (strings)asinputand prints the names of those soccer players whose ﬁrst name starts with a letter between and including AandM. 

# In[24]:



def partition(x):
    for i in x:
        if i[0] in 'ABCDEFGHIJKLM':
            print(i)
            
partition(['Wassay','Evelyn','Sammy','Owen','Gavin'])


#  3.41 Write function last F() that takes as input two strings of the form 'First Name'and 'LastName', respectively, and returns a string of the form 'LastName, F.'. (Only the initial should be outputfor the ﬁrst name.) 

# In[25]:


def lastF(f,l):
        print(l,f[0]+'.')
        
lastF('Wassay','Sardar')


# 3.42 Implement function avg() that takes as input a list that contains lists of numbers.Each number list represents the grades a particular student received for a course.  here is an input list for a class of four students: [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]

# In[26]:


def avg(x):
    for i in x:
        average=sum(i)/len(i)
        print(average)
        
lists=[[95,92,86,87],[66,54],[89,72,100],[33,0,0]]
avg(lists)


# 3.43 The computer game function hit() takes ﬁve numbers as input: the x and y coordinates of the center and the radius of a circle C, and the x and y coordinates of a point P. The function should return True if point P is inside or on circle C and False otherwise. 

# In[27]:


import math
def hit(x1,y1,r,x2,y2):
    if math.sqrt(((x1-x2)**2)+((y1-y2)**2)) > r:
        return 'false'
    else:
        return True
    
hit(0,0,3,3,0)


# 3.44 Writeafunction distance() that takes as input a number : the time elapsed (inseconds) between the ﬂash and the sound of thunder.Your function should return the distance to the lightning strike in kilometers .The speed of sound is approximately 340. 29 meters per second;there are 1000 meters in one kilometer. 

# In[28]:



def distance(t):
    s=340.29 #The approximate speed of sound.
    d=s*t
    km=d/1000
    return km

distance(3)


# In[ ]:




