#!/usr/bin/env python
# coding: utf-8

# In[1]:


def TwoWayInsertionSort(Data):
    first=0            #first、final分别指示Sort中排好序的记录的第1个和最后1个记录的位置
    final=0
    lens=len(Data)
    Sort=[0 for i in range(lens)]
    
    Sort[0]=Data[0]
    for i in range(1,lens):
        if Data[i]<=Sort[first]:      #待插入记录小于Sort中最小值，插入到Sort[first]之前（不需移动Sort数组的元素）
            first=(first-1+lens)%lens
            Sort[first]=Data[i]
        else:
            if Data[i]>=Sort[final]:  #待插入记录大于Sort中最大值，插入到Sort[final]之后（不需移动Sort数组的元素）
                final+=1
                Sort[final]=Data[i]
            else:
                if Data[i]>Sort[first] and Data[i]<Sort[final]: #待插入记录大于Sort中最小值，小于d中最大值，插入到Sort的中间（需要移动Sort数组的元素）
                    j=final
                    final+=1
                    while Data[i]<Sort[j]:
                        Sort[(j+1)%lens]=Sort[j]
                        j=(j-1+lens)%lens
                    Sort[(j+1)%lens]=Data[i]    
    for i in range(lens):#循环把Sort赋给Data
        Data[i]=Sort[(i+first)%lens]


# In[2]:


#测试
testData1=[5,1,0,4,8,3,1,2,9]
testData2=[92,149,34,12,193,21,4,0,12,54]

TwoWayInsertionSort(testData1)
TwoWayInsertionSort(testData2)
print(testData1)
print(testData2)

