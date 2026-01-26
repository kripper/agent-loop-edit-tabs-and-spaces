- Only read files using this code:

import sys

data = sys.stdin.read()

out = []
i = 0

while i < len(data):
    c = data[i]

    # count spaces
    if c == " ":
        j = i
        while j < len(data) and data[j] == " ":
            j += 1
        out.append(f"[SP×{j-i}]")
        i = j

    # tabs
    elif c == "\t":
        out.append("[TAB]")
        i += 1

    # newlines
    elif c == "\n":
        out.append("[NL]\n")
        i += 1

    else:
        out.append(c)
        i += 1

print("".join(out), end="")

- This will output files like:

[SP×3]foo[TAB][SP×1]bar[SP×2][NL]

- Please note that this are only visible representations of the chars, but not literal content.

- Don't use your internal file reader tool

- Only edit files using "sed". Make sure to use the real characters (not visible representations) and to escape them correctly to use with sed.
