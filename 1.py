digits = {"one": 1,
          "two": 2,
          "three": 3,
          "four": 4,
          "five": 5,
          "six": 6,
          "seven": 7,
          "eight": 8,
          "nine": 9}

def solve():
    result = 0
    for line in open("input.txt"):
        i = 0
        nums = []
        while i < len(line):
            if '0' <= line[i] <= '9':
                nums.append(int(line[i]))
                i += 1
                continue
            suffix = line[i:]
            found = False
            for digit in digits:
                if suffix.startswith(digit):
                    nums.append(digits[digit])
                    i += 1
                    found = True
                    break
            if not found:
                i += 1
        result += int(f"{nums[0]}{nums[-1]}")
    print(result)   

if __name__ == '__main__':
    solve()