# code_inject
📁 Cấu trúc thư mục
Sao chép
Chỉnh sửa
~~~bash
python-projects/
├── calculator/
│   └── calculator.py
├── guess_number/
│   └── guess_number.py
├── contact_book/
│   └── contact_book.py
├── word_counter/
│   └── word_counter.py
├── .gitignore
└── README.md
~~~
📄 Nội dung file .gitignore
gitignore
```bash
__pycache__/
*.pyc
*.log
*.txt
```
📄 Nội dung README.md
# 🐍 Python Projects for Beginners

This repository contains small Python projects to help you practice basic programming skills and learn how to use GitHub.

---

## 📂 Project List

### 1. `calculator/`
A simple calculator that performs basic arithmetic operations.
- Operations: Add, Subtract, Multiply, Divide
- Handles division by zero

Run:
```bash
python calculator/calculator.py
```
2. guess_number/
A number guessing game between 1 and 100.
Random number generation
Tracks number of attempts

Run:

```bash
python guess_number/guess_number.py
```
3. contact_book/
A basic contact management system.
Add, search, and display contacts
Stores data in memory (not saved after program exits)

Run:

```bash
python contact_book/contact_book.py
```
4. word_counter/
Counts the number of words in a .txt file.
Handles file reading and error checking
Splits text into words

Run:
```bash
python word_counter/word_counter.py
```
💡 Example:
Create a text file named sample.txt and run the script.

🚀 How to Use This Repo
Clone this repository:

```bash
git clone https://github.com/your-username/python-projects.git
cd python-projects
```
Navigate into any project folder and run the script.
Feel free to edit, commit, and push your changes as you learn Git & GitHub.

🧪 Optional Enhancements
Add file saving for ```contact_book```
Use classes and objects
Convert ```calculator``` into a GUI version with Tkinter
Add error logging to ```word_counter```

📝 License
This project is open source and available under the MIT License.

### 📄 Nội dung các file `.py`

#### `calculator/calculator.py`
```python
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
```
guess_number/guess_number.py

```python
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
```
contact_book/contact_book.py
```python
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact(name):
    print(f"{name}: {contacts.get(name, 'Không tìm thấy')}")

while True:
    print("\n--- Quản lý danh bạ ---")
    print("1. Thêm liên hệ")
    print("2. Xem tất cả")
    print("3. Tìm kiếm")
    print("4. Thoát")

    choice = input("Chọn: ")

    if choice == '1':
        name = input("Tên: ")
        phone = input("Số điện thoại: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Nhập tên cần tìm: ")
        search_contact(name)
    elif choice == '4':
        break
    else:
        print("Lựa chọn không hợp lệ!")
```
word_counter/word_counter.py
```python
def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            print(f"Tổng số từ: {len(words)}")
    except FileNotFoundError:
        print("Không tìm thấy file.")

filename = input("Nhập tên file (có đuôi .txt): ")
count_words(filename)
```
