from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#=====================================
# S3 es hijo de ReposotirioDeUsuarios
#=====================================
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str

    def __init__(mi, clientId:str, secretKey: str, bucket: str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}:{mi.__secretKey}")

    def guardar(mi,usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),"apellido":usuario.getApellido,"edad":usuario.getDad()}
        print("Guardando usuario de la bandeja_ {mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")
