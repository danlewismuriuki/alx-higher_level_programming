#!/usr/bin/python3
"""
This method prints text characters adding new lines when they get
to the char symbols
"""


def text_indentation(text):
    """
    prints text with new lines added after certain chars

    args:
        text (str): Text input to be processed

    Raises:
        TypeError: If text is not string

    Returns: None
    """
    # Check if input text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    # Iterate through each character in the input text
    for char in text:
        # Add the current character to the new text
        new_text += char
        # check if the current character is one of the specified symbols
        if char in ["." or "?" or ":"]:
            # If so, add two new lines after the character
            new_text += "\n\n"
    # split the new text into lines
    lines = new_text.split("\n")
    # print each line with leading leading and trailing whitespaces removed
    for line in lines:
        print(line.strip())
