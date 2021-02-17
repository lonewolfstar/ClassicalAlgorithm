#!/usr/bin/env python
# coding: utf-8

# In[1]:


def DirectInsertionSort(Data):
    """直接插入排序"""
    i=1
    while i<len(Data):
        sign=Data[i]
        j=i-1
        while Data[j]>sign and j>=0:
            Data[j+1]=Data[j]
            j-=1
        Data[j+1]=sign
        i+=1


# In[2]:


#测试
testData1=[5,1,0,4,8,3,1,2,9]
testData2=[92,149,34,12,193,21,4,0,12,54]

DirectInsertionSort(testData1)
DirectInsertionSort(testData2)
print(testData1)
print(testData2)

