# Backend Programming with Python
# Homework 1
# Question 1 & 2
def check_password(prompt):
    while True:
        password = str(input(prompt))  # Ask user to enter a password
        a = bool()
        for i in range(len(password) - 1):
            if password[i].isdigit() & password[i + 1].isdigit():
                a = True
            else:
                a = False
        if len(password) < 8:
            print('First criteria failed: Minimum 8 characters required!')
            continue
        elif not any(i.isupper() for i in password):
            print('Second criteria failed: At least one letter should be uppercase!')
            continue
        elif len([i for i in password if i.isdigit()]) < 2:
            print('Third criteria failed: At least 2 digits required!')
            continue
        elif a:
            print('Fourth criteria failed: Two consecutive digits not allowed!')
            continue
        else:
            print('Congratulations, password is valid!')
        break


def split_sent(sent):
    result = sent.split(' ')
    return result


def check_freq(sep_words):
    i = 0
    c_final = list()
    while i <= len(sep_words)-1:
        if (sep_words[i], sep_words.count(sep_words[i])) not in c_final:
            c = (sep_words[i], sep_words.count(sep_words[i]))
            c_final.append(c)
        i += 1
    return c_final


def arrange_alphabetically(sep_words):  # arranging words with frequency but alphabetically when frequency is same
    sorted_alpha = sorted(sep_words)
    sorted_list = sorted(sorted_alpha, key=lambda c: sep_words.count(c), reverse=True)
    return sorted_list


def find_most_freq_words(sorted_alpha):  # finding the most frequent word(s)
    a = [sorted_alpha.count(x) for x in sorted_alpha]  # set of counts of the elements
    set_most_freq_words = set([sorted_alpha[i] for i in range(len(a)) if a[i] == max(a)])  # using max counts as index
    result = sorted(set_most_freq_words)  # arranging the set alphabetically
    return result


def make_str_form(most_freq_words):
    s = str()
    for i in range(len(most_freq_words)):
        a = most_freq_words[i]
        s = s + a + ' '
    return s


def main():
    check_password("Ques 1. Enter password: ")
    sent = str(input('Ques 2. Enter sentence: '))       # Ask use to enter a sentence
    sep_words = split_sent(sent)                # Call to the function which splits the sentence into list of words
    print(f'2)a) List of separated words from the sentence: {sep_words}')
    freq_word = check_freq(sep_words)
    print(f'2)b) Words with their frequency: {freq_word}')
    sorted_alpha = arrange_alphabetically(sep_words)
    most_freq_words = find_most_freq_words(sorted_alpha)
    print(f'2)c) Most frequent word(s) in alphabetical order: {most_freq_words}')
    final_str_form = make_str_form(most_freq_words)
    print(f'Final string form: {final_str_form}')


if __name__ == "__main__":
    main()
