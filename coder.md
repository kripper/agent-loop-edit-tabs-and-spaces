Create a python program 'generate.py':
- receive two positional command line arguments: num_lines (default 30), num_chars (default 10)
- function get_random_chars(n): returns a string of length n composed of random characters that can be: tab character or space character
- function get_random_line(i): returns get_random_chars(num_chars), but inserts in a random position the str(i)
- function write_lines(n): write n lines containing get_random_line(i) where i is the line number from 1 to n
- function escape(s): returns s, but replacing tab chars with '<TAB>' and space chars with '<SPACE>'
- write the file /tmp/test.txt using write_lines(num_lines)
- create the file /tmp/instructions.md with replacement instructions
- create the file /tmp/target.txt with target content
- For each line you generated in /tmp/test.txt:
	- you must also generate a line in /tmp/instructions.md with this format: Replace string "$old_str_escaped" with "$new_str_escaped"
	- and you must also generate a line in /tmp/target.txt with $new_str
	- where:
		- $old_str is the line added to test.txt
		- $new_str is generated with get_random_line(i)
		- $old_str_escaped = escaped($old_str)
		- $new_str_escaped = escaped($new_str)

Create another program 'evaluate.py':
- For every line in /tmp/test.txt, check if the line in the same line number in /tmp/target.txt has exactly the same content
- At the end, print this info:
correct: <number of lines that match exactly>
wrong: <number of lines that didn't match>

Run: generate.py 30 20
Run: evalute.py

Validation:
If evaluate.py returns "wrong: 0", then it means it is not working, because both files should have different random content. In this case, fix it.
