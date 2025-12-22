import re

def infix_to_postfix(expression):
    rpn_stack = []
    op_stack = []

    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # Use the expression passed into the function; don't call input() here
    expression = expression.replace("X", "*").replace("x", "*").replace("**", "^").strip()
    tokens = re.findall(r"\d+|\-|\+|\/|\*|\)|\(|\^", expression)

    for token in tokens:
        if token.isdigit():
            rpn_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack and op_stack[-1] != "(":
                rpn_stack.append(op_stack.pop())
            op_stack.pop()
        else:
            prec = precedence.get(token)
            while (op_stack and op_stack[-1] in precedence and 
                   ((precedence[op_stack[-1]] > prec) or
                   (precedence[op_stack[-1]] == prec and token != "^"))):
                rpn_stack.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        rpn_stack.append(op_stack.pop())
    
    return rpn_stack


def postfix_eval(postfix):
    eval_stack = []

    for token_2 in postfix:
        if token_2.isdigit():
            eval_stack.append(float(token_2))
        else:
            b = eval_stack.pop()
            a = eval_stack.pop()
            
            if token_2 == "+":
                eval_stack.append(a+b)
            elif token_2 == "-":
                eval_stack.append(a-b)
            elif token_2 == "*":
                eval_stack.append(a*b)
            elif token_2 == "/":
                eval_stack.append(a/b)
            elif token_2 == "^":
                eval_stack.append(a**b)
    return eval_stack[0]

# --- Main program ---
while True:
    expr = input("Enter expression: ")        # input happens here
    postfix = infix_to_postfix(expr)          # run function
    print("Postfix:", postfix)                # show result
    result = postfix_eval(postfix)
    if result.is_integer():
        result = int(result)
    print(result)
