# prueba1
Antes de empezar con los ejercicios, para empezar a realizarlos 
1.- Cree una matriz 100x100 llena de ceros
2.- Cree un arreglo en donde se iban a guardar los digitos del numero de cedula, uno por uno
3.- Para llenar la matriz con los digitos del numero de cedula, hice un doble for con un rango de 100
3.1.- Dentro del segundo for puse una variable que almacenaba el %10, es decir los digitos del 0-9, la utilice de referencia para almacenar los elementos del arreglo en cada elemento de la matriz
SUMA COLUMNA
1.-Almacene dentro de una variable la columna a sumar
2.-Cree una variable inicializada con 0, para almacenar los elementos
3.-Cree los 2 tipicos for, dentro del segundo valide con un if, si la variable que ingresa el usuario es(con-1) igual  a la columna en la que esta el for, entonces sumo todos los elementos ue pasen por esa columna
SUMA FILA
1.- Casi el mismo principio que la suma solo que el if va dentro del primer for ya que este for es el que determina las filas
2.-- Si la variable del for es igual (-1) a la variable ingresada por el usuario, entonces se suma cada elemento de esa fila mediante un for interno
SUMA DIAGONALES
1.- Cree dos variables inicializadas en 0, la primera(diago1) para que tomara el primer valor de la primera fila e incrementase a medida que avance las filas, creando asi la diagonal
2.- la otra variable para ir suman esos elementos
3.- Cree los 2 for, dentro del segundo validando si el iterador que da las columnas fuese igual a (diago1), y si es asi sumar ese elemento en la segunda variable
4.- Con eso tenia la suma de los elementos de la primera diagonal
5.- Para la segunda diagonal fue casi lo mismo pero de adelante hacia atras
6.- Es decir la primera variable (diago2) la inicializaba en 99, para que haga referencia al ultimo elemento de la primera fila e ir decrementando uno, creando asi la ilusión de una diagonal inversa
7.- Los pasos son los mismos que en la primera diagonal sumando elemento a elemento si el iterador de las columnas es igual a (diago2)
8.- diago2 se iba decrementando en 1 en el primer for(a medida que las filas avanzaban)
MULTIPLICACION COLUMNA
1.- Utilice casi el mismo codigo que en la suma de columnas, solo que en lugar de inicializar la variable que iba sumando los valores en 0, la inicialice en 1 para que la multiplicación no fuera cero
2.- En el if, en lugar de suma5 += matriz[b][c], le cambie a suma5 *= matriz[b][c]
MULTIPLICACION FILA
1.- Casi lo mismo que en suma de fila, solo cambio la variable que almacenaba de 0 a 1 
2.- En el if que estaba en el primer for, en lugar de suma2 += matriz[b][c], le cambie a suma2 *= matriz[b][c]
MULTIPLICACION DIAGONAL
1.- Lo mismo que en suma de diagonales solo que aplique la multiplicación de una sola columna en lugar de las 2, debido al espacio de memoria
2.- diago2 lo inicialice en 99 para que vaya multiplicando el ultimo elemento de la primera fila, con el penultimo elemento de la segunda fila y asi
