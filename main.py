def pedir_numero(mensaje: str = "Introduce un número: ") -> float:
    """Solicita un número al usuario y valida que sea correcto."""
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            return int(valor) if valor.is_integer() else valor
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un número válido.")

def main():
    print("=== Programa de Lectura de Números ===")
    numero = pedir_numero("Por favor, ingresa un número: ")
    print(f"✅ Has ingresado el número: {numero}")
    
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

if __name__ == "__main__":
    main()
