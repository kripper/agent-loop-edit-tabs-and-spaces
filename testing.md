Perform test:
- IMPORTANT RULES:
	- Check rules contained in rules-4.md (they only apply to performing the test)
	- You must perform only one single independent function or tool call for every line
	- When editing files, the old_str and new_str must be provided by you (the LLM), and not by other means like a script.
	- You must always follow these rules. Don't even try to solve the problem in other ways.
- Run: python generate.py 10 10
- Apply /tmp/instructions.md to file /tmp/test.txt

Evalute:
- Run: python evaluate.py
- Print this info:
tool_failures: <total number of file editor tool call failures>
tool_calls: <total number of editor tool calls>

- Srictly follow the instructions (don't cheat). Remember that the goal is to test your ability to read and edit files.
- When finished, analyze again if you cheated or not. If you cheated, your results are invalid and you will have to continue iterating.

