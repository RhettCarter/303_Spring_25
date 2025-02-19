def encode(input, shift):
    letters = list('abcdefghijklmnopqrstuvwxyz')

    encode_text = []

    for char in input:
        if char.islower():
            index = letters.index(char)
            new_index = (index + shift) % 26
            encode_text.append(letters[new_index])
        else:
            encode_text.append(char)
    encode_text = ''.join(encode_text)
    return letters, encode_text

def decode(input, shift):
    letters = list('abcdefghijklmnopqrstuvwxyz')

    decode_text = []

    for char in input:
        if char.islower():
            index = letters.index(char)
            new_index = (index - shift) % 26
            decode_text.append(letters[new_index])
        else: decode_text.append(char)
    decode_text = ''.join(decode_text)
    return decode_text