#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


# In[40]:


#Creating a 100x100 matrix with 100 columns and 100 rows containing random integers with max value of 100.

ary = np.random.randint(100, size=(100,100))  

#To show the dimensions I'll use the below code. 

ary.shape

# The number in the first position shows the row number while the number in the second position shows the column number.


# In[89]:


#To produce a heatmap of my 100X100 matrix, I have used plt.imshow().interpolation= 'nearest' option creates a heatmap with higher resolution.

plt.imshow(ary, interpolation= 'nearest')
plt.show()


# In[100]:


#To filter out the odd numbers (or select the even ones in other words), I created a logical vector that returns True for even numbers.

even = (ary % 2 == 0 )
print(even)


# In[103]:


#If I want to see the numbers as they are, I need to use ary[even].

print(ary[even])


# In[102]:


#To convert the logical vector to integers, I have used .astype option and called it ary_even_int

ary_even_int = even.astype(int)
print(ary_even_int)


# In[97]:


ary.shape #Shape of my starting matrix.


# In[98]:


ary_even_int.shape #To show that the shape of the array is preserved.


# In[104]:


#To create the heatmap of my new array, I have used the below code.

plt.imshow(ary_even_int, interpolation='nearest')
plt.show()

