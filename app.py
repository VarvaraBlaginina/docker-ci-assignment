import random
import sys

alf = "%#-&$ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
alf_len = len(alf)  # Длина алфавита (67 символов)

def only_alf(vvod_str):
    for symbol in vvod_str:
        if symbol not in alf:
            return False
    return True

def generate_passwords(pwd_len=12, pwd_kol=3, key="DockerCI2024"):
    print("=== ГЕНЕРАТОР И ШИФРОВАТЕЛЬ ПАРОЛЕЙ ===")
    print("CI/CD Демо-режим в Docker контейнере")
    print("="*50 + "\n")
    
    print(f"Параметры:")
    print(f"  • Длина пароля: {pwd_len}")
    print(f"  • Количество паролей: {pwd_kol}")
    print(f"  • Ключ шифрования: {key}")
    print()
    
    # Генерация паролей
    password_list = []
    for n in range(pwd_kol):
        password = ''.join(random.choice(alf) for n in range(pwd_len))
        password_list.append(password)
    
    print("Созданные пароли: ")
    for i, pwd in enumerate(password_list, 1):
        print(f"  {i}. {pwd}")
    
    # Шифрование паролей
    shifr_passwords = []
    for pwd in password_list:
        shifr_pwd = []
        for i in range(len(pwd)):
            symbol_index = alf.find(pwd[i])
            key_symbol_index = alf.find(key[i % len(key)])
            shifr_symbol_index = (symbol_index + key_symbol_index) % alf_len
            shifr_symbol = alf[shifr_symbol_index]
            shifr_pwd.append(shifr_symbol)
        shifr_passwords.append(''.join(shifr_pwd))
    
    print("\nЗашифрованные пароли: ")
    for i, shifr_pwd in enumerate(shifr_passwords, 1):
        print(f"  {i}. {shifr_pwd}")
    
    # Сохранение в файл
    with open('passwords_shifr.txt', 'w', encoding='utf-8') as f:
        for shifr_pwd in shifr_passwords:
            f.write(shifr_pwd + '\n')
    
    print('\n' + '='*50)
    print('✅ Пароли сохранены в файл "passwords_shifr.txt"')
    print('✅ CI/CD процесс завершен успешно!')
    print('='*50)
    
    return password_list, shifr_passwords

if __name__ == "__main__":
    # Автоматический режим для CI/CD
    print("=== CI/CD Assignment: Docker + Jenkins ===")
    print()
    
    # Фиксированные параметры для демо
    passwords, encrypted = generate_passwords()
    
    print("\n" + "="*60)
    print("ОТЧЕТ О ВЫПОЛНЕНИИ:")
    print("="*60)
    print(f"• Сгенерировано паролей: {len(passwords)}")
    print(f"• Длина каждого пароля: 12 символов")
    print(f"• Все пароли зашифрованы и сохранены")
    print("="*60)
