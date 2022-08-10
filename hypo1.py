#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[ ]:





# In[ ]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[2]:


x = stats.norm.rvs(30,10,30)
results = stats.ttest_1samp(x, 27)
alpha = 0.05
if (results[0] < 0) & (results[1]/2 < alpha):
    print ("reject null hypothesis, mean is greater than 27")
else:
    print ("accept null hypothesis")


# In[ ]:





# In[ ]:





# In[ ]:




