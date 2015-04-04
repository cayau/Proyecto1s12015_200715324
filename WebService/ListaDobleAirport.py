import json
from flask import json
class NodeAirport(object):
 
    def __init__(self, ide, nom, pai, con, prev, next):
        self.identificador = ide
        self.nombre = nom
        self.pais = pai
        self.contrasena = con
        self.prev = prev
        self.next = next
 
 
class DoubleListAirport(object):
 
    head = None
    tail = None
 
    def append(self,ide, nom, pai, con):
        new_node = NodeAirport(ide, nom, pai, con, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            return True
        else:
            if not self.dat(ide):
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
                return True
            else:
                return False
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.nombre == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
 
    def show(self):
        current_node = self.head
        vuelos=[]
        while current_node is not None:
            vuelos.append({'id':current_node.identificador,'nombre':current_node.nombre,'pais':current_node.pais,'contra':current_node.contrasena})
            current_node = current_node.next
        return vuelos

    def dat(self, node_value):
        encontrado = "false"
        current_node = self.head
        # print("Showing complete data from selected airport:")
        
        while current_node is not None and encontrado != "true":
            
            if current_node.identificador == node_value:
                # print('aeropuerto encontrado')
                # print(current_node.identificador + " " +  current_node.nombre + " " +current_node.pais + " " + str(current_node.contrasena) )
                encontrado = "true"
                return True
            else:
                if current_node.next is None and encontrado != "true":
                    # print ("aeropuerto no encontrado")
                    return False
                

            current_node = current_node.next    
