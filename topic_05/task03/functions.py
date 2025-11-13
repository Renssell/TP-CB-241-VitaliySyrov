def add(a:float, b: float):
    return a+b
def sub(a:float,b:float):
    return a-b
def mul(a:float,b:float):
    return a*b
def div(a:float,b:float):
    try:
        return a / b
    except Exception as ex:
        print(type(ex))
        print(ex.args)
        print(ex)
        return None
        
