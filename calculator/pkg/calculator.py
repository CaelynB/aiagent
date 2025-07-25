# implementation of a simple command line calculator application
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

    # method to evaluate a given arithmetic expression
    def evaluate(self, expression):
        # if the expression is empty or contains only whitespace, return None
        if not expression or expression.isspace():
            return None
         
        # strip any whitespace and split the expression into tokens
        tokens = expression.strip().split()

        # return the result of evaluating the tokens using infix notation
        return self._evaluate_infix(tokens)

    # method to evaluate an tokenized expression in infix notation
    def _evaluate_infix(self, tokens):
        # initialize empty stacks for values and operators
        values = []
        operators = []

        # for each token in the expression
        for token in tokens:
            # if the token is a supported operator
            if token in self.operators:
                # while there are operators on the stack with higher or equal precedence
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    # apply the last operator to the last two values
                    self._apply_operator(operators, values)

                # push the operator onto the stack
                operators.append(token)
            # otherwise, attempt to convert the token into a float and push it onto the stack
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        # apply any remaining operators
        while operators:
            self._apply_operator(operators, values)

        # if the amount of values left is not equal to 1, raise an error
        if len(values) != 1:
            raise ValueError("invalid expression")

        # return the final value
        return values[0]

    # method to apply the last operator to the last two values
    def _apply_operator(self, operators, values):
        # if there are no operators, return
        if not operators:
            return

        # remove the last operator from the stack
        operator = operators.pop()

        # if there are fewer than two values, raise an error
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        # remove the last two values from the stack
        b = values.pop()
        a = values.pop()

        # apply the operator to the two values and push the result onto the stack
        values.append(self.operators[operator](a, b))
