# Implement the Luhn Algorithm

def verify_card_number(num):
    num = num.replace("-", "").replace(" ", "")
    num_reversed = num[::-1]

    sum_digits = 0

    for index, char in enumerate(num_reversed):
        digit = int(char)

        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        sum_digits += digit

    if sum_digits % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

if __name__ == "__main__":
    print(verify_card_number('453914889'))
    print(verify_card_number('4111-1111-1111-1111'))
    print(verify_card_number('1234 5678 9012 3456'))
