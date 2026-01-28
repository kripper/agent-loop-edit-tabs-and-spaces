def read_file(file_path):
    """Read the contents of a file and return as tokenized string."""
    with open(file_path, "r") as f:
        content = f.read()
    return tokenize_string(content)


def tokenize_string(s):
    """Convert string to unique tokens for spaces and tabs"""
    result = []
    for char in s:
        if char == "\t":
            result.append("↦")  # Tab token - rightwards arrow
        elif char == " ":
            result.append("·")  # Space token - middle dot
        else:
            result.append(char)
    return "".join(result)


def detokenize_string(s):
    """Convert tokens back to actual spaces and tabs"""
    return s.replace("↦", "\t").replace("·", " ")


def edit_file(file_path, old_str, new_str):
    """Edit a file by replacing old_str with new_str using unique tokens."""
    with open(file_path, "r") as f:
        content = f.read()

    # Convert both content and old_str to tokens for precise matching
    tokenized_content = tokenize_string(content)
    tokenized_old_str = tokenize_string(old_str)

    # Tokenize the new_str directly
    tokenized_new_str = tokenize_string(new_str)

    # Check if old_str was found
    found = tokenized_old_str in tokenized_content

    if not found:
        raise ValueError(f"Old string not found: {repr(old_str)}")

    # Replace in tokenized content
    updated_tokenized = tokenized_content.replace(tokenized_old_str, tokenized_new_str)
    # Convert back to actual characters
    updated_content = detokenize_string(updated_tokenized)

    with open(file_path, "w") as f:
        f.write(updated_content)
