def format_text(text):
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] == '@':
            for j in range(i, len(text_list)):
                if text_list[j] == '#':
                    text_list[j] = ''
                    break
    text = ''.join(text_list)
    text = text.replace('\\n', '\n')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

text = input()
print("Formatted Text: " + format_text(text))
