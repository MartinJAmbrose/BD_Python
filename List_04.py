# Use Modulo to find ODD numbers in a list.
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):

        if i % 2 != 0:
            odd_numbers.append(i)



    return odd_numbers