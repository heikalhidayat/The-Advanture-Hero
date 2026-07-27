def login():
    user_name = input("Masukkan username: ")
    return user_name

def validasi_menu():
    print("-" * 40, "\n   Welcome In Game The Advanture Hero   \n", "-" * 40, sep="")
    print("1. Main")
    print("2. Status karakter")
    print("3. Shop")
    print("4. Exit")

login()
validasi_menu()
