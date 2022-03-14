########################################################################################################################
#                                                   Lainupcomputer                                                     #
#                                                   ez_user v1.0                                                       #
########################################################################################################################

from lucs_ez.utils import *
from lucs_ez.log import *

version = "v1.0"

module_log = log("user_log.log", False)  # Setup logging path/new on start


class ez_user:

    def __init__(self, filepath="ez_user.txt", debug=False, enable_access_time=False, loging=False):
        self.debug = debug                                      # Global debug enable
        self.file_path = filepath                               # Global filepath / name
        self.enable_access_time = enable_access_time            # Global access_time
        self.enable_log = loging                                # Global logging
        send_debug("Active: ", f"ez_user {version}", self.debug)

        check = True                                            # File Setup
        while check:
            try:  # Check if storage file exists else create
                self.internal_read()
                send_debug("OK", "Data found!", self.debug)
                check = False                                   # break if found

            except FileNotFoundError:                           # create 1 line with text
                lines = [">ez_user_file<\n"]
                self.internal_write(lines)
                send_debug(" !", "creating Data", self.debug)  # after creation redo

    def internal_read(self):                                   # return file
        with open(self.file_path, "r") as f:
            file_lines = f.readlines()
            return file_lines

    def internal_write(self, lines):                           # Save Lines to File
        with open(self.file_path, "w") as f:
            f.writelines(lines)

    def get_user_id(self, user_name):                          # return user ID / line id
        file_lines = self.internal_read()
        w = -1
        for line in file_lines:
            w += 1
            if user_name in line:
                return w

    def get_all_user_names(self):
        user_list = []
        lines = self.internal_read()            # read all data
        for user in range(len(lines)):          # loop over lines
            user_data = lines[user].split(";")  # split file to user by id !
            for data in user_data:              # get value stack from user
                val = data.split("=")           # split value stack to identify search
                if val[0] == "username":        # val0 datastack identify !!! val1 datastack value
                    user_list.append(val[1])    # append username to user_list
        send_debug("OK", f"User: {user_list}", self.debug)
        return user_list

    def create_user(self, user_name, user_password):            # Create user if not exits
        user_id = self.get_user_id(user_name)                   # Check for User returns ID // Check if user there
        if user_id is None:                                     # Crate user
            if self.enable_access_time:                         # Create with access time indicator
                user_line = f"""
                username={user_name};         
                password={gen_password_hash(user_password)};
                last_access={timestamp_now()}\n             
                """

            else:                                               # Create without access time indicator
                user_line = f"username={user_name};password={gen_password_hash(user_password)}\n"  # Password Hashing

            file_lines = self.internal_read()                   # Read Data File
            file_lines.append(user_line)
            self.internal_write(file_lines)
            send_debug("OK", f'User "{user_name}" created', self.debug)  # user created
            if self.enable_log:
                module_log.log(f'User "{user_name}" created.')
            return True
        else:                                                   # User is there
            send_debug(" !", f"User exists. ID:{user_id}", self.debug)
            if self.enable_log:
                module_log.log(f'User "{user_name}" already exits.')
            return False

    def delete_user(self, user_name, user_password):
        check = self.get_user_id(user_name)  # Check for User returns ID
        if check:
            if check_password(user_password, self.get(user_name, "password")):
                file_lines = self.internal_read()
                file_lines.pop(check)
                self.internal_write(file_lines)
                send_debug("OK", "User deleted", self.debug)
                if self.enable_log:
                    module_log.log(f'User "{user_name}" Deleted with password.')
                return 200
            else:
                send_debug(" ?", "Password wrong !", self.debug)
                if self.enable_log:
                    module_log.log(f'User "{user_name}" try to delete: password wrong.')
                return 401
        else:
            send_debug(" ?", "User not found", self.debug)
            if self.enable_log:
                module_log.log(f'User "{user_name}" try to delete: User not found.')
            return 404

    def get(self, user_name, obj):
        id = self.get_user_id(user_name)  # Check for User returns ID
        if id:  # if userid != none
            file_lines = self.internal_read()
            user_data = file_lines[id].split(";")  # find user line
            for field in user_data:
                val = field.split("=")
                if obj in val[0]:
                    rm_nl = val[1].split("\n")
                    if self.enable_log:
                        module_log.log(f'User "{user_name}" requested "{obj}. received"')
                    return rm_nl[0]
        else:
            send_debug(" ?", f"Cant get '{obj}' User not found", self.debug)
            if self.enable_log:
                module_log.log(f'User "{user_name}" requested "{obj}. User not found"')
            return False

    def add_field(self, user_name, field, data):
        uid = self.get_user_id(user_name)  # Check for User returns ID
        if uid:
            if not self.get(user_name, field):
                lines = self.internal_read()  # read file lines
                line = lines[uid]
                user_line = line.split("\n")  # remove newline
                user_str = f"{user_line[0]};{field}={data}\n"
                lines[uid] = user_str
                self.internal_write(lines)
                send_debug("OK", f"added {field}={data} to ID:{uid}", self.debug)
            else:
                send_debug(" !", "Data found abort", self.debug)

        else:
            send_debug(" ?", "User not found", self.debug)


    def remove_field(self, user_name, password, field):
        user_id = self.get_user_id(user_name)

        if check_password(password, self.get(user_name, "password")):
            print("pass ok")
        else:
            send_debug(" !", "Password wrong", self.debug)




