#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List

alist = ["nasir", "ali", "faisal", "kazim"]
#Index      0       1       2         3 


# In[2]:


alist


# In[3]:


alist


# In[4]:


city1 = "Karachi"
city2 = "Lahore"
city3 = "Islamabad"
city4 = "Quetta"

cities = ["Karachi", "Lahore", "Islamamad", "Quetta", "Faisalabad"]


# In[5]:


cities


# In[6]:


#how to access members

alist[1]


# In[7]:


cities[3]


# In[11]:


fruits=[]


# In[12]:


len(fruits)


# In[13]:


len(cities)


# In[14]:


len(alist)


# In[15]:


#adding a memeber to the list (append & insert)

fruits.append("apples")            #append by default add items at the end of list
                                   #append only add one items 


# In[16]:


fruits


# In[17]:


fruits.append("orange")


# In[18]:


fruits


# In[19]:


fruits.insert(3,"mango")           #through insert add items where u want to add in the list 
                                   #insert also only add one items 


# In[20]:


fruits


# In[22]:


fruits.extend(["banana", "orange", "strawberry","cherry"]) #Through extend one or more value add in list
fruits


# In[23]:


fruits.count("orange")


# In[24]:


fruits.index("orange")


# In[25]:


fruits.clear()


# In[26]:


fruits


# In[30]:


fruits.extend(['apples','orange','mango','banana','orange','strawberry','cherry'])


# In[31]:


fruits


# In[32]:


fruits2 = fruits.copy() #by value copy


# In[33]:


fruits


# In[34]:


fruits2


# In[35]:


fruits3 = fruits # by reference 


# In[36]:


fruits3


# In[37]:


fruits.append("Peach")


# In[38]:


fruits


# In[39]:


fruits3  #by reference


# In[40]:


fruits2  # new fruits not shown in fruits2 because of copy


# In[41]:


#Removing items from a list  (del, remove, pop)
   
del fruits2[1]       #orange remove from fruits2


# In[42]:


fruits2


# In[44]:


fruits2.remove("orange")


# In[45]:


fruits2


# In[46]:


fruits.pop()


# In[51]:


cities


# In[57]:


cities_poped = cities.pop()  #through pop remove & added into new variable
print(f"This city is popped from list {cities_poped}")
print(f"The remaining cities {cities}")


# In[54]:


cities_poped


# In[58]:


cities = ['Karachi', 'Lahore', 'Islamamad']


# In[64]:


cities


# In[ ]:





# In[67]:


cities.extend(["Multan", "Lahore", "Faislabad", "Sialkot"])
cities


# In[68]:


cities.sort()  #by defaul sort by alphabaticaly


# In[69]:


cities


# In[70]:


cities.sort(reverse=True)


# In[71]:


cities


# In[73]:


cities.reverse()


# In[77]:


cities


# In[76]:


len(cities)


# In[80]:


cities


# In[82]:


print(cities[2])


# In[84]:


cities.append("Islamabad")


# In[85]:


print(cities)


# In[88]:


cities.insert(2,"Peshawar")


# In[89]:


cities


# In[90]:


del cities[2]


# In[91]:


cities


# In[93]:


cities.remove("Karachi")


# In[94]:


cities


# In[99]:


cities


# In[101]:


cities.index("Lahore") #for find 


# In[102]:


"Lahore" in cities #for find


# In[103]:


"Karachi" in cities


# In[104]:


cities


# In[107]:


cities.extend(["Karachi", "Peshawar", "Hyderabad"])


# In[108]:


cities


# In[109]:


print(cities[1:3])    #star index (1) inclusive & stop (3) exlusive 


# In[110]:


print(cities[2:4])


# In[112]:


#Index       -7       -6       -5        -4         -3        -2         -1
students = ["Ali", "Fatima", "Kashif", "Saleem", "Abdullah", "Saif", "Ibrahim"]
#Index       0       1          2         3          4         5        6


# In[113]:


students[4]


# In[114]:


print(students[0])
print(students[-7])


# In[116]:


students[2:4]             #Start:End   (End not include)
             


# In[117]:


students[-6:-4]


# In[118]:


students[3:]


# In[119]:


students[ : 4]


# In[120]:


students[4:-1]


# In[127]:


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
nums


# In[124]:


nums [0:18:1] #step wise


# In[128]:


nums [0:18:2]


# In[129]:


nums [::4]


# In[131]:


del nums[3]


# In[132]:


nums


# In[133]:


del nums[2:4]


# In[134]:


nums


# In[135]:


nums.remove(6)


# In[136]:


nums


# In[137]:


nums.pop()


# In[138]:


nums


# In[142]:


nums.pop(1)


# In[143]:


nums


# # Tuples       (Not changebale, Immutable)
# 

# In[144]:


atupple = ("salim", 214, "nasir" )


# In[145]:


len(atupple)


# In[147]:


del atupple(2)


# In[148]:


atupple[2]


# In[149]:


a = 1, "haseeb", "imran" 


# In[150]:


a


# In[151]:


a.index("haseeb")


# In[153]:


a.count("haseeb")


# In[ ]:




