# Backend Programming with Python
# Homework 1
# Question 1 & 2
def check_password(password):
    if len(password) < 9:
        print('Error: Minimum 8 characters required!')
    if not any(i.isupper() for i in password):
        print('Error: At least one letter should be uppercase!')
    if len([i for i in password if i.isdigit()]) < 2:
        print('Error: At least 2 digits required!')
    i = 0
    while i < len(password)-1:
        if password[i].isdigit() & password[i+1].isdigit():
            print('Error: Two consecutive digits not allowed!')
            break
        i += 1


def split_sent(sent):
    result = sent.split(' ')
    return result


def check_freq(sep_words):
    i = 0
    c = tuple()
    c_final = list()
    while i <= len(sep_words)-1:
        if (sep_words[i], sep_words.count(sep_words[i])) not in c_final:
            c = (sep_words[i], sep_words.count(sep_words[i]))
            c_final.append(c)
        i += 1
    return c_final


def sort_words(freq_word):
    sorted_words = freq_word
    sorted_words.sort(key=lambda x: x[1], reverse=True)
    return sorted_words


def most_freq_words(sorted_words):
    result = [sorted_words[0], sorted_words[1]]
    result.sort()
    return result


def str_most_freq_words(most_freq_word):
    result = f"{most_freq_word[0][0]} {most_freq_word[1][0]}"
    return result


def main():
    password = str(input("Enter password: "))
    check_password(password)
    sent = str(input('Enter sentence: '))
    split_sent(sent)
    sep_words = split_sent(sent)
    print(sep_words)
    freq_word = check_freq(sep_words)
    print(freq_word)
    sorted_words = sort_words(freq_word)
    print(sorted_words)
    most_freq_word = most_freq_words(sorted_words)
    print(most_freq_word)
    str_most_freq_word = str_most_freq_words(most_freq_word)
    print(str_most_freq_word)


if __name__ == "__main__":
    main()
