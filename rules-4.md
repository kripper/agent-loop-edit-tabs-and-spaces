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
- You must first read the files to identify what needs to be changed
- You must determine the old_str and new_str values yourself by comparing test.txt with target.txt
- The read_file function returns tokenized content using \x1E for tabs and \x1F for spaces
- The edit_file function receives untokenized old_str but uses tokenization internally for reliable matching
- After evaluating the test, analyze the results and issues and improve your functions until getting good results.

