
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class VisualArtGenerator:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        # Colors: (R, G, B) normalized 0-1
        self.colors = {
            'keyword': (0.8, 0.2, 0.2),    # Red
            'variable': (0.3, 0.3, 0.3),   # Dark Gray
            'string': (0.2, 0.6, 0.2),     # Green
            'number': (0.2, 0.2, 0.8),     # Blue
            'operator': (0.6, 0.4, 0.2),   # Orange-ish
            'comment': (0.6, 0.6, 0.6, 0.5), # Transparent Gray
            'other': (0.1, 0.1, 0.1)       # Black
        }
        
    def generate(self, tokens, output_file):
        """
        Generates a PNG image visualizing the code structure.
        """
        # Analyze code structure
        max_lines = max(t['line'] for t in tokens) if tokens else 1
        max_cols = max(t['end_column'] if 'end_column' in t else t['column'] + len(t['value']) for t in tokens) if tokens else 1
        
        # Setup plot
        # Aspect ratio based on lines vs width
        # Let's say we want each character to be roughly square-ish or blocky
        fig_width = 10
        fig_height = fig_width * (max_lines / max(max_cols, 40)) # Heuristic
        fig_height = max(fig_height, 2) # Min height
        
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        # Remove axes
        ax.set_axis_off()
        ax.set_xlim(0, max_cols + 5)
        ax.set_ylim(max_lines + 1, 0) # Invert Y axis: line 1 at top
        
        for token in tokens:
            token_type = token.get('type', 'other')
            val = token.get('value', '')
            line = token.get('line', 1)
            col = token.get('column', 0)
            
            # Simple length estimation if end column not provided
            # (Our parser uses start pos, might need to estimate length)
            length = len(val)
            
            color = self.colors.get(token_type, self.colors['other'])
            
            # Draw rectangle
            # (x, y) is bottom-left corner usually, but we inverted Y
            # Using patches.Rectangle((x, y), width, height)
            rect = patches.Rectangle(
                (col, line - 0.8), # y position
                length, # width
                0.8,    # height (row height)
                linewidth=0,
                edgecolor='none',
                facecolor=color
            )
            ax.add_patch(rect)
            
        plt.tight_layout()
        plt.savefig(output_file, dpi=100, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
        return output_file
