# Lab4_Robotica
Desarrollo e implementación del laboratorio 4 de robótica


Daniel Felipe Cantor Santana

Juan David Morales Restrepo

David Leonardo Cocoma Reyes

# 1) Requisitos
Para el desarrollo de esta práctica del laboratorio,se necesita lo siguiente:
  - Ubuntu versión 20.xx preferible 20.04 LTS con ROS.
  - Espacio de trabajo para catkin correctamente configurado.
  - Paquetes de Dynamixel Workbench. 
  - Paquete del robot Phantom X.
  - Python o MATLAB 2015b o superior instalado en el equipo.
  - Robotics toolbox de Mathworks
  - Toolbox de robótica de Peter Corke.
  - Un manipulador Phantom X Pincher con su base en madera.


# 2) Análisis

El Pincher debe moverse y tomar los siguientes ángulos, desde el cero de la configuración que este tenga:
|Articulación|Posición 1|Posición 2|Posición 3|Posición 4|Posición 5|
|:----------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|1|0|-25| 35|-85|-80|
|2|0| 15|-35| 20| 35|
|3|0|-20| 30|-55|-55|
|4|0| 20|-30| 17| 45|
|5|0|  0|  0|  0|  0|

Las posiciones del pincher se simularon en matlab para ver que posición deberia esperarse del brazo. Además se realizaron los pasos dados en el repositorio https://github.com/fegonzalez7/rob_unal_clase3, para descargar y conectar Dynamixel Workbench en el PC. Con esto se determinaron los límites articulares del pincher y se fotografió en las mismas posiciones. La comparación de ambos pasos se presenta a continuación:
![Imagen 1](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Comparación_P1.png)
![Imagen 2](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Comparación_P2.png)
![Imagen 3](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Comparación_P3.png)
![Imagen 4](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Comparación_P4.png)
![Imagen 5](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Comparación_P5.png)

Además, se tiene la tabla correspondiente al DH del robot:
| j |     theta |         d |         a |     alpha |    offset |
|:-:|:---------:|:---------:|:---------:|:---------:|:---------:|
|  1|         q1|       14.5|          0|      1.571|          0|
|  2|         q2|          0|       10.7|          0|      1.571|
|  3|         q3|          0|       10.7|          0|          0|
|  4|         q4|          0|          0|          0|          0|

# 3)HMI en Python
Para lograr el desarrollo del laboratorio, se realizó una HMI, empleando el paquete tkinter. Dicha HMI es capaz de inicializar ROS además se buscó que fuese capaz de ubicar el brazo según las posiciones iniciales, agregarle una posición esperada y mostrar la posición actual del pincher.El archivo "HMI.py" se encuentra adjunto en este repositorio. El procedimiento de su funcionamiento es el siguiente:
   - Inicializar ROS
   - La HMI genera el nodo necesario
   - El usuario debe darle la posición al brazo, sea de las 5 iniciales o escribir otra posición deseada.

Se tomó como base los archivos presentes en el paquete de Dynamixel "jointPub.py", "jointSub.py" y "jointSrv.py"  y el archivo "basic.yalm" se modificó, para agregar 4 joints mas.


# 4)Video de implementación
A continuación se presenta el video de la implementación del laboratorio:


  [![Alt text](https://img.youtube.com/vi/uRHSwcJ6vfw/0.jpg)](https://www.youtube.com/watch?v=uRHSwcJ6vfw)


