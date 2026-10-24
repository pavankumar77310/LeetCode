class Solution(object):
    def countDaysTogether(self, aA, lA, aB, lB):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [0,31,59,90,120, 151, 181, 212, 243, 273, 304, 334]

        a1 = days[int(aA[:2])-1] + int(aA[3:])
        a2 = days[int(lA[:2])-1] + int(lA[3:])
        b1 = days[int(aB[:2])-1] + int(aB[3:])
        b2 = days[int(lB[:2])-1] + int(lB[3:])

        return max(0, min(a2, b2) - max(a1, b1) + 1)