def gcd(nums):
    n = nums[0]
    for num in nums[1:]:
        n = _gcd(n, num)
    return n
    
def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
x = [5, 10, 15]
print(gcd(x))
