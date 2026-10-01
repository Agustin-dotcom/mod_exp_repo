from qsimov import Drewom, QCircuit, QGate

def get_sum():
    gate = QGate(3, 0, "SUM")
    gate.add_operation("X", targets=2, controls=1)
    gate.add_operation("X", targets=2, controls=0)
    return gate