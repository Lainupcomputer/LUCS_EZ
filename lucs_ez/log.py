########################################################################################################################
#                                                   Lainupcomputer                                                     #
#                                                   ez_log v1.0                                                        #
########################################################################################################################
import datetime


class log:

    def write_init(self, opt):
        with open(self.filepath, "w") as f:
            f.write(f"> lucs_ez logfile ({opt}) <\n")

    def __init__(self, destination="log.txt", new=True):
        self.filepath = destination
        if new:
            self.write_init("temporary")
        else:
            try:
                self.internal_read()

            except FileNotFoundError:
                self.write_init("static")

    def log(self, msg="blanc"):
        logstr = f"{datetime.datetime.now()} : {msg}\n"
        with open(self.filepath, "r") as f:
            lines = f.readlines()
            lines.append(logstr)
        with open(self.filepath, "w") as wf:
            wf.writelines(lines)

