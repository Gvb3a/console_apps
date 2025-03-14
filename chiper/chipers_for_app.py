from time import sleep

# ================================<   Caesar cipher   >================================
def caesar_cipher(text, shift, settings = {}):
    shift = int(shift)
    result = ''
    upper_letter = settings.get('upper_letter', 'A')
    lower_letter = settings.get('lower_letter', 'a')
    alphabet_size = settings.get('alphabet_size', 26)
    format_text = settings.get('format_text', False)

    if format_text:
        text = text.upper()
        text = ''.join([char for char in text if char.isalpha()])

    for char in text:
        if char.isalpha():
            start = ord(lower_letter) if char.islower() else ord(upper_letter)
            shifted_char = chr((ord(char) - start + shift) % alphabet_size + start)
        else:
            shifted_char = char
        result += shifted_char

    if format_text:
        result = result.upper() if upper_letter.isupper() else result.lower()

    return result


def breaking_caesar_cipher(text, settings = {}):
    alphabet_size = settings.get('alphabet', 26)
    upper_letter = settings.get('upper_letter', 'A')
    lower_letter = settings.get('lower_letter', 'a')

    for shift in range(alphabet_size):
        result = ''
        for char in text:
            if char.isalpha():
                start = ord(lower_letter) if char.islower() else ord(upper_letter)
                shifted_char = chr((ord(char) - start - shift) % alphabet_size + start)
            else:
                shifted_char = char
            result += shifted_char
        print(f'Shift {shift}: {result}')
    return ''


def visualization_caesar_cipher(text, shift, settings = {}):
    shift = int(shift)
    upper_letter = settings.get('upper_letter', 'A')
    lower_letter = settings.get('lower_letter', 'a')
    alphabet_size = settings.get('alphabet_size', 26)
    format_text = settings.get('format_text', False)

    if format_text:
        text = text.upper()
        text = ''.join([char for char in text if char.isalpha()])
    
    for i in range(shift + 1):
        shifted_text = ""
        for char in text:
            if char.isupper():
                start = ord(upper_letter)
                shifted_char = chr((ord(char) - start - i) % alphabet_size + start)
            elif char.islower():
                start = ord(lower_letter)
                shifted_char = chr((ord(char) - start - i) % alphabet_size + start)
            else:
                shifted_char = char
            shifted_text += shifted_char


        spaced_text = " ".join(shifted_text)
        print(f"{spaced_text}")
        if i != shift:
            arrows = " ".join(["↓" for _ in shifted_text])
            print(f"{arrows}")
        sleep(0.2)
# ================================<   Caesar cipher   >================================


# ================================<   Zigzag cipher   >================================
def zigzag_cipher(text, key, settings = {}):
    result = ''
    key = int(key)
    symbol_for_space = settings.get('symbol_for_space', 'X')
    if settings.get('format_text', False):
        text = text.upper()
        text = text.replace(' ', symbol_for_space)
        text = ''.join([char for char in text if char.isalpha()])

    matrix = [[""] * len(text) for _ in range(key)]
    rail = 0 
    variation = 1 

    for i in range(len(text)):
        matrix[rail][i] = text[i]
        rail += variation
        if rail == key - 1 or rail == 0:
            variation = -variation

    result = "".join("".join(matrix[r]) for r in range(key))
    return result


def zigzag_decrypt(text, rails):
    if rails == 1:
        return text

    matrix = [[""] * len(text) for _ in range(rails)]
    rail = 0
    variation = 1

    for i in range(len(text)):
        matrix[rail][i] = "*"
        rail += variation
        if rail == rails - 1 or rail == 0:
            variation = -variation

    index = 0
    for r in range(rails):
        for c in range(len(text)):
            if matrix[r][c] == "*" and index < len(text):
                matrix[r][c] = text[index]
                index += 1

    result = []
    rail = 0
    variation = 1
    for i in range(len(text)):
        result.append(matrix[rail][i])
        rail += variation
        if rail == rails - 1 or rail == 0:
            variation = -variation

    return "".join(result)


def breaking_zigzag_cipher(text, settings):
    
    for i in range(2, len(text)):
        print(f'Rails {i}: {zigzag_decrypt(text, i)}')
    return ''
# ================================<  Zigzag cipher  >================================


# ================================< Vigenere cipher >================================
def vigenere_cipher(text: str, key: str, settings: dict = {}):
    upper_letter = settings.get('upper_letter', 'A')
    alphabet_size = settings.get('alphabet_size', 26)

    text = text.upper()
    text = ''.join([char for char in text if char.isalpha()])

    alphabet = [chr(ord(upper_letter) + i) for i in range(alphabet_size)]
    encrypted_text = []

    if key == int:
        key = str(key)

    if key.isdigit() or '-' in key:
        if '-' in key:
            key = key.split('-')
        key = [alphabet[int(digit)] for digit in key] 
        key = ''.join(key)
    key = key.upper().replace(' ', '')
    key_length = len(key)
    
    for i, char in enumerate(text.upper()):
        if char in alphabet:
            shift = alphabet.index(key[i % key_length])
            encrypted_char = alphabet[(alphabet.index(char) + shift) % alphabet_size]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)
# ================================< Vigenere cipher >================================
