def calculator(a, b, operator):
    
    try:
        a=int(a)
        b=int(b) 

        if(operator=='+'):
            a+b
        elif(operator=='-'):
            a-b
        elif(operator=='*'):
            a*b
        elif(operator=='/'):
            a/b
        elif(operator=='%'):
            a%b
        elif(operator=='**'):
            a**b
        else:
           raise TypeError("Error: Unsupported operator")
       
    except ZeroDivisionError as e:
        return "Error : " +str(e)
    except ValueError as e:
        return "Error: Invalid input type"
    except Exception as e:
        return e

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"