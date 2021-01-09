from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure, All, CNOT # import the operations we want to perform
from projectq.backends import Simulator, CommandPrinter
engines=[CommandPrinter()]
eng=MainEngine(Simulator(),engines)

qubit = eng.allocate_qureg(2)  # allocate 2 qubit
H | qubit[0]  # apply a Hadamard gate
CNOT | (qubit[0],qubit[1])
All(Measure) | qubit

eng.flush()