# 📚 Kindle Highlights to Markdown

Convert your Kindle notebook `.html` exports into clean, readable Markdown notes — perfect for journaling, second-brain workflows, or personal archives.

---

## ✨ Features

- Highlights are exported as bullet points, hierarchically nested by section or chapter
- Important notes (e.g. those starting with "Wow") are automatically highlighted
- Outputs clean `.md` files for use with Obsidian, Logseq, or any Markdown editor

---

## 🚀 Usage

1. Export your notebook from the Kindle mobile app (as `.html`)
2. Place the file in the `notebooks/` folder
3. Run the script:

```bash
python process_kindle.py notebooks/<your_notebook.html>
```

## Example

### Sample Input (html notebook)

```html

<div class="sectionHeading">Foreword</div>
<div class="noteText">When I sat down to write *The Alchemist*, all I knew is that I wanted to write about my soul. I wanted to write about my quest to find my treasure.</div>
<div class="sectionHeading">Prologue</div>
<div class="noteText">He could see, in the depths of his eyes, his own beauty reflected.” “What a lovely story,” the alchemist thought.</div>

```

### Sample output


```md
- Foreword
  - When I sat down to write *The Alchemist*, all I knew is that I wanted to write about my soul. I wanted to write about my quest to find my treasure.
- Prologue
  - He could see, in the depths of his eyes, his own beauty reflected.” “What a lovely story,” the alchemist thought.
- Part One
  - Thinking about that for a moment, he realized that it could be the other way around: that it was he who had become accustomed to their schedule.
```

