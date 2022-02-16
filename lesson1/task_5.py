list = 'abcdefghijklmnopqrstuvwxyz'
def char_position(letter, letter1):

    letter_pos_1 = list.find(letter1.lower())+1
    letter_pos = list.find(letter.lower())+1

    print(f'{letter} - {letter_pos}')
    print(f'{letter1} - {letter_pos_1}')
    print(letter_pos_1-letter_pos)


letter = input('Введите первую букву')
letter1 = input('Введите иторую букву')
char_position(letter, letter1)