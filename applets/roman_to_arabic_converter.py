def roman_to_arabic(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_dict[roman_numeral[i]] > roman_dict[roman_numeral[i-1]]:
            arabic_numeral += roman_dict[roman_numeral[i]] - 2 * roman_dict[roman_numeral[i-1]]
        else:
            arabic_numeral += roman_dict[roman_numeral[i]]
    return arabic_numeral