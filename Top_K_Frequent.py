class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(list)
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1

        for num,cnt in freq.items():
            count[cnt].append(num)

        result = []
        max_freq = max(count.keys())
        for freq in range(max_freq, 0, -1):  
            if freq in count:
                result.extend(count[freq])
                if len(result) >= k: 
                    return result[:k]

        return result

    
            
    

        