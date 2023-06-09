from mpi4py import MPI

#===================
#   Objeto  mensaje 
#===================
class Mensaje:
    def __init__(self,rank):
        # Iterador
        self.x = range(rank*10)
        # String
        self.p = "Vengo del proceso" + str(rank)

#=====================
#   Progrma principal
#=====================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    #print(x.s)

    #===========================================================
    #   Que te mande el anterior y si es cero que sea el último 
    #===========================================================
    fuente = rank -1 if rank != 0 else size-1

    #============================================================
    #   Mándalo al siguiente y si eres el ultimo mándalo primero
    #============================================================
    destino = rank+1 if rank!=size-1 else 0

    #==========================================================
    # send y recv son operaciones bloqueadas y generan que el
    # código se atore esperando que alguien reciba un mensaje
    # estes se resuelve enviando con los pares y recibimos con
    # los impares
    #===========================================================

    # Si soy par
    if rank%2==0:
        #=================================
        #   Enviar el mensaje al destino
        #=================================
        comm.send(s,dest = destino)

        #====================================
        #   Recibir de source y lo pone en m
        #====================================
        m = comm.recv(source = fuente)

    # Si no soy par
    else:
        #============================================
        #   Recibir primero y mandar mensaje despupés
        #============================================
        m = comm.recv(source = fuente)
        comm.send(s,dest = destino)

    print("Soye el proceso ", rank, ", el resultado es ", len(m.x),",",m.p)


