from qsimov import Drewom, QCircuit, QGate

def get_rs():
    gate = QGate(3, 0, "RS")
    gate.add_operation("X", targets=2, controls=0) 
    gate.add_operation("X", targets=2, controls=1) 
    return gate