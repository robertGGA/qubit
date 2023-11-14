# https://github.com/gltronred/itis-quantum-0xx-fall-2023/blob/trunk/demo1.py

import cirq

qc = cirq.Circuit()
qubits = cirq.LineQubit.range(4)

for i in range(3):
    qc.append(cirq.CNOT(qubits[i], qubits[3]))

qc.append(cirq.X(qubits[3]).controlled_by(qubits[0], qubits[1], qubits[2]))

qc.append(cirq.measure(qubits[3], key='result'))
simulator = cirq.Simulator()
result = simulator.simulate(qc)

print(result)
# output_file_path = 'results.txt'
# with open(output_file_path, 'w') as file:
#     file.write(str(result.histogram(key='result')))

# print(f"Результаты сохранены в файл: {output_file_path}")