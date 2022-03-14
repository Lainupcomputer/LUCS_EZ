########################################################################################################################
#                                                   Lainupcomputer                                                     #
#                                                   ez_log v1.0.2                                                      #
########################################################################################################################
from lucs_ez import utils


class log:

    def write_init(self, opt):
        with open(self.filepath, "w") as f:
            f.write(f">{utils.timestamp_now()} : logfile ({opt}) <\n")

    def __init__(self, destination="log.txt", new=True):
        self.filepath = destination
        if new:
            self.write_init("temporary")
        else:
            try:
                self.internal_read()

            except FileNotFoundError:
                self.write_init("static")

    def internal_read(self):
        with open(self.filepath, "r")as f:
            return f.readlines()

    def internal_write(self, lines):
        with open(self.filepath, "w") as wf:
            wf.writelines(lines)

    def log(self, msg="no message provided"):
        logstr = f"{datetime.datetime.now()} : {msg}\n"
        lines = self.internal_read()
        lines.append(logstr)
        self.internal_write(lines)
