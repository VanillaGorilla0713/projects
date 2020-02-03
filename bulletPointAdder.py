#! python3
# Adds bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# spearate lines and add star bullets
lines = text.split('\n')
for line in range(len(lines)):
    lines[line] = '* ' + lines[line]
text = '\n'.join(lines)


pyperclip.copy(text)