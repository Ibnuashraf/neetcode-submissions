class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        out = []
        for num in nums:
            if num not in count:
                count[num] = 1
            else :
                count[num] += 1
        sort = sorted(count, key=count.get, reverse=True)
        for i in range(k):
            out.append(sort[i])
        # out = []
        # count=Counter(nums)
        # for count.key in count in range(k):
        #     out.append(key)
        
        return out

