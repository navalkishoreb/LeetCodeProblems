class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        values are from 1 to N inclusive
        array indexes are from 0 to N inclusive

        since there are N+1 holes and N objects; one object will repeat itself
        Piegon-hole principle

        if 1 to N are nodes then one value in refrenced atleast more than once

        index are nodes
        value at index is pointer to next node

        since thre 

        """

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
