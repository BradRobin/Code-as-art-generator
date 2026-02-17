
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from parser import PythonCodeParser
from ascii_generator import AsciiArtGenerator
from visual_generator import VisualArtGenerator

def generate_gallery():
    src_dir = "src"
    ascii_dir = "gallery/ascii"
    graphics_dir = "gallery/graphics"
    
    # Ensure directories exist
    os.makedirs(ascii_dir, exist_ok=True)
    os.makedirs(graphics_dir, exist_ok=True)
    
    parser = PythonCodeParser()
    ascii_gen = AsciiArtGenerator()
    viz_gen = VisualArtGenerator()
    
    print(f"Scanning {src_dir} for Python files...")
    
    for filename in os.listdir(src_dir):
        if filename.endswith(".py"):
            filepath = os.path.join(src_dir, filename)
            print(f"Processing {filename}...")
            
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
                
            tokens = parser.parse(code)
            
            # Generate ASCII Art
            ascii_art = ascii_gen.generate(tokens)
            ascii_filename = f"{os.path.splitext(filename)[0]}.txt"
            ascii_path = os.path.join(ascii_dir, ascii_filename)
            with open(ascii_path, "w", encoding="utf-8") as f:
                f.write(ascii_art)
            print(f"  -> Generated ASCII: {ascii_path}")
            
            # Generate Visual Art
            graphics_filename = f"{os.path.splitext(filename)[0]}.png"
            graphics_path = os.path.join(graphics_dir, graphics_filename)
            viz_gen.generate(tokens, graphics_path)
            print(f"  -> Generated Visual: {graphics_path}")

if __name__ == "__main__":
    generate_gallery()
