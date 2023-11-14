import cirq

def balanced(qubits):
    circuit = cirq.Circuit()
    for i in range(3):
        circuit.append(cirq.CNOT(qubits[i], qubits[3]))


    return circuit

def constant(qubits):
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[3]))
    
    return circuit

def run(gate):
    circuit = cirq.Circuit()
    qubits = cirq.LineQubit.range(4)

    for i in range(4):
        circuit.append(cirq.H(qubits[i]))

    circuit.append(gate(qubits))

    for i in range(3):
        circuit.append(cirq.H(qubits[i]))

    circuit.append(cirq.measure(qubits[3], key='result'))
    
    # Запускаем схему на симуляторе
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10)
    
    print(result)

run(balanced)

run(constant)