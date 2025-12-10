class Operations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        try:
             result = a / b
             return result
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            print(ex)
            return None