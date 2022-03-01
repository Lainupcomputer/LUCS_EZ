from lucs_ez.utils import send_debug
version = "0.1"


class ez_list:
    def __init__(self, filepath="ez_list.txt", debug=False):
        self.debug = debug  # Global debug enable
        send_debug("Active: ", f"ez_list {version}", self.debug)
        self.file_path = filepath  # Global filepath / name

        check = True
        while check:
            try:  # Check if storage file exists else create
                self.internal_read()
                send_debug("OK", "Data found!", self.debug)
                check = False  # break if found

            except FileNotFoundError:  # create 1 line with text
                lines = [">ez_list_file<\n"]
                self.internal_write(lines)
                send_debug(" !", "creating Data", self.debug)  # after creation redo

    def internal_read(self):  # return file
        with open(self.file_path, "r") as f:
            file_lines = f.readlines()
            return file_lines

    def internal_write(self, lines):  # Save Lines to File
        with open(self.file_path, "w") as f:
            f.writelines(lines)

    def create(self, user, data):
        lines = self.internal_read()
        print(lines)
        c = -1
        for line in lines:
            c += 1
            if user in line:
                user_line = lines[c].split(">")
                print(user_line)
                user_split = user_line[1].split("\n")
                print(user_split)

            else:
                print("not found")
                user_line = f"{user}>{data}\n"
                lines.append(user_line)
                self.internal_write(lines)


        ...
    def delete(self):
        ...
    def get(self):
        ...
