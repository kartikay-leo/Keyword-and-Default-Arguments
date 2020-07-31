#!/usr/bin/env python
# coding: utf-8

# In[82]:


## CUBE
## without parameters
def cube():
    x=int(input("Enter the Number: "))
    print(x**3)
    


# In[83]:


cube()


# In[84]:


## with parameters
def cube_3(x):
    print(x**3)


# In[85]:


x=int(input("Enter the Number: "))
cube_3(x)


# In[86]:


## CIRCLE
## without parameters
def area():
    r=float(input("Enter the Radius of the Circle: "))
    f=3.14*r**2
    print('The area of the circle is: ',f)


# In[87]:


area()


# In[88]:


## with parameters
def area_1(a):
    f=3.14*a**2
    print('The area of the circle is: ',f)


# In[89]:


a=float(input("Enter the Radius of the Circle: "))
area_1(a)


# In[97]:


## sum of numbers from n1 to n2
## without parameters
def num():
    n1=int(input("Enter the 1st Number: "))
    n2=int(input("Enter the 2nd Number: "))
    c=0
    for i in range(n1,n2+1):
        c=c+i
    print('Sum of two numbers is:',c)
        


# In[36]:


num()


# In[98]:


## with parameters
def number(x1,x2):
    cnt=0
    for i in range(x1,x2+1):
        cnt=cnt+i
    print('Sum of two numbers is:',cnt)


# In[41]:


x1=int(input("Enter the 1st Number: "))
x2=int(input("Enter the 2nd Number: "))
number(x1,x2)


# In[99]:


## KEY WORD
def key(y1,y2):
    ct=0
    for i in range(y1,y2+1):
        ct=ct+i
    print('Sum of two numbers is:',ct)
    


# In[91]:


key(y2=8,y1=4)


# In[100]:


## DEFAULT
def defa(z1,z2=9):
    cnt=0
    for i in range(z1,z2+1):
        cnt=cnt+i
    print('Sum of two numbers is:',cnt)


# In[93]:


z1=int(input("Enter the 1st Number: "))
defa(z1)


# In[94]:


#### CONCATINATE STRINGS
def st(s1,s2):
    print(s1,s2)


# In[74]:


s1=input('Enter the 1st string: ')
s2=input('Enter the 2nd string: ')
st(s1,s2)


# In[95]:


## KEY WORD
def mk(a2,a1):
    print(a1,a2)


# In[77]:


mk(a1='Hello',a2='Mam!')


# In[96]:


## DEFAULT 
def df(b1,b2,b3='are',b4='you.'):
    print(b1,b2,b3,b4)


# In[81]:


b1=input('Enter the 1st string: ')
b2=input('Enter the 2nd string: ')
df(b1,b2)


# In[ ]:


##################################    THE END    ###############################

