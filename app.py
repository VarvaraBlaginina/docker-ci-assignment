import random

alf = "%#-&$ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
alf_len = len(alf)  # Длина алфавита (67 символов)
def only_alf(vvod_str):
    for symbol in vvod_str:
        if symbol not in alf:
            return False
    return True

if __name__ == "__main__":

    while True:
        pwd_len_vvod = input("Укажите длину пароля(ей): ")
        if pwd_len_vvod.isdigit():
            pwd_len = int(pwd_len_vvod)
            if pwd_len >= 8:
                break
            else:
                print("Ошибка: длина пароля должна быть не менее 8 символов.")
        else:
            print("Ошибка: длина пароля должна быть целым числом.")

    while True:
        pwd_kol_vvod = input("Укажите количество паролей: ")
        if pwd_kol_vvod.isdigit():
            pwd_kol = int(pwd_kol_vvod)
            if pwd_kol >= 1:
                break
            else:
                print("Ошибка: количество паролей должно быть не менее 1.")
        else:
            print("Ошибка: количество паролей должно быть целым числом.")

    password_list = []
    for n in range(pwd_kol):
        password = ''.join(random.choice(alf) for n in range(pwd_len))
        password_list.append(password)

    print("\nСозданные пароли: ")
    for pwd in password_list:
        print(pwd)

    while True:
        key = input("Введите ключ для шифрования: ")
        if len(key) >= 1 and only_alf(key):
            break
        else:
            print("Ошибка: ключ должен содержать только символы из алфавита и не может быть пустым.")

    # Шифрование паролей
    shifr_passwords = []
    for pwd in password_list:
        shifr_pwd = []
        for i in range(len(pwd)):
            # Индекс символа сообщения в алфавите
            symbol_index = alf.find(pwd[i])
            # Индекс символа ключа в алфавите (ключ повторяется, если он короче сообщения)
            key_symbol_index = alf.find(key[i % len(key)])
            # Шифрование: (symbol_index + key_symbol_index) mod alfa_len
            shifr_symbol_index = (symbol_index + key_symbol_index) % alf_len
            # Преобразование индекса обратно в символ
            shifr_symbol = alf[shifr_symbol_index]
            # Добавляет зашифрованный символ в список
            shifr_pwd.append(shifr_symbol)
            # Добавляет зашифрованный пароль (строку) в общий список зашифрованных паролей.
        shifr_passwords.append(''.join(shifr_pwd))

    with open('passwords_shifr.txt', 'w', encoding='utf-8') as f:
        for shifr_pwd in shifr_passwords:
            f.write(shifr_pwd + '\n')
    print('Пароли сохранены в файл "passwords_shifr.txt" в зашифрованном виде.')