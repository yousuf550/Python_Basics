#!/usr/bin/env python
# coding: utf-8

# # For Loop

# In[1]:


print("Nasir")
print("Nasir")
print("Nasir")
print("Nasir")
print("Nasir")
print("Nasir")


# In[2]:


for a in range(5):   #10 exlusive
    print(a,"nasir")


# In[3]:


print(a)


# In[4]:


for number in range(1,10):
    print(number)


# In[5]:


for number in range(1,10,2):
    print(number)


# In[6]:


for number in range(10,1,-1):
    print(number)


# In[7]:


cities = ["Karachi", "Lahore", "Multan"]


# In[8]:


cities


# In[9]:


for city in cities:
    print(f"The city under consideration is {city}")


# In[10]:


for num in [11, 12, 12, 44, 55]:
    print(num)


# In[11]:


country = "Pakistan"


# In[12]:


for char in country:
    print(char)


# In[13]:


for number in range(10):
    if number %3==1:
        break
    print(number)


# In[14]:


for numbers in range(10):
    if numbers==7 or numbers==4:
        continue
    print(numbers)


# In[15]:


city_to_check = "Faislabad"
cleanest_city = ["Karachi", "Faislabad", "Islamabad", "Lahore", "Multan"]


# In[16]:


for a_clean_city in cleanest_city:
    if city_to_check == a_clean_city:
        print("{} is one of the cleanest cities".format(city_to_check))
    


# In[17]:


for a in range(0,50,5):
    print(a)


# In[18]:


#Nested Loop
first_name = ["Ali", "Kasim", "Zia", "Jafar"]
last_name = ["Mustafa", "Ibrahim", "Moosa", "Ijaz", "Kazim"]
full_name = []
for a_first_name in first_name:
    for a_last_name in last_name:
        full_name.append(a_first_name + " " + a_last_name)
print(full_name)


# In[19]:


a = 10
b = float(a)
print(b)


# In[20]:


for a in range(5):
    print("Inner loop begins")
    for char in "China":
        print(a, char)


# In[38]:


table = int(input("Enter Table Number: "))
for a in range(1,10):
    print(table, "*", a, "=" ,table * a)


# In[43]:


table_number = int(input("Enter table number "))
for a in range(1,11):
    print(f"{table_number} * {a} = {table_number * a}")


# In[52]:


tables = int(input("Enter tables "))
for table in range (2, tables+1):
    for num in range(1,11):
        print(f"{table} * {num} = {table*num}")


# In[61]:


#Type Casting
userInput = input("Enter something ")  #input always give string reslult
type(userInput)


# In[67]:


#Changing case
name_a = "yOusUf"
print(name_a.lower())
print(name_a.title())
print(name_a.upper())


# # Dictionary 

# In[70]:


customer = {
    "first name": "Ali",
    # key         Value
    "last name": "Akbar",
    "address": "Silicon Valley, California"
}
print(customer["address"])


# In[ ]:





# In[ ]:




