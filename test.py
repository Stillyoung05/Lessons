def rom_to_arab(roman):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    global arabic_num
    arabic_num = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and roman_num[roman[i]] < roman_num[roman[i + 1]]:
            arabic_num -= roman_num[roman[i]]
        else:
            arabic_num += roman_num[roman[i]]
    return arabic_num


roman_numeral = input("Enter Roman num: ").capitalize()
arabic_num = rom_to_arab(roman_numeral)
print(f'The Arabic numeral for {roman_numeral} is {arabic_num}')
