def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Не може ділитись на 0")
    return x / y

def main():
    while True:
        print("\nВиберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("0. Вихід")

        choice = input("Введіть вибір (1/2/3/4/5): ")

        if choice == '5':
            print("Вихід із калькулятора")
            break

        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"Результат: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Неправильний вибір")

if __name__ == "__main__":
    main()
