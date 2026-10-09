
import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def find_emails(text):
    """Find email addresses in the given text."""
    return EMAIL_PATTERN.findall(text)


def main():
    text = input("Enter some text: ")
    emails = find_emails(text)

    if emails:
        print("\nEmail addresses found:")
        for email in emails:
            print(f"- {email}")
    else:
        print("\nNo email addresses found.")


if __name__ == "__main__":
    main()
