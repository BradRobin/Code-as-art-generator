
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from parser import PythonCodeParser
from visual_generator import VisualArtGenerator

sample_code_1 = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

sample_code_2 = """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
"""

if __name__ == "__main__":
    parser = PythonCodeParser()
    viz_gen = VisualArtGenerator()
    
    output_dir = "outputs/graphics"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Generating visual art for bubble_sort...")
    tokens1 = parser.parse(sample_code_1)
    viz_gen.generate(tokens1, os.path.join(output_dir, "bubble_sort.png"))
    
    print("Generating visual art for linked_list...")
    tokens2 = parser.parse(sample_code_2)
    viz_gen.generate(tokens2, os.path.join(output_dir, "linked_list.png"))
    
    print("Done!")
