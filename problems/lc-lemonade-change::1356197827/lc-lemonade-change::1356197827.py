class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 5 -> 0
        # 10 -> 5
        # 20 -> 10, 5
        # [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
        five = 0
        ten = 0
        for i in range(len(bills)):
            bill = bills[i]
            if bill == 5:
                five+=1
                continue
            elif bill == 10:
                if five != 0:
                    five-=1
                    ten+=1
                    continue
                return False
            elif bill == 20:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                    continue
                elif five>=3:
                    five-=3
                    continue
                return False
        
        return True
