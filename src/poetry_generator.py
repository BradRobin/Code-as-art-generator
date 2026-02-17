
import keyword

class PoetryGenerator:
    def __init__(self):
        pass

    def generate(self, tokens):
        """
        Generates a 'poem' from the code tokens.
        Extracts:
        - Function definitions (titles/stanzas)
        - Strings (content)
        - Comments (content)
        - Keywords (structure/rhythm)
        """
        poem_lines = []
        current_stanza = []
        
        for token in tokens:
            token_type = token.get('type')
            value = token.get('value', '').strip()
            
            if not value:
                continue

            if token_type == 'keyword' and value == 'def':
                # Start new stanza on function definition
                if current_stanza:
                    poem_lines.extend(current_stanza)
                    poem_lines.append("") # Empty line between stanzas
                    current_stanza = []
            
            if token_type == 'variable' and token.get('column', 0) == 4: # Heuristic for function name if following def
                 # Trying to capture function name... 
                 # But parsing state is hard with just a flat list.
                 # Let's just use strings and comments mainly.
                 pass

            if token_type == 'string':
                # Clean up quotes
                clean_val = value.strip('"\'')
                if clean_val:
                    current_stanza.append(f"  {clean_val}")
            
            elif token_type == 'comment':
                clean_val = value.lstrip('#').strip()
                if clean_val:
                    current_stanza.append(f"    ( {clean_val} )")
            
            elif token_type == 'keyword' and value in ['return', 'yield', 'break']:
                current_stanza.append(f"{value}.")

        if current_stanza:
            poem_lines.extend(current_stanza)

        if not poem_lines:
            return "The code is silent.\nNo strings, no comments,\nVoid."

        return "\n".join(poem_lines)
