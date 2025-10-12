def test_list_functions():
    print("Test")
    
    lst = [1, 3, 5]
    print("Початковий список:", lst)

    
    lst.append(7)
    print("Після append(7):", lst)

    
    lst.extend([9, 11])
    print("Після extend([9, 11]):", lst)

   
    lst.insert(1, 2)
    print("Після insert(1, 2):", lst)

    
    lst.remove(5)
    print("Після remove(5):", lst)

    
    copy_lst = lst.copy()
    print("Копія списку:", copy_lst)

    lst.sort()
    print("Після sort():", lst)

    lst.reverse()
    print("Після reverse():", lst)

    lst.clear()
    print("Після clear():", lst)

test_list_functions()
