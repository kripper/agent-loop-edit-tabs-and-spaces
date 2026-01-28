#!/usr/bin/env python3
import sys
import random
import os


def get_random_chars(n):
    chars = []
    for _ in range(n):
        chars.append("\t" if random.choice([True, False]) else " ")
    return "".join(chars)


def get_random_line(i, num_chars):
    s = get_random_chars(num_chars)
    pos = random.randint(0, len(s))
    return s[:pos] + str(i) + s[pos:]


def escape(s):
    return s.replace("\t", "<TAB>").replace(" ", "<SPACE>")


def write_lines(n, num_chars):
    lines = []
    for i in range(1, n + 1):
        lines.append(get_random_line(i, num_chars))
    return lines


def main():
    num_lines = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    num_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    # Write test.txt
    test_lines = write_lines(num_lines, num_chars)
    with open("/tmp/test.txt", "w") as f:
        for line in test_lines:
            f.write(line + "\n")

    # Create target.txt only
    target_lines = []
    for i, old_str in enumerate(test_lines, 1):
        new_str = get_random_line(i, num_chars)
        target_lines.append(new_str)

    # Create target.txt
    with open("/tmp/target.txt", "w") as f:
        for line in target_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
