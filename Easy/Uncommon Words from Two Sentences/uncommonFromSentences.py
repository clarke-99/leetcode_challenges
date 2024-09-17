class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        def get_f(s):
            f = {}
            for word in s:
                if word in f:
                    f[word] += 1
                else:
                    f[word] = 1
            return f

        def check_common(f1, f2):
            uncommon = []
            for key in f1.keys():
                if f1[key] == 1 and key not in f2:
                    uncommon.append(key)
            return uncommon

        f1, f2 = get_f(s1.split()), get_f(s2.split())

        uncom1, uncom2 = check_common(f1, f2), check_common(f2, f1)
        return uncom1 + uncom2

  

        
