# function to render an arithmetic expression and its result in a box
def render(expression, result):
    # if the result is a float and an integer, convert it into an integer string
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    # otherwise, convert the result to a string
    else:
        result_str = str(result)

    # calculate the width of the box using the longest of expression or result plus padding
    box_width = max(len(expression), len(result_str)) + 4

    # initialize an empty list to hold the lines of the box
    box = []

    # build the box
    box.append("┌" + "─" * box_width + "┐")
    box.append("│" + " " * 2 + expression + " " * (box_width - len(expression) - 2) + "│")
    box.append("│" + " " * box_width + "│")
    box.append("│" + " " * 2 + "=" + " " * (box_width - 3) + "│")
    box.append("│" + " " * box_width + "│")
    box.append("│" + " " * 2 + result_str + " " * (box_width - len(result_str) - 2) + "│")
    box.append("└" + "─" * box_width + "┘")
    
    # return the formatted box
    return "\n".join(box)
