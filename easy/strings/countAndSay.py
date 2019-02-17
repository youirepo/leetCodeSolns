class Solution:
    """
        Function to return next string in sequence.
        
        The algorithm uses two pointers to count occurences
        of characters in the string. One static and one moving.

        The pointers start off at the same position. The moving
        pointer compares the character with the value the static
        pointer is pointing to. If it is the same it will increment
        the counter.

        When the values the pointers point to don't match, you cast
        the count to a string and append it to the character and 
        append that value to the previous count string (newStr), point
        the static pointer to where the moving pointer is currently
        at and then reset the counter to 1 (not 0 as it has already
        been counted by the moving pointer in the current iteration).

        You do this in a loop till you exhaust the string. By this time,
        you still have a number of characters that haven't been appended
        to newStr, so you have to append it after the for-loop.
    """
    def genString(self, string: 'str') -> 'str':
        N = len(string)
        
        newStr = ""
        i, count = 0, 0
        for j in range(N):            
            if string[j] != string[i]:
                newStr += str(count) + string[i]
                i = j
                count = 1
            else:
                count += 1
        
        # Having exhausted the string, append last count to string
        newStr += str(count) + string[i]

        return newStr
            
    def countAndSay(self, n: 'int') -> 'str':    
        s = "1"
        for i in range(n-1):
            s = self.genString(s)
        
        return s