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

def pending_occurances(ocu):
        for i in range(0,len(ocu)-1):
            if(ocu[i+1]-ocu[i]>2):
                print('invalid ocu',ocu)
                return False


def get_minimal_dict(input):
    # step 1 get unique characters which is potential dict elements
    unique_char = get_dict_element(input)
    # step 2 pending if characters can be convert to dictionary
    input_len = len(unique_char)

    if(input_len > 1):
        for i in unique_char:
            occurances = get_element_occurency(input,i)
            if(len(occurances)>4):
                print('invalid transfroms')
            else:
                print('pending input',input,occurances)
                pending_occurances(occurances)
            


        
    else:
        # simple IIII or XXX case
        return unique_char[0]


def minimally_operation(test_input):
    operation_code = get_operation_code(test_input);
    operations=[impossible_alert,to_roman,to_arabic_with_dict];
    if(operation_code == 2):
        new_dict = get_minimal_dict(test_input)

    # operations[operation_code](test_input,[])

for i in input_cases[1:4]:
    minimally_operation(i)

# hybrid_input(test_input);
