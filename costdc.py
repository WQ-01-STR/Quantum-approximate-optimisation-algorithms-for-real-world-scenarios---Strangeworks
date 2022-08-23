from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.tools.visualization import circuit_drawer
from qiskit import Aer
from qiskit import execute
from qiskit import transpile
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import NoiseModel, amplitude_damping_error
from qiskit.providers.models.backendconfiguration import QasmBackendConfiguration


import numpy as np
import scipy.sparse.linalg as sla
import copy
import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations, groupby

def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

def print_gates(qc):
    for gate in qc.data:
        print('\ngate name:', gate[0].name) 

#Description Gates
class Gates:
    #dictionary {name gate: number qubit}
    gates = {'cx': 2}
    #get number qubits for gate
    @staticmethod    
    def get_number_qubits(gate_name):
        if gate_name not in Gates.gates:
            return 1
        return Gates.gates.get(gate_name)

class QPlatform:
    #nqubit - max number of qubits on platform
    #basis_gates_price - is dictionary of price gates accessed on the platform
    def __init__(self, nqubit, basis_gates_price, stuffs_price):
        self.nqubit = nqubit
        self.basis_gates_price = basis_gates_price
        self.stuffs_price = stuffs_price
        noise_model = NoiseModel()
        noise_model.add_basis_gates(self.get_basis_gates())
        self.simulator = AerSimulator(noise_model=noise_model)

    #return array of basis_gates       
    def get_basis_gates(self):
        return list(self.basis_gates_price.keys())
    #get price of stuff
    def get_stuff_price(self, stuff_name):
        if stuff_name not in self.stuffs_price:
            return 0.0
        return self.stuffs_price.get(stuff_name)
    #get price of basis gate
    def get_gate_price(self, gate_name):
        if gate_name not in self.basis_gates_price:
            return 0.0
        return self.basis_gates_price.get(gate_name)
    #get cost of circuit item
    def get_cost_circuit_item(self, item_name):
        return self.get_gate_price(item_name)* Gates.get_number_qubits(item_name) + self.get_stuff_price(item_name)

    #set and convert the circuit to basis gates circuit
    def set_basis_circuit(self, circuit):
        self.qc_basis = transpile(circuit, self.simulator)
        return self.qc_basis
    #get basis circuit
    def get_basis_circuit(self):
        return self.qc_basis
    #cost of circuit
    def cost_circuit(self):
        cost = 0.0
        for gate in self.qc_basis.data:
            cost += self.get_cost_circuit_item(gate[0].name)
        return cost
    #cost of access to platphorm
    def cost_access(self):
        return self.get_stuff_price('access')
    #cost of running circuit
    def cost_running(self, shots):
        return shots*self.cost_circuit() + self.cost_access()
    #cost of multi running circuit
    def cost_multi_running(self, count, shots):
        return count * self.cost_running(shots)
    #cost task
    def cost(self, circuit, count, shots):
        self.set_basis_circuit(circuit)
        return self.cost_multi_running(count, shots)
    
def get_ibmq_basis_gates():
    return ['id', 'rz', 'sx', 'x', 'cx'];

def get_common_price(gates, price):
    return  { i : price for i in gates }

def get_price_gates_ibmq_127():
    return {
        'id': 0.0,
        'rz': 0.00003,
        'sx': 0.00008,
        'x':0.00008,
        'cx': 0.0001
    }

def ibmq_7_factory():
    return QPlatform(7, get_common_price(get_ibmq_basis_gates(), 0.0), {'access':0.0, 'measure':0.0})
def ibmq_27_factory():
    return QPlatform(27, get_common_price(get_ibmq_basis_gates(), 0.00001), {'access':0.1, 'measure':0.00001})
def ibmq_127_factory():
    return QPlatform(127, get_price_gates_ibmq_127(), {'access':0.25, 'measure':0.00001})

# Available Platforms for circuit
class AvailablePlatforms:
    #constructor 
    def __init__(self, circuit):
        self.platforms = {
             'IbmQ_7qubits': ibmq_7_factory(),
             'IbmQ_27qubits': ibmq_27_factory(),
             'IbmQ_127qubits': ibmq_127_factory(),
#             'IonQ': ionq_factory()
        }
        for key in self.platforms:
            self.platforms[key].set_basis_circuit(circuit)
           
        self.circuit = circuit

    #get suite platforms for circuit
    def get_suite_platforms(self):
        num_qubits = self.circuit.num_qubits
        return filterTheDict(self.platforms, lambda elem: elem[1].nqubit >= num_qubits)
    #get keys of all platforms
    def get_name_platforms(self):
        return list(self.platforms.keys())
    #get keys of suite platforms
    def get_name_suite_platforms(self):
        return list(self.get_suite_platforms().keys())
    #get cost of platform
    def get_cost_platform(self, platform_name, count, shots):
        if platform_name not in self.platforms:
            return 0.0
        return self.platforms.get(platform_name).cost(self.circuit, count, shots)
    #get basis gate circuit     
    def get_basis_circuit(self,platform_name):
        if platform_name not in self.platforms:
            return self.circuit
        return self.platforms.get(platform_name).get_basis_circuit()
        #get basis gate circuit     
    def get_basis_gates(self,platform_name):
        if platform_name not in self.platforms:
            return []
        return self.platforms.get(platform_name).get_basis_gates()

    #is platform suite for circuit
    def is_suite(self, platform_name):
        return platform_name in self.get_suite_platforms()
    #get max qubits
    def get_number_qubits(self, platform_name):
        if platform_name not in self.platforms:
            return 0
        return self.platforms.get(platform_name).nqubit
    #cost of circuit
    def cost_circuit(self, platform_name):
        if platform_name not in self.platforms:
            return 0.0
        return self.platforms.get(platform_name).cost_circuit()
    #cost of access to platphorm
    def cost_access(self, platform_name):
        if platform_name not in self.platforms:
            return 0.0
        return self.platforms.get(platform_name).cost_access()
    #cost of running circuit
    def cost_running(self, platform_name, shots):
        if platform_name not in self.platforms:
            return 0.0
        return self.platforms.get(platform_name).cost_running(shots)
    #cost of multi running circuit
    def cost_multi_running(self, platform_name, count, shots):
        if platform_name not in self.platforms:
            return 0.0
        return self.platforms.get(platform_name).cost_multi_running(count, shots)
   
class PlatformsViewController:
    #constructor 
    def __init__(self, circuit):
        self.platforms = AvailablePlatforms(circuit)
    #get available platforms
    def platforms():
        return self.platforms
    #print list platform
    def print_platforms(self, list_name_platforms):
        for platform_name in list_name_platforms:
            print(platform_name) 
    def print_all_platforms(self):
        self.print_platforms(self.platforms.get_name_platforms())
    def print_suite_platforms(self):
        self.print_platforms(self.platforms.get_name_suite_platforms())
    def print_list_cost_platforms(self, count, shots):
        for platform_name in self.platforms.get_name_platforms():
            if  self.platforms.is_suite(platform_name):
                print('name: ' + platform_name + ' cost: ' + f'{self.platforms.get_cost_platform(platform_name, count, shots):.5f}')
            else:
                print('name: ' + platform_name + ' is not available for this circuit')
              
    def print_card_of_platform(self, platform_name):
        print('__________________________________________________________')
        print('platform: ' + platform_name + ' max number qubits:' + str(self.platforms.get_number_qubits(platform_name)))
        print('basis gates is ')
        print(self.platforms.get_basis_gates(platform_name))
        print('Circuit')
        cir = self.platforms.get_basis_circuit(platform_name)
        #print(cir)
        #cir.draw(output='mpl')
        
        
    def print_card_of_suite_platfotm(self, platform_name, count, shots):
        self.print_card_of_platform(platform_name)
        print('cost: ' + f'{self.platforms.get_cost_platform(platform_name, count, shots):.5f}')
        print('cost per circuit: ' + f'{self.platforms.cost_circuit(platform_name):.5f}')
        print('cost per access to platform: ' + f'{self.platforms.cost_access(platform_name):.5f}')
        print('cost per running ' + str(shots) + ' shots: ' + f'{self.platforms.cost_running(platform_name, shots):.5f}')
        print('Cost per task launch (' + str(count) + ' times for ' + str(shots) + ' shots) : ' + f'{self.platforms.cost_multi_running(platform_name, count, shots):.5f}')

        
    def print_card_of_not_suite_platfotm(self, platform_name):
        self.print_card_of_platform(platform_name)
        print('Platform is not available for this circuit')
        
        
    def print_list_card_of_platfotm(self, count, shots):
        for platform_name in self.platforms.get_name_platforms():
            if  self.platforms.is_suite(platform_name):
                self.print_card_of_suite_platfotm(platform_name, count, shots)
            else:
                self.print_card_of_not_suite_platfotm(platform_name)
    