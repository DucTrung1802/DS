# Hàm này có nhiệm vụ đọc số N từ bàn phím
# và trả về mảng chứa N câu lệnh tương ứng


def read_data():
    # Hoc viên điền các câu lệnh vào giữa 2 dòng comment này
    nunber_of_commands = int(input())
    raw_string_list_command = []
    for i in range(nunber_of_commands):
        raw_string_list_command.append(input())
    return raw_string_list_command
    # Hoc viên điền các câu lệnh vào giữa 2 dòng comment này
    pass


# Hàm này nhận đầu vào là mảng old_bookshelf ứng với kệ sách
# và mảng commands gồm các câu lệnh thực hiện
# kết quả trả về là một mảng ứng với kệ sách sau khi thực hiện các câu lệnh
def get_new_bookshelf(old_bookshelf: list, commands: str):
    # Hoc viên điền các câu lệnh vào giữa 2 dòng comment này
    if not old_bookshelf:
        old_bookshelf = []
    for command in commands:
        command = command.split()
        if command[0] == "insert":
            old_bookshelf.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            old_bookshelf.remove(int(command[1]))
        elif command[0] == "append":
            old_bookshelf.append(int(command[1]))
        elif command[0] == "sort":
            old_bookshelf.sort()
        elif command[0] == "pop":
            old_bookshelf.pop()
        elif command[0] == "reverse":
            old_bookshelf.reverse()
    return old_bookshelf
    # Hoc viên điền các câu lệnh vào giữa 2 dòng comment này


# test = read_data()

# print(get_new_bookshelf([], test))
