class Solution:
    def arraysum(self,num):
        return self.sum(num,0)
        

    def sum(self, num,left) :
        if left>=len(num):
            return 0

        return num[left]+self.sum(num,left+1) 
    
if __name__=="__main__":
    solution=Solution()
    num=[1,3,5]
    result=solution.arraysum(num)   
    print(result) 