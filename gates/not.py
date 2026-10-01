from qsimov import Drewom, QCircuit, QGate
import numpy as np
use_system = False
size = 1
c = QCircuit(size, size , "Gate NOT or X Pauli Gate", ancilla= [0])
#c.add_operation("X", targets=size-1, anticontrols=size-2)
c.add_operation("X", targets=0)
c.add_operation("MEASURE", targets=0, outputs=0)
executor = Drewom(qmachine="doki",
                      extra={"num_threads": -1,
                             "random_generator": np.random.rand,
                             "use_system": use_system})
circuit = c
iterations = 1
mes = executor.execute(circuit, iterations=iterations)
print(mes)
