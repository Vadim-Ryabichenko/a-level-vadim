def my_sum(list_of_numbers):

    summa = 0
    for i in list_of_numbers:
       summa += i
    
    return summa

l = [1, 3, 5, 7, 9]

print(my_sum(l))