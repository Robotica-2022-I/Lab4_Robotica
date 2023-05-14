from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import os
ruta_absoluta = os.path.abspath("images")

rt1 = ruta_absoluta + "/Pos0.png"
rt2 = ruta_absoluta + "/Escudo_unal_2016.png"
rtp1 = ruta_absoluta + "/Pos0.png"
rtp2 = ruta_absoluta + "/Pos1.png"
rtp3 = ruta_absoluta + "/Pos2.png"
rtp4 = ruta_absoluta + "/Pos3.png"
rtp5 = ruta_absoluta + "/Pos4.png"



root = Tk()
root.title("HMI")
root.config(bg="silver")
root.geometry("800x700")
root.geometry("+300+0")

global joint1pos, joint2pos,joint3pos,joint4pos,joint5pos

joint1pos = 0
joint2pos = 0
joint3pos = 0
joint4pos = 0
joint5pos = 0

dat1 = []
dat2 = []
dat3 = []
dat4 = []
dat5 = []


frame1 = LabelFrame(root, text="Controlador Phantom X", font=('Times', 20))
frame2 = LabelFrame(root, text="Configurar pose", font=('Times', 20))
frame3 = LabelFrame(root, text="Leer pose", font=('Times', 20))

frame1.pack(fill="both", expand="yes", padx=20, pady=10)
frame2.pack(fill="both", expand="yes", padx=20, pady=10)
frame3.pack(fill="both", expand="yes", padx=20, pady=10)


lbl1 = Label(frame1, text="Integrantes", font=('Times', 14))
lbl1.grid(column=0, row=0, padx=5, pady=3)
lbl1 = Label(frame1, text="David Leonardo Cocoma Reyes", font=('Times', 12))
lbl1.grid(column=0, row=1, padx=5, pady=3)
lbl1 = Label(frame1, text="Juan David Morales Restrepo", font=('Times', 12))
lbl1.grid(column=0, row=2, padx=5, pady=3)
lbl1 = Label(frame1, text="Daniel Felipe Cantor Santana", font=('Times', 12))
lbl1.grid(column=0, row=3, padx=5, pady=3)

etiquet = tk.Label(frame1, text=" ",width=15)
etiquet.grid(column=1, row=3, padx=5, pady=3)

lbl1 = Label(frame1, text="Correo unal", font=('Times', 14))
lbl1.grid(column=2, row=0, padx=5, pady=3)
lbl1 = Label(frame1, text="dcocoma", font=('Times', 12))
lbl1.grid(column=2, row=1, padx=5, pady=3)
lbl1 = Label(frame1, text="jumoralesr", font=('Times', 12))
lbl1.grid(column=2, row=2, padx=5, pady=3)
lbl1 = Label(frame1, text="dfcantors", font=('Times', 12))
lbl1.grid(column=2, row=3, padx=5, pady=3)

etiqueta = tk.Label(frame1, text=" ",width=15)
etiqueta.grid(column=3, row=3, padx=5, pady=3)

posi0 = tk.PhotoImage(file=rt1)
posi1 = tk.PhotoImage(file=rtp1)
posi2 = tk.PhotoImage(file=rtp2)
posi3 = tk.PhotoImage(file=rtp3)
posi4 = tk.PhotoImage(file=rtp4)
posi5 = tk.PhotoImage(file=rtp5)
imagen2 = tk.PhotoImage(file=rt2)

etiqueta2 = tk.Label(frame1, image=imagen2)
#etiqueta2 = tk.Label(frame1, text="no c")
etiqueta2.grid(column=4, row=0,rowspan=4, padx=5, pady=3)

var1 = tk.IntVar()

pos1 = tk.Radiobutton(frame2,text="Posición 1",variable=var1,value=1,font=('Times', 12))
pos2 = tk.Radiobutton(frame2,text="Posición 2",variable=var1,value=2,font=('Times', 12))
pos3 = tk.Radiobutton(frame2,text="Posición 3",variable=var1,value=3,font=('Times', 12))
pos4 = tk.Radiobutton(frame2,text="Posición 4",variable=var1,value=4,font=('Times', 12))
pos5 = tk.Radiobutton(frame2,text="Posición 5",variable=var1,value=5,font=('Times', 12))

pos1.grid(column=0, row=0, padx=5, pady=3)
pos2.grid(column=0, row=1, padx=5, pady=3)
pos3.grid(column=0, row=2, padx=5, pady=3)
pos4.grid(column=0, row=3, padx=5, pady=3)
pos5.grid(column=0, row=4, padx=5, pady=3)

cord1 = Label(frame2,text="(0, 0, 0, 0, 0)", font=('Times', 12))
cord2 = Label(frame2,text="(-25, 15, -20, 20, 0)", font=('Times', 12))
cord3 = Label(frame2,text="(35,-35, 30, -30, 0)", font=('Times', 12))
cord4 = Label(frame2,text="(-85, 20, -55, 17, 0)", font=('Times', 12))
cord5 = Label(frame2,text="(-80, 35, -55, 45, 0)", font=('Times', 12))

cord1.grid(column=1, row=0, padx=5, pady=3)
cord2.grid(column=1, row=1, padx=5, pady=3)
cord3.grid(column=1, row=2, padx=5, pady=3)
cord4.grid(column=1, row=3, padx=5, pady=3)
cord5.grid(column=1, row=4, padx=5, pady=3)

ent1 = tk.Entry(frame2, font=("Times", 12), width=20)
ent1.grid(column=3, row=0, padx=5, pady=3)
ent2 = tk.Entry(frame2, font=("Times", 12), width=20)
ent2.grid(column=3, row=1, padx=5, pady=3)
ent3 = tk.Entry(frame2, font=("Times", 12), width=20)
ent3.grid(column=3, row=2, padx=5, pady=3)
ent4 = tk.Entry(frame2, font=("Times", 12), width=20)
ent4.grid(column=3, row=3, padx=5, pady=3)
ent5 = tk.Entry(frame2, font=("Times", 12), width=20)
ent5.grid(column=3, row=4, padx=5, pady=3)

cbtn = Button(frame2, text="Aceptar")
cbtn.grid(column=2, row=4, padx=5, pady=3)

ac2 = Button(frame2, text="Enviar")
ac2.grid(column=5, row=4, padx=5, pady=3)

act = Button(frame3, text="Actualizar")
act.pack()


etiqueta3 = tk.Label(frame2, image=posi0)
#etiqueta3 = tk.Label(frame2, text="no c")
etiqueta3.grid(column=6, row=0, rowspan=5, padx=5, pady=3)

trv = ttk.Treeview(frame3, columns=(1,2,3), show="headings", height="10")
trv.pack()

trv.heading(1, text="Joint", anchor="w")
trv.heading(2, text="Posicion actual",anchor="w")
trv.heading(3, text="Torque Enable", anchor="w")



def updateval(d1, d2, d3, d4, d5):
    dat1 = [1,round(d1,1),"Enable"]
    dat2 = [2,round(d2,1),"Enable"]
    dat3 = [3,round(d3,1),"Enable"]
    dat4 = [4,round(d4,1),"Enable"]
    dat5 = [5,round(d5,1),"Enable"]

    trv.insert("", "end", values=dat1)
    trv.insert("", "end", values=dat2)
    trv.insert("", "end", values=dat3)
    trv.insert("", "end", values=dat4)
    trv.insert("", "end", values=dat5)

def enviar_pose():
    
    if var1.get() == 0:
        joint1pos = 0
        joint2pos = 0
        joint3pos = 0
        joint4pos = 0
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi0)
    elif var1.get() == 2:
        joint1pos = -25
        joint2pos = 15
        joint3pos = -20
        joint4pos = 20
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi2)
    elif var1.get() == 3:
        joint1pos = 35
        joint2pos = -35
        joint3pos = 30
        joint4pos = -30
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi3)
    elif var1.get() == 4:
        joint1pos = -85
        joint2pos = 20
        joint3pos = -55
        joint4pos = 17
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi4)
    elif var1.get() == 5:
        joint1pos = -80
        joint2pos = 35
        joint3pos = -55
        joint4pos = 45
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi5)
    elif var1.get() == 1:
        joint1pos = 0
        joint2pos = 0
        joint3pos = 0
        joint4pos = 0
        joint5pos = 0
        etiqueta3 = tk.Label(frame2, image=posi1)
    try:
        joint_publisher(parserad(joint1pos),parserad(joint2pos),parserad(joint3pos),parserad(joint4pos),parserad(joint5pos))
    except rospy.ROSInterruptException:
        pass

    etiqueta3.grid(column=6, row=0, rowspan=5, padx=5, pady=3)
    



def parserad(p):
    return p * 3.1416 / 180

def rad2deg(p):
    return p * 180 / 3.1416

def joint_publisher(p1,p2,p3,p4,p5):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [p1,p2,p3,p4,p5]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
        break
    #rospy.signal_shutdown()

def callback(data):
    rospy.loginfo(data.position)
    trv.delete(*trv.get_children())
    updateval(rad2deg(data.position[0]), rad2deg(data.position[1]), rad2deg(data.position[2]), rad2deg(data.position[3]), rad2deg(data.position[4]))
    trv.update()

    
    
def listener():
    #sub = rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.init_node('joint_listener', anonymous=True)
    #rospy.spin()
    #sub.unregister()
    rospy.signal_shutdown()


def randompos():
    try:
        en1 = int(ent1.get())
        en2 = int(ent2.get())
        en3 = int(ent3.get())
        en4 = int(ent4.get())
        en5 = int(ent5.get())
    except ValueError as error:
        en1 = 0
        en2 = 0
        en3 = 0
        en4 = 0
        en5 = 0

    joint1pos = en1
    joint2pos = en2
    joint3pos = en3
    joint4pos = en4
    joint5pos = en5

    try:
        joint_publisher(parserad(en1),parserad(en2),parserad(en3),parserad(en4),parserad(en5))
    except rospy.ROSInterruptException:
        pass

def tryListener():
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

    

cbtn.config(command=enviar_pose)
ac2.config(command=randompos)
act.config(command = tryListener)



root.mainloop()