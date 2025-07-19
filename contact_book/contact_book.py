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