# Args: 
#       --name | -n : Tree type name
#       --file | -f : File to scan
#       --var  | -v : specific tree to draw (if it exists) (optional)

import argparse
import treeparser

parser = argparse.ArgumentParser(
            prog="Tree Visualizer",
            description="Visualize trees written in the Clean Language"
        )
parser.add_argument('-t', '--tree', type=str, required=True, help='Declared Tree type name')
parser.add_argument('-f', '--file', type=str, required=True, help='File to scan')
parser.add_argument('-v', '--var', type=str, required=False, help='Specific tree to draw (if it exists) (optional)')

args = parser.parse_args()

treeparser.findUserSelection(args.file, args.tree)