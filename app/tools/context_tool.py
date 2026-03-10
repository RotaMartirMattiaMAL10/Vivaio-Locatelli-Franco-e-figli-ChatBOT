# Context Tool

This module contains the context update tool for the ChatBOT.

## Overview
The context tool is responsible for managing the conversational context of the chatbot, ensuring that it can maintain a coherent dialogue with users.

## Features
- Update context based on user inputs
- Maintain state across multiple interactions

## Usage
```python
from context_tool import ContextTool

context_tool = ContextTool()

# Example of updating context
context_tool.update_context(user_input)
```
