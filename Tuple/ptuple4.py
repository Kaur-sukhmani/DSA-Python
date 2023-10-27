"""Concatenate
Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

Example

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python"""

def concatenate_strings(input_tuple):
    # TODO
    string  = str()
    for i in range(0, len(input_tuple)):
        if i == 0:
           string += f'{input_tuple[i]}' 
        else:
            string += f' {input_tuple[i]}'
    return string
# ALT
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)