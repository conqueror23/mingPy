import re
import math

Roman_number = ['I','V','X','L','C','D','M']
Arabic_number = [0,1,2,3,4,5,6,7,8,9]
Dict = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]


def please_convert():
    word = input('How can I help you? ')
    word_new = word.split()
    # print(word_new)

    while (word_new[0] == 'Please' and word_new[1] =='convert'):
        if len(word_new) == 3:
            string = word_new[-1]
            if string[0] == '0':
                print("Hey, ask me something that's not impossible to do!")
            elif string[0] in Roman_number:
                if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string))==True:
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
                    print("Sure! It is",roman_to_int(string))
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
            print('2')
            break
        elif len(word_new) == 5:
            if word_new[3] == 'using':
                # print('1111')
                string_a = word_new[2]
                string_b = word_new[-1]
                if string_a[0].isalpha() is True:
                    string_a = word_new[2]
                    string_b = word_new[-1]
                    string_b = string_b[::-1]
                    create_dict = { }
                    for i in string_b:
                        a = string_b.index(i)
                        if a == 0:
                            create_dict.update([(i,1)])
                        elif a%2 == 0:
                            n = a/2
                            create_dict.update([(i,int(1*(10**n)))])
                            a += 2
                            #print(create_dict)
                        elif a%2 == 1:
                            n = (a-1)/2
                            create_dict.update([(i,int(5*(10**n)))])
                    # print(create_dict)
                    def roman_to_int(string_a):
                        res = 0
                        for i in range(len(string_a)):
                            if i<len(string_a)-1 and create_dict[string_a[i]]<create_dict[string_a[i+1]]:
                                res -= create_dict[string_a[i]]
                            else:
                                res += create_dict[string_a[i]]
                        return res
                    print("Sure! It is",roman_to_int(string_a))
                elif word_new[2] == '_':
                    print("Hey, ask me something that's not impossible to do!")
                else:
                    string_a = int(string_a)
                    string = string_b[::-1]
                    create_dict = { }
                    # print(create_dict)
                    for i in string:
                        a = string.index(i)
                        if a == 0:
                            create_dict.update([(1,i)])
                        elif a%2 == 0:
                            n = a/2
                            create_dict.update([(int(1*(10**n)),i)])
                            a += 2
                            #print(create_dict)
                        elif a%2 == 1:
                            n = (a-1)/2
                            create_dict.update([(int(5*(10**n)),i)])
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
