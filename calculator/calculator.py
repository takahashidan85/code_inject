def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Không thể chia cho 0"

while True:
    print("\nChọn phép tính:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

    choice = input("Lựa chọn (1/2/3/4/5): ")

    if choice == '5':
        break

    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    if choice == '1':
        print("Kết quả:", add(a, b))
    elif choice == '2':
        print("Kết quả:", subtract(a, b))
    elif choice == '3':
        print("Kết quả:", multiply(a, b))
    elif choice == '4':
        print("Kết quả:", divide(a, b))
    else:
        print("Lựa chọn không hợp lệ!")