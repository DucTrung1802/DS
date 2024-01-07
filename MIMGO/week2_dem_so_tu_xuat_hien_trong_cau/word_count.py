def get_word_count(s):
    """
    Hàm này nhận đầu vào là một chuỗi s, chỉ chứa các từ và chữ cái trong bảng chữ cái.
    Học viên cần thực hiện yêu cầu đề bài và in ra theo đúng định dạng được yêu cầu.
    """

    word_dictionary = dict()
    for word in s.split(" "):
        if word not in word_dictionary:
            word_dictionary[word.lower()] = 1
        else:
            word_dictionary[word.lower()] += 1
    word_dictionary = dict(sorted(word_dictionary.items(), key=lambda item: item[0]))
    word_dictionary = dict(sorted(word_dictionary.items(), key=lambda item: item[1], reverse=True))
    print(len(word_dictionary))
    for key, value in word_dictionary.items():
        print(str(key) + " " + str(value))

    # Học viên viết chương trình ở giữa dòng này và dòng mô tả trên.

# get_word_count("Lua nep la lua nep lang lua len lop lop long nang lang lang")