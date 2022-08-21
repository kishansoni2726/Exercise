# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:37:34 2022

@author: Kishan
"""
import re
class StringCalculator:
   
    def add(self,numbers):
        #total=0
        if(numbers == ""):
            print("0")
        else:
            num = self.split_into_list(numbers)
            num = self.check_for_alphabet(num)
            num = list(map(int,num))
            num = self.check_greater_than_thound(num)
            num = self.check_for_negative_number(num)
            print(sum(num))
    def split_into_list(self,numbers):
        num = re.split("[,\n]",numbers)
        return num
    def check_for_alphabet(self,num):
        count = 0  
        int_array = []
        for i in range(len(num)):
            if(self.isNumeric(num[i])):
                int_array.append(num[i])
            if(num[i].isalpha()):
                int_array.append(ord(num[i])-96)
            count += 1
        return int_array
    def check_greater_than_thound(self,num):
        for i in num: 
            if(i>1000):
                num.remove(i)
        return num
    def check_for_negative_number(self,num):
        negative = []
        for i in num:
            if(i<0):
                negative.append(i)
                num.remove(i)
        try:
            if(len(negative)>=1):
                raise AssertionError
        except AssertionError:
            print("Negative is not allowed",negative)
        return num
    def isNumeric(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

st = StringCalculator()
st.add("")
st.add("1,2")
st.add("1,2,-2")
st.add("1,2,-1,\n7")
st.add("1,-1,7\n2")
st.add("1,2,a,c")
