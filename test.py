# from lucs_ez.config import *  # Import Config Module
#
# cfg = config(file_path="test.json", debug=True)  # Setup instance
#
#from lucs_ez.user import *  # Import User Module

#user = ez_user(debug=True)
#print(user.create_user("lain3", "cool"))
#print(user.get("lain3", "cat"))
#user.remove_field("lain", "cool", "cat")
#user.add_field("lain3", "cat", "data")
# print(user.get_all_user_names())



# from lucs_ez.log import *
# l = log(new=T)
# l.log("1")
# l.log("12")
# l.log("113")

# def test_log():
#
#     l.log()
#     l.log()
#     l.log()
#
#
# def müll():
#     if field in user_data:  # check if field is there
#         send_debug(" !", "Already exits", self.debug)
#         return False
#
#     else:  # append filed
#         user_line = user_data[0].split(";")  # split values
#         if single:  # spilt entity - value
#             user_line.append(field)
#             la = file_lines[check]
#             new = la + f";{field}\n"
#             file_lines[check] = new
#             self.internal_write(file_lines)
#
#             Debug.send("OK", f"{user_line}")
#
#     print(file_lines)
#
#     print(user_line)
from lucs_ez.list import *

list = ez_list()
list.create(user="Test", data="testdata")