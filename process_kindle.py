from lxml import html
import sys
from pathlib import Path

def main():
    filename = sys.argv[1]
    title = Path(filename).stem
    output_file = f"{title}_notes.md"

    print(":::kindle-to-markdown:::")
    print(f"Processing highlights for {title}")

    with open(filename, 'rb') as f:
        doc = html.parse(f)

    notes = []
    process_notes(doc, notes)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(notes))

    print(f"📖 Succesfully exported notebook '{output_file}' ...")
    print(". . . . .")

def process_notes(doc, notes):
    items = doc.xpath("//*[contains(@class, 'noteText') or contains(@class, 'sectionHeading')]")
    for item in sorted(items, key=lambda x: etree.tostring(x)):
        line = item.text or ''
        spaces = 0 if is_heading(item) else 2
        if is_important(line):
            line = highlight(line)
        notes.append(f"{prefix(spaces)} {line}")

def is_heading(elem):
    return elem.attrib.get('class') == 'sectionHeading'

def is_important(line):
    return line.startswith('Wow')

def prefix(spaces):
    return ' ' * spaces + '-'

def highlight(line):
    return f"=={line}=="

if __name__ == "__main__":
    main()