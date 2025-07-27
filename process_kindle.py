from bs4 import BeautifulSoup
import sys
from pathlib import Path

def main():
    filename = sys.argv[1]
    title = Path(filename).stem
    output_file = f"{title}_notes.md"

    print(":::kindle-to-markdown:::")
    print(f"Processing highlights for {title}")

    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    notes = []
    process_notes(soup, notes)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(notes))

    print(f"📖 Succesfully exported notebook '{output_file}' ...")
    print(". . . . .")

def process_notes(soup, notes):
    items = soup.select('.noteText, .sectionHeading')
    for item in items:
        line = item.get_text(strip=True)
        spaces = 0 if is_heading(item) else 2
        if is_important(line):
            line = highlight(line)
        notes.append(f"{prefix(spaces)} {line}")

def is_heading(tag):
    return 'sectionHeading' in tag.get('class', [])

def is_important(line):
    return line.startswith('Wow')

def prefix(spaces):
    return ' ' * spaces + '-'

def highlight(line):
    return f"=={line}=="

if __name__ == "__main__":
    main()