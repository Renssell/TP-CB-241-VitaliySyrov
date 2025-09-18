def test_string_methods():
    text = "   hello world   "
    print("Оригінал:", repr(text))
    print("strip():", repr(text.strip()))       
    print("capitalize():", text.strip().capitalize())  
    print("title():", text.strip().title())     
    print("upper():", text.strip().upper())      
    print("lower():", text.strip().lower())     
test_string_methods()