#!/usr/bin/env python
# coding: utf-8

# #Day2
# #

# In[94]:


nums2=list(range(10))
print("List=",nums2)

a=int(len(nums2)/2)
b=int(len(nums2))

x=slice(0,a)
y=slice(a,b)
print("Swap List= " ,nums2[y]+nums2[x])


# In[96]:


num = int(input("Enter a number: "))
for i in range(num+1):
    if (i % 2) == 0:
        print(i)


# Day3
# 

# #User login application

# In[15]:


name=input("Username=")
password=input("password")

if name=="sezin" and password=="123":
    print("You've passed")
elif name !="sezin" and password =="123":
    print("Check the Username")
elif name =="sezin" and password !="123":
    print("Check the password")
else:
    print("Check username and password")


# #Extra

# In[21]:


myDict= {"sezin":"123",
         "mehmet":"111",
          "ayşe":"222"}

name=input("Username=")
password=input("password")

if name in myDict.keys() and password == myDict[name]:
    print("Correct username and password")
    pass
else:
    print("Incorrect username/password")
    pass


# #Day4 Prime Numbers

# In[34]:


for i in range(1,101):
    count = 0
    for a in range(2,(i//2+1)):
        if (i%a) == 0:
            count=count+1
            break
    
    if(count==0 and i!=1):
        print(i)


# #Day-5
# 

# In[93]:


class Animals:
    def __init__(self,types,classificaion):
        self.types=types                  
        self.classificaion=classificaion  

        
class Dogs(Animals):
    def __init__(self,types,classificaion,bark):
        super().__init__(types,classificaion)
        self.bark=bark
    def yaz(self):
        print("Dog")
        print("Type = ",self.types)
        print("Classificaiton = ",self.classificaion)
        print("Barking = ",self.bark)



class Cats(Animals):
    def __init__(self,types,classificaion,color):
        super().__init__(types,classificaion)
        self.color=color
    def yaz(self):
        print("Cat")
        print("Type = ",self.types)
        print("Classificaiton = ",self.classificaion)
        print("Color = ",self.color)


kopek=Dogs("vertebrates","mammals","yes")
kopek.yaz()

kedi=Cats("vertebrates","mammals","white")
kedi.yaz()


# In[ ]:




