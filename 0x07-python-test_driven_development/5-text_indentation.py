#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n\n", end="")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1


if __name__ == "__main__":
    example_text = "This is a sample text. It contains multiple sentences?
    And some colons: like this one."
    text_indentation(example_text)
