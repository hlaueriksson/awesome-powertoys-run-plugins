import re

README_FILE = "readme.md"

# Read the entire README file
with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Define the boundaries of the Plugins section
start_header = "## Plugins"
end_header = "## Resources"

start_index = content.find(start_header)
end_index = content.find(end_header)

# Split the file into 3 parts
before = content[:start_index + len(start_header)]
plugin_block = content[start_index + len(start_header):end_index]
after = content[end_index:]

# Extract all plugin lines (they start with "- [")
plugin_lines = re.findall(r"^\- \[.*", plugin_block, re.MULTILINE)

# Sort plugins alphabetically (case-insensitive)
sorted_plugins = sorted(plugin_lines, key=lambda x: x.lower())

# Reassemble the new content
sorted_plugin_block = "\n\n" + "\n".join(sorted_plugins) + "\n"
new_content = before + sorted_plugin_block + after

# Overwrite the README with the sorted content
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)
