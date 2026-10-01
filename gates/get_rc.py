from qsimov import Drewom, QCircuit, QGate

def get_rc():
    gate = QGate(4, 0, "RC")
    gate.add_operation("X", targets=3, controls=[0,2])
    gate.add_operation("X", targets=2, controls=1)
    gate.add_operation("X", targets=3, controls=[1,2])
    return gate