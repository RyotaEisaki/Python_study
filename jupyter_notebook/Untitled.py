#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+1


# In[6]:


names=['spam', 'ham', 'eggs']
lens =[]
for name in names:
    lens.append(len(name))
lens


# In[7]:


get_ipython().run_line_magic('timeit', '-n 1000 -r 10 [ x*x for x in range(1000)]')


# In[8]:


get_ipython().run_cell_magic('timeit', '-n 1000 -r 10', '\nret = []\nfor x in range(1000):\n    ret.append(x*x)')


# In[9]:


get_ipython().system('pip list')


# In[10]:


get_ipython().system('ls')


# In[ ]:




