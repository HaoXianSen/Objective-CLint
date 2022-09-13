# NewLineAtEndOfFileInserter.py
# Ensures there's a newline at the end of each file.
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

from AbstractCustomFormatter import AbstractCustomFormatter

class NewLineAtEndOfFileInserter(AbstractCustomFormatter):
    def format_lines(self, lines, file):
        if len(lines) > 0 and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
            line_index = "第{0}行\n".format(lines.count)
            # self.errorMsg += (
                    # "\033[31m自定义规则format错误：文件最后需要换行\n" + "line: " + line_index + lines[-1] + '\n' + 'at: ' + file + "\033[0m\n")
        return "".join(lines)


if __name__ == "__main__":
    NewLineAtEndOfFileInserter().run()
