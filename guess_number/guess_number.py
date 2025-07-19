import random

secret = random.randint(1, 100)
attempts = 0

print("Tôi đã chọn một số từ 1 đến 100. Hãy đoán nó!")

while True:
    guess = int(input("Nhập số của bạn: "))
    attempts += 1

    if guess < secret:
        print("Lớn hơn!")
    elif guess > secret:
        print("Nhỏ hơn!")
    else:
        print(f"Chính xác! Bạn đoán đúng sau {attempts} lần.")
        break