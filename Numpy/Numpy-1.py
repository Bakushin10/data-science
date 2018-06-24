
# coding: utf-8

# In[1]:


mylist = [1 , 2, 3]


# In[2]:


import numpy as np


# In[4]:


arr = np.array(mylist)


# In[5]:


arr


# In[6]:


my_mat = [[1,2,3], [4,5,6],[7,8,9]]


# In[7]:


np.array(my_mat)


# In[10]:


np.arange(0, 11,2)


# In[9]:


np.zeros(3)


# In[11]:


np.zeros((5,5))


# In[12]:


np.ones(4)


# In[13]:


np.ones((2,3))


# In[15]:


np.linspace(0,5,100)


# np.linspace(0,5,100) will yield 100 numbers that is evenly spaced

# In[16]:


np.eye(4)


# In[18]:


np.random.rand(5)


# In[21]:


np.random.randn(2)


# In[22]:


np.random.randint(1,100,10)


# np.random.randint(1,100,10) selecting the random number between 1 to 100 and 1 is included and 100 is excluded. the thrid argumanet specifyies the number of item that will be displayed.

# In[24]:


arr = np.arange(25)


# In[25]:


arr


# In[26]:


ranarr = np.random.randint(0,50,10)


# In[32]:


ranarr


# In[34]:


ranarr.max()


# In[35]:


ranarr.argmax()


# ranarr.argmax() returns the index location of the max value

# In[31]:


arr.reshape(5,5)


# In[36]:


arr.shape


# In[38]:


arr = arr.reshape(5,5)


# In[39]:


arr.shape


# In[40]:


arr.dtype

