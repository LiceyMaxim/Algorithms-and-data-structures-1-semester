def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return text == '\n'


input_file = open('brackets.in', 'r')
output_file = open('brackets.out', 'a')
input_text = input_file.readline()
while input_text:
    if is_correct_brackets(input_text):
        print('YES', file=output_file)
    else:
        print('NO', file=output_file)
    input_text = input_file.readline()
