def apply_all_func(int_list, *functions):   #функция, принимающая список чисел и неограниченное количесвто функций
    results = {}    #создание пустого словаря
    for func in functions:  #переборка функций
        results[func.__name__] = func(int_list)     #пополнение словаря ключ = имя функции, значение = результат работы
    return results


# пример работы функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
