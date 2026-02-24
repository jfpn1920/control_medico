class Paciente:
    def __init__(self, nombre, edad, telefono, correo):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.citas = []
    def agregar_cita(self, fecha, hora, motivo):
        cita = {"fecha": fecha, "hora": hora, "motivo": motivo}
        self.citas.append(cita)
        print(f"cita agregada para {self.nombre}.\n")
    def mostrar_info(self):
        print(f"\n paciente: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"telefono: {self.telefono}")
        print(f"correo: {self.correo}")
        if not self.citas:
            print("no tiene citas registradas.")
        else:
            print("citas:")
            for i, cita in enumerate(self.citas, start=1):
                print(f"{i}. fecha: {cita['fecha']}, hora: {cita['hora']}, motivo: {cita['motivo']}")
        print()
class ControlMedico:
    def __init__(self):
        self.pacientes = {}
    def registrar_paciente(self, paciente):
        self.pacientes[paciente.nombre.lower()] = paciente
        print(f"paciente {paciente.nombre} registrado.\n")
    def buscar_paciente(self, nombre):
        return self.pacientes.get(nombre.lower(), None)
    def mostrar_todos(self):
        if not self.pacientes:
            print("no hay pacientes registrados.\n")
        else:
            print("\n pacientes registrados:")
            for paciente in self.pacientes.values():
                print(f"- {paciente.nombre}")
            print()
def menu():
    control = ControlMedico()
    while True:
        print("control medico")
        print("1. registrar paciente")
        print("2. agregar cita a paciente")
        print("3. consultar paciente")
        print("4. mostrar todos los pacientes")
        print("5. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            nombre = input("nombre del paciente: ")
            edad = input("edad: ")
            telefono = input("telefono: ")
            correo = input("correo: ")
            paciente = Paciente(nombre, edad, telefono, correo)
            control.registrar_paciente(paciente)
        elif opcion == "2":
            nombre = input("ingrese el nombre del paciente: ")
            paciente = control.buscar_paciente(nombre)
            if paciente:
                fecha = input("fecha de la cita (dd/mm/aaaa): ")
                hora = input("hora de la cita (hh:mm): ")
                motivo = input("motivo de la cita: ")
                paciente.agregar_cita(fecha, hora, motivo)
            else:
                print("paciente no encontrado.\n")
        elif opcion == "3":
            nombre = input("ingrese el nombre del paciente: ")
            paciente = control.buscar_paciente(nombre)
            if paciente:
                paciente.mostrar_info()
            else:
                print("paciente no encontrado.\n")
        elif opcion == "4":
            control.mostrar_todos()
        elif opcion == "5":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()