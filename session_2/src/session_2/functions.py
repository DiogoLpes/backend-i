def sum_values(*args):
    total = sum(args)
    return total
result = sum_values(1, 2, 3, 4, 5)
print(result) 


def filter_dic(*kwargs):
    threshold = 25

    for value in kwargs:
        if value > threshold: 
            print(f"{value} - oh ze")
        else:
            #or
            print(value, "hfhgfhgf")
filter_dic(10, 20, 30, 40, 50)
