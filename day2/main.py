from dataclasses import dataclass


@dataclass
class PasswordRule:
    min: int
    max: int
    letter: str

    def valid(self, password: str):
        count = password.count(self.letter)
        if count > self.max or count < self.min:
            return False
        else:
            return True

@dataclass
class PasswordRule2:
    min: int
    max: int
    letter: str

    def valid(self, password: str):
        # 1 index based
        position1 = password[self.min-1]
        position2 = password[self.max-1]
        condition1 = position1 == self.letter and position2 != self.letter
        condition2 = position1 != self.letter and position2 == self.letter
        if condition1 or condition2:
            return True
        else:
            return False


def parse_records(input_list: list[str], rule_engine):
    valid = list()
    invalid = list()
    for record in input_list:
        r = record.strip().rstrip().split()
        minmax = r[0].split("-")
        minimumm = int(minmax[0])
        maximum = int(minmax[1])
        char = r[1][0]
        password = r[2]
        p = rule_engine(minimumm, maximum, char)
        if p.valid(password):
            valid.append(password)
        else:
            invalid.append(password)
    return valid, invalid


def part1():
    with open("day2/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    valid, invalid = parse_records(lines, PasswordRule)
    print(len(valid), len(invalid))

def part2():
    with open("day2/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    valid, invalid = parse_records(lines, PasswordRule2)
    print(len(valid), len(invalid))

if __name__ == "__main__":
    part2()
