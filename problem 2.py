def isPalindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

print(isPalindrome("anna"))
print(isPalindrome("civic"))
print(isPalindrome("a"))
print(isPalindrome("tx1aa1xt"))
print(isPalindrome(""))
print(isPalindrome("Civic"))
print(isPalindrome("ab"))

