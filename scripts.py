import sys
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines if line.strip()]

# function to get first word and rest of the content
split_lines = lambda line : (line.split(' ')[0], line.split(' ')[1:])

main_index = []
intendation = ''
for line_index, line in enumerate(lines):
    first_word, content = split_lines(line)
    if first_word.startswith('*'):
        if len(first_word) == 1:
            main_index = [1] if not main_index else [main_index[0] + 1]
            print('{} {}'.format('.'.join(map(str,main_index)), ' '.join(content)))
        else:
            first_word_length = len(first_word)
            if len(main_index) < first_word_length:
                main_index.append(1)
            elif len(main_index) > first_word_length:
                main_index = main_index[:first_word_length]
                main_index[first_word_length-1] += 1
            else:
                main_index[first_word_length-1] += 1
            print('{} {}'.format('.'.join(map(str,main_index)), ' '.join(content)))
        intendation = ''
    elif first_word.startswith('.'):
        next_first_word, _content = split_lines(lines[line_index+1]) if len(lines) > line_index + 1 else (None, None)
        if next_first_word and next_first_word == '*' * len(next_first_word):
            intendation = '   '*len(first_word)
            print('{} - {}'.format(intendation,' '.join(content)))
        else:
            intendation = '   '*len(first_word)
            if next_first_word and len(next_first_word) > len(first_word):
                print('{} + {}'.format(intendation,' '.join(content)))
            else:
                print('{} - {}'.format(intendation,' '.join(content)))
    else:
        print('{}   {}'.format(intendation, line))
        