#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
arr1 = np.array([1,2,3])
print(arr1)


# In[4]:


arr1[2]


# In[5]:


arr1[2] = 5


# In[6]:


arr1


# In[8]:


arr2 = np.array([[1,2,3] , [4,5,6]])
print(arr2)


# In[9]:


print("The shape is 2 rows and 3 columns:", arr2.shape)


# In[11]:


print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1, 0])


# In[12]:


arr3 = np.array(['India', 'China', 'USA', 'Mexico'])
print(arr3)


# In[45]:


arr3[1]


# In[38]:


arr = np.arange(0, 20, 2)
print(arr)


# In[40]:


arr = np.linspace(0, 10, 20)
print(arr)


# In[44]:


arr = np.random.rand(10)
print(arr)
print('\n')
arr = np.random.rand(3,4)
print(arr)


# In[46]:


print(np.full((4,6), 10))


# In[48]:


arr = [0, 1, 2]
print(np.repeat(arr, 3))


# In[50]:


arr = [0, 1, 2]
print(np.tile(arr, 3))


# In[51]:


identity_matrix = np.eye(3)
print(identity_matrix)


# In[52]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[54]:


arr = np.random.rand(5,5)
print(arr)


# In[55]:


print(np.sum(arr, axis = 0))


# In[56]:


print(np.sum(arr, axis=1))


# In[58]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[59]:


arr = np.random.rand(5,5)
print(arr)


# In[60]:


print(np.sort(arr, axis=1))


# In[61]:


arr = np.array([4,5,6,7])


# In[62]:


arr1 = np.append(arr, 8)
arr1


# In[63]:


arr2 = np.append(arr, [9,10,11])
print(arr2)


# In[65]:


arr2 = np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5 = np.delete(arr2, [1,4])
print(arr5)


# In[74]:


arr1 = np.array([[1,2,3,4], [1,2,3,4]])
arr2 = np.array([[5,6,7,8],[5,6,7,8]])


# In[75]:


cat = np.concatenate((arr1,arr2), axis=0)
print(cat)


# In[76]:


cat = np.concatenate((arr1,arr2), axis=1)
print(cat)


# In[ ]:




