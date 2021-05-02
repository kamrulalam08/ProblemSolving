"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

"""
My solution
Runtime O(n)
Space O(n)
"""
def isUnique(testString):
    seen = set()
    for i in testString:
        if i not in seen:
            seen.add(i)
        else:
            return False
    return True
