# 📚 Kindle Highlights to Markdown

Convert your Kindle notebook `.html` exports into clean, readable Markdown notes — perfect for journaling, second-brain workflows, or personal archives.

---

## ✨ Features

- Highlights are exported as bullet points, hierarchically organized by section or chapter
- Important notes (e.g., those starting with "Wow") are formatted as `**bold**`, while very important notes (e.g., "Wow iii") are also `==highlighted==`
- Outputs clean `.md` files compatible with Obsidian, Logseq, and any Markdown editor

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

### 🔧 Install as a Global Command (macOS/Linux)

You can make this script globally accessible from the terminal by installing it as a command-line tool:

1. **Ensure the script starts with a shebang line** at the top of `process_kindle.py`:

    ```python
    #!/usr/bin/env python3
    ```

2. **Make the script executable:**

    ```bash
    chmod +x process_kindle.py
    ```

3. **Move it to a directory in your system PATH** (you’ll need admin permissions):

    ```bash
    sudo mv process_kindle.py /usr/local/bin/kindle-notes
    ```

4. **Run it from anywhere:**

    ```bash
    kindle-notes path/to/your_notebook.html
    ```

    The Markdown file will be saved in your current working directory as `<notebook>_notes.md`.

5. **To uninstall later:**

    ```bash
    sudo rm /usr/local/bin/kindle-notes
    ```
