def test_dict_functions():
    print("Test")

    d = {"name": "Alex", "age": 20, "city": "Kyiv"}
    print("Початковий словник:", d)

    d.update({"age": 21, "country": "Ukraine"})
    print("After update", d)


    print("Ключі:", d.keys())

    print("Значення:", d.values())

    print("Пари ключ-значення:", d.items())

    del d["city"]
    print("Після del d['city']:", d)

    d.clear()
    print("Після clear():", d)

test_dict_functions()
