def saludo(nombre: str = "mundo") -> str:
    return f"¡Hola, {nombre} desde Python!"

def main():
    mensaje = saludo("Elizabeth")
    print(mensaje)

if __name__ == "__main__":
    main()
