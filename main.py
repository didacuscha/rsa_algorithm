from rsa_utils import generar_par_claves, encriptar_mensaje, desencriptar_mensaje

def main():
    # Generamos las claves
    print("Generando par de claves...")
    resultado = generar_par_claves()
    print(resultado)
    
    while True:
        print("\nMenú de opciones:")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "1":
            mensaje = input("\nIngrese el mensaje a encriptar: ")
            mensaje_encriptado = encriptar_mensaje(mensaje)
            print(f"\nMensaje encriptado: {mensaje_encriptado}")
            
        elif opcion == "2":
            mensaje_encriptado = input("\nIngrese el mensaje encriptado: ")
            mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado)
            print(f"\nMensaje desencriptado: {mensaje_desencriptado}")
            
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()