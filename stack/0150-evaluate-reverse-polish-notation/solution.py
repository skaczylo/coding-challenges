import sys
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+':lambda a,b : a+b,
                     '-':lambda a,b :a-b,
                     '*':lambda a,b : a*b,
                     '/':lambda a,b : a/b}

        stack = []

        for token in tokens:
            if not token in operators:
                stack.append(token)
            else:
                
                b = int(stack.pop())
                a = int(stack.pop())

                result = operators[token](a,b)

                stack.append(result)

        return int(stack.pop())


def test_case():
    line = sys.stdin.readline()
    if not line:
        return False

    actual = Solution().evalRPN(line.split())
    expected = int(sys.stdin.readline())

    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] {actual} | {expected}")
    return True


def main():
    while test_case():
        pass


if __name__ == "__main__":
    main()
