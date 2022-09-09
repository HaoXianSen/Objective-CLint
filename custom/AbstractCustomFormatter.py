# AbstractCustomFormatter.py
# Provides common functionality for custom formatters.
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2015 Square, Inc
import sys


class AbstractCustomFormatter(object):

    errorMsg = ""

    def run(self):
        if len(sys.argv) == 3:
            with open(sys.argv[1], "r+b") as f:
                formatted_lines = self.format_lines(f.readlines(), sys.argv[2])

            with open(sys.argv[1], "w+b") as f:
                f.write(formatted_lines)
        elif len(sys.argv) == 2:
            formatted_lines = self.format_lines(sys.stdin.readlines(), sys.argv[1])
            sys.stdout.write(formatted_lines)
        else:
            # formatted_lines = self.format_lines(sys.stdin.readlines(), "test")
            # sys.stdout.write(formatted_lines)
            return "parameters error：please put in file content and file name must"

    def format_lines(self, lines, file):
        return "".join(lines)


if __name__ == "__main__":
    AbstractCustomFormatter().run()
