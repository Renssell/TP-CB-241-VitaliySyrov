from log import write_log
def add(a:float, b: float):
    result = a + b
    write_log(f"Add: {a} + {b} = {result}")
    return result
def sub(a:float,b:float):
    result = a-b
    write_log(f"Sub: {a} - {b} = {result}")
    return result
def mul(a:float,b:float):
    result = a * b
    write_log(f"Mul: {a} * {b} = {result}")
    return result
def div(a:float,b:float):
    try:
        result = a / b
        write_log(f"Div: {a} / {b} = {result}")
        return result
    except Exception as ex:
        write_log("Divide zero unavalaible")
        print(type(ex))
        print(ex.args)
        print(ex)
        return None
        
