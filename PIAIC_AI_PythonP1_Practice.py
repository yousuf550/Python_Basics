#!/usr/bin/env python
# coding: utf-8

# In[2]:


num1 = 13
num2 = 3


# In[3]:


print("Remainder of", num1, num2, "is ", (num1 % num2))


# In[4]:


num3 = 9
x = int(input("Enter increment value: "))
num3 += x  #num3 = num3 + x
print(num3)


# In[5]:


num4 = 4


# In[6]:


print(num4)


# In[7]:


total_cost = 1 + 4 * 3


# In[8]:


total_cost


# In[9]:


total_cost2 = 1 + (3 * 3)


# In[10]:


total_cost2


# In[11]:


cost = (1 + 2) * (4 - 3)
cost


# In[12]:


cost2 = (2 + (2 * 3)) / 2


# In[13]:


cost2


# In[14]:


typ(cost2)


# In[ ]:


species = "cat"
if species == "cat":
    print("Yep, it's cat.")


# In[ ]:


if 2 + 2 == 4:
    print("Everything make sense.")


# In[ ]:


number_of_husbands = 2
if number_of_husbands != 1:           # != means not equal to
    print("So far so good")
    print("Congratulatios")
    print("All done")


# In[ ]:


lucky_ticket_number = 123451
if lucky_ticket_number != int(input("Enter your ticket number: ")):
    print("Better luck next time.")


# In[17]:


lucky_ticket_number = 123451
if lucky_ticket_number == int(input("Enter your ticket number: ")):
    print("Congratulation you won!")
else:
    print("Better luck next time")


# In[11]:


name = "Ijaz"
age = 23
print("My name is " + name + " and My Age is " + str(age)) #1st method to concatenate strings


# In[12]:


print("My name is {} and My Age is {}".format(name, age)) #2nd method to concatenate 


# In[13]:


print("My name is {1} and My Age is {0}".format(name, age)) 


# In[14]:


print("{0} is my student. {0} is a very good student. He is {1} years old".format(name,age))


# In[17]:


print("My name is {a} and My Age is {b}".format(a=name, b=age))  #through key


# In[22]:


print(type(age))


# In[23]:


print(3 > 5)


# In[24]:



print(3 < 4)


# In[25]:


#comparison operator
'''
<
>
<=
>=
==
!=

'''


# In[28]:


available_drink = input("Do you have pepsi ")
if available_drink =="yes":
    print("Plz Give me a Jumbo Pack")


# In[4]:


age = int(input("what is your age? "))
if age >= 18:
    print("allowed to ride")
else:
    print("not allowed")


# In[11]:


per = int(input("Enter your percentage % "))
if per >= 80 and per <= 100:
    print("A+")
elif per >= 70 and per < 80:
    print("A")
elif per >= 60 and per < 70:
    print("B")
elif per >= 0 and per < 60:
    print("Fail")
else:
    print("You have given inappropriate %")


# In[13]:


a = 5
b = 2
c = 6
d = 6
e = 1
f = 8
g = 10
x = 4
y = 4
h = 0

if (x == y or a == b) and c == d:
    g = h
    print(g)
else:
    e = f
    print(e)
    


# In[14]:


tp = ("ali", "umer", "salim")


# In[15]:


tp


# In[18]:


tp[1] = "aslam"


# In[19]:


print(tp)


# In[20]:


tp[1]


# In[ ]:




