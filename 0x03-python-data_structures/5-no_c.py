#!/usr/bin/python3
def no_c(my_string):
    return ''.join(char for char in my_string if char.lower() not in {'c', 'C'})

# this is an example usage:
if __name__ == "__main__":
    input_string = "This is just a Simple Sample String with Cs and Cs"
    result = no_c(input_string)
    print(result)
