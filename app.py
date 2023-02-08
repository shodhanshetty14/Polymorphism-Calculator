
class Add:
    def calculate(self, x, y):
        return x + y


class Sub:
    def calculate(self, x, y):
        return x - y


class Mul:
    def calculate(self, x, y):
        return x * y


class Div:
    def calculate(self, x, y):
        return x / y


class Pow:
    def calculate(self, x, y):
        return x ** y



class Mod:
    def calculate(self, x, y):
        return x % y


operator = {
    '+' : Add(),
    '-' : Sub(),
    '*' : Mul(),
    '/' : Div(),
    '**' : Pow(),
    '%' : Mod()
}


if __name__ == '__main__':
    while True:
        choice = input("Select opertaion to perform(to quit press q): ")
        if choice.lower() == 'q':
            break
        op = operator[choice]
        x, y = int(input("Enter first number: ")), int(input("Enter second number: "))
        print(f"{x} {choice} {y} = {op.calculate(x, y)}")