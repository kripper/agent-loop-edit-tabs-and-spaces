Create a python program 'generate.py':
- receive two arguments: num_lines (default 30), num_chars (default 10)
- function get_random_chars(n): returns a string of length n composed of random characters than can be: tab character or space character
- function get_random_line(i): returns get_random_chars(num_chars), but inserts in a random position the str(i)
- function write_lines(n): write n lines containing get_rando_line(i) where i is the line number from 1 to n
- function escape(str): returns str, but replacing tab chars with '<TAB>' and ' ' with '<SPACE>'
- write the file /workspace/test.txt using write_lines(num_lines)
- write another new file in /workspace/instructions.md
- For each line you generated in /workspace/test.txt:
	- you must also generate a line in /workspace/instructions.md with this format: Replace string "$old_str_escaped" with "$new_str_escaped"
	- and you must also generate a line in /workspace/target.txt with $new_str
	- where:
		- $old_str is the line added to test.txt
		- $new_str is generated with get_random_line(i)
		- $old_str_escaped = escaped($old_str)
		- $new_str_escaped = escaped($new_str)

Create another program 'evaluate.py':
- For every line in /workspace/test.txt, check if the line in the same linenumber in /workspace/target.txt has exactly the same content
- At the end, print this info:
correct: <number of lines that match exactly>
wrong: <number of lines that didn't match>

Run both programs.

Validation:
If evaluate.py returns "wrong: 0", then it means it is not working, because both files should have different random content. In this case, fix it.
