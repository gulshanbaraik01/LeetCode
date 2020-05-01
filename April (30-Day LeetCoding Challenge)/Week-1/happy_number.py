class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0;
        temp = [];

        while 1:
           for i in str(n): 
              sum += int(i)**2;         
           n = sum;
           if(n in temp):
               break;
           else:
               temp.append(n);
           sum = 0;

        if(n==1):
           return True;
        else:
           return False;