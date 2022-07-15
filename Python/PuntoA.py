"""
Nombres de los archivos de lectura y escritura, modifique como considere.
 """
nombreLectura = "inA"
nombreEscritura = "outA"


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
        n = int(readLine())
        p = []
        for i in range(n):
            linea = readLine()
            data = linea.split(" ")
            horas = data[1].split("-")
            tiempo = horas[0].split(":")
            horaI = int(tiempo[0])
            minI = int(tiempo[1])
            tiempo = horas[1].split(":")
            horaF = int(tiempo[0])
            minF = int(tiempo[1])
            p.append(Procedimiento(data[0], Hora(horaI, minI), Hora(horaF, minF)))
        return p





def output(obj):
    '''
    Método para realizar la escritura de la respuesta del problema, no modificar.
    '''
    out = obj.n + "\n"
    out += obj.tiempoTotal + "\n"
    for i in range(obj.n):
        out+= obj.nombreProcedimientos[i] +"\n"
    

    with open(nombreEscritura+".txt", "w") as f:
        f.write(out)




def solve(n, procedimientos):
    """
    Implementar el algoritmo y devolver un objeto de tipo Respuesta, el cual servirá
    para imprimir la solución al problema como se requiere en el enunciado.
    """

    return Procedimiento(0, Hora(0,0), [])


def main():
    p = input()
    n = len(p)
    res = solve(n,p)
    output(res)


if __name__ == "__main__":
    main()


class Respuesta():
    def __init__(self, n, tiempoTotal, nombreProcedimientos):
        self.n = n
        self.tiempoTotal = tiempoTotal
        self.nombreProcedimientos = nombreProcedimientos

class Procedimiento():
    def __init__(self, nombre, horaInicio, horaFin):
        self.nombre = nombre
        self.horaInicio = horaInicio
        self.horaFin = horaFin

class Hora():
    def __init__(self, hora, minutos):
        self.hora = hora
        self.minutos = minutos
    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'