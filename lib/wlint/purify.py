#!/usr/bin/python3

import re


def text(s):
    return s


def tex(s):
    def strip_comment(text):
        index = text.find("%")
        return text[:index]

    pattern = re.compile(r"(\\\w+)")

    def strip_commands(text):
        def replace_fn(m):
            return " " * len(m.group(0))

        return re.sub(pattern, replace_fn, text)

    return strip_commands(strip_comment(s))