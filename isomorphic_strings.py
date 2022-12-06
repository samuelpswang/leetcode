'''
205. Isomorphic Strings
(https://leetcode.com/problems/isomorphic-strings)

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to 
get t. All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the 
same character, but a character may map to itself.

---

Example 1:
Input: s = "egg", t = "add"
Output: true

---

Example 2:
Input: s = "foo", t = "bar"
Output: false

---

Example 3:
Input: s = "paper", t = "title"
Output: true
 
---

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''


from typing import List


def replace(s: str) -> List[int]:
    flag = 0
    curr = None
    identified = {}
    parsed = []
    for i in range(len(s)):
        if curr != s[i]:
            if s[i] in identified:
                parsed.append(identified[s[i]])
            else:
                parsed.append(flag)
                identified[s[i]] = flag
                flag += 1
        else:
            parsed.append(flag)
    
    return parsed

def is_isomorphic(s: str, t: str) -> bool:
    sparsed = replace(s)
    tparsed = replace(t)
    return (sparsed == tparsed)
