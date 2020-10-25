testCases=[
        'Please convert 0I minimally',
        'Please convert ABAA minimally', # no
        'Please convert ABCDEFA minimally', #no
        'Please convert MDCCLXXXVII minimally',
        'Please convert MDCCLXXXIX minimally',
        'Please convert MMMVII minimally',
        'Please convert VI minimally',
        'Please convert ABCADDEFGF minimally',
        'Please convert ABCCDED minimally'
        ]

input_cases=[
    "0I","ABAA","ABCDEFA","MDCCLXXXVII","MDCCLXXXIX","MMMVII","VI","ABCADDEFGF","ABCCDED","123124"
        ]

Arabic_numbers = ['0','1','2','3','4','5','6','7','8','9']

def is_type(input,type):
    return input in type

def impossible_alert():
    print("Hey, ask me something that's not impossible to do!")

def to_roman(input):
    print('converting arabic to roman')

def to_arabic_with_dict(input,dict):
    print('converting roman to arabic')

def get_operation_code(input):
    pending_pos= input[0]
    rest = input[1:]
    if(is_type(pending_pos,Arabic_numbers)):
        for i in rest:
            if(not is_type(i,Arabic_numbers)):
                return 0
            else:
                return 1
    else:
        for i in rest:
            if(is_type(i,Arabic_numbers)):
                return 0
            else:
                return 2

def get_dict_element(input):
    unique_char = []
    for i in input:
        if(i not in unique_char):
            unique_char.append(i)
    return unique_char[::-1]

def get_element_occurency(input,ele):
    occurances = []

    for i in range(0,len(input)):
        if(input[i] == ele):
            occurances.append(i)

    return occurances

def occurences_pending (occurances):

    dup =0
    invalid = False

    for i in (0,len(occurances)-1):
        if(occurances[i+1]== occurances[i]):
            dup+=1
            break
        else:
            break

    if(dup >2 and not invalid ):
        return False
    else:
        return True

def complex_new_dict(input):

    new_dict = []
    pos = 0

    reversed_input = input[::-1]

    pending_pos = reversed_input[pos]

    loop_time = len(reversed_input)

    res = reversed_input[pos+1:]

#     for i in range(0,loop_time-1):
#         if(res[i] == pending_pos):
#             min = res[]
#         else:
#             new_dict.append(pending_pos)

        # print(res)


def get_minimal_dict(input):
    # step 1 get unique characters which is potential dict elements
    unique_char = get_dict_element(input)
    # step 2 pending if characters can be convert to dictionary
    dict_len = len(unique_char)
    
    for i in unique_char:
        occurances = get_element_occurency(input[::-1],i)
        print(occurances)
        occurences_pending(occurances)
        #if(occurences_pending(occurances)):
        #    if(dict_len > 1):
        #        return complex_new_dict(input)
        #    else:
        #        # simple IIII or XXX case
        #        return unique_char[0]
        #else:
        #    return False
        ## for i in range(0,len(occurances)):
        ##

def minimally_operation(test_input):
    operation_code = get_operation_code(test_input);
    operations=[impossible_alert,to_roman,to_arabic_with_dict];
    if(operation_code == 2):
        new_dict = get_minimal_dict(test_input)

    # operations[operation_code](test_input,[])

for i in input_cases[1:3]:
    minimally_operation(i)

# hybrid_input(test_input);
