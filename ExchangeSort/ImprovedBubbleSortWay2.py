#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ImprovedBubbleSortWay2(Data):
    sign=1
    lens=len(Data)
    while sign>0:
        sign=0
        for i in range(1,lens):
            if Data[i-1]>Data[i]:
                temp=Data[i]
                Data[i]=Data[i-1]
                Data[i-1]=temp
                sign=i
        lens=i


# In[2]:


#测试
testData1=[5,1,0,4,8,3,1,2,9]
testData2=[92,149,34,12,193,21,4,0,12,54]

ImprovedBubbleSortWay2(testData1)
ImprovedBubbleSortWay2(testData2)
print(testData1)
print(testData2)

