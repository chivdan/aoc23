vars = {}

def solve():
    filename = "input.txt"

    rules = {}
    parts = []
    for line in open(filename):
        line = line.replace("\n", "")
        if line.startswith("{"):
            values = []
            for e in line[1:-1].split(","):
                values.append(int(e.split("=")[1]))
            parts.append(values)
        elif not line.strip():
            pass
        else:
            name, rest = line.split("{")
            if name == "in":
                name = "in_"
            rest = rest.replace("}", "")
            instructions = rest.split(",")

            foo = f"""
def {name} (x, m, a, s):"""
            for instruction in instructions:
                if ">" in instruction or "<" in instruction:
                    condition, action = instruction.split(":")
                    code = f"""
    if {condition}:
        return '{action}'"""
                else:
                    code = f"""
    return '{instruction}'"""
                foo += code
            exec(foo, vars)
            rules[name] = foo

    for rule in rules:
        print(rules[rule])
    print(parts)

    accepted = []
    for part in parts:
        foo = "in_"
        while True:
            arguments = str(tuple(part))[1:-1]
            print(arguments)
            exec(f"symbol = {foo}({arguments})", vars)
            if vars["symbol"] == "A": 
                accepted.append(part)
                print("accepted", part)
                break
            elif vars["symbol"] == "R":
                print("rejected", part)
                break
            else:
                print("redirect to", vars["symbol"])
                foo = vars["symbol"]

    print(accepted)                
    print(sum(sum(v) for v in accepted))


if __name__ == '__main__':
    solve()