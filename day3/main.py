from dataclasses import dataclass

class Map:
    def __init__(self, input_list:list[str]):
        self.map_input = input_list
        self.map_width = len(input_list[0])
        self.map_height = len(input_list)

    def getChar(self, right:int, down:int):
        if down >= self.map_height:
            raise RuntimeError(f"{down} Exceeds Map Height {self.map_height}")

        if right >= self.map_width:
            adjusted_right = self._adjustRight(right)
            while adjusted_right >= self.map_width:
                adjusted_right = self._adjustRight(adjusted_right)
        else:
            adjusted_right = right
        return self.map_input[down][adjusted_right]
    def _adjustRight(self, right):
        return right - self.map_width

TEMP = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""
@dataclass
class Searcher:
    right: int
    down: int
    right_slope: int
    down_slope: int
    def isTree(self, map:Map):
        self.right += self.right_slope
        self.down += self.down_slope
        c = map.getChar(self.right, self.down)
        return c =="#"

def part1():
    #map_list = TEMP.splitlines()
    #print(map_list)
    map_list = list()
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            map_list.append(l.strip().rstrip())
    s = Searcher(0,0,3,1)
    m = Map(map_list)
    trees = 0
    while True:
        try:
            if s.isTree(m):
                trees+=1
        except RuntimeError:
            break
    print(trees)

def part2():
    #map_list = TEMP.splitlines()
    #print(map_list)
    map_list = list()
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            map_list.append(l.strip().rstrip())
    m = Map(map_list)
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    results = list()
    for s in slopes:
        s = Searcher(0,0,s[0],s[1])
        trees = 0
        while True:
            try:
                if s.isTree(m):
                    trees+=1
            except RuntimeError:
                break
        print(trees)
        results.append(trees)
    rtn = 1
    for r in results:
        rtn *= r
    print(rtn)




if __name__ == "__main__":
    part2()