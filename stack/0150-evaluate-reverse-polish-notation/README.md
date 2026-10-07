# 150. Evaluate Reverse Polish Notation

**Category:** Stack
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Problem

You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always truncates toward zero.

## Example 1

```
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
```

## Constraints

- `1 <= tokens.length <= 10000`
- `tokens[i]` is `"+"`, `"-"`, `"*"`, or `"/"`, or a string representing an integer in the range `[-200, 200]`.

## Solution

Stack: iterate over the tokens; numbers are pushed and, when an operator is found, the last two operands are popped (`b` first, then `a`), `a op b` is computed and the result is pushed back. Division uses true division (`/`) and the later `int()` conversion truncates toward zero.

- **Time complexity:** O(n)
- **Space complexity:** O(n)

## Test cases

`cases.txt` contains one pair of lines per test case: the expression (tokens separated by spaces) followed by the expected result. The solution reads pairs until the end of input (Scheme 3) and prints one line per case: `[PASS|FAIL] <actual> | <expected>`.

## Run

```
python3 solution.py < cases.txt
```
