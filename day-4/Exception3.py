def process_data(data, index):
    """
    Processes data with error handling.
    
    :param data: List of numbers (strings that should be converted to int)
    :param index: Index to divide with
    :return: Processed result or error message
    """
    try:
        c=index/int(data[index])
          
    except ZeroDivisionError as e:
        return e
    except ValueError as e:
       return "Invalid conversion from string to int"
    except IndexError as e:
        return e
    except Exception as e:
       return e
# Example Usage:
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2))  # Should handle division by zero
print(process_data(["10", "abc", "30"], 1))  # Should handle ValueError
print(process_data([10, 20], 5))  # Should handle IndexError