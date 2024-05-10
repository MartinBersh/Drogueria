from Services.DrogueriaServices import DrogueriaServices

if __name__ == '__main__':

    drogueria_services = DrogueriaServices()

    while True:
        print("\nMenú:")
        print("1. Crear Producto con Builder")
        print("2. Uso de Singleton")
        print("3. Uso de Prototype")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            drogueria_services.crearProductoBuilder()
        elif opcion == "2":
            drogueria_services.usoSingleton()
        elif opcion == "3":
            drogueria_services.usoPrototype()
        elif opcion == "4":
            print("Saliendo")
            break
        else:
            print("Opción inválida")
