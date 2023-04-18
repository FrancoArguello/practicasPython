import os


def limpioPantalla():
    sisOper = os.name
    if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
        os.system("clear")
    elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
        os.system("cls")
