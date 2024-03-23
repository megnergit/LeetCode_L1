from typing import List
import pandas as pd

prices = [7,1,5,3,6,4]

class Solution():
    def maxProfit(self, prices: List[int]) -> int:

      prices_after = prices[1:] + prices[:1]
      prices_before = prices[-1:] + prices[:-1]

      i1 = [x-y for (x,y) in zip(prices_after, prices)]
      i2 = [x-y for (x,y) in zip(prices_before,prices)]
      ix = list(range(len(prices)))

      i_max = [ ix for (ix, i, j) in zip(ix, i1, i2) if i <= 0 and j <=0]
      i_min = [ ix for (ix, i, j) in zip(ix, i1, i2) if i >= 0 and j >=0]

      i_max = [0] + i_max + [len(prices)-1]
      i_min = [0] + i_min + [len(prices)-1]

      z = 0
      for i in i_max:
         for j in i_min:
            z0 = prices[i] - prices[j]
            if (i > j) and  (z < z0):
#               print(i, j, z, z0) 
               z = z0

      return z


#========================

print(prices)
z = Solution()
print(z.maxProfit(prices))


#========================


#========================

