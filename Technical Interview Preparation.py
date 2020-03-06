#!/usr/bin/env python
# coding: utf-8

# In[14]:


def pair_sum(arr, key):
    p = set()
    for i in arr:
        x = key - i
        if x not in p and x in arr:
            print ( "[",i,",",x,"]")
        p.add(x)
        p.add(i)


# In[15]:


pair_sum([1,3,2,2,4,5,6,7],8)


# In[16]:


def find_missing_element(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    for i, j in zip(arr1, arr2):
        if i != j:
            return i


# In[17]:


find_missing_element([1,2,3,4,5,6,7], [3,7,2,1,4,6])


# In[1]:


def string_compression(s):
    length = len(s)
    
    if length == 0:
        return "Invalid Input"
    
    elif length == 1:
        return s + "1"
    
    count = 1
    
    result = ""
    
    for i in range(1, length):
        if s[i] == s[i-1]:
            count += 1
            
        else:
            result += s[i-1] + str(count)
            count = 1
            
    result += s[i-1] + str(count)
    
    return result


# In[2]:


string_compression("AAABBCCCCDEE")

