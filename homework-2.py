# Backend Programming with Python
# Homework 2
# Question 1 & 3

def split_letters(text_from_file):
    letters = ''.join(e for e in text_from_file if e.isalnum())
    return letters


def arrange_alphabetically(letters):
    sorted_alpha = sorted(letters)
    sorted_list = sorted(sorted_alpha, key=lambda c: letters.count(c), reverse=True)
    return sorted_list


def count_letters(letters_arranged):
    return [letters_arranged.count(i) for i in letters_arranged]


def combine_letters_with_count(letters_count, letters_arranged):
    a = list(zip(letters_arranged, letters_count))
    i = 0
    c = list()
    while i <= len(a)-1:
        if a[i] not in c:
            c.append(a[i])
        i += 1
    return c


def convert_to_string_form(letters_with_count):
    i = 0
    s = str()
    while i <= len(letters_with_count)-1:
        c = f'{letters_with_count[i][0]}: {letters_with_count[i][1]}, '
        s = s + c
        i += 1
    return s


def check_num_belongs(input_list, number):
    print(f'Question 3) part 1) {number} belongs in {input_list}') \
        if len([i for i in input_list if i == number]) > 0 \
        else print(f'{number} does not belongs in {input_list}')


def main():
    with open('homework-2.txt', 'r') as out:
        text_from_file = str(out.read())
        letters = split_letters(text_from_file)
        letters_arranged = arrange_alphabetically(letters)
        letters_count = count_letters(letters_arranged)
        letters_with_count = combine_letters_with_count(letters_count, letters_arranged)
        final_form = convert_to_string_form(letters_with_count)

        print(f'Ques 1) {final_form}')

    with open('result.txt', 'w') as out:
        out.write(final_form)

        input_list = [1, 2, 3, 4, 5, 6]
        number = 7
        check_num_belongs(input_list, number)


if __name__ == "__main__":
    main()
