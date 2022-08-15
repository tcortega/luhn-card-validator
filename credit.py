def sum_digits(number):
    return number if number < 10 else sum(int(d) for d in str(number))


def is_valid_card_number(card):
    digits = [int(d) for d in str(card)]

    first_case = sum(digits[::-2])

    second_case_digits = [d * 2 for d in digits[-2::-2]]
    second_case_digits = [sum_digits(d) for d in second_case_digits]
    second_case = sum(second_case_digits)

    checksum = first_case + second_case
    return checksum % 10 == 0


def find_card_provider(card):
    card_length = len(card)
    if card_length in [13, 16] and card[0] == '4':
        return 'VISA\n'

    first_two_digits = int(card[:2])
    if card_length == 15 and first_two_digits in [34, 37]:
        return 'AMEX\n'

    if card_length == 16 and 51 <= first_two_digits <= 55:
        return 'MASTERCARD\n'

    return 'INVÁLIDO\n'


if __name__ == '__main__':
    while True:
        card_input = input('Número: ')
        if not card_input.isnumeric():
            continue

        if not is_valid_card_number(card_input):
            print('INVÁLIDO\n')
            break

        provider = find_card_provider(card_input)
        print(provider)
        break
