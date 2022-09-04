def add_space_after_operator(expresion: str) -> str:
    '''a function to add a space after the operator' in a string'''
    if expresion.startswith('-') or expresion.startswith('+'):
        return expresion[0] + ' ' + expresion[1:]
    else:
        return expresion


def ajust_size(array: list) -> None:
    '''a function to adjust the size of the problem'''
    array[1] = add_space_after_operator(array[1])
    larger = 0
    for line in array:
        if larger < len(line):
            larger = len(line)

    for i in range(len(array)):
        array[i] = (' ' * (larger - len(array[i]))) + array[i]


def convert_list_to_string(array: list) -> str:
    '''a function to convert the list to string'''
    return ''.join([line + '\n' for line in array])




def arithmetic_arranger(array: list, resolve=False) -> None:
    '''a function to arrange the arithmetic problem in a list'''
    arranged_array = []
    error = ''

    if len(array) > 5:
        error = "Error: Too many problems."
        return error

    for calc in array:
        elements = calc.split()

        if elements[1] not in ['+', '-']:
            error = "Error: Operator must be '+' or '-'."
            return error
        for i in range(0, 3, 2):
            if not elements[i].isdigit():
                error = 'Error: Numbers must only contain digits.'
                return error
            if len(elements[i]) > 4:
                error = 'Error: Numbers cannot be more than four digits.'
                return error

        out = [elements[0], elements[1] + elements[2]]

        if resolve:
            out.append(str(int(out[0]) + int(out[1])))

        ajust_size(out)
        out.insert(2, '-' * len(out[0]))
        arranged_array.append(out)

    for expresion in arranged_array:
        print(convert_list_to_string(expresion), end='\n\n\n\n')

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
    arithmetic_arranger(["320 + 2", "100 - 1"], True)
