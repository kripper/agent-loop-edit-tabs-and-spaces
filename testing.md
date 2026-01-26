- Run: python /workspace/tabs-editor-test/generate.py --num_lines 10 --num_chars 10
- Apply /workspace/instructions.md to file /workspace/test.txt
- IMPORTANT RULES: Check rules contained in /workspace/tabs-editor-test/rules-2.md
- Run /workspace/tabs-editor-test/evaluate.py
- Print this info:
tool_failures: <total number of file editor tool call failures>
tool_calls: <total number of editor tool calls>
- Only run the test once
