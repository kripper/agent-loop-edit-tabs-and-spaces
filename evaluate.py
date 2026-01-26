#!/usr/bin/env python3


def main():
    try:
        with open("/tmp/test.txt", "r") as f:
            test_lines = f.readlines()

        with open("/tmp/target.txt", "r") as f:
            target_lines = f.readlines()

        correct = 0
        wrong = 0

        min_len = min(len(test_lines), len(target_lines))

        for i in range(min_len):
            test_line = test_lines[i].rstrip("\n")
            target_line = target_lines[i].rstrip("\n")

            if test_line == target_line:
                correct += 1
            else:
                wrong += 1

        # Handle different file lengths
        if len(test_lines) > min_len:
            wrong += len(test_lines) - min_len
        elif len(target_lines) > min_len:
            wrong += len(target_lines) - min_len

        print(f"correct: {correct}")
        print(f"wrong: {wrong}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("correct: 0")
        print("wrong: 0")


if __name__ == "__main__":
    main()
