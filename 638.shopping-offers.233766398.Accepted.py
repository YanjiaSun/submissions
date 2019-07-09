_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper():
            needs_tuple = tuple(needs)
            if needs_tuple in memo:
                return memo[needs_tuple]
            min_cost = 0
            for cost, need in zip(price, needs):
                min_cost += need * cost
            if min_cost == 0:
                return 0
            for offer in special:
                for i, need in enumerate(needs):
                    if offer[i] > need:
                        break
                else:
                    for i, need in enumerate(needs):
                        needs[i] -= offer[i]
                    min_cost = min(min_cost, offer[-1] + helper())
                    for i, need in enumerate(needs):
                        needs[i] += offer[i]
            memo[needs_tuple] = min_cost
            return min_cost
        memo = {}
        return helper()