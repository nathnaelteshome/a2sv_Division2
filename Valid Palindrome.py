class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', "j",
               'k', 'l', 'z', "x", 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        newStr = ''
        for word in s:
            if word.lower() in alph:
                newStr += word.lower()
        if newStr == newStr[::-1]:
            return True
        return False
