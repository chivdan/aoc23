from abc import ABC, abstractmethod
from enum import StrEnum
from math import prod
from typing import Self, List

def solve():
    low = 0
    high = 0
    gates = {}
    Q = []

    class Pulse(StrEnum):
        LOW = "low"
        HIGH = "high"

    class Gate(ABC):
        def __init__(self, name: str, inputs: List[str], outputs: List[str]) -> None:
            self.name = name
            self.inputs = inputs
            self.outputs = outputs

        @abstractmethod
        def receive(self, input_gate: str, pulse: Pulse):
            pass

        def __str__(self) -> str:
            return f"{self.__class__.__name__} {self.name} inputs={self.inputs} ouputs={self.outputs}"
        
        def __repr__(self) -> str:
            return str(self)

    class UntypedGate(Gate):
        def __init__(self, name: str, inputs: List[str], outputs: List[str]) -> None:
            super().__init__(name, inputs, outputs)

        def receive(self, input_gate: str, pulse: Pulse):
            pass

    class FlipFlop(Gate):
        def __init__(self, name: str, inputs: List[str], outputs: List[str]) -> None:
            super().__init__(name, inputs, outputs)
            self.on = False

        def receive(self, input_gate: str, pulse: Pulse):
            nonlocal low
            nonlocal high
            if pulse == Pulse.HIGH:
                pass
            else:
                if self.on:
                    self.on = False
                    for output in self.outputs:
                        Q.append((gates[output], self.name, Pulse.LOW))
                        low += 1
                else:
                    self.on = True
                    for output in self.outputs:
                        Q.append((gates[output], self.name, Pulse.HIGH))
                        high += 1


    class Conjunction(Gate):
        def __init__(self, name: str, inputs: List[str], outputs: List[str]) -> None:
            super().__init__(name, inputs, outputs)

        def init(self):
            self.last = [Pulse.LOW for i in self.inputs]

        def receive(self, input_gate: str, pulse: Pulse):
            nonlocal low
            nonlocal high
            index = self.inputs.index(input_gate)
            self.last[index] = pulse

            if all(pulse == Pulse.HIGH for pulse in self.last):
                for output in self.outputs:
                    Q.append((gates[output], self.name, Pulse.LOW))
                    low += 1
            else:
                for output in self.outputs:
                    Q.append((gates[output], self.name, Pulse.HIGH))
                    high += 1

    class Broadcaster(Gate):
        def __init__(self, name: str, inputs: List[str], outputs: List[str]) -> None:
            super().__init__(name, inputs, outputs)

        def receive(self, input_gate: str, pulse: Pulse):
            nonlocal low
            nonlocal high
            for output in self.outputs:
                Q.append((gates[output], self.name, pulse))
                if pulse == Pulse.LOW:
                    low += 1
                else:
                    high += 1

    filename = "input.txt"
    for line in open(filename):
        line = line.replace("\n", "")
        left, right = line.split(" -> ")
        right = right.split(", ")
        if left == "broadcaster":
            gates[left] = Broadcaster("broadcaster", [], right)
        elif left.startswith("%"):
            gates[left[1:]] = FlipFlop(name=left[1:], inputs=[], outputs=right)
        elif left.startswith("&"):
            gates[left[1:]] = Conjunction(name=left[1:], inputs=[], outputs=right)

    while True:
        gate_to_add = None
        for gate in gates:
            for output_gate in gates[gate].outputs:
                if output_gate not in gates:
                    gate_to_add = output_gate
                    break
        if gate_to_add:
            gates[gate_to_add] = UntypedGate(gate_to_add, inputs=[], outputs=[])
        else:
            break

    for gate in gates:
        for output_gate in gates[gate].outputs:
            if gate not in gates[output_gate].inputs:
                gates[output_gate].inputs.append(gate)

    for gate in gates.values():
        if isinstance(gate, Conjunction):
            gate.init()

    # for gate in gates:
    #     print(gates[gate])

    edges = set()
    for gate in gates:
        for i in gates[gate].inputs:
            for o in gates[gate].outputs:
                edges.add((i, gate))
                edges.add((gate, o))

    with open("graph.gv", "w") as f:
        f.write("digraph g{\n")
        for gate in gates:
            if isinstance(gates[gate], FlipFlop):
                f.write(f"{gate} [color=blue];\n")
            elif isinstance(gates[gate], Conjunction):
                f.write(f"{gate} [color=red];\n")
        for src, dst in edges:
            f.write(f"{src} -> {dst};\n")
        f.write("}")

    min_act_ns = {}
    cnt = 0
    while True:
        cnt += 1
        Q = []
        gates["broadcaster"].receive(None, Pulse.LOW)
        found = False
        while Q:
            gate, name, pulse = Q.pop(0)
            # print(f"{name} -{pulse}-> {gate.name}")
            if len(min_act_ns) == 4:
                found = True
                break
            for i in range(4):
                if gate.name == "ns" and gate.last[i] == Pulse.HIGH:
                    if i not in min_act_ns:
                        min_act_ns[i] = cnt
            gate.receive(name, pulse)
        if found:
            break

    print(prod(min_act_ns.values()))

if __name__ == '__main__':
    solve()