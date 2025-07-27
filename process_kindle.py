#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: kindle-notes <your_file.html>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    title_stem = input_path.stem
    output_file = Path(f"{title_stem}_notes.md")

    print(":::kindle-to-markdown:::")
    print(f"Processing highlights for {title_stem}")

    with input_path.open('r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    notes = []
    add_title_and_author(soup, notes)
    notes.append("")  # blank line before highlights
    process_notes(soup, notes)

    with output_file.open('w', encoding='utf-8') as f:
        f.write('\n'.join(notes))

    print(f"📖 Successfully exported: {output_file.resolve()}")
    print(". . . . .")

def add_title_and_author(soup, notes):
    title_tag = soup.find(class_='bookTitle')
    author_tag = soup.find(class_='authors')

    title = title_tag.get_text(strip=True) if title_tag else 'Untitled'
    author = author_tag.get_text(strip=True) if author_tag else 'Unknown Author'

    notes.append(f"{title} – {author}")

def process_notes(soup, notes):
    items = soup.select('.noteText, .sectionHeading')
    last_note_index = None

    for item in items:
        line = item.get_text(strip=True)

        if is_heading(item):
            notes.append(f"## {line}")
            last_note_index = None

        elif is_very_important(line):
            # Very important: highlight
            if last_note_index is not None and notes[last_note_index].startswith(prefix(2)):
                prefix_len = len(prefix(2)) + 1
                original_text = notes[last_note_index][prefix_len:]
                notes[last_note_index] = f"{prefix(2)} =={original_text}=="

        elif is_important(line):
            # Important: bold
            if last_note_index is not None and notes[last_note_index].startswith(prefix(2)):
                prefix_len = len(prefix(2)) + 1
                original_text = notes[last_note_index][prefix_len:]
                notes[last_note_index] = f"{prefix(2)} **{original_text}**"

        else:
            formatted_line = f"{prefix(2)} {line}"
            notes.append(formatted_line)
            last_note_index = len(notes) - 1

def is_heading(tag):
    return 'sectionHeading' in tag.get('class', [])

def is_very_important(line):
    return line.startswith("Wow iii")

def is_important(line):
    return line.startswith("Wow") and not is_very_important(line)

def prefix(spaces):
    return ' ' * spaces + '-'

if __name__ == "__main__":
    main()