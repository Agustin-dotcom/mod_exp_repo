from qsimov import Drewom, QCircuit, QGate
from carry import get_carry
from sum import get_sum
from rc import get_rc
import numpy as np
n=3
size = 3*n+1
# a0 a1 a2 | b0 b1 b2 | s0 s1 s2 s3 | [0,a0,b0,0,a1,b1,0,a2,b2,0] [0,a0,s0,0,a1,s1,0,a2,s2,s3]
# 0  0  0  | 0  0  0  | 0  0  0  0  | [0,0,0,0,0,0,0,0,0,0] [0,0,0,0,0]
# [0,0,0,0,0,0,0,0,0,0] [0,0,0,0,0,0,0,0,0,0]
# [0,1,0,0,0,0,0,0,0,0] [0,1,1,0,0,0,0,0,0,0] 
# [0,0,0,0,1,0,0,0,0,0] [0,0,0,0,1,1,0,0,0,0]
c = QCircuit(size, size, "Adder", ancilla=[0,0,0,0,1,0,0,0,0,0])
carry = get_carry()
c.add_operation(carry, targets=[0,1,2,3])
c.add_operation(carry, targets=[3,4,5,6])
c.add_operation(carry, targets=[6,7,8,9])

c.add_operation("X", targets=8, controls=7)

sum = get_sum()

c.add_operation(sum, targets=[6,7,8])

rc = get_rc()

c.add_operation(rc, targets=[3,4,5,6])

c.add_operation(sum, targets=[3,4,5])

c.add_operation(rc, targets=[0,1,2,3])

c.add_operation(sum, targets=[0,1,2])

targets = [i for i in range(size)]
c.add_operation("MEASURE", targets=targets, outputs=targets)
use_system = False
executor = Drewom(qmachine="doki",
                      extra={"num_threads": -1,
                             "random_generator": np.random.rand,
                             "use_system": use_system})
circuit = c
iterations = 1
mes = executor.execute(circuit, iterations=iterations)

print("RawMes:", mes)