from minesweeper import minesweeper
import nose.tools, difflib

def test_simple():
    result = minesweeper.process_grid("data/simple.txt")
    target = """2 2 1 0 0 0 0
X X 1 0 0 0 0
X 3 1 0 0 0 0
1 1 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""


    nose.tools.eq_(result,target, "difference is "+''.join(difflib.ndiff(result,target)))

