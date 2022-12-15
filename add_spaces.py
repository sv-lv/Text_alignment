from text_alignment.input_k import input_k

def add_spaces(new_list_changed, k):
    k = input_k()
    new_list_changed_spaces = []
    list_sp = new_list_changed.split(' ')
    spaces = k - len(new_list_changed) + len(list_sp) - 1

    while spaces != 0:
        new_list_changed_spaces = []
        for p in range(len(list_sp)):
            if p == len(list_sp) - 1:
                list_sp_1 = list_sp[p]
                new_list_changed_spaces.append(list_sp_1)

            else:
                list_sp_1 = list_sp[p] + ' '
                new_list_changed_spaces.append(list_sp_1)
                spaces -= 1
        list_sp = new_list_changed_spaces
    return new_list_changed_spaces