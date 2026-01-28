# Intro
LLMs struggle to reliably distinguish between tabs and spaces.
How are we supposed to reach AGI if an LLM can’t safely edit a file with tab-based indentation?

# About this repo
This repository contains agent instructions to:
- Generate agent tools capable of reading and editing files that contain both tabs and spaces
- Test and validate those tools

# How it works
- `generate.py` generates:
  - `test.txt`: a text file with random tabs and spaces
  - `instructions.md`: instructions for the agent to edit this file
  - `target.txt`: a text file with the expected resulting file (used to evaluate).
- The agent is instructed to apply `instructions.md`
- `evaluate.py` evaluates the edits performaed by the agent.

# Run
opencode --prompt "Process run.md"

# Motivation

* It is a very simple yet still unsolved problem.
* Reliable file editing by agents is critically important.
* Test results can be evaluated objectively using `evaluate.py`.
* It is a good example for testing agent loops.
* The agent creates and tests its own tools.

# Documentation

* **run.md**: Contains instructions for running the test within an agent loop.
* **testing.md**: Describes how to perform the test. It references **rules-4.md**, which defines the rules for generating file-editing functions.
* **coder.md**: Contains the instructions used to generate `generate.py` and `evaluate.py`. This file can be ignored, as the scripts have already been generated and tested.
