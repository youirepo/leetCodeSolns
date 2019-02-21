class Solution:
    """
    Algorithm:
    
    * Iterate over all strings at the same time by using python's
      zip() function.
      
    * If every nth element in the strings match, then append to a string
      (common).
      
    * Once you find a mismatch, break the loop and return common.
    """
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        common = ""
        for x in zip(*strs):
            if len(set(x)) == 1:
                common += x[0]
            else:
                break
        return common