from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#========================
# Clase storemanager
# NO TIENE VARIABLES !!!
#========================
class ManejoDeInscripciones:
    #=================================================================
    # Decorador staticmethod
    # El objeto sólo tiene la funcion inscribirUsuario
    # ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    #==================================================================
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios:RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

