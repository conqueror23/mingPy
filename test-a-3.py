import sys
testCases = [
    'Please convert 0I minimally',
    'Please convert ABAA minimally',  # no
    'Please convert ABCDEFA minimally',  # no
    'Please convert MDCCLXXXVII minimally',
    'Please convert MDCCLXXXIX minimally',
    'Please convert MMMVII minimally',
    'Please convert VI minimally',
    'Please convert ABCADDEFGF minimally',
    'Please convert ABCCDED minimally'
]

input_cases = [
    "0I", "ABAA", "ABCDEFA", "MDCCLXXXVII", "MDCCLXXXIX", "MMMVII", "VI", "ABCADDEFGF", "ABCCDED", "123124"
]

Arabic_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_type(data_input, data_type):
    return data_input in data_type


def impossible_alert(data_input='none'):
    print("Hey, ask me something that's not impossible to do!")


def to_roman(data_input):
    print('converting arabic to roman')


def to_arabic_with_dict(data_input, new_dict):
    print('converting roman to arabic', data_input, new_dict)


def get_operation_code(data_input):
    pending_pos = data_input[0]
    rest = data_input[1:]
    if is_type(pending_pos, Arabic_numbers):
        for rest_char in rest:
            if not is_type(rest_char, Arabic_numbers):
                return 0
            else:
                return 1
    else:
        for rest_char in rest:
            if is_type(rest_char, Arabic_numbers):
                return 0
            else:
                return 2


def get_dict_element(data_input):
    unique_char = []
    for data_char in data_input:
        if data_char not in unique_char:
            unique_char.append(data_char)
    return unique_char[::-1]


def get_element_occurrence(data_input, ele):
    occurrences = []

    for input_char in range(0, len(data_input)):
        if data_input[input_char] == ele:
            occurrences.append(input_char)

    return occurrences


def occurrences_pending(occurrences):
    if len(occurrences) >= 4:
        impossible_alert()
        # sys.exit()
        # return False
    elif len(occurrences) == 3:
        if occurrences[1] - occurrences[0] == 1:
            if occurrences[2] - occurrences[1] == 1:
                return True
            elif occurrences[2] - occurrences[1] == 2:
                impossible_alert()
                # sys.exit()
                # return False
        else:
            return True

    elif len(occurrences) == 2:
        if occurrences[1] - occurrences[0] > 2:
            impossible_alert()
            # sys.exit()
        else:
            return True
    else:
        # when there is only one occurrences
        return True


def complex_new_dict(data_input):
    print('generate dict', data_input)


def get_occurrence_pending_list(data_input):
    unique_char = get_dict_element(data_input)
    # step 2 pending if characters can be convert to dictionary
    dict_min_len = len(unique_char)

    occurrences_pending_list = []

    for char in unique_char:
        occurrences = get_element_occurrence(data_input[::-1], char)

        occurrences_pending_list.append(occurrences_pending(occurrences))

    return occurrences_pending_list


def get_minimal_dict(data_input):
    get_occurrence_pending_list(data_input)

    return complex_new_dict(data_input)


def minimally_operation(test_input, operations=None):
    operation_code = get_operation_code(test_input)
    operations = [impossible_alert, to_roman, to_arabic_with_dict]
    if operation_code == 2:
        new_dict = get_minimal_dict(test_input)

        if new_dict:
            operations[operation_code](test_input, new_dict)
        else:
            return False
    else:
        operations[operation_code](test_input)

    # operations[operation_code](test_input,[])


for i in input_cases[4:6]:
    minimally_operation(i)

# hybrid_input(test_input);
