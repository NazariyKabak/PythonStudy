# task1
def method_ceaser(s, n):
    encrypted_s = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord("a") + n) % 26 + ord("a"))

            elif char.isupper():
                new_char = chr((ord(char) - ord("A") + n) % 26 + ord("A"))

            encrypted_s += new_char
        else:
            encrypted_s += char
    return encrypted_s


#task2
