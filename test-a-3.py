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


def impossible_alert():
    print("Hey, ask me something that's not impossible to do!")


def to_roman():
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
        return False
    elif len(occurrences) == 3:

        # only works out here
        # aaa
        # aaba no
        # abaa yes
        # process
        dup = 0;
        pos = 0;
        temp = 0;
        for i in range(0, len(occurrences)):
            print('i here', i)

    elif len(occurrences) == 2:
        if occurrences[1] - occurrences[0] > 2:
            return False
        else:
            return True
    else:
        # when there is only one occurrences
        return True


def complex_new_dict(data_input):
    new_dict = []
    pos = 0

    reversed_input = data_input[::-1]

    pending_pos = reversed_input[pos]

    loop_time = len(reversed_input)

    res = reversed_input[pos + 1:]
    # print(res)


def get_occurrence_pending_list(input):
    unique_char = get_dict_element(input)
    # step 2 pending if characters can be convert to dictionary
    dict_min_len = len(unique_char)

    occurrences_pending_list = []

    for i in unique_char:
        occurrences = get_element_occurrence(input[::-1], i)

        occurrences_pending_list.append(occurrences_pending(occurrences))

    return occurrences_pending_list


def get_minimal_dict(input):
    occurrences_pending_list = get_occurrence_pending_list(input)

    print('is valid roma ', input, occurrences_pending_list)
    # if(occurences_pending(occurances)):
    #    if(dict_min_len > 1):
    #        return complex_new_dict(input)
    #    else:
    #        # simple IIII or XXX case
    #        return unique_char[0]
    # else:
    #    return False
    ## for i in range(0,len(occurances)):
    ##


def minimally_operation(test_input, operations=None):
    operation_code = get_operation_code(test_input);
    operations = [impossible_alert, to_roman, to_arabic_with_dict];
    if operation_code == 2:
        new_dict = get_minimal_dict(test_input)
        operations[operation_code](test_input, new_dict)
    else:
        operations[operation_code](test_input)

    # operations[operation_code](test_input,[])


for i in input_cases[1:3]:
    minimally_operation(i)

# hybrid_input(test_input);
