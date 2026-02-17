
import sys
import os
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from parser import PythonCodeParser
from ascii_generator import AsciiArtGenerator
from visual_generator import VisualArtGenerator
from poetry_generator import PoetryGenerator

def main():
    parser = argparse.ArgumentParser(description="Code-as-Art Generator: Visualize your Python code.")
    
    parser.add_argument("input_file", help="Path to the Python file to process")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ascii", action="store_true", help="Generate ASCII art")
    group.add_argument("--graphics", action="store_true", help="Generate Visual art (PNG)")
    group.add_argument("--poetry", action="store_true", help="Generate Code Poetry")
    
    parser.add_argument("-o", "--output", help="Output filename (optional)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
        
    with open(args.input_file, "r", encoding="utf-8") as f:
        code = f.read()
        
    parser_tool = PythonCodeParser()
    tokens = parser_tool.parse(code)
    
    if args.ascii:
        generator = AsciiArtGenerator()
        art = generator.generate(tokens)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(art)
            print(f"ASCII art saved to {args.output}")
        else:
            print(art)
            
    elif args.graphics:
        # Check matplotlib first
        try:
            import matplotlib
        except ImportError:
            print("Error: matplotlib is required for graphics mode. Install it with 'pip install matplotlib'.")
            sys.exit(1)
            
        generator = VisualArtGenerator()
        output_path = args.output if args.output else "output.png"
        generator.generate(tokens, output_path)
        print(f"Visual art saved to {output_path}")
        
    elif args.poetry:
        generator = PoetryGenerator()
        poem = generator.generate(tokens)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(poem)
            print(f"Poetry saved to {args.output}")
        else:
            print(poem)

if __name__ == "__main__":
    main()
