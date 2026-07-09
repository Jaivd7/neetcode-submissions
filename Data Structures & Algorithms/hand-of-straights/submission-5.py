class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        
        count = {}

        for i in hand:
            count[i] = count.get(i, 0) + 1
        hand.sort()
        
        for num in hand:
            # Only attempt to build a group if this card has not been used up.
            if count[num]:
                # We want to build the group: num, num+1, ..., num+groupSize-1
                for i in range(num, num + groupSize):
                    # If ANY needed number is missing, we cannot form a valid group.
                    if count.get(i, 0) <=0:
                        return False
                    # Use up one occurrence of this card value.
                    count[i] -= 1

        # If all groups were successfully formed, return True.
        return True

            