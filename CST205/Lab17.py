import operator

def number_of_unique_words(word_array):
    unique_word_array = []
    for word in word_array:
        if word.lower() not in unique_word_array:
            unique_word_array.append(word.lower())
    # print(unique_word_array)
    print('The total number of UNIQUE WORDS, not including case sensitivity: ' + str(len(unique_word_array)))


def word_count(word_array):
    file = open("C:\\Developing\\School\\CST205\\greeneggs.html", "wt")
    words_dict = {}
    words_dict_string = ''
    for word in word_array:
        word = word.lower()
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    for k,v in words_dict.items():
        if v in range(10):        
          words_dict_string += '<p style="font-size:10px; color:#2c3e50">' + k + ':' + str(v) + '</p>'
        elif v in range(10,20):
            words_dict_string += '<p style="font-size:12px; color:#5DADE2">' + k + ':' + str(v) + '</p>'
        elif v in range(20,30):
            words_dict_string += '<p style="font-size:14px; color:#5499C7">' + k + ':' + str(v) + '</p>'
        elif v in range(30,40):
            words_dict_string +='<p style="font-size:16px; color:#48C9B0">' + k + ':' + str(v) + '</p>'
        elif v in range(40,50):
            words_dict_string += '<p style="font-size:18px; color:#45B39D">' + k + ':' + str(v) + '</p>'
        elif v in range(50,60):
            words_dict_string +='<p style="font-size:20px; color:#BB8FCE">' + k + ':' + str(v) + '</p>'
        elif v in range(60,70):
            words_dict_string +='<p style="font-size:22px; color:#F1948A">' + k + ':' + str(v) + '</p>'
        elif v in range(70,80):
            words_dict_string +='<p style="font-size:24px; color:#E59866">' + k + ':' + str(v) + '</p>'
        else:
            words_dict_string +='<p style="font-size:26px; color:#E74C3C; font-weight:bold">' + k + ':' + str(v) + '</p>'
    file.write(words_dict_string)
    file.close()
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
