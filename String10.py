def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    
    c=(x+y)*2 
    return f"(x+y)*2={c}"

x=main(3,5)
print (x)