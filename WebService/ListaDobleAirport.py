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
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
 
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
        # print("Show list data:")
        current_node = self.head
        VUELOS = ""
        while current_node is not None:
            VUELOS += current_node.identificador+":{'nombre':"+current_node.nombre+", 'pais':"+current_node.pais+", 'contra':"+current_node.contrasena+"},"
            # print(current_node.prev.nombre if hasattr(current_node.prev, "nombre") else None)
            # print(current_node.nombre)
            # print(current_node.next.nombre if hasattr(current_node.next, "nombre") else None)
            current_node = current_node.next
        VUELOS = {VUELOS}
        return VUELOS
        print("*"*50)

    def dat(self, node_value):
        encontrado = "false"
        current_node = self.head
        print("Showing complete data from selected airport:")
        
        while current_node is not None and encontrado != "true":
            
            if current_node.identificador == node_value:
                print('aeropuerto encontrado')
                print(current_node.identificador + " " +  current_node.nombre + " " +current_node.pais + " " + str(current_node.contrasena) )
                encontrado = "true"
                
            else:
                if current_node.next is None and encontrado != "true":
                    print ("aeropuerto no encontrado")
                
                
                
            current_node = current_node.next    
        
        
 
# d = DoubleListAirport()
# d.show()
# d.append("A1","Bruselas","Belgica",123)
# d.append("A2","Tikal","Guatemala",1234)
# d.append("A3","Copenhagen","Dinamarca",12345)
# d.append("A4","Madrid","Espana",123456)
# d.append("A5","Roma","Italia",1234567)
# d.show()
# d.dat("A2")
# d.dat("A5")
# d.dat("A8")
#d.append(6)
#d.append(50)
#d.append(30)
#d.append(100)

#d.show()
 
#d.remove(50)
#d.remove(5)
 
# d.show()
        
            
    
