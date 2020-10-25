import re
import math
import time
import sys

Roman_number = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
Arabic_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Dict = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def please_convert():
    time.sleep(0.01)
    word = input('How can I help you? ')
    time.sleep(0.01)
    word_new = word.split()
    # print(word_new)

    while (word_new[0] == 'Please' and word_new[1] == 'convert'):

        if len(word_new) == 3:
            string = word_new[-1]
            if string[0] == '0':
                print("Hey, ask me something that's not impossible to do!")

            elif string[0] in Roman_number:
                if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string)) == True:
                    def roman_to_int(string):
                        ix = 0
                        result = 0
                        while ix < len(string):
                            for arabic, roman in Dict:
                                if string.startswith(roman, ix):
                                    result += arabic
                                    ix += len(roman)
                                    break
                            else:
                                raise ValueError('Invalid Roman number.')
                        return result

                    print("Sure! It is", roman_to_int(string))

                else:
                    print("Hey, ask me something that's not impossible to do!")

            else:
                if int(string) > 3999:
                    print("Hey, ask me something that's not impossible to do!")
                elif int(string) < 0:
                    print("Hey, ask me something that's not impossible to do!")
                else:
                    string = int(string)

                    def int_to_roman(string):
                        result = ""
                        for (arabic, roman) in Dict:
                            (factor, string) = divmod(string, arabic)
                            result += roman * factor
                        return result

                    print("Sure! It is", int_to_roman(string))
            break


        elif len(word_new) == 4:
            string = word_new[2]

            if word_new[-1] != 'minimally':
                print("I don't get what you want, sorry mate!")

            elif not string.isalpha():
                print("Hey, ask me something that's not impossible to do!")

            else:
                def get_idx(string_):
                    return [string_.index(i) for i in string_]

                def get_roman_string():
                    roman_ = []
                    row = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
                    column = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

                    for i in range(10):
                        for j in range(10):
                            combin = column[i] + row[j]
                            roman_.append(combin)
                    return roman_[1:]

                def get_roman_idxs(roman_list):
                    roman_idxs = []
                    for i in roman_list:
                        roman_idx = get_idx(i)
                        roman_idxs.append(roman_idx)
                    return roman_idxs

                def get_minimize_string(input_):
                    input_reverse = input_[::-1]
                    first_str = input_reverse[0]
                    idx = 0
                    for idx_, i in enumerate(input_reverse):
                        if i == first_str:
                            idx = idx_

                    return (input_reverse[:idx + 1])[::-1], (input_reverse[idx + 1:])[::-1]

                def get_min_idx(roman_idxs, string_idx):
                    if string_idx in roman_idxs:
                        return True, roman_idxs.index(string_idx)
                    else:
                        return False, None

                def to_roman(power, quotient,
                             power_to_roman={0: ["I", "V", "X"], 1: ["X", "L", "C"], 2: ["C", "D", "M"], 3: ["M"]}):
                    romans = power_to_roman[power]
                    if quotient <= 3:
                        out = quotient * romans[0]
                    elif quotient == 4:
                        out = romans[0] + romans[1]
                    elif quotient == 5:
                        out = romans[1]
                    elif quotient <= 8:
                        out = romans[1] + (quotient - 5) * romans[0]
                    else:
                        out = romans[0] + romans[2]
                    return out

                def minimize_using(num_list, input_list):
                    ii = 1
                    roman_dict = {}
                    roman_num = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100}
                    for n, il in zip(num_list, input_list):
                        n = int(n)
                        out = ""
                        i = 3
                        while i >= 0:
                            out += to_roman(i, n // (10 ** i))
                            n %= (10 ** i)
                            i = i - 1
                        if ii == 1:
                            for idx in range(len(out)):
                                roman_dict.update({il[idx]: roman_num[out[idx]]})
                        else:
                            for idx in range(len(out)):
                                roman_dict.update({il[idx]: roman_num[out[idx]] * (10 ** ii)})
                        ii += 1

                    output = ''
                    sort_dict = sorted(roman_dict.items(), key=lambda kv: (kv[1], kv[0]))
                    for jj in range(len(sort_dict)):
                        output += sort_dict[jj][0]
                        if jj == len(sort_dict) - 1:
                            break
                        if sort_dict[jj][1] * 2 == sort_dict[jj + 1][1] or sort_dict[jj][1] * 5 == sort_dict[jj + 1][1]:
                            pass
                        else:
                            output += '_'

                    return output[::-1]

                def minimize_roman(input_):
                    tmp_input = input_
                    flag = True
                    roman_string = get_roman_string()
                    roman_idxs = get_roman_idxs(roman_string)
                    num_list = []
                    roman_list = []
                    o_string_ = ''
                    n_string_ = ''
                    while flag:
                        min_string, remain_string = get_minimize_string(tmp_input)
                        o_string_ = min_string + o_string_
                        o_idx = get_idx(o_string_)
                        idx_flag, min_idx = get_min_idx(roman_idxs, o_idx)
                        if idx_flag and len(remain_string) != 0:
                            n_string_ = min_string + n_string_
                            tmp_input = remain_string
                        elif idx_flag and len(remain_string) == 0:
                            n_string_ = min_string + n_string_
                            if len(n_string_) == 1:
                                for iii in roman_list:
                                    if n_string_ in iii:
                                        print('Hey, ask me something that\'s not impossible to do!')
                                        sys.exit()
                            roman_list.append(n_string_)
                            num_list.append(str(min_idx + 1))
                            p_string_ = ''.join(num_list[::-1])
                            min_using = minimize_using(num_list, roman_list)
                            print(f'Sure! It is {p_string_} using {min_using}')
                            sys.exit()
                        else:
                            if len(n_string_) == 0:
                                print('Hey, ask me something that\'s not impossible to do!')
                                sys.exit()
                            else:
                                if len(n_string_) == 1:
                                    for iii in roman_list:
                                        if n_string_ in iii:
                                            print('Hey, ask me something that\'s not impossible to do!')
                                            sys.exit()
                                roman_list.append(n_string_)
                                _, nn_idx = get_min_idx(roman_idxs, get_idx(n_string_))
                                num_list.append(str(nn_idx + 1))
                                o_string_ = ''
                                n_string_ = ''
                                tmp_input = remain_string + min_string

                        nn_string_ = ''.join(roman_list)
                        if len(nn_string_) == len(input_):
                            p_string_ = ''.join(num_list[::-1])
                            min_using = minimize_using(num_list, roman_list)
                            print(f'Sure! It is {p_string_} using {min_using}')
                            sys.exit()

                minimize_roman(string)

            break


        elif len(word_new) == 5:
            if word_new[3] == 'using':

                # print('1111')
                string_a = word_new[2]
                string_b = word_new[-1]

                if string_b[0].isalpha() is False:
                    print("Hey, ask me something that's not impossible to do!")


                elif string_a[0].isalpha() is True:
                    string_a = word_new[2]
                    string_b = word_new[-1]
                    string_b = string_b[::-1]
                    create_dict = {}

                    for i in string_b:
                        a = string_b.index(i)
                        if a == 0:
                            create_dict.update([(i, 1)])
                        elif a % 2 == 0:
                            n = a / 2
                            create_dict.update([(i, int(1 * (10 ** n)))])
                            a += 2
                            # print(create_dict)
                        elif a % 2 == 1:
                            n = (a - 1) / 2
                            create_dict.update([(i, int(5 * (10 ** n)))])

                    # print(create_dict)

                    def roman_to_int(string_a):

                        if (string_a[-1] != string_b[0] and string_a.count(string_b[0]) > 1):
                            print("Hey, ask me something that's not impossible to do!")
                            sys.exit()

                        elif not all(x in string_b for x in string_a):
                            print("Hey, ask me something that's not impossible to do!")
                            sys.exit()

                        elif any(string_b.count(x) > 1 for x in string_b):
                            print("Hey, ask me something that's not impossible to do!")
                            sys.exit()

                        elif any(string_a.count(x) > 1 and string_b.index(x) % 2 == 1 for x in string_b):
                            print("Hey, ask me something that's not impossible to do!")
                            sys.exit()

                        else:
                            res = 0

                            for i in range(len(string_a)):
                                if i < len(string_a) - 1 and create_dict[string_a[i]] < create_dict[string_a[i + 1]]:
                                    res -= create_dict[string_a[i]]
                                else:
                                    res += create_dict[string_a[i]]
                            return res

                    print("Sure! It is", roman_to_int(string_a))
                    break

                else:
                    string_a = int(string_a)
                    string = string_b[::-1]
                    create_dict = {}
                    # print(create_dict)
                    for i in string:
                        a = string.index(i)
                        if a == 0:
                            create_dict.update([(1, i)])
                        elif a % 2 == 0:
                            n = a / 2
                            create_dict.update([(int(1 * (10 ** n)), i)])
                            a += 2
                            # print(create_dict)
                        elif a % 2 == 1:
                            n = (a - 1) / 2
                            create_dict.update([(int(5 * (10 ** n)), i)])

                    def int_to_roman(string_a):

                        div = 1

                        while string_a >= div:
                            div *= 10

                        div /= 10

                        res = ""

                        while string_a:
                            lastNum = int(string_a / div)

                            if lastNum <= 3:
                                res += (create_dict[div] * lastNum)
                            elif lastNum == 4:
                                res += (create_dict[div] + create_dict[div * 5])
                            elif 5 <= lastNum <= 8:
                                res += (create_dict[div * 5] + (create_dict[div] * (lastNum - 5)))
                            elif lastNum == 9:
                                res += (create_dict[div] + create_dict[div * 10])

                            string_a = math.floor(string_a % div)
                            div /= 10
                        return res

                    print("Sure! It is", str(int_to_roman(string_a)))

            else:
                print("I don't get what you want, sorry mate!")
            break

        else:
            print("I don't get what you want, sorry mate!")
            break
    else:
        print("I don't get what you want, sorry mate!")


please_convert()
