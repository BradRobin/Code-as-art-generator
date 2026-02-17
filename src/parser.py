
import tokenize
import token
import keyword
import json
from io import BytesIO

class PythonCodeParser:
    def __init__(self):
        self.keywords = set(keyword.kwlist)

    def parse(self, code_str):
        """
        Parses a python code string and returns a JSON-serializable structure
        containing syntax elements.
        """
        tokens = []
        try:
            # tokenize.tokenize requires bytes
            code_bytes = code_str.encode('utf-8')
            token_gen = tokenize.tokenize(BytesIO(code_bytes).readline)
            
            for tok in token_gen:
                token_type = tok.type
                token_string = tok.string
                start_line, start_col = tok.start
                end_line, end_col = tok.end
                
                # Determine element type
                element_type = 'other'
                
                if token_type == token.NAME:
                    if keyword.iskeyword(token_string):
                        element_type = 'keyword'
                    else:
                        element_type = 'variable' # Identifying all non-keyword names as variables for simplicity
                elif token_type == token.STRING:
                    element_type = 'string'
                elif token_type == token.NUMBER:
                    element_type = 'number'
                elif token_type == token.OP:
                    element_type = 'operator'
                elif token_type == token.INDENT:
                    element_type = 'indent'
                elif token_type == token.DEDENT:
                    element_type = 'dedent'
                elif token_type == token.NEWLINE or token_type == token.NL:
                    element_type = 'newline'
                elif token_type == token.COMMENT:
                    element_type = 'comment'
                elif token_type == token.ENCODING:
                    continue
                elif token_type == token.ENDMARKER:
                    continue

                if element_type in ['indent', 'dedent']:
                    # Indent/Dedent tokens don't always have meaningful string values in the same way
                    # But token.INDENT usually carries the whitespace string.
                    pass

                token_data = {
                    'type': element_type,
                    'value': token_string,
                    'line': start_line,
                    'column': start_col
                }
                
                tokens.append(token_data)
                
        except tokenize.TokenError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

        return tokens

    def to_json(self, code_str, indent=2):
        """Returns the parsed structure as a JSON string."""
        structure = self.parse(code_str)
        return json.dumps(structure, indent=indent)

if __name__ == "__main__":
    import sys
    
    # Example usage
    sample_code = """
def hello_world():
    print("Hello, world!")
    x = 10
    if x > 5:
        return True
    return False
"""
    parser = PythonCodeParser()
    json_output = parser.to_json(sample_code)
    print(json_output)
