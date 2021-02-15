#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find(Data,target):
    low=0
    high=len(Data)-1

    while low<=high:
        mid=int((low+high)/2.0)
        if target>Data[mid]:
            low=mid+1
        if target<Data[mid]:
            high=mid-1
        if target==Data[mid]:
            return mid
    return None


# In[4]:


#测试
testData1=[1,2,3,4,5,6,7,8,9,10]
testData2=[33,35,78,93,102,159,253,673,792]

print(find(testData1,10))
print(find(testData2,792))


# In[ ]:




