class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        count = 0


        for num in nums:
            if num  not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))

        for key in sorted_freq:
            count +=1
            ans.append(key)
            if(count == k):
                return ans