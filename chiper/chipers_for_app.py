def caesar_cipher(text, shift, settings):
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


def breaking_caesar_cipher(text, settings):
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


def zigzag_cipher(text, key, settings = {}):
    result = ''
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