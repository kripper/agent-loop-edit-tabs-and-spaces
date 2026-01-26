Perform test:
- IMPORTANT RULES: Check rules contained in rules-4.md
- Run: python generate.py 10 10
- Apply /tmp/instructions.md to file /tmp/test.txt
- Make sure to make a single independent tool call for every line

Evalute:
- Run: python evaluate.py
- Print this info:
tool_failures: <total number of file editor tool call failures>
tool_calls: <total number of editor tool calls>

- Srictly follow the instructions (don't cheat). Remember that the goal is to test your ability to read and edit files.

