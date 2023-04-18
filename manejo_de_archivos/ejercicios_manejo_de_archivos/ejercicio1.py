#2 listas 1 con nombres y otras con apellidos

nombres= ["Franco","Thiago","Ivana", "Lucho","Yoana"]
apellidos = ["Argüello","Pereira","Aquino","Fernandez","Grimoldi"]

#refistrar estos datos en eun txt
with open("manejo_de_archivos\\ejercicios_manejo_de_archivos\\nombres_y_apellidos.txt","w", encoding="UTF-8") as arch:
    arch.write("Los datos son: \n\n")
    
    [arch.writelines(f'Nombres: {n}\nApellido: {a}\n----------------\n') for n, a in zip(nombres,apellidos)]


