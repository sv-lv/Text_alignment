'''условие для первой итерации (строчки)'''
from text_alignment.input_k import input_k
from text_alignment.input_str import input_str

def first():
    k = input_k()
    string = input_str()
    new_string = []
    new_list = []
    len_result = 0
    x = 0
    result = []  # итоговый список с выровненными строками
    for i in range(1, 1 + len(string)):
        '''условие для первой итерации (строчки)'''
        if i == k:
            new_list = string[:i]
            if string[i] != ' ':  # вариант, когда k-ый символ равен букве, не последней в слове
                new_list_changed = new_list[:new_list.rfind(' ')]
                return new_list_changed
            if string[i] == ' ' or string[i + 1] == ' ' and i + 1 <= len(
                    string):  # вариант, когда либо k-ый символ, либо следующий символ после k =" "
                new_list_changed = new_list[:i]
                return new_list_changed