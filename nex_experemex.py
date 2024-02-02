def sum_of_multiples_six_and_ends_six():

    sum_of_numbers = 0

    while True:
        num = int(input())

        if num == 0:
            break

        if num % 6 == 0 and num % 10 == 6:
            sum_of_numbers += num
    print(sum_of_numbers)


sum_of_multiples_six_and_ends_six()