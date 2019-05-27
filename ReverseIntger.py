from typing import List
import sys.maxint

class Solution:
    def reverse(self, x: int) -> int:
        ret = ""
        if x > 0:
            strX = str(x)
            for i in range(len(strX)):
                idx = len(strX) - i
                ret += strX[idx-1:idx]
        else:
            strX = str(-x)
            for i in range(len(strX)):
                idx = len(strX) - i
                ret += strX[idx-1:idx]
            ret = "-" + ret
            print(ret)
        val = int(ret)
        min = -pow(2,31)
        max = pow(2,31)-1
        if min <=val and max >= val :
            return val
        else:
            return 0

def main():
    solution = Solution()
    val = solution.reverse(123)
    print(val)

    val = solution.reverse(-123)
    print(val)

if __name__ == "__main__":
    main()