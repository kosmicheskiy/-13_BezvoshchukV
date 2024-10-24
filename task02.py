from collections import Counter
import re

# Шифрування тексту за допомогою шифру Віженера
def vigenere_cipher_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    
    for i in range(len(plaintext_int)):
        if plaintext[i].isalpha():
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            encrypted_text.append(chr(value + 65 if plaintext[i].isupper() else value + 97))
        else:
            encrypted_text.append(plaintext[i])
    
    return ''.join(encrypted_text)

# Частотний аналіз шифрованого тексту
def frequency_analysis(text):
    text = [char.lower() for char in text if char.isalpha()]
    frequencies = Counter(text)
    total_letters = sum(frequencies.values())
    return {char: round(frequency / total_letters, 4) for char, frequency in frequencies.items()}

# Метод Касіскі для визначення довжини ключа
def kasiski_examination(ciphertext):
    sequences = {}
    
    # Пошук тризнакових підрядків у шифротексті
    for i in range(len(ciphertext) - 3):
        trigram = ciphertext[i:i+3]
        occurrences = [m.start() for m in re.finditer(f'(?={trigram})', ciphertext)]
        if len(occurrences) > 1:
            distances = [occurrences[j+1] - occurrences[j] for j in range(len(occurrences)-1)]
            sequences[trigram] = distances
    
    # Визначення найбільш ймовірної довжини ключа як НСД (найбільшого спільного дільника) між відстанями
    all_distances = [dist for dists in sequences.values() for dist in dists]
    key_length = gcd_multiple(all_distances)
    
    return key_length

# Пошук НСД для кількох чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    return numbers[0] if len(numbers) == 1 else gcd(numbers[0], gcd_multiple(numbers[1:]))

# Тест Фрідмана для визначення довжини ключа
def friedman_test(ciphertext):
    n = len(ciphertext)
    frequency = Counter([c for c in ciphertext if c.isalpha()])
    
    # Індекс відповідності для англійської мови
    ic = sum(f * (f - 1) for f in frequency.values()) / (n * (n - 1))
    
    # Очікуваний індекс відповідності для випадкового тексту (англ.)
    expected_ic = 0.0385
    key_length_estimate = 0.0265 / (ic - expected_ic) if ic != expected_ic else 1
    
    return round(key_length_estimate)

# Розділення шифротексту на сегменти відповідно до довжини ключа
def split_by_key_length(ciphertext, key_length):
    segments = [''] * key_length
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            segments[i % key_length] += char
    return segments

# Розшифрування шифру Віженера
def vigenere_cipher_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            decrypted_text.append(chr(value + 65 if ciphertext[i].isupper() else value + 97))
        else:
            decrypted_text.append(ciphertext[i])
    
    return ''.join(decrypted_text)

# Основна функція для шифрування, частотного аналізу та розшифрування
def main():
    plaintext = "Hello, this is an example of Vigenere cipher encryption."
    key = "KEY"

    # Шифрування тексту
    encrypted_text = vigenere_cipher_encrypt(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")
    
    # Частотний аналіз шифрованого тексту
    cipher_frequencies = frequency_analysis(encrypted_text)
    print(f"Frequency Analysis: {cipher_frequencies}")
    
    # Визначення довжини ключа
    kasiski_key_length = kasiski_examination(encrypted_text)
    print(f"Kasiski Key Length: {kasiski_key_length}")
    
    friedman_key_length = friedman_test(encrypted_text)
    print(f"Friedman Key Length: {friedman_key_length}")
    
    # Розшифрування тексту з відомим ключем
    decrypted_text = vigenere_cipher_decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")

# Запуск основної функції
if __name__ == "__main__":
    main()
