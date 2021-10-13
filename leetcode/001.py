# 题目
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''
# 题解
def isValid(s: str) -> bool:
    print(s)
    dict1 = {'{':'}', '[':']', '(':')'}
    stack = []
    idx = 0
    for idx in range(len(s)):
        if s[idx] == '{' or s[idx] == '[' or s[idx] == '(':
            stack.append(s[idx])
        elif s[idx] == '}' or s[idx] == ']' or s[idx] == ')':
            if not stack:
                return False
            tmp = stack.pop()
            if dict1[tmp] != s[idx]:
                return False
        else:
            return False
    if stack:
        return False
    return True
