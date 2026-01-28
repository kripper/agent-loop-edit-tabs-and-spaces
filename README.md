# Intro
LLMs struggle to reliably distinguish between tabs and spaces.
How are we supposed to reach AGI if an LLM can’t safely edit a file with tab-based indentation?

# About This Repo
This repository contains agent instructions to:
- Generate agent tools capable of reading and editing files that contain both tabs and spaces
- Test and validate those tools

# Run
opencode --prompt "Process run.md"
