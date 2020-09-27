#print("Hello World")
#print(5+5)

'''Rules for creating variables'''
# 1. Variable should start with a letter or an underscore 
# 2. Variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive (e.g Yousuf and yousuf are two difference variables)

#a = 3
#b = "Yousuf"
#c = 23.3
#print (a + c)
#print (type(a))
#print (type(b))
#print (type(c))
#typeA = type(a)
#typeB = type(b)
#print(typeA,typeB)

#name = '''Amir 
#is a good boy'''
#name = "Yousuf"
#var = name.upper()
#var = name.replace("u", "l")
#print(name[2:5])
#print(var) 
#print(len(name))

'''
name1 = "Salim"
name2 = "Kashif"
template = "This is a {1} and he is a good boy named {0}". format (name1, name2)
print(template)
'''
#Turte move program
'''import turtle
my_turtle = turtle.Turtle()

def square(length,angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

for i in range(10):
    square(100, 90)'''

'''my_turtle = turtle.Turtle()

def circle(length,angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

for i in range(50):
    circle(70, 45)
'''

'''
full_name = 'John Smith'
age = 20
is_new = True
name = input('What is your name? ')
fav_color = input('What is your favourite color? ')
print (name + ' likes ' + fav_color)
'''
#Birth Year Program
'''     birth_year = input ('Your Birth Year: ')
current_year = input ('Current Year: ')          
print(int(current_year) - int(birth_year)) '''

#Pound to Kgs Program
'''     weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)    '''

#Three quote (''') also use to break lines
#email = '''Hi John,

#Here is our first email to you.

#Thank you,
#Support Team''' 
#print(email) 

# Slicing [#START:STOP:STEP]
'''course = 'Python for Beginners'
print(course)
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
print(course[0:3]) #Prints starts index 0 to 3 but exclude index 3, it prints upto index 2 
print(course[1:]) #Print upto last index in variables
print(course[:5]) #If we not write start index then python will assume 0 is starting index 
name = 'Yousuf'
print(name[1:-1])
'''

#Formated string
'''first = 'Yousuf'
last = 'Hanif'
message = first + ' [' + last + '] is a coder'
print(message)
msg = f'{first} [{last}] is a coder' #Foramted string 
print(msg) '''

#
'''name = 'Muhammad Yousuf'
print(len(name)) 
print(name[::-1]) #Reverses name
print(name.upper())
print(name.find('Y'))
print(name.replace('Yousuf', 'Yousuf Hanif'))
'''

'''import math
x = 2.9
print(round(x))
'''

#IF STATEMENT 
#1
'''
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")         #Second msg 

#2
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: ${down_payment}")

#3
has_high_income = True
has_good_credit = False

if has_good_credit and has_high_income:
    print('Eligible for loan')

if has_good_credit or has_high_income:
    print('Eligible for loan')

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')

#4
temperature = 40

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#5
name = input("Enter Your Name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 10:
    print("Name must be a maximum of 10 characters")
else:
    print("Name looks good!")
'''

#Weight conversion lbs & kgs
'''
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

'''
#Loop
'''
i = 1
while i <= 10:
    print( i)
    i = i + 1
print("Done")
'''

#Guess number 
'''secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')
'''

#Car game
'''
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to star the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break 
    else:
        print("Sorry, I don't understand that!")
'''
#print("Harry is \n good boy \t1")  #Escape sequence charachters (\n used for new line & \t used for tab space)
#print(10 * "Yousuf\n")

'''Num1 = input("Enter first number: ")
Num2 = input("Enter second number: ")
print("Sum: ", int(Num1) + int(Num2))'''

'''
name = "Muhammad Yousuf".lower()
print(name.endswith("yousuf"))
print(name.count("m"))
print(name.find("yousuf"))
print(name.replace("yousuf","Yousuf Hanif"))'''

#List
'''grocery = ["Harpic", "vim bar", "deodran", "Bhindi", "Lollypop"]  #List
print(grocery)
print(grocery[0])
numbers = [2, 7, 2, 4, 26, 27, 24, 12]  #List
numbers[1] = 4    #List can changeable
numbers.sort()      #to sort out numbers
numbers.reverse()   #to reverser numbers
print(numbers)
print(numbers[3])
print(max(numbers))
numbers.append(9)    #through append values add only in end of list
numbers.insert(2,  45)    #Insert use for add value any where in list (1st write index no & second write values you want to add in bracket)  
numbers.remove(27)
print(numbers)
numbers.pop()   #last value remove throught pop
print(numbers)'''

#list can change   (List should be make throught square bracket[])
#Tupple cannot change (Tuppe should be make throught  paranthesis () )
#Tupple
'''nos = (1, 3, 5, 6, 4)
print(nos)
#nos[1] = 3   #tupple value cant change

noslist = list(nos) #Throught this method we can change tuple valuse
noslist[1] = 5
nos = tuple(noslist)
print(nos)
del nos     #del keyword can delete the tuple completely
print(nos)   #this will raise an error because the tuple no longer exists
'''