# NOTE: Speed factor is to beat 95.37%
from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Clarify - Define - Propose - Alternative - Implement
        # {'e':1} {'a':1}
        # ascii code is number! => Nope!
        # NOTE: [IDEA] Index comparison!
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for index, (ss, tt) in enumerate(zip(s, t)):
            if ss not in dict1:
                dict1[ss] = index
            if tt not in dict2:
                dict2[tt] = index
            
            if dict1[ss] == dict2[tt]:
                pass
            else:
                return False
        return True


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        relations_Dict = {}
        for i in range(0, len(s)):
            if(s[i] in relations_Dict.keys()):
                if(relations_Dict[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in relations_Dict.values()):
                    return False
                relations_Dict[s[i]] = t[i]
        return True