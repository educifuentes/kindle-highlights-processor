from bs4 import BeautifulSoup
import sys
from pathlib import Path

def main():
    filename = sys.argv[1]
    title_stem = Path(filename).stem
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{title_stem}_notes.md"

    print(":::kindle-to-markdown:::")
    print(f"Processing highlights for {title_stem}")

    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    notes = []
    add_title_and_author(soup, notes)
    notes.append("")  # Add empty line before highlights
    process_notes(soup, notes)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(notes))

    print(f"📖 Successfully exported notebook '{output_file}' ...")
    print(". . . . .")

def add_title_and_author(soup, notes):
    title_tag = soup.find(class_='bookTitle')
    author_tag = soup.find(class_='authors')

    title = title_tag.get_text(strip=True) if title_tag else 'Untitled'
    author = author_tag.get_text(strip=True) if author_tag else 'Unknown Author'

    notes.append(f"Notes from {title} – {author}")

def process_notes(soup, notes):
    items = soup.select('.noteText, .sectionHeading')
    last_note_index = None

    for item in items:
        line = item.get_text(strip=True)

        if is_heading(item):
            notes.append(f"## {line}")
            last_note_index = None  # reset index after heading

        elif is_important(line):
            # Don't include "Wow..." line; instead highlight the previous note
            if last_note_index is not None and notes[last_note_index].startswith(prefix(2)):
                prefix_len = len(prefix(2)) + 1  # for "  - "
                original_text = notes[last_note_index][prefix_len:]
                notes[last_note_index] = f"{prefix(2)} =={original_text}=="

        else:
            formatted_line = f"{prefix(2)} {line}"
            notes.append(formatted_line)
            last_note_index = len(notes) - 1

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