with open('day_one_numbers.txt') as my_file:
    numbers_array = my_file.read().splitlines()
    numbers_array = [int(i) for i in numbers_array]

def get_product_with_two_factors(numbers_array, sum):
    for first_number in numbers_array:
        remaining_number = sum - first_number
        if remaining_number in numbers_array:
            product = first_number * remaining_number
            print('First number: ' + str(first_number) +
                  '; Second number: ' + str(remaining_number) +
                  '; Product: ' + str(product))
            return product
    raise ValueError("No two factors result in the given sum: " + str(sum) + '; Array starts with: ' + str(numbers_array[0]))

test = list(map(int, '''\
1721
979
366
299
675
1456
'''.splitlines()))
assert get_product_with_two_factors(test, 2020) == 514579

def get_product_with_three_factors(numbers_array, sum):
    for first_number in numbers_array:
        remaining_number = sum - first_number
        for second_number in numbers_array:
            if first_number != second_number and remaining_number > second_number:  # for a little optimization
                third_number = remaining_number - second_number
                if third_number in numbers_array:
                    product = first_number * second_number * third_number
                    print('First number: ' + str(first_number) +
                          '; Second number: ' + str(second_number) +
                          '; Third number: ' + str(third_number) +
                          '; Product: ' + str(product))
                    return product
    raise ValueError("No three factors result in the given sum: " + str(sum) + '; Array starts with: ' + str(numbers_array[0]))

test = list(map(int, '''\
1721
979
366
299
675
1456
'''.splitlines()))
assert get_product_with_three_factors(test, 2020) == 241861950

if __name__ == '__main__':
    get_product_with_two_factors(numbers_array, 2020)
    get_product_with_three_factors(numbers_array, 2020)
