"""Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.
Example 1: Input: s = "egg", t = "add" Output: true
Example 2: Input: s = "foo", t = "bar" Output: false
Example 3: Input: s = "paper", t = "title" Output: true Note: You may assume both s and t have the same length.
"""


def isIsomorphic(self, s, t):

    # O(n) Time Complexity | O(1) Space Complexity
    # Two hashmap with reverse mapping

    if len(s) != len(t):
        return False

    mapS = {}
    mapT = {}

    for i in range(len(s)):
        if s[i] not in mapS:
            mapS[s[i]] = t[i]
        else:
            if mapS[s[i]] != t[i]:
                return False
        if t[i] not in mapT:
            mapT[t[i]] = s[i]
        else:
            if mapT[t[i]] != s[i]:
                return False
    return True
