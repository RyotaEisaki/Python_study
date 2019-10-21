#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3])


# In[3]:


a


# In[4]:


type(a)


# In[5]:


a.shape


# In[6]:


b= np.array([1,2,3],[4,5,6]))


# In[7]:


b= np.array([[1,2,3],[4,5,6]])


# In[8]:


b


# In[9]:


b.shape


# c1 = np.array([0,1,2,3,4,5)]

# In[10]:


c1 = np.array([0,1,2,3,4,5)]


# In[11]:


c1 = np.array([0,1,2,3,4,5])


# In[12]:


c1


# In[13]:


c1.shape


# In[14]:


len(c1)


# In[15]:


c2 = c1.reshape((2,3))


# In[16]:


c2


# In[17]:


c2.shape


# In[20]:


c3 = c2.ravel()


# 

# In[21]:


c3


# In[22]:


c4 = c2.flatten()


# In[23]:


c4


# In[24]:


a.dtype


# In[25]:


d = np.array([1,2],dtype = np.int16)


# In[26]:


d


# In[28]:


d.dtype


# In[29]:


a


# In[30]:


a[0]


# In[31]:


a[1:]


# In[32]:


a[-1]


# In[33]:


b


# In[34]:


b[0]


# In[35]:


b[1,0]


# In[36]:


b


# In[38]:


b[:,2]


# In[39]:


b[1:,2]


# In[40]:


b[1,:]


# In[41]:


b[:,[0,2]]


# In[42]:


a


# In[43]:


a[2]=4


# In[44]:


a


# In[45]:


b


# In[46]:


b[1,2]=7


# In[47]:


b


# In[48]:


b[:,2]=8


# In[49]:


b


# In[50]:


a1=a


# In[51]:


a1


# In[52]:


a1[1] = 5


# In[53]:


a1


# In[54]:


a


# In[56]:


a2=a.copy()


# In[57]:


a2


# In[58]:


a2[0]= 6


# In[59]:


a2


# In[60]:


a


# In[61]:


c2


# In[62]:


c3= c2.ravel()


# In[63]:


c4 =c2.flatten()


# In[64]:


c3[0]=6


# In[65]:


c4[1]=7


# In[66]:


c3


# In[67]:


c4


# In[68]:


c2


# In[69]:


np.arange(10)


# In[72]:


np.arange(1,11)


# In[73]:


np.arange(1,11,2)


# In[74]:


np.random.random((3,2))


# In[75]:


np.random.seed(123)


# In[77]:


np.random.random((3,2))


# In[78]:


np.random.randint(1,10)


# In[79]:


np.random.randint(1,10,(3,2))


# In[80]:


np.zeros(3)


# In[81]:


np.eye(3)


# In[82]:


np.full(4,3.14)


# In[83]:


np.full((4,2),np.pi)


# In[85]:


np.linspace(0,5,3)


# In[86]:


np.linspace(0,np.pi,21)


# In[87]:


l=np.array([2,2,6,1,3])
np.diff(l)


# In[88]:


print(a)


# In[89]:


print(a1)


# In[91]:


np.concatenate([a,a1])


# In[92]:


b


# In[ ]:





# In[93]:


b1=np.array([[10],[20]])


# In[94]:


b1


# In[98]:


np.concatenate([b,b1],axis=1)


# In[96]:


np.hstack([b,b1])


# In[99]:


m=np.arange(0,4)


# In[100]:


m


# In[101]:


n=np.arange(4,7)


# In[102]:


n


# xx, yy = np.meshgrid(m,n)

# In[103]:


xx, yy = np.meshgrid(m,n)


# In[104]:


xx


# In[105]:


yy


# In[ ]:




