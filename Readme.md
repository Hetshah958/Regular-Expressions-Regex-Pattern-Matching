# Regex Email Finder

This is a small Python project for Experiment 7: Regular Expressions (Regex) – Pattern Matching.

The program takes a piece of text and finds email addresses using Python's built-in `re` module. It prints all the matches found in the text.

## Aim

To write a Python program using regular expressions to find email patterns.

## Requirements

- Python 3
- No additional libraries required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python email_finder.py
```

4. Enter some text when prompted.

## Example

**Input:**

```text
Contact me at alex@example.com or team.help@sample.org
```

**Output:**

```text
Email addresses found:
- alex@example.com
- team.help@sample.org
```

## How It Works

- The `re` module handles regular expressions.
- `re.compile()` creates the email-matching pattern.
- `find_emails()` uses `findall()` to collect matching addresses.
- The program prints the results or displays a message if no matches are found.

## Conclusion

This experiment demonstrates how regular expressions can be used to extract email addresses from text. It is a basic example of pattern matching in Python.

**Note:** The program matches common email formats. It does not verify whether an email address actually exists.
