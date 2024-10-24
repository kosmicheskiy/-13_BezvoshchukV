from collections import Counter

# Шифрування Цезаря з заданим зсувом
def caesar_cipher_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_char = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - shift_char + shift) % 26 + shift_char))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Частотний аналіз шифрованого тексту
def frequency_analysis(text):
    text = [char.lower() for char in text if char.isalpha()]
    frequencies = Counter(text)
    total_letters = sum(frequencies.values())
    return {char: round(frequency / total_letters, 4) for char, frequency in frequencies.items()}

# Розшифрування Цезаря з використанням зсуву
def caesar_cipher_decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            shift_char = 65 if char.isupper() else 97
            decrypted_text.append(chr((ord(char) - shift_char - shift) % 26 + shift_char))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Функція для перебору всіх можливих зсувів
def brute_force_caesar(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Приклад використання
original_text = "Hello, World!"
shift = 3

# Шифруємо текст
encrypted_text = caesar_cipher_encrypt(original_text, shift)
print(f"Encrypted Text: {encrypted_text}")

# Виконуємо частотний аналіз шифрованого тексту
cipher_frequencies = frequency_analysis(encrypted_text)
print(f"Frequency Analysis: {cipher_frequencies}")

# Виконуємо brute-force для пошуку правильного зсуву
print("\nTrying all possible shifts:")
brute_force_caesar(encrypted_text)



# Encrypted Text: Khoor, Zruog!
# Frequency Analysis: {'k': 0.1, 'h': 0.1, 'o': 0.3, 'r': 0.2, 'z': 0.1, 'u': 0.1, 'g': 0.1}

# Trying all possible shifts:
# Shift 0: Khoor, Zruog!
# Shift 1: Jgnnq, Yqtnf!
# Shift 2: Ifmmp, Xpsme!
# Shift 3: Hello, World!
# Shift 4: Gdkkn, Vnqkc!
# Shift 5: Fcjjm, Umpjb!
# Shift 6: Ebiil, Tloia!
# Shift 7: Dahhk, Sknhz!
# Shift 8: Czggj, Rjmgy!
# Shift 9: Byffi, Qilfx!
# Shift 10: Axeeh, Phkew!
# Shift 11: Zwddg, Ogjdv!
# Shift 12: Yvccf, Nficu!
# Shift 13: Xubbe, Mehbt!
# Shift 14: Wtaad, Ldgas!
# Shift 15: Vszzc, Kcfzr!
# Shift 16: Uryyb, Jbeyq!
# Shift 17: Tqxxa, Iadxp!
# Shift 18: Spwwz, Hzcwo!
# Shift 19: Rovvy, Gybvn!
# Shift 20: Qnuux, Fxaum!
# Shift 21: Pmttw, Ewztl!
# Shift 22: Olssv, Dvysk!
# Shift 23: Nkrru, Cuxrj!
# Shift 24: Mjqqt, Btwqi!
# Shift 25: Lipps, Asvph!

# === Code Execution Successful ===
