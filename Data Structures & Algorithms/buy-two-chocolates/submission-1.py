class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        buy = prices[0] + prices[1]
        return money if buy > money else money-buy