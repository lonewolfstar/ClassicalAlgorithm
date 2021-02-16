#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findMin(Data,index):
    """寻找最小值"""
    sign=index
    mins=Data[index]
    t=index
    while t<len(Data):
        if mins>Data[t]:
            mins=Data[t]
            sign=t
        t+=1
    return sign


# In[2]:


def SimpleSelectionSort(Data):
    """简单选择排序"""
    for i in range(len(Data)):
        pos=findMin(Data,i)#返回[i,len(Data))之间的最小值的坐标
        temp=Data[i]#将当前值与最小值交换
        Data[i]=Data[pos]
        Data[pos]=temp
    return Data


# In[3]:


#测试
testData1=[6,9,10,5,8,3,1,2,1,0,7,100]
testData2=[19,0,54,26,73,12,90,131,413,263]

result1=SimpleSelectionSort(testData1)
result2=SimpleSelectionSort(testData2)

print(result1)
print(result2)


# In[ ]:




