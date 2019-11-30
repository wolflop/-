# -*- coding:utf-8 -*-
#filename:sort.py
'''
本段代码会写入很多排序实例
'''
class solution:
    def __init__(self, seq):
        self.seq = seq
     
    #迭代的方式插入排序
    '''
    插入排序：假定n-1个元素已经排序完成，第n个元素插入到正确的位置上
    '''
    def ins_sort(self):
        for i in range(len(self.seq)):                  #选择i在self.seq中从0到len（self.seq）递增
            j = i                                       #选出j，j=i，让j递减，在i的范围内比较大小，按照从小到大排序
            while j > 0 and seq[j-1] > seq[j]: 
                seq[j-1], seq[j] = seq[j], seq[j-1]
                j -= 1
         return self.seq                                #返回排序的self.seq
      
      #迭代的方式选择排序
      '''
      先找到其中最大的元素放到n的位置上，然后继续比较余下的值。
      '''
      def sel_sort(self):
        for i in range(len(self.seq)-1, 0, -1):         #选择i在self.seq中循环，从到小，递减
            max_j = i                                   #先将i赋值给max_j
            for j in range(i):                          #j在i中循环，选出最大的max_j,依次从大到小排序
                if self.seq[j] > self.seq[max_j]:
                    max_j = j
                self.seq[i], self.seq[max_j] = self.seq[max_j], self.seq[i]
        return self.seq
        
        
        
      
    
  

