# class to implement a simple calculator application
class Calculator:
    # constructor to initialize the calculator with the supported operators and their precedence
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    # method to evaluate a mathematical expression
    def evaluate(self, expression):
        # if the expression is empty or contains only whitespace, return None
        if not expression or expression.isspace():
            return None
        
        # remove any leading or trailing whitespace and split the expression into tokens
        tokens = expression.strip().split()

        # return the result of evaluating the tokens using infix notation
        return self._evaluate_infix(tokens)

    # method to evaluate an infix expression
    def _evaluate_infix(self, tokens):
        # initialize empty stacks for values and operators
        values = []
        operators = []
        
        # for each token in the expression
        for token in tokens:
            # if the token is a supported operator
            if token in self.operators:
                # while there are operators in the stack and the precedence of the last operator is greater than or equal to the current token's precedence
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    # apply the last operator to the last two values in the stack
                    self._apply_operator(operators, values)

                # append the current token to the operators stack
                operators.append(token)
            else:
                # attempt to convert the token to a float and append it to the values stack
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        # apply any remaining operators
        while operators:
            self._apply_operator(operators, values)

        # if the amount of values left is not 1, raise a ValueError
        if len(values) != 1:
            raise ValueError("invalid expression")

        # return the only value left in the stack
        return values[0]

    # method to apply the last operator to the last two values in the stack
    def _apply_operator(self, operators, values):
        # if there are no operators, return
        if not operators:
            return

        # pop the last operator from the stack
        operator = operators.pop()
        
        # if there are less than two values, raise a ValueError
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        # pop the last two values from the stack
        b = values.pop()
        a = values.pop()

        # apply the operator to the two values and append the result back to the values stack
        values.append(self.operators[operator](a, b))
