def number_of_unique_words(word_array):
    unique_word_array = []
    for word in word_array:
        if word.lower() not in unique_word_array:
            unique_word_array.append(word.lower())
    # print(unique_word_array)
    print('The total number of UNIQUE WORDS, not including case sensitivity: ' + str(len(unique_word_array)))


def word_count(word_array):
    words_dict = {}
    for word in word_array:
        word = word.lower()
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    print(words_dict)
    return words_dict


def most_common_word(words_dict):
    values = []
    for k in words_dict:
        values.append(words_dict[k])
    max_value = max(values)
    for k in words_dict:
        if words_dict[k] == max_value:
            print('The most commonly occuring word: "' + k + '"')


def main(file):
    f = open(file,'r')
    read_data = f.read()
    text_array = read_data.split()
    number_of_unique_words(text_array)
    word_count_dict = word_count(text_array)
    most_common_word(word_count_dict)
    f.close()
