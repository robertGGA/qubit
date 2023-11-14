# https://github.com/gltronred/itis-quantum-0xx-fall-2023/blob/trunk/demo1.py

import cirq

circuit = cirq.Circuit()
qubits = cirq.LineQubit.range(4)

for i in range(3):
    circuit.append(cirq.CNOT(qubits[i], qubits[3]))

circuit.append(cirq.X(qubits[3]).controlled_by(qubits[0], qubits[1], qubits[2]))

circuit.append(cirq.measure(qubits[3], key='result'))
simulator = cirq.Simulator()
resultSimulate = simulator.simulate(circuit)

result = simulator.run(circuit, repetitions=10)
print(resultSimulate)

print(result)

