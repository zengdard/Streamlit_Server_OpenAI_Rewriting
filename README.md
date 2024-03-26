# Project Description

This project is a simple Streamlit application that uses the OpenAI API to rewrite user input text in an objective manner.

## Features

- Uses OpenAI's text completion feature to rewrite text.
- Provides a user-friendly interface using Streamlit.

## Requirements

- OpenAI API key
- Streamlit

## Usage

1. Set the `openai.api_key` to your OpenAI API key.
2. Run the application using Streamlit.
3. Enter a text with a maximum of 200 words in the provided text area.
4. Click the "Réécrire" button to see the objectively rewritten text.

## File Structure

- `main.py`: The main file containing the Streamlit application and the `rewrite_text_objectively` function.

## Future Work

- Improve error handling and user input validation.
- Add support for more languages.
- Allow users to specify the desired tone or style of the rewritten text.
