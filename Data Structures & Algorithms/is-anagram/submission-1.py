class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}

        if len(s) != len(t):
            return False
        else:
            for char1, char2 in zip(s, t):
                print(char1, char2)
                if char1 in s1:
                    s1[char1] += 1 
                else:
                    s1[char1] = 1 

                if char2 in s2:
                    s2[char2] += 1 
                else:
                    s2[char2] = 1 

            return s1 == s2
        