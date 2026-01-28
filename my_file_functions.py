def read_file(file_path):
    """Read the contents of a file and return as tokenized string."""
    with open(file_path, "r") as f:
        content = f.read()
    return tokenize_string(content)


def tokenize_string(s):
    """Convert string to unique tokens for spaces and tabs with escaping"""
    result = []
    for char in s:
        if char == "\t":
            result.append("↦")  # Tab token
        elif char == " ":
            result.append("·")  # Space token
        elif char == "↦":
            # Escape existing tab token
            result.append("§↦")
        elif char == "·":
            # Escape existing space token
            result.append("§·")
        elif char == "§":
            # Escape existing escape character
            result.append("§§")
        else:
            result.append(char)
    return "".join(result)


def detokenize_string(s):
    """Convert tokens back to actual spaces and tabs with unescaping"""
    result = []
    i = 0
    while i < len(s):
        if s[i] == "§":
            if i + 1 < len(s):
                next_char = s[i + 1]
                if next_char == "↦":
                    # Escaped tab token
                    result.append("↦")
                    i += 2
                elif next_char == "·":
                    # Escaped space token
                    result.append("·")
                    i += 2
                elif next_char == "§":
                    # Escaped escape character
                    result.append("§")
                    i += 2
                else:
                    # Standalone escape character - shouldn't happen
                    result.append("§")
                    i += 1
            else:
                # Last character is escape - shouldn't happen
                result.append("§")
                i += 1
        elif s[i] == "↦":
            # Standalone arrow - treat as tab token
            result.append("\t")
            i += 1
        elif s[i] == "·":
            # Standalone middle dot - treat as space token
            result.append(" ")
            i += 1
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


def edit_file(file_path, old_str, new_str):
    """Edit a file by replacing old_str with new_str using unique tokens."""
    with open(file_path, "r") as f:
        content = f.read()

    # Detokenize the old_str and new_str (they come in tokenized format)
    detokenized_old_str = detokenize_string(old_str)
    detokenized_new_str = detokenize_string(new_str)

    # Check if old_str was found in raw content
    found = detokenized_old_str in content

    if not found:
        raise ValueError(f"Old string not found: {repr(detokenized_old_str)}")

    # Replace in raw content
    updated_content = content.replace(detokenized_old_str, detokenized_new_str)

    with open(file_path, "w") as f:
        f.write(updated_content)
