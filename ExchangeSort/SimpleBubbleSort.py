#!/usr/bin/env python
# coding: utf-8

# In[1]:


def SimpleBubbleSort(Data):
    """简单冒泡排序"""
    for i in range(len(Data)):
        for j in range(len(Data)-i-1):
            if Data[j]>Data[j+1]:
                temp=Data[j]
                Data[j]=Data[j+1]
                Data[j+1]=temp


# In[2]:


#测试
testData1=[5,1,0,4,8,3,1,2,9]
testData2=[92,149,34,12,193,21,4,0,12,54]

SimpleBubbleSort(testData1)
SimpleBubbleSort(testData2)
print(testData1)
print(testData2)

