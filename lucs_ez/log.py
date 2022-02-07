import datetime


class log:

    def __init__(self, destination="log.txt"):
        self.filepath = destination
        with open(self.filepath, "w") as f:
            f.write("> lucs_ez logfile <\n")

    def log(self, msg="blanc"):
        logstr = f"{datetime.datetime.now()} : {msg}\n"
        with open(self.filepath, "r") as f:
            lines = f.readlines()
            lines.append(logstr)
        with open(self.filepath, "w") as wf:
            wf.writelines(lines)

