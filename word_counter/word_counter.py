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