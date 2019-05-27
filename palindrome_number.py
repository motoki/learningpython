class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        str_x = str(x)
        l = len(str_x)
        q, mod = divmod(l,2)
        for i in range(q):
            if str_x[i] != str_x[l-i-1]:
                return False
        return True
    def isPalindrome2(self, x: int) -> bool:
        l_x = list(str(x))
        l_rx = l_x[::-1]
        return l_x == l_rx

def main():
    solution = Solution()
    val = solution.isPalindrome(12344321)
    print(val)

if __name__ == "__main__":
    main()