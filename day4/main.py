TEMP = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""
INVALID_PASSPORTS = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

VALID_PASSPORTS = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

class Passport:
    def __init__(self, contents: list[str]) -> None:
        self.values = dict()
        self._parseContents(contents)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"<Passport: {self.values}"

    def _parseContents(self, contents: list[str]):
        for line in contents:
            self._parseTokensInLine(line)

    def _parseTokensInLine(self, line: str):
        pairs = line.split()
        for p in pairs:
            parts = p.split(":")
            self._parseTokenValue(parts[0], parts[1])

    def _parseTokenValue(self, token, value):
        self.values[token] = value

def validate_byr(value):
    """
    four digits; at least 1920 and at most 2002.
    """
    if len(value) != 4:
        return False

    if int(value) >= 1920 and int(value) <= 2002:
        return True
    else:
        return False

def validate_iyr(value):
    """
    four digits; at least 2010 and at most 2020.
    """
    if len(value) != 4:
        return False
    if int(value) >= 2010 and int(value) <= 2020:
        return True
    else:
        return False
    
def validate_eyr(value):
    """
    four digits; at least 2020 and at most 2030
    """
    if len(value) != 4:
        return False
    if int(value) >= 2020 and int(value) <= 2030:
        return True
    else:
        return False

def validate_hgt(value:str):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76
    """
    if "cm" not in value and "in" not in value:
        return False
    if "cm" in value:
        temp = int(value.split("cm")[0])
        return (temp >=150) and (temp <=193)
    if "in" in value:
        temp = int(value.split("in")[0])
        return (temp >=59) and (temp <=76)
    return False

def validate_hcl(value:str):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    valid = set(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
    if len(value) != 7:
        return False
    if value[0] != "#":
        return False
    for v in value[1:]:
        if v not in valid:
            return False
    return True

def validate_ecl(value):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth"""
    valid = set("amb blu brn gry grn hzl oth".split())
    return value in valid

def validate_pid(value):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    return len(value) == 9

class Validator:
    def __init__(self, required: set[str], optional: set[str], datavalidation: dict = None) -> None:
        self.required = required
        self.datavalidation = datavalidation
        self.optional = optional

    def valid(self, passport: Passport):
        missing = list()
        validation = list()
        for v in self.required:
            if v not in passport.values:
                return False # required value not found
            else:
                if self.datavalidation is not None:
                    if v in self.datavalidation:
                        validation.append(self.datavalidation[v](passport.values[v])) # whether or not it passes validation
                    else:
                        return True # didn't need to be validated
                else:
                    return True # data validation not used
        if self.datavalidation is not None:
            return all(validation)
        return True
        # i don't think i care about optional fields at all

def part1():
    content: list[str] = list()
    passports: list[Passport] = list()
    #input_list = TEMP.splitlines()
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        input_list = f.readlines()
    for line in input_list:
        l = line.strip().rstrip()
        if len(content) == 0:
            content.append(l)
            continue
        if l == "":
            passports.append(Passport(content))
            content = list()
            continue
        content.append(l)
    passports.append(Passport(content))
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    optional = set(["cid"])
    v = Validator(required, optional)
    valid = 0
    for p in passports:
        if v.valid(p):
            valid += 1
    print(f"Valid: {valid}")

def part2():
    content: list[str] = list()
    passports: list[Passport] = list()
    #input_list = INVALID_PASSPORTS.splitlines()
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        input_list = f.readlines()
    for line in input_list:
        l = line.strip().rstrip()
        if len(content) == 0:
            content.append(l)
            continue
        if l == "":
            passports.append(Passport(content))
            content = list()
            continue
        content.append(l)
    passports.append(Passport(content))
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    optional = set(["cid"])
    datavalidation = dict()
    datavalidation["byr"] = validate_byr
    datavalidation["iyr"] = validate_iyr
    datavalidation["eyr"] = validate_eyr
    datavalidation["hgt"] = validate_hgt
    datavalidation["hcl"] = validate_hcl
    datavalidation["ecl"] = validate_ecl
    datavalidation["pid"] = validate_pid
    v = Validator(required, optional, datavalidation)
    valid = 0
    for p in passports:
        if v.valid(p):
            print(p)
            valid += 1
    print(f"Valid: {valid}")


if __name__ == "__main__":
    part2()
