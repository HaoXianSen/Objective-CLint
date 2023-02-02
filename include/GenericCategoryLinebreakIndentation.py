# GenericCategoryLinebreakIndentation.py
# Undoes extraneous linebreak and indentation when a category has a generic expression.
# 当类别具有泛型表达式时，取消多余的换行和缩进。 如：SomeClass <T> (SomeCategory)
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc

from AbstractCustomFormatter import AbstractCustomFormatter


class GenericCategoryLinebreakIndentation(AbstractCustomFormatter):
    def format_lines(self, lines, file):
        lines_to_write = []
        entered_generic_interface = False
        entered_generic_category = False

        for line_index, line in enumerate(lines):
            stripped_line = line.strip()
            # We are on the next line with the category description because of an extraneous linebreak
            if entered_generic_interface and stripped_line.startswith("("):
                entered_generic_category = True
                # Remove the extra line break
                interface_line_index = -1
                interface_line_temp = lines_to_write[interface_line_index].strip()
                while len(interface_line_temp) == 0:
                    interface_line_index -= 1
                    interface_line_temp = lines_to_write[interface_line_index].strip()

                suffix = " " + line.lstrip()
                interface_line = lines_to_write[interface_line_index].rstrip()
                lines_to_write[interface_line_index] = interface_line + suffix
                # line_index = "第{0}行\n".format(line_index + 1)
                # self.errorMsg += ("\033[31m自定义规则format错误：当类别具有泛型表达式时，取消多余的换行和缩进\n" + "line: " + line_index + line + '\n' + 'at: ' + file + "\033[0m\n")
                continue
            else:
                # reset if we don't find a category after the first line
                if len(line.strip()) != 0 and entered_generic_interface:
                    entered_generic_interface = False

            if entered_generic_category and len(line.lstrip()) > 0:
                # Removes unwanted indentation
                lines_to_write.append(line.lstrip())
            else:
                lines_to_write.append(line)

            if stripped_line.startswith("@interface") and "<" in stripped_line and ">" in stripped_line:
                entered_generic_interface = True
            elif stripped_line.startswith("@end"):
                entered_generic_interface = False
                entered_generic_category = False

        # print(self.errorMsg)
        return "".join(lines_to_write)

    
if __name__ == "__main__":
    GenericCategoryLinebreakIndentation().run()
