# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
'''name = input("Enter your name:")
print("Hello "+name)'''
'''
# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
def computepay(hours,rate):
    if hours>40:
        print(f"Pay: {str(40*rate+(hours-40)*rate*1.5)}")
    else:
        print(f"Pay: {str(hours*rate)}")

try:
    hours = int(input("Enter hours:"))
    rate = float(input("Enter rate:"))
    computepay(hours,rate)
    
except ValueError:
    print("Error, please enter numeric input")
'''
'''
# Exercise 4: Assume that we execute the following assignment statements:

width = 17
height = 12.0

print(width//2)
print(width/2.0)
print(height/3)
print(1+2*5)

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

temperature = float(input("Enter Temperature in Celcius: "))
print(str(temperature*9/5+32)+" F")'''

# Exercise 6
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
'''
def computegrade(grade):
    if grade >= 0.9:
        score = 'A'
    elif grade >= 0.8:
        score = 'B'
    elif grade >= 0.7:
        score = 'C'
    elif grade >= 0.6:
        score = 'D'
    else:
        score = 'F'

    print(score)

try:
    grade = float(input("Enter grade:"))
    computegrade(grade)

except:
    print("Bad Score")'''

'''import random
print(random.randint(0,10))'''

#EXERCISE 1

""" Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number. """

""" list = []

while True:
    try:
        number = input("Enter a number: ")
        if number.lower() == "done":
            break
        else:
            list.append(int(number))
    except ValueError:
        print("Error in number")
        continue
print(max(list), min(list)) """

""" str = 'X-DSPAM-Confidence:0.8475'
a = str.find(":")
print(float(str[a+1:])) """
""" 
# 7.11
total = 0
count = 0

filename = input("Enter the name of the file:")
file = open(filename)
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        n = line.find(":")
        number = float(line[n+2:n+7])
        count+=1
        total+=number
print("Average spam confidence:", total/count) """

# LISTS CHAPTER 8
poem = open("romeo.txt")
words = []
for line in poem:
    line = line.split()
    for word in line:
        if word not in words:
            words.append(word)
words.sort()
print(words)
