
import os

class AsciiArtGenerator:
    def __init__(self):
        self.mappings = {
            'if': '<?>',
            'else': ' : ',
            'elif': ' :?',
            'for': '(O)',
            'while': '(O)',
            'def': '[F]',
            'class': '[C]',
            'return': '<-',
            'print': '>>>',
            'try': '/!\\',
            'except': '!!!',
        }

    def generate(self, tokens):
        """
        Generates ASCII art from a list of tokens.
        """
        ascii_lines = []
        current_indent = 0
        indent_str = " |  "
        
        # Group tokens by line
        lines = {}
        for token in tokens:
            line_num = token['line']
            if line_num not in lines:
                lines[line_num] = []
            lines[line_num].append(token)
            
        sorted_lines = sorted(lines.keys())
        
        for line_num in sorted_lines:
            line_tokens = lines[line_num]
            line_content = ""
            
            # Use the indentation from the first token if possible, but 
            # usually `tokenize` gives indent tokens.
            # Our parser output structure includes 'column'.
            # A simple heuristic: column / 4 = indent level
            if line_tokens:
                first_token = line_tokens[0]
                current_indent = first_token['column'] // 4

            padding = indent_str * current_indent
            
            # Check for keywords to map
            mapped = False
            for token in line_tokens:
                if token['type'] == 'keyword' and token['value'] in self.mappings:
                    line_content += self.mappings[token['value']] + " "
                    mapped = True
                elif token['type'] == 'variable' and token['value'] == 'print': # Special case for print which is a function now
                     line_content += self.mappings.get('print', '>>>') + " "
                     mapped = True

            if not mapped:
                # If no keyword mapping, use a generic shape based on content
                # e.g., assignment `x = 1` -> `[=]`
                # For now, just print a generic block if it's code
                if any(t['type'] in ['variable', 'operator'] for t in line_tokens):
                     line_content += "[=]"
                else:
                    line_content += "..."

            ascii_lines.append(f"{padding}{line_content.strip()}")
            
        return "\n".join(ascii_lines)

    def save_to_file(self, content, filename, output_dir="outputs/ascii"):
        """Saves the ASCII content to a file."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

if __name__ == "__main__":
    # Test stub
    pass
