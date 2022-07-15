"""
Nombres de los archivos de lectura y escritura, modifique como considere.
 """
nombreLectura = "inB"
nombreEscritura = "outB"


def input():
    '''
    Método para realizar la lectura del problema, no modificar.
    '''
    readData = []
    line = 0
    def readLine():
        inputLine = readData[line]
        line+=1
        return inputLine

    with open(nombreLectura+".txt", "r") as f:
        readData = f.read().split('\n')
        data = readLine().split(" ")
        n = int(data[0])
        m = int(data[1])
        libros = []
        for i in range(m):
            data = readLine().split(" ")
            nombre = data[0]
            paginas = int(data[1])
            libros.append(Libro(nombre, paginas))
        return Entrada(n, m, libros)



def output(obj):
    '''
    Método para realizar la escritura de la respuesta del problema, no modificar.
    '''
    out = obj.tiempoTotal + "\n"
    for i in range(len(obj.libroQueEmpieza)):
        out+= obj.libroQueEmpieza[i] +" " +obj.libroQueTermina[i] +"\n"
    

    with open(nombreEscritura+".txt", "w") as f:
        f.write(out)





def solve(n, a, b, ab, ba):
    """
    Implementar el algoritmo y devolver un objeto de tipo Respuesta, el cual servirá
    para imprimir la solución al problema como se requiere en el enunciado.
    """
    return Respuesta(0, [],[])


def main():
    n, a, b, ab, ba = input()
    res = solve(n, a, b, ab, ba)
    output(res)


if __name__ == "__main__":
    main()


class Entrada():
    def __init__(self, n, m, libros):
        self.n = n
        self.m = m
        self.libros = libros

class Respuesta():
    def __init__(self, tiempoTotal, libroQueEmpieza, libroQueTermina):
        self.tiempoTotal = tiempoTotal
        self.libroQueEmpieza = libroQueEmpieza
        self.libroQueTermina = libroQueTermina

class Libro():
    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas