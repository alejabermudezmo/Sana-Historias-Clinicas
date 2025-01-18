
# DATOS DE USUARIOS
usuarios = {
    "super user": {"contraseña": "9999", "rol": "Super User"}, 
    "admin": {"contraseña": "1234", "rol": "Administrador"},
    "digitador": {"contraseña": "5678", "rol": "Digitador"},
    "usuario":{"contraseña":"abcd", "rol": "Usuario"}
}


def verusuarios():
                  print("\n << USUARIOS REGISTRADOS >>")
                  print("------------------------------------")
                  for usuario, datos in usuarios.items():
                      print("\nUsuario: ", usuario)
                      print("contraseña: ", datos["contraseña"])
                      print("Rol: ", datos["rol"])
                      print()

def quitar_rool():
                 print("\n<< ELIMINAR ROL A USUARIO >>")
                 print("-----------------------------")
                 usuario_asignado = input("\nIngrese nombre de usuario: ")
                 if usuario_asignado in usuarios:
                     usuarios[usuario_asignado]["rol"] = "Usuario"
                     print("\n--------------------------------------------------------------------")
                     print("\x1b[3;32m" + f"El rol de {usuario_asignado} eliminado, Ahora su rol es de ´Usuario´." + "\033[0;m")    # mensaje en verde
                     print("--------------------------------------------------------------------")

def asignarrol():
                print("\n<< ASIGNAR ROL A USUARIO >>")
                print("--------------------------")
                usuario_asignado = input("\nIngrese nombre del usuario: ")
                if usuario_asignado in usuarios:
                    nuevo_rol = input("Ingrese el nuevo Rol de usuario: ")  
                    if nuevo_rol == "Admin" and "digitador":
                       print("")
                    usuarios[usuario_asignado]["rol"] = nuevo_rol
                    print("\n-------------------------------------------")
                    print("\x1b[3;32m" + f"El rol para el usuario  {usuario_asignado} ahora es {nuevo_rol}" + "\033[0;m")  #saldra mensaje en verde
                    print("-------------------------------------------")
                else:
                     print("\033[4;31m" + "\nEl usuario no existe." + "\033[0;m")  # mensaje en rojo
                     print("\n")
                    
def eliminaruser():
                 print("\n<< ELIMINAR USUARIO >>")
                 print("-----------------------")
                 usuario_asignado = input("\nIngrese el nombre de usuario: ")          
                 if usuario_asignado in usuarios:
                     if usuarios[usuario_asignado]["rol"] != "Super User":
                         del usuarios[usuario_asignado]
                         print("\n----------------------------------")
                         print("\x1b[3;32m" + f"{usuario_asignado} eliminado con éxito." + "\033[0;m")  # mensaje en verde
                         print("-----------------------------------")
                     else:
                         print("\033[4;31m" + "\nNo se puede eliminar un usuario con rol 'Super User'." + "\033[0;m")   
                 else:
                    print("\033[4;31m" + f"\nEl {usuario_asignado} no existe" + "\033[0;m")  # mensaje en rojo 

