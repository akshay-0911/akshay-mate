#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# In[ ]:


print("Enter a String: ", end="")
text = input()

textlen = len(text)
for ch in text:
    asc = ord(ch)
    print(ch, "\t", asc)
    


# In[ ]:




