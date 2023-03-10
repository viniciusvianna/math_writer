def adjust_spaces(member, slots):
    spaces = slots - len(member)
    print(" " * spaces, end="")


def print_member(member, slots):
    adjust_spaces(member, slots)
    for digit in member:
        print(digit, end="")
    print("")


def print_calc_main_body(slots, first_member, second_member):
    print_member(first_member, slots)
    print("X ", end="")
    print_member(second_member, slots - 2)
    print("-" * (slots + 1))


def check_if_binary(number):
    bits = {"0", "1"}
    return number.startswith("0b") and bits.issuperset(set(number[2:]))

def check_if_digit(string_number):
    return string_number.isdigit()


def print_result(slots, first_member, second_member, number_one, result, is_binary):
    if len(second_member) > 1:
        displacement = 0
        for digit in second_member[::-1]:
            if is_binary:
                partial_result = str(bin(int(digit) * number_one))[2:]
            else:
                partial_result = str(int(digit) * number_one)
            if partial_result == "0":
                partial_result = "0" * len(first_member)
            partial_result = partial_result + (" " * displacement)
            print_member(partial_result, slots)
            displacement += 1
        print("-" * (slots + 1))
    print_member(result, slots)


def main():
    number_one = input("Qual será o primeiro número? ").strip()
    number_two = input("Qual será o segundo número? ").strip()
    is_binary = check_if_binary(number_one) and check_if_binary(number_two)
    if is_binary:
        first_member, second_member = sorted(
        [number_one[2:], number_two[2:]], key=len, reverse=True
        )       
        number_one = int(number_one, 2)
        number_two = int(number_two, 2)
        result = str(bin(number_one * number_two))[2:]    
    else:
        is_digit = check_if_digit(number_one) and check_if_digit(number_two)
        if not is_digit:
            raise ValueError("Os dois valores devem ser números inteiros na mesma base (10 ou 2)")
        first_member, second_member = sorted(
        [number_one, number_two], key=len, reverse=True
        )
        number_one = int(number_one)
        number_two = int(number_two)        
        result = str(number_one * number_two)
    slots = len(result) + 2
   
    print_calc_main_body(slots, first_member, second_member)
    print_result(slots, first_member, second_member, number_one, result, is_binary)


if __name__ == "__main__":
    main()