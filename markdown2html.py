#!/usr/bin/env python3
import sys
import os
import markdown

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get input and output file names
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML and write to the output file
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)

    with open(html_file, 'w') as output_file:
        output_file.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    main()
