def isBalanced(s):
    _map = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    stack = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if not stack or _map[stack.pop()] != c:
                return 'NO'

    if stack:
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    assert isBalanced('{[()]}') == 'YES'
    assert isBalanced('{[(])}') == 'NO'
    assert isBalanced('{{[[(())]]}}') == 'YES'

    assert isBalanced('{{([])}}') == 'YES'
    assert isBalanced('{{)[](}}') == 'NO'

    assert isBalanced('{(([])[])[]}') == 'YES'
    assert isBalanced('{(([])[])[]]}') == 'NO'
    assert isBalanced('{(([])[])[]}[]') == 'YES'

    assert isBalanced('}][}}(}][))]') == 'NO'
    assert isBalanced('[](){()}') == 'YES'
    assert isBalanced('()') == 'YES'
    assert isBalanced('({}([][]))[]()') == 'YES'
    assert isBalanced('{)[](}]}]}))}(())(') == 'NO'
    assert isBalanced('([[)') == 'NO'

    assert isBalanced('((((((') == 'NO'
