# Prime Product Hashing Approach for group anagrams
# Time COmplexity: O(N*K) bcz loop over N words and each word takes K time/length
# Space com. : O(N*K) in the worst case

from typing import List
from collections import defaultdict


class Solution:
    PRIMES = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]

    def get_prime_product(self, s):
        product = 1
        for char in s:
            product *= self.PRIMES[
                ord(char) - ord("a")
            ]  # Multiply prime for each character
        return product

    def groupAnagrams(
        self, strs: List[str]
    ) -> List[List[str]]:  # N((O(klog k)) + O(k))
        hashMap = defaultdict(list)

        for word in strs:
            prime_hash = self.get_prime_product(word)  # Compute prime product hash
            hashMap[prime_hash].append(word)  # Store in HashMap

        return list(hashMap.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# character frequency count approach
# res = defaultdict(list)  # Initialize a dictionary with default values as lists
# for s in strs:
#     count = [0] * 26  # Initialize a list to count characters for each string
#     for c in s:
#         count[ord(c) - ord("a")] += 1  # Count each character in the string
#     res[tuple(count)].append(s)  # Use the tuple of counts as a key and append the string
# return list(res.values())  # Return grouped anagrams
