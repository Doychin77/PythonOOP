def get_primes(list):
    for num in list:
        if num == 2 or num == 3:
            yield num
        if num % 2 != 0 and num % 3 != 0 and num > 3:
            yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))