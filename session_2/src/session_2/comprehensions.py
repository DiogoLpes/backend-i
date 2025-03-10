def main():
    my_list: list[float] = [...]
    my_set: set[float] = [...]
    my_tuple: tuple[float] = (...)
    my_dict: dict[str, float] = {'a': 1.0}


    def add_to_list(value):
        my_list.append(value)

    
    my_tuple.__add__(2)
    add_to_list(2)
    print(my_tuple)

    if __name__ == "__main__":
        main()