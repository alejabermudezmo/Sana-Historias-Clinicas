
pacientes= {
       #DNI DE PACIENTE
     "1234567890": {
        "Nombre": "Juan Perez",
        "Edad": "35 años",
        "Sexo":"Masculino",
        "Motivo de Consulta": "Vomito, indigestion, problemas digestivos e inflamacion de las vias respiratorias.",
        "Enfermedad Actual": "Paciente con alergias alimentarias",
        "Fecha": "2023/04/4"},
       #DNI DE  PACIENTE
    "0987654321": {
        "Nombre": "Maria Garcia",
        "Edad": "45 años",
        "Sexo": "Femenino",
        "Motivo de Consulta": "Dolor de cabeza fuerte, vomitos, cambios en la vision y sangrado nasal.",
        "Enfermedad Actual": "Paciente con hipertensión arterial",
        "Fecha": "2023/04/26"},
        # DNI DE PACIENTE
    "1029384756": {
        "Nombre": "Pedro Rodriguez",
        "Edad": "25 años",
        "Sexo": "Masculino",
        "Motivo de Consulta": "Dolor abdominal, nauseas, vomito, perdida del sueño y fiebre.",
        "Enfermedad Actual": "Paciente con  apendicitis.",
        "Fecha": "2023/04/30"},
       #DNI DE PACIENTE
     "1223344099": {
        "Nombre": "Ana Lopez",
        "Edad": "35 años",
        "Sexo": "Femenino",
        "Motivo de Consulta": "Sarpullido con ampollas en el cuerpo, picazón, cansancio y fiebre ",
        "Enfermedad Actual":  "Paciente con infeccion viral; Varicela.",
        "Fecha": "2023/05/1"}
}


def crearhistorial():
                     print("\n\t<< Crear Historial >>")
                     print("-------------------------------------------------------")
                     while True: 
                        dni = input("---- Ingrese el DNI del paciente: ")
                        if dni in pacientes: 
                            print("\x1b[1;33m" + "Ya existe historial." + "\033[0;m")   # mensaje en amarillo
                        else: 
                         nombre = input("---- Ingrese el nombre del paciente: ")
                         edad = input("---- Ingrese la edad del paciente: ")
                         sexo = input("---- Ingrese el sexo del paciente: ")
                         motivo_de_consulta = input("---- Motivo de consulta del paciente: ") 
                         enfermedad_actual = input("---- Enfermedad actual del paciente: ")
                         fecha = input("---- Ingrese fecha (AA/MM/DD): ")
                         pacientes[dni] = {"Nombre": nombre, "Edad": edad, "Sexo": sexo, "Motivo de Consulta":
                                           motivo_de_consulta, "Enfermedad Actual": enfermedad_actual, "Fecha": fecha}
                         print("-------------------------------------------------------")
                         print("\x1b[3;32m" + "Historial creado con éxito." + "\033[0;m")    # mensaje en verde
                         print("-------------------------------------------------------")
                         break 


            
def consultarhist():
                 print("\n\t<< Consultar Historial >>")
                 print("-------------------------------------------------------")
                 dni = input("Ingrese el DNI del paciente que desea consultar -> ")
                 print("-------------------------------------------------------")
                 paciente = pacientes.get(dni)
                 if paciente:
                      print("\n\n\t<< Historial del Paciente >>")
                      print("-------------------------------------------------------")
                      print("--- Nombre: ", paciente["Nombre"])
                      print("--- Edad: ", paciente["Edad"])
                      print("--- Sexo: ", paciente["Sexo"])
                      print("--- Motivo de consulta: ", paciente["Motivo de Consulta"])
                      print("--- Enfermedad actual: ", paciente["Enfermedad Actual"])
                      print("--- Fecha: ", paciente["Fecha"])
                      print("-------------------------------------------------------")
                 else:
                     print("\033[4;31m"+"No se encuentra historial, ingrese un DNI valido." + "\033[0;m" )  #mensaje en rojo

def modificarhisto():
                   print("\n<< Modificar Historial >>")
                   print("-------------------------------------------------------")
                   dni = input("\nIngrese el DNI del paciente que desea modificar -> ")
                   paciente = pacientes.get(dni)
                   if paciente:
                      print("-------------------------------------------------------")
                      print("\t1 => Modificar Nombre")
                      print("\t2 => Modificar Edad")
                      print("\t3 => Modificar Sexo")
                      print("\t4 => Modificar Motivo de Consulta")
                      print("\t5 => Modificar Enfermedad Actual")
                      print("\t6 => Modificar Fecha")
                      print("\t7 => Modificar Historial Completo ")
                      print("-------------------------------------------------------")
                      opcionM = input("Ingrese la opcion que desea modificar -> ")
                      if opcionM == "1":
                          nombre = input("\nIngrese el nuevo nombre -> ")
                          pacientes[dni]["Nombre"] = nombre
                          print("\x1b[3;32m" + "\nNombre modificado con éxito." + "\033[0;m")    # mensaje en verde
                          print("-------------------------------------------------------")
                      elif opcionM == "2":
                           edad = input("\nIngrese la nueva edad -> ")
                           pacientes[dni]["Edad"] = edad
                           print("\x1b[3;32m" + "\nEdad modificada con éxito." + "\033[0;m")    # mensaje en verde
                           print("-------------------------------------------------------")
                      elif opcionM == "3":
                          sexo = input("\nIngrese el nuevo sexo -> ")
                          pacientes[dni]["Sexo"] = sexo
                          print("\x1b[3;32m" + "\nSexo modificado con éxito." + "\033[0;m")    # en verde
                          print("-------------------------------------------------------")
                      elif opcionM == "4":
                          motivo = input("\nIngrese el nuevo motivo de consulta -> ")
                          pacientes[dni]["Motivo de Consulta"] = motivo
                          print("\x1b[3;32m" + "\nMotivo de consulta modificado con éxito." + "\033[0;m")   # msj en verde
                          print("-------------------------------------------------------")
                      elif opcionM == "5":
                         enfermedad_actual = input("\nIngrese la nueva enfermedad actual -> ")
                         pacientes[dni]["Enfermedad Actual"] = enfermedad_actual
                         print("\x1b[3;32m" + "\nEnfermedad actual modificada con éxito." + "\033[0;m")  # msj en verde
                         print("-------------------------------------------------------")
                      elif opcionM == "6":
                          fecha = input("\nIngrese la nueva fecha -> ")
                          pacientes[dni]["Fecha"] = fecha
                          print("\x1b[3;32m" + "\nFecha modificada con éxito." + "\033[0;m")    # mj en verde
                          print("-------------------------------------------------------")
                      elif opcionM == "7":
                          paciente = pacientes.get(dni)
                          if paciente:
                              print("-------------------------------------------------------")
                              print("\tModificar Historial Completo")
                              print("-------------------------------------------------------")
                              paciente["Nombre"]= input("Ingrese nombre modificado: ")
                              paciente["Edad"]= input ("Ingrese edad modificada: ")
                              paciente["Sexo"]= input("Ingrese sexo modificado: ")
                              paciente["Motivo de Consulta"]= input ("Motivo de consulta modificado: ")
                              paciente["Enfermedad Actual"]= input ("Enfermedad Actual modificado: ")
                              paciente["Fecha"]= input ("Ingrese fecha modificada: ")
                              print("\n----------------------------------------")
                              print("\x1b[3;32m"+ "Historial modificado con exito." + "\033[0;m")  # mensaje en verde
                              print("----------------------------------------")        
                      else:
                          print("\033[4;31m" + "\n Opcion invalida." + "\033[0;m")  # mensaje en rojo
                   else:
                         print("\n")
                         print("\033[4;31m"+"No se encuentra historial, ingrese un DNI valido." + "\033[0;m" )  # mensaje en rojo

                        
def eliminarhis():
                
                print("\n<< Eliminar Historial >>")
                print("---------------------------------")
                dni = input("\nIngrese el DNI del paciente que desea eliminar -> ")
                if dni in pacientes:
                     del pacientes[dni]
                     print("\n----------------------------------")
                     print("\x1b[3;32m" + "Historial eliminado con éxito." + "\033[0;m")  # mensaje en verde
                     print("-----------------------------------")
                else:
                    print("\033[4;31m" + "\nEl historial no existe." + "\033[0;m")  # mensaje en rojo


def verhistorial():
                print("\n  <<  HISTORIALES CLINICOS REGISTRADOS  >>")
                print("-------------------------------------------------------")
                for dni, paciente in pacientes.items():
                  print("\nDNI: ", dni)
                  print("Nombre: ", paciente["Nombre"])
                  print("Edad:", paciente["Edad"])
                  print("Sexo:", paciente["Sexo"])
                  print("Motivo de consulta:", paciente["Motivo de Consulta"])
                  print("Enfermedad actual:", paciente["Enfermedad Actual"])
                  print("Fecha:", paciente["Fecha"])
                  print()

