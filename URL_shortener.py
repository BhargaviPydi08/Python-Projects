#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyshorteners


# In[2]:


pip install pyperclip


# In[17]:


import pyperclip
import pyshorteners
from tkinter import *


# In[20]:


s = pyshorteners.Shortener()
long_url = input()
short_url = s.tinyurl.short(long_url)
print("The short URL is : ",short_url)


# In[ ]:




