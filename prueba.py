from modelo.Procesos import Procesos

p1 = Procesos(1,'p1',1,None,[1,2,3])

p1.set_tamano(int (p1.get_tamano()) - 2)
print(p1.get_tamano())