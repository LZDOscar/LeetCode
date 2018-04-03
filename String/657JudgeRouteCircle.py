class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 != 0:
            return False
        LRcount = 0
        UDcount = 0
        for move in moves:
            if move == "U":
                UDcount += 1
            elif move == "D":
                UDcount -= 1
            elif move == "L":
                LRcount += 1
            else:
                LRcount -= 1
        if (LRcount == 0 and UDcount == 0):
            return True
        return False



//use string.count

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 != 0:
            return False
        if(moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")):
            return True
        return False
