# Python Gemini Agent CLI

A robust and lightweight AI agent designed for interacting with the Gemini API and performing autonomous tasks within a codebase.

## Description

This agent is a full-featured tool that provides a seamless workflow for developers to interact with the Gemini API. It can explore directory structures, read files, execute Python code, and write new files, allowing it to perform complex multi-step tasks autonomously. It leverages the Gemini 2.0 Flash model and custom function calling to bridge the gap between AI generation and local file system operations.

## Motivation

Interacting with LLMs often requires manual copy-pasting of code and context. This project was developed to provide a minimalist yet powerful alternative by:

*   **Ensuring Simplicity**: Leveraging a minimalist Python structure for maximum portability and zero complex framework overhead.
*   **Streamlining Workflow**: Automating codebase exploration and modification with a single CLI command.
*   **Improving Accuracy**: Implementing a loop-based generation engine that uses real-time tool feedback to refine its plan.
*   **Enhancing Flexibility**: Supporting custom tool definitions and easy configuration via `config.py`.

## Quick Start

### Prerequisites

*   Python 3.10+
*   Gemini API Key (set in a `.env` file)
*   `uv` (optional, for dependency management)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/joseflores1/python_agent
    cd python-agent
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure your environment:
    Create a `.env` file in the root directory and add your API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

4.  Run the agent:
    ```bash
    python main.py "your prompt here"
    ```

## Usage

### Project Structure

*   `functions/`: Contains the implementation of tools the agent can use (read, write, list, run).
*   `main.py`: The entry point for the CLI.
*   `config.py`: Configuration for the model, system prompt, and iteration limits.
*   `generate.py`: The core logic for interacting with the Gemini API and handling tool calls.

### Commands

*   `python main.py "<prompt>"`: Starts the agent with the given prompt.
*   `python main.py "<prompt>" --verbose`: Runs the agent in verbose mode, showing tool outputs.
*   `python tests.py`: Runs a basic suite of integration tests for the `run_python` tool.

## Key Features

*   **Autonomous Exploration**: Automatically scans the working directory to locate relevant files and context.
*   **Recursive Tool Execution**: Handles multi-step plans by executing tools and feeding results back into the model.
*   **Python Execution Engine**: Can run Python scripts within the project and capture their output for further analysis.
*   **File I/O Tools**: Integrated capabilities to read existing code and write/overwrite files to apply fixes or new features.

## Architecture

The agent is organized into modular components:

*   `main.py`: The orchestration layer that handles user input and the main execution loop.
*   `generate.py`: Manages the communication with the Gemini API, including tool configuration and message history.
*   `call_function.py`: A routing layer that maps Gemini function calls to their Python implementations.
*   `functions/`: A directory of modular scripts, each implementing a specific capability (e.g., `write_file`, `get_files_info`).
*   `flags.py`: A simple utility for parsing CLI arguments like `--verbose`.
