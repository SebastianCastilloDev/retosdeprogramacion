"""
1.- Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos.
"""

def custom_max(n1: int, n2: int) -> int:
    """[summary]

    Args:
        n1 (int): first number
        n2 (int): second number

        Returns:
        int: max number between n1 and n2
    """

    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    else:
        raise ValueError("Both numbers are equal")
    raise Exception("This line should not be reached")
    
print(custom_max(1, 2))
print(custom_max(1, 3))
print(custom_max(3, 3))