class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) == 1:
            return asteroids
        res = []
        res.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if asteroids[i] < 0:
                j = len(res)-1
                while(j>=0): 
                    if(res[j] > 0):
                        if abs(asteroids[i]) > abs(res[j]):
                            del res[j]
                            j -= 1
                            continue
                        elif abs(asteroids[i]) == abs(res[j]):
                            del res[j]
                        break
                            
                   
                    else:
                        res.append(asteroids[i])
                        break
                if j < 0:
                    res.append(asteroids[i])
                
            else:
                res.append(asteroids[i])
   
        return res
                        
                        
            
