def decrypt_message(input_string):
    input_list = input_string.split()
    char_pos_dict = {int(item[1:]): item[0] for item in input_list}
    sorted_items = sorted(char_pos_dict.items())
    decrypted_string = ''.join(char for pos, char in sorted_items)
    return decrypted_string

encrypted_message = input()
print(decrypt_message(encrypted_message))
