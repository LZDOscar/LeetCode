class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s)-1
        forks,forke = -1, -1
        count = 0
        while(start < end):
           
    
            if(s[start] == s[end]):
                start += 1
                end -= 1
            else:
                count += 1
                if count==1 and s[start] == s[end-1] and s[start+1] == s[end]:
                    forks, forke = start+2, end-1
                    start += 1
                    end -= 2
                    
                elif s[start] == s[end-1]:
                    start += 1
                    end -= 2
                   
                elif s[start+1] == s[end]:
                    start +=2
                    end -= 1
                   
              
                if count >=2 :
                    if forks != -1:
                        start, end = forks, forke
                        forks, forke = -1, -1
                        count = 1
                    else:
                        return False  
   
  
        return True
            
