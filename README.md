# Lab4_Robotica
Desarrollo e implementación del laboratorio 4 de robótica


Daniel Felipe Cantor Santana

Juan David Morales Restrepo

David Leonardo Cocoma Reyes

# 1) Requisitos
Para el desarrollo de esta práctica del laboratorio,se necesita lo siguiente:
  - Ubuntu versi´on 20.xx preferible 20.04 LTS con ROS.
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

Las posiciones del pincher se tomaron em matlab para ver que posición deberia esperarse del brazo:
![Imagen 1](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición1_matlab.png)
![Imagen 2](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición2_matlab.png)
![Imagen 3](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición3_matlab.png)
![Imagen 4](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición4_matlab.png)
![Imagen 5](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición5_matlab.png)

Una vez simuladas las posiciones en Matlab, se realizaron los pasos dados en el repositorio https://github.com/fegonzalez7/rob_unal_clase3, para descargar y contectar Dynamixel Workbench en el PC.Con esto se determianron los límites articulares del pincher y se fotografió en las mismas posiciones dadas, como se ve a continuación:
![Imagen 6 ](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posicion1.jpeg)
![Imagen 7](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posicion2.jpeg)
![Imagen 8](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posicion3.jpeg)
![Imagen 9](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/Posición4.jpeg)
![Imagen 10](https://github.com/Robotica-2022-I/Lab4_Robotica/blob/main/Imagenes/posición5.jpeg)



# )HMI y Python
Para lograr el desarrollo del laboratorio, se realizó una HMI, empleando el paquete tkinter. Dicha HMI es capaz de inicializar ROS además se buscó que fuese capaz de ubicar el brazo según las posiciones iniciales, agregarle una posición esperada y mostrar la posición actual del pincher.
   El procedimiento de su funcionamiento es el siguiente:
   - Inicializar ROS
   - La HMI genera el nodo necesario
   - El usuario debe darle la posición al brazo, sea de las 5 iniciales o escribir otra posición deseada.

  
Se tomó como base los archivos presentes en el paquete de Dynamixel >jointPub.py, >jointSub.py y >joint  para el movimiento como tal del brazo.   


# )Video de implementación
A continuación se presenta el video de la implementación del laboratorio:
  [![Alt text](https://img.youtube.com/vi/uRHSwcJ6vfw/0.jpg)](https://www.youtube.com/watch?v=uRHSwcJ6vfw)


