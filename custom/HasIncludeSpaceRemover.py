# HasIncludeSpaceRemover.py
# clang-format gets confused by __has_include() macro when there is a file path present.
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

from AbstractCustomFormatter import AbstractCustomFormatter

class HasIncludeSpaceRemover(AbstractCustomFormatter):
    def format_lines(self, lines, file):

        lines_to_write = []
        for line_index, line in enumerate(lines):
            to_append = line
            if "__has_include(" in line: 
                has_include_prefix = line.split("__has_include(")[0]
                has_include_suffix = line.split("__has_include(")[1]
                if ")" in has_include_suffix:
                    has_include_interior = has_include_suffix.split(")")[0]
                    # Remove the extra space that clang-format erroneously added.
                    new_interior = has_include_interior.replace(" / ", "/")
                    to_append = line.replace(has_include_interior, new_interior)
                    # line_index = "第{0}行\n".format(line_index + 1)
                    # self.errorMsg += (
                    #             "\033[31m自定义规则format错误：__has_include去除空格\n" + "line: " + line_index + line + '\n' + 'at: ' + file + "\033[0m\n")

            lines_to_write.append(to_append)
        # print(self.errorMsg)
        return "".join(lines_to_write)

if __name__ == "__main__":
    HasIncludeSpaceRemover().run()
