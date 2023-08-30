# Developer "Nikhil Vishwakarma"  , GitHub : https://github.com/nikhivishwaa
# Development Partner  : Knilce
# ©️ Knilce - All Rights are reserved
# first Update on : 31/08/2023


from random import choice as cd

alpha_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_small = alpha_capital.lower()
Special_char = "_-"
numbers = "0123456789"

def login_code():
    code_1 = cd(alpha_capital) + cd(numbers) + cd(alpha_small) + cd(Special_char) + cd(alpha_small) + cd(numbers) + cd(alpha_capital) + cd(alpha_small)
    code_2 = cd(alpha_small) + cd(Special_char) + cd(numbers) + cd(Special_char) + cd(alpha_small) + cd(numbers)
    code_3 = cd(alpha_small) + cd(numbers) + cd(numbers) + cd(Special_char) + cd(numbers) + cd(numbers) + cd(alpha_capital)
    code_4 = cd(alpha_capital) + cd(numbers) + cd(alpha_small) + cd(Special_char) + cd(alpha_capital) + cd(alpha_small) + cd(alpha_capital) + cd(alpha_small)
    code_5 = cd(numbers) + cd(alpha_capital) + cd(numbers) + cd(Special_char) + cd(alpha_small) + cd(numbers)
    code_6 = cd(alpha_capital) + cd(numbers) + cd(numbers) + cd(Special_char) + cd(alpha_small) + cd(alpha_capital) + cd(numbers)
    code_7 = cd(alpha_small) + cd(alpha_small) + cd(alpha_capital) + cd(Special_char) + cd(alpha_small) + cd(numbers)
    code_8 = cd(alpha_capital) + cd(numbers) + cd(numbers) + cd(Special_char) + cd(alpha_small) + cd(Special_char)
    code_9 = cd(alpha_small) + cd(Special_char) + cd(numbers) + cd(Special_char) + cd(alpha_capital) + cd(numbers) + cd(numbers) + cd(alpha_small) 
    code_10 = cd(numbers) + cd(Special_char) + cd(numbers) + cd(alpha_small) + cd(alpha_capital) + cd(numbers) + cd(numbers) + cd(alpha_small) 
    code_11 = cd(numbers) + cd(alpha_capital) + cd(numbers) + cd(Special_char) + cd(alpha_capital) + cd(alpha_small)

    forward = [ code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10, code_11]

    reverse = [ code_1[::-1], code_2[::-1], code_3[::-1], code_4[::-1], code_5[::-1], code_6[::-1], code_7[::-1], code_8[::-1], 
                code_9[::-1], code_10[::-1], code_11[::-1]]

    final = [ cd(forward) + cd(reverse), cd(forward), cd(reverse) + cd(reverse), cd(forward) + cd(forward), cd(reverse) + code_1,
            code_10 + code_11, code_5 + cd(reverse), code_9 + cd(forward), cd(reverse) + code_2]
    
    result = cd(final)
    return result
    
if __name__ == "__main__":
    code = login_code()
    print(code)