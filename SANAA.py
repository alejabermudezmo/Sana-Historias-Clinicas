
import getpass
from opcionHistorial import *
from opcionUsuario import *



def limpa():
    import os
    sistoper = os.name
    if sistoper=="posix":
        os.system("clear")
    elif sistoper == "nt":
        os.system("cls")
    else:
        print("\033[;31m" + "La pantalla no se puede limpiar" + "\033[0;m")
 
#OPCIONES DE LOGIN
def iniciosession():

     pass
     limpa()
     print("\n** INICIAR SESION **")
     print("----------------------")
     usuario= input("Ingrese su usuario: ")
     contraseña= getpass.getpass("Ingrese su contraseña: ")
     if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            limpa()
            print("\n============================================")
            print("\x1b[3;32m"+f"\tBienvenido Usuario, {usuario}!"+ "\033[0;m")  # mensaje en verde
            print("==============================================")
            rol = usuarios[usuario]["rol"]           
            if rol == "Super User":
                 menusuper()
            elif rol == "Administrador":
                 menuadmin()
            elif rol == "Digitador":
                 menuDigitador()
            elif rol == "Usuario":
                  menuUsuarios()
     else:
         print("\n----------------------------------")
         print("No se encuentra registrado.")
         print("----------------------------------")
         print("\033[4;31m"+ "\nIr a registrarse." + "\033[0;m")  #mensaje en rojo
         ir = input("\nPara ir a registrarse escriba ´ir´ -> ")
         if ir == "ir":
               limpa()
               regristrarus()         
         else:
             if ir == " ":
               login()

def regristrarus():
        print("\n===============")
        print(": REGISTRARSE :")
        print("===============")
        usuario_nuevo = input("\nIngrese su nombre de usuario: ")
        if usuario_nuevo in usuarios:
            print("\033[4;31m"+"El nombre de usuario ya existe." + "\033[0;m")  #mensaje en rojo
            print("\n")
            regresar = input("\nEscriba ´ok´ para regresar -> ")
            if regresar == "ok":
                  login()
        else: 
            contraseña_nueva = input("Ingrese su contraseña: ")
            usuarios[usuario_nuevo] = {"contraseña": contraseña_nueva, "rol": "Usuario"}
            print("\n--------------------------")
            print("\x1b[3;32m" + "Registro exitoso." + "\033[0;m")    # mensaje en verde
            print("--------------------------")
            limpa()
            login()     

# LOGIN
def login():
    print("\t\t\t\t\t\t============================================================")
    print("\t\t\t\t\t\t\t\tHISTORIALES MEDICOS DE SANA")
    print("\t\t\t\t\t\t============================================================")

    print("\n\t\t\t\t\t\t---------------------------------------------------------")
    print("\t\t\t\t\t\t\t¿Qué desea hacer?")
    print("\n\t\t\t\t\t\t\t1. Iniciar sesión")
    print("\t\t\t\t\t\t\t2. Registrarse")
    print("\t\t\t\t\t\t\t3. Salir")
    print("\t\t\t\t\t\t----------------------------------------------------------")
    opcion = input("\n\t\t\t\t\t\t\tSeleccione una opción -> ")

    if opcion == "1":
        iniciosession()
    elif opcion == "2":
        regristrarus()
    elif opcion =="3":
         limpa()
         print("\n\t\t\t\t\t\t\t\t<< Salir >>")
         print("\n\t\t\t\t\t\t-------------------------------------------------------")
         print("\x1b[3;33m" + "\t\t\t\t\t\t\tGracias por utilizar el sistema SANA." + "\033[0;m") # mensaj en amarillo
         print("\t\t\t\t\t\t-------------------------------------------------------")
         print("\n\n")
         exit()
    else:   
         limpa()     
         print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m")   # mensaje en rojo
         login()


# menu super user
def menusuper():
         print("\n\t ::: MENU SUPER USER :::")
         print("\n\t1 => Historiales Clinicos")
         print("\t2 => Gestion De Usuarios ")
         print("\t3 => Salir")
         opcionS = input("\n\tSeleccione una opción -> ")

         if opcionS == "1":
            limpa()
            print("\n\t<< Historiales Clinicos >>")
            print("----------------------------------------")
            print("\t1 => Crear Historial")
            print("\t2 => Consultar Historial ")
            print("\t3 => Ver Todos Los Historiales")
            print("\t4 => Modificar Historial")
            print("\t5 => Eliminar Historial")
            print("\t6 => Regresar atras")
            print("----------------------------------------")
            opcionH = input("\tSeleccione una opcion -> ")
            if opcionH == "1":
                 limpa()
                 crearhistorial()
                 a=input("\nSeleccione ´1´ para regresar -> ")
                 if a == "1":
                      limpa()
                      menusuper()
                 else:
                       limpa()
                       menusuper()      
              
            elif opcionH =="2":
                 limpa()
                 consultarhist()
                 a=input("\nSeleccione ´1´ para regresar -> ")
                 if a == "1":
                      limpa()
                      menusuper()
                 else:
                       limpa()
                       menusuper()

            elif opcionH == "3":
                  limpa()
                  verhistorial()
                  a=input("\nSeleccione ´1´ para regresar -> ")
                  if a == "1":
                      limpa()
                      menusuper()
                  else:
                       limpa()
                       menusuper()

            elif opcionH == "4":
                limpa()
                modificarhisto()
                a=input("\nSeleccione ´1´ para regresar -> ")
                if a == "1":
                      limpa()
                      menusuper()
                else:
                       limpa()
                       menusuper()

            elif opcionH == "5": 
                 limpa()
                 eliminarhis()
                 a=input("\nSeleccione ´1´ para regresar -> ")
                 if a == "1":
                      limpa()
                      menusuper() 
                 else:
                       limpa()
                       menusuper() 

            elif opcionH == "6":
                  limpa()
                  menusuper()

            else:
                  limpa()
                  print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
                  menusuper()
         
         elif opcionS == "2":
             limpa()
             print("\n\t<< Usuarios >>")
             print("----------------------------------------")
             print("\t1 => Ver Usuarios Registrados")
             print("\t2 => Eliminar Rol")
             print("\t3 => Asignar Rol ")
             print("\t4 => Eliminar Usuario") 
             print("\t5 => Regresar Atras")
             print("----------------------------------------")
             opcionUU = input("\n\tSeleccione una opcion -> ")

             if opcionUU == "1":
                     limpa()
                     verusuarios()
                     a = input("Seleccione ´1´ para regresar -> ")
                     if a == "1":
                          limpa()
                          menusuper()
                     else:
                       limpa()
                       menusuper()

             elif opcionUU == "2":
                       limpa()
                       quitar_rool()
                       a = input("Seleccione ´1´ para regresar -> ")
                       if a == "1":
                            limpa()
                            menusuper()
                       else:
                            limpa()
                            menusuper()

             elif opcionUU == "3":
                       limpa()
                       asignarrol()
                       a=input("Seleccione ´1´ para regresar -> ")
                       if a == "1":
                          limpa()
                          menusuper()
                       else:
                            limpa()
                            menusuper()

             elif opcionUU == "4":
                     limpa()
                     eliminaruser()
                     a=input("Seleccione ´1´ para regresar -> ")
                     if a == "1":
                          limpa()
                          menusuper()
                     else:
                        limpa()
                        menusuper()

             elif opcionUU == "5":
                   limpa()
                   menusuper()
             else:
                limpa()
                print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
                menusuper()

         elif opcionS == "3":
              limpa()
              login()
         else: 
            limpa()      
            print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
            menusuper()

# menu admin
def menuadmin():
         print("\n\t ::: MENU ADMINISTRADOR :::")
         print("\n\t1 => Crear Historial")
         print("\t2 => Consultar Historial ")
         print("\t3 => Ver Todos Los Historiales")
         print("\t4 => Modificar Historial")
         print("\t5 => Eliminar Historial") 
         print("\t6 => Salir")
         opcionA = input("\n\tSeleccione una opción -> ")

         if opcionA == "1":
                limpa()
                crearhistorial()
                a=input("\nSeleccione ´1´ para regresar -> ")
                if a == "1":
                      limpa()
                      menuadmin()
                else:
                       limpa()
                       menuadmin()

         elif opcionA == "2":
                limpa()
                consultarhist()
                a=input("\nSeleccione ´1´ para regresar -> ")
                if a == "1":
                      limpa()
                      menuadmin()
                else:
                       limpa()
                       menuadmin()

         elif opcionA == "3":
                limpa()
                verhistorial()
                a=input("\nSeleccione ´1´ para regresar -> ")
                if a == "1":
                      limpa()
                      menuadmin()
                else:
                       limpa()
                       menuadmin()
              
         elif opcionA == "4":
              limpa()
              modificarhisto()
              a=input("\nSeleccione ´1´ para regresar -> ")
              if a == "1":
                      limpa()
                      menuadmin()
              else:
                       limpa()
                       menuadmin()

         elif opcionA == "5":
              limpa()
              eliminarhis()
              a=input("\nSeleccione ´1´ para regresar -> ")
              if a == "1":
                     limpa()
                     menuadmin()
              else:
                       limpa()
                       menuadmin()

         elif opcionA == "6":
              limpa()
              login()
         else:
              limpa()
              print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
              menuadmin()


# menu digitadors
def menuDigitador():
           print("\n\t ::: MENU DIGITADOR :::")
           print("\n\t1. => Crear historial")
           print("\t2. => Consultar historial")
           print("\t3. => Modificar historial")
           print("\t4. => Salir")
           opcionD = input("\n\tSeleccione una opción -> ")

           if opcionD == "1":
                 limpa()
                 crearhistorial()
                 a=input("\nSeleccione ´1´ para regresar -> ")
                 if a == "1":
                      limpa()
                      menuDigitador()
                 else:
                       limpa()
                       menuDigitador()

           elif opcionD == "2":
                       limpa()
                       consultarhist()
                       a=input("\nSeleccione ´1´ para regresar -> ")
                       if a == "1":
                             limpa()
                             menuDigitador()
                       else:
                            limpa()
                            menuDigitador()

           elif opcionD == "3":
                       limpa()
                       modificarhisto()
                       a=input("\nSeleccione ´1´ para regresar -> ")
                       if a == "1":
                             limpa()
                             menuDigitador()
                       else:
                             limpa()
                             menuDigitador()

           elif opcionD == "4":
                       limpa()
                       login()
           else:
                limpa()
                print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
                menuDigitador()

# menu de usuarios                       
def menuUsuarios():
      print("\n\t ::: MENU USUARIO :::")
      print("\n\t1. => Consultar Mi Historial")
      print("\t2. => Salir")
      opcionU= input("\n\tSeleccione una opcion -> ") 
      if opcionU == "1":
            consultarhist()
            a=input("\nSeleccione ´1´ para regresar -> ")
            if a == "1":
                  limpa()
                  menuUsuarios()
            else:
                  limpa()
                  menuUsuarios()
      elif opcionU == "2":
            limpa()
            login()
      else:
            limpa()
            print("\033[4;31m" + "Opcion no valida, intente nuevamente." + "\033[0;m") #mensaje en rojo
            menuUsuarios()

login()
