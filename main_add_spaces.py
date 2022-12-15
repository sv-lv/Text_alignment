'''Добавление необходимого количества пробелов '''
from text_alignment.input_k import input_k
from text_alignment.concat import concat

def add_spaces():
    result = concat() #результат разделения исходной строки на равные строки с количеством символов не более К
    k = input_k()
    result_spaces = [] #итоговый список со строками с кол-вом символов = К
    for f in result: #рассматриваем каждую строку поотдельности

        new_list_changed = f.strip() #убираем из строк ненужные пробелы, т.е. перед первой и после последней буквы
        new_list_changed_spaces = []
        list_sp = new_list_changed.split(' ')
        spaces = k - len(new_list_changed) + len(list_sp) - 1  # кол-во пробелов, которое нужно вставить между слов

        while spaces > 0:
            new_list_changed_spaces = []
            for p in range(len(list_sp)):
                if p == len(list_sp) - 1 and spaces > 0:
                    list_sp_1 = list_sp[p]
                    new_list_changed_spaces.append(list_sp_1)

                elif spaces == 0:
                    list_sp_1 = list_sp[p]
                    new_list_changed_spaces.append(list_sp_1)

                else:
                    list_sp_1 = list_sp[p] + ' '
                    new_list_changed_spaces.append(list_sp_1)
                    spaces -= 1
            list_sp = new_list_changed_spaces

        result_spaces.append(''.join(new_list_changed_spaces))

    print(result_spaces)

add_spaces()