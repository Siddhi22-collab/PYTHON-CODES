def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token ==
