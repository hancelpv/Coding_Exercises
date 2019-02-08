
# coding: utf-8

# In[6]:


series = [0, 1]


# In[7]:


# Taking User input 
num_points = int(input("Enter num of terms required in Fibonacci Sequence :"))


# In[8]:


for i in range(2, num_points+1):
#     print(i)

    temp = series[i-1] + series[i-2]
    
    series.append(temp)


# In[9]:


series.pop(0) # removing first element - zero
series

