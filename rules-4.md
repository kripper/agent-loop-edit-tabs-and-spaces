# Intro

- It's a fact that LLMs like you are not able to reliable distinguish between tabs and space characters.
- To workaround this problem, you must:
	- Implement a function for reading files. Arguments: file
	- Implement a function for editing files. Arguments: file, old_str, new_str

*** IMPORTANT RULES ***

You must follow these rules and not cheat:

- ONLY USE THESE TWO FUNCTIONS instead of your internal tools to read and edit files
- Do not implement other functions to apply the instructions.
- The function for editing files MUST receive old_str and new_str arguments provided by you (the LLM)
- After evaluating the test, analyze the results and issues and improve your functions until getting good results.

