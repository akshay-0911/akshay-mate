#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that accepts a word from the user and reverse it.
# 

# In[ ]:


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s =input("Enter a word")
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string is : ", end="")
print(reverse(s))


# In[ ]:




