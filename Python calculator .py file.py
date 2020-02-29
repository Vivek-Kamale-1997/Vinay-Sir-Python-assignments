#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1=int(input('Enter 1st num:'))


# In[2]:


num2=int(input('Enter 2nd num:'))


# In[3]:


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


# In[4]:


choice = input("Enter choice(1/2/3/4): ")


# In[9]:


if choice == '1':
    add=num1+num2
    print(add)

elif choice == '2':
    sub=num1-num2
    print(sub)

elif choice == '3':
    mul=num1*num2
    print(mul)

elif choice == '4':
    div=num1/num2
    print(div)
else:
   print("Invalid input")


# In[ ]:




