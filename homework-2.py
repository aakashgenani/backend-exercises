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
    while i <= len(a) - 1:
        if a[i] not in c:
            c.append(a[i])
        i += 1
    return c


def convert_to_string_form(letters_with_count):
    i = 0
    s = str()
    while i <= len(letters_with_count) - 1:
        c = f'{letters_with_count[i][0]}: {letters_with_count[i][1]}, '
        s = s + c
        i += 1
    return s


def check_num_belongs(input_list, number):  # Question 3 part 1
    if len([i for i in input_list if i == number]) > 0:
        print(f'Question 3) part 1) {number} belongs in the list:{input_list} and the index is: {input_list.index(number)}')
    else:
        print(f'Question 3) part 1) {number} does not belong in the list:{input_list} and the index is N/A')


def check_recursive(input_list_sorted, input_list, i, number):  # Question 3 part 2
    if i == len(input_list_sorted):
        print(f'Question 3) part 2) & part 3) {number} does not belong in the list: {input_list} and the index is N/A')
    elif number == input_list_sorted[i]:
        print(f'Question 3) part 2) & part 3) {number} belongs in the list: {input_list} and the index is: {i}')
    else:
        check_recursive(input_list_sorted, input_list, i + 1, number)


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

        input_list = [1, 2, 3, 4, 5, 6]  # Input list
        number = int(input('Enter the number to be checked: '))  # Number that is to be found
        check_num_belongs(input_list, number)
        i = 0
        input_list_sorted = sorted(input_list)
        check_recursive(input_list_sorted, input_list, i, number)


if __name__ == "__main__":
    main()
