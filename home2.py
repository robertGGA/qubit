import cirq

def balanced_oracle(qubits):
    # Создаем квантовую схему для сбалансированного оракула
    circuit = cirq.Circuit()
    
    # Применяем операции XOR к первым трём кубитам
    circuit.append([cirq.CNOT(qubits[i], qubits[3]) for i in range(3)])
    
    return circuit

def constant_oracle(qubits):
    # Создаем квантовую схему для константного оракула (всегда применяем NOT к четвертому кубиту)
    circuit = cirq.Circuit()
    
    # Применяем операцию NOT (X) к четвертому кубиту
    circuit.append(cirq.X(qubits[3]))
    
    return circuit

def run_deutsch_jozsa_algorithm(oracle):
    # Создаем квантовую схему для алгоритма Дойча-Йожи
    qubits = cirq.LineQubit.range(4)
    circuit = cirq.Circuit()
    
    # Применяем операцию Hadamard ко всем кубитам
    circuit.append(cirq.H(q) for q in qubits)
    
    # Применяем оракул
    circuit.append(oracle(qubits))
    
    # Применяем операцию Hadamard ко всем кубитам, кроме последнего
    circuit.append(cirq.H(q) for q in qubits[:-1])
    
    # Измеряем результат
    circuit.append(cirq.measure(qubits[3], key='result'))
    
    # Запускаем схему на симуляторе
    simulator = cirq.Simulator()
    result = simulator.simulate(circuit)
    
    # Выводим результаты
    print(result)

# Тестирование сбалансированного оракула
print("Сбалансированный оракул:")
run_deutsch_jozsa_algorithm(balanced_oracle)

# Тестирование константного оракула
print("\nКонстантный оракул:")
run_deutsch_jozsa_algorithm(constant_oracle)