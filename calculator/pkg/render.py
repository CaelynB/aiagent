# function to render a mathematical expression and its result in a box
def render(expression, result):
    # if the result is a float and is an integer, convert it to an integer string
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    # otherwise, convert the result to a string
    else:
        result_str = str(result)

    # calculate the width of the box based on the longer string (expression or result), plus padding
    box_width = max(len(expression), len(result_str)) + 4

    # initialize the box as an empty list
    box = []

    # build the box layout displaying the expression and result
    box.append("┌" + "─" * box_width + "┐")
    box.append(
        "│" + " " * 2 + expression + " " * (box_width - len(expression) - 2) + "│"
    )
    box.append("│" + " " * box_width + "│")
    box.append("│" + " " * 2 + "=" + " " * (box_width - 3) + "│")
    box.append("│" + " " * box_width + "│")
    box.append(
        "│" + " " * 2 + result_str + " " * (box_width - len(result_str) - 2) + "│"
    )
    box.append("└" + "─" * box_width + "┘")

    # return the box as a newline-separated string
    return "\n".join(box)
