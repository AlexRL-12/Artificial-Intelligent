# Libreries
import time
from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import imutils
import mediapipe as mp
import math
import os
import face_recognition as fr
from database import DatabaseConnection
from home_access.users.user_repository import UserRepository
from home_access.entrances.entrance_repository import EntranceRepository
import uuid
import serial

connection = DatabaseConnection().connect()
userRepository = UserRepository(connection)
entranceRepository = EntranceRepository(connection)

# Face Code
def Code_Face(images):
    listacod = []

    # Iteramos
    for img in images:
        # Correccion de color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Codificamos la imagen
        cod = fr.face_encodings(img)[0]
        # Almacenamos
        listacod.append(cod)

    return listacod

# Close Windows LogBiometric
def Close_Windows():
    global step, conteo
    # Reset Variables
    conteo = 0
    step = 0
    pantalla2.destroy()

# Close Windows SignBiometric
def Close_Windows2():
    global step, conteo
    # Reset Variables
    conteo = 0
    step = 0
    pantalla3.destroy()

# Profile
def Profile(username, image_path):
    global step, conteo, OutFolderPathUser
    # Reset Variables
    conteo = 0
    step = 0

    allowed = False; user_id = None; file_path = image_path
    user = userRepository.find_user_by_username(username)

    if user:
        try:
            # abrir la puerta
            ser = serial.Serial("COM3", 9600,timeout=1)
            time.sleep(2)
            ser.write(b'1')
        
            print("Puerta abierta")
        except:
            print("Something else went wrong")

        user_id = user[0]
        name = user[1]
        username = user[2]
        allowed = True
        print_allowed_screen(username, name)


    entranceRepository.create(user_id, file_path, allowed)


def print_allowed_screen(username, name):
    pantalla4 = Toplevel(pantalla)
    pantalla4.title("BIOMETRIC SIGN")
    pantalla4.geometry("1280x720")

    back = Label(pantalla4, image=imagenB, text="Back")
    back.place(x=0, y=0, relwidth=1, relheight=1)

        # Interfaz
    texto1 = Label(pantalla4, text=f"BIENVENIDO {name}")
    texto1.place(x=580, y=50)
        # Label
        # Video
    lblImgUser = Label(pantalla4)
    lblImgUser.place(x=490, y=80)

        # Imagen
    PosUserImg = clases.index(username)
    UserImg = images[PosUserImg]

    ImgUser = Image.fromarray(UserImg)
        #
    ImgUser = cv2.imread(f"{OutFolderPathFace}/{username}.png")
    ImgUser = cv2.cvtColor(ImgUser, cv2.COLOR_RGB2BGR)
    ImgUser = Image.fromarray(ImgUser)
        #
    IMG = ImageTk.PhotoImage(image=ImgUser)

    lblImgUser.configure(image=IMG)
    lblImgUser.image = IMG

# Register Biometric
def Log_Biometric():
    global pantalla, pantalla2, conteo, parpadeo, img_info, step

    if cap is None:
        return

    ret, frame = cap.read()

    # Frame Save
    frameSave = frame.copy()

    # RGB
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Show
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Si es correcta
    if ret == False:
        cap.release()
        return

    # Inference
    res = FaceMesh.process(frameRGB)

    # List Results
    px = []
    py = []
    lista = []
    r = 5
    t = 3

    if not res.multi_face_landmarks:
        return

    # Iteramos
    for rostros in res.multi_face_landmarks:
        # Draw Face Mesh
        mpDraw.draw_landmarks(frame, rostros, FacemeshObject.FACEMESH_TESSELATION, ConfigDraw, ConfigDraw)

        # Extract KeyPoints
        for id, puntos in enumerate(rostros.landmark):

            # Info IMG
            al, an, c = frame.shape
            x, y = int(puntos.x * an), int(puntos.y * al)
            px.append(x)
            py.append(y)
            lista.append([id, x, y])

            # 468 KeyPoints
            if len(lista) == 468:
                # Ojo derecho
                x1, y1 = lista[145][1:]
                x2, y2 = lista[159][1:]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                longitud1 = math.hypot(x2 - x1, y2 - y1)
                #print(longitud1)

                # Ojo Izquierdo
                x3, y3 = lista[374][1:]
                x4, y4 = lista[386][1:]
                cx2, cy2 = (x3 + x4) // 2, (y3 + y4) // 2
                longitud2 = math.hypot(x4 - x3, y4 - y3)
                #print(longitud2)

                # Parietal Derecho
                x5, y5 = lista[139][1:]
                # Parietal Izquierdo
                x6, y6 = lista[368][1:]

                # Ceja Derecha
                x7, y7 = lista[70][1:]
                # Ceja Izquierda
                x8, y8 = lista[300][1:]

                #cv2.circle(frame, (x5, y5), 2, (255, 0, 0), cv2.FILLED)
                #cv2.circle(frame, (x6, y6), 2, (0, 0, 0), cv2.FILLED)
                #cv2.circle(frame, (x7, y7), 2, (0, 255, 0), cv2.FILLED)
                #cv2.circle(frame, (x8, y8), 2, (0, 255, 0), cv2.FILLED)

                # Face Detect
                faces = detector.process(frameRGB)

                if faces.detections is not None:
                    for face in faces.detections:

                        # bboxInfo - "id","bbox","score","center"
                        score = face.score
                        score = score[0]
                        bbox = face.location_data.relative_bounding_box

                        # Threshold
                        if score > confThreshold:
                            # Info IMG
                            alimg, animg, c = frame.shape

                            # Coordenates
                            xi, yi, an, al = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                            xi, yi, an, al = int(xi * animg), int(yi * alimg), int(
                                an * animg), int(al * alimg)

                            # Width
                            offsetan = (offsetx / 100) * an
                            xi = int(xi - int(offsetan/2))
                            an = int(an + offsetan)
                            xf = xi + an

                            # Height
                            offsetal = (offsety / 100) * al
                            yi = int(yi - offsetal)
                            al = int(al + offsetal)
                            yf = yi + al

                            # Error < 0
                            if xi < 0: xi = 0
                            if yi < 0: yi = 0
                            if an < 0: an = 0
                            if al < 0: al = 0

                        # Steps
                        if step == 0:
                            # Draw
                            cv2.rectangle(frame, (xi, yi, an, al), (255, 0, 255), 2)
                            # IMG Step0
                            alis0, anis0, c = img_step0.shape
                            frame[50:50 + alis0, 50:50 + anis0] = img_step0

                            # IMG Step1
                            alis1, anis1, c = img_step1.shape
                            frame[50:50 + alis1, 1030:1030 + anis1] = img_step1

                            #IMG Step2
                            alis2, anis2, c = img_step2.shape
                            frame[270:270 + alis2, 1030:1030 + anis2] = img_step2

                            # Condiciones
                            if x7 > x5 and x8 < x6:

                                # Cont Parpadeos
                                if longitud1 <= 10 and longitud2 <= 10 and parpadeo == False:  # Parpadeo
                                    conteo = conteo + 1
                                    parpadeo = True

                                elif longitud1 > 10 and longitud2 > 10 and parpadeo == True:  # Seguridad parpadeo
                                    parpadeo = False

                                # IMG check
                                alich, anich, c = img_check.shape
                                frame[165:165 + alich, 1105:1105 + anich] = img_check

                                # Parpadeos
                                # Conteo de parpadeos
                                cv2.putText(frame, f'Parpadeos: {int(conteo)}', (1070, 375), cv2.FONT_HERSHEY_COMPLEX,0.5,
                                            (255, 255, 255), 1)


                                if conteo >= 3:
                                    # IMG check
                                    alich, anich, c = img_check.shape
                                    frame[385:385 + alich, 1105:1105 + anich] = img_check

                                    # Open Eyes
                                    if longitud1 > 14 and longitud2 > 14:
                                        # Cut
                                        cut = frameSave[yi:yf, xi:xf]
                                        # Save Image Without Draw
                                        cv2.imwrite(f"{OutFolderPathFace}/{RegUser}.png", cut)
                                        pantalla2.setvar("image_path", f"{OutFolderPathFace}/{RegUser}.png")
                                        # Cerramos
                                        step = 1
                            else:
                                conteo = 0

                        if step == 1:
                            # Draw
                            cv2.rectangle(frame, (xi, yi, an, al), (0, 255, 0), 2)
                            # IMG check Liveness
                            allich, anlich, c = img_liche.shape
                            frame[50:50 + allich, 50:50 + anlich] = img_liche
                            pantalla2.after(5000, Close_Windows)
                            break

                # close = pantalla2.protocol("WM_DELETE_WINDOW", Close_Windows())

    # Rendimensionamos el video
    frame = imutils.resize(frame, width=1280)

    # Convertimos el video
    im = Image.fromarray(frame)
    img = ImageTk.PhotoImage(image=im)

    # Mostramos en el GUI
    lblVideo.configure(image=img)
    lblVideo.image = img
    lblVideo.after(10, Log_Biometric)


# Sign Biometric
def Sign_Biometric():
    global pantalla, pantalla3, conteo, parpadeo, img_info, step, user_name, prueba

    # Leemos la videocaptura
    if cap is not None:
        ret, frame = cap.read()

        # Frame Save
        frameCopy = frame.copy()

        # Resize
        frameFR = cv2.resize(frameCopy, (0, 0), None, 0.25, 0.25)

        # Color
        rgb = cv2.cvtColor(frameFR, cv2.COLOR_BGR2RGB)

        # RGB
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Si es correcta
        if ret == True:

            # Inference
            res = FaceMesh.process(frameRGB)

            # List Results
            px = []
            py = []
            lista = []
            r = 5
            t = 3

            # Resultados
            if res.multi_face_landmarks:
                # Iteramos
                for rostros in res.multi_face_landmarks:

                    # Draw Face Mesh
                    mpDraw.draw_landmarks(frame, rostros, FacemeshObject.FACEMESH_TESSELATION, ConfigDraw, ConfigDraw)

                    # Extract KeyPoints
                    for id, puntos in enumerate(rostros.landmark):

                        # Info IMG
                        al, an, c = frame.shape
                        x, y = int(puntos.x * an), int(puntos.y * al)
                        px.append(x)
                        py.append(y)
                        lista.append([id, x, y])

                        # 468 KeyPoints
                        if len(lista) == 468:
                            # Ojo derecho
                            x1, y1 = lista[145][1:]
                            x2, y2 = lista[159][1:]
                            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                            longitud1 = math.hypot(x2 - x1, y2 - y1)
                            #print(longitud1)

                            # Ojo Izquierdo
                            x3, y3 = lista[374][1:]
                            x4, y4 = lista[386][1:]
                            cx2, cy2 = (x3 + x4) // 2, (y3 + y4) // 2
                            longitud2 = math.hypot(x4 - x3, y4 - y3)
                            #print(longitud2)

                            # Parietal Derecho
                            x5, y5 = lista[139][1:]
                            # Parietal Izquierdo
                            x6, y6 = lista[368][1:]

                            # Ceja Derecha
                            x7, y7 = lista[70][1:]
                            # Ceja Izquierda
                            x8, y8 = lista[300][1:]

                            #cv2.circle(frame, (x5, y5), 2, (255, 0, 0), cv2.FILLED)
                            #cv2.circle(frame, (x6, y6), 2, (0, 0, 0), cv2.FILLED)
                            #cv2.circle(frame, (x7, y7), 2, (0, 255, 0), cv2.FILLED)
                            #cv2.circle(frame, (x8, y8), 2, (0, 255, 0), cv2.FILLED)

                            # Face Detect
                            faces = detector.process(frameRGB)

                            if faces.detections is not None:
                                for face in faces.detections:

                                    # bboxInfo - "id","bbox","score","center"
                                    score = face.score
                                    score = score[0]
                                    bbox = face.location_data.relative_bounding_box

                                    # Threshold
                                    if score > confThreshold:
                                        # Info IMG
                                        alimg, animg, c = frame.shape

                                        # Coordenates
                                        xi, yi, an, al = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                                        xi, yi, an, al = int(xi * animg), int(yi * alimg), int(
                                            an * animg), int(al * alimg)

                                        # Width
                                        offsetan = (offsetx / 100) * an
                                        xi = int(xi - int(offsetan/2))
                                        an = int(an + offsetan)
                                        xf = xi + an

                                        # Height
                                        offsetal = (offsety / 100) * al
                                        yi = int(yi - offsetal)
                                        al = int(al + offsetal)
                                        yf = yi + al

                                        # Error < 0
                                        if xi < 0: xi = 0
                                        if yi < 0: yi = 0
                                        if an < 0: an = 0
                                        if al < 0: al = 0

                                        # Steps
                                        if step == 0:
                                            # Draw
                                            cv2.rectangle(frame, (xi, yi, an, al), (255, 0, 255), 2)
                                            # IMG Step0
                                            alis0, anis0, c = img_step0.shape
                                            frame[50:50 + alis0, 50:50 + anis0] = img_step0

                                            # IMG Step1
                                            alis1, anis1, c = img_step1.shape
                                            frame[50:50 + alis1, 1030:1030 + anis1] = img_step1

                                            # IMG Step2
                                            alis2, anis2, c = img_step2.shape
                                            frame[270:270 + alis2, 1030:1030 + anis2] = img_step2

                                            # Condiciones
                                            if x7 > x5 and x8 < x6:

                                                # Cont Parpadeos
                                                if longitud1 <= 10 and longitud2 <= 10 and parpadeo == False:  # Parpadeo
                                                    conteo = conteo + 1
                                                    parpadeo = True

                                                elif longitud2 > 10 and longitud2 > 10 and parpadeo == True:  # Seguridad parpadeo
                                                    parpadeo = False

                                                # IMG check
                                                alich, anich, c = img_check.shape
                                                frame[165:165 + alich, 1105:1105 + anich] = img_check

                                                # Parpadeos
                                                # Conteo de parpadeos
                                                cv2.putText(frame, f'Parpadeos: {int(conteo)}', (1070, 375),
                                                            cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                                            (255, 255, 255), 1)

                                                if conteo >= 3:
                                                    # IMG check
                                                    alich, anich, c = img_check.shape
                                                    frame[385:385 + alich, 1105:1105 + anich] = img_check

                                                    # Open Eyes
                                                    if longitud1 > 14 and longitud2 > 14:
                                                        step = 1
                                            else:
                                                conteo = 0

                                        if step == 1:
                                            # Draw
                                            cv2.rectangle(frame, (xi, yi, an, al), (0, 255, 0), 2)
                                            # IMG check Liveness
                                            allich, anlich, c = img_liche.shape
                                            frame[50:50 + allich, 50:50 + anlich] = img_liche

                                            # Find Faces
                                            faces = fr.face_locations(rgb)
                                            facescod = fr.face_encodings(rgb, faces)

                                            # Iteramos
                                            for facecod, faceloc in zip(facescod, faces):

                                                # Matching
                                                Match = fr.compare_faces(FaceCode, facecod)

                                                # Similitud
                                                simi = fr.face_distance(FaceCode, facecod)

                                                # Min
                                                min = np.argmin(simi)

                                                user_name = None
                                                unique_id = uuid.uuid4().__str__()
                                                imagePath = f"{OutFolderPathEntrace}/{unique_id}.png"
                                                image = frameCopy[yi:yf, xi:xf]
                                                cv2.imwrite(imagePath, image)
                                                # User
                                                if Match[min]:
                                                    # UserName
                                                    user_name = clases[min].upper()

                                                Profile(user_name, imagePath)


                            # Close Window
                            close = pantalla3.protocol("WM_DELETE_WINDOW", Close_Windows2)

            # Rendimensionamos el video
            frame = imutils.resize(frame, width=1280)

            # Convertimos el video
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, Sign_Biometric)

        else:
            cap.release()


# Sign Function
def Sign():
    global LogUser, LogPass, OutFolderPath, cap, lblVideo, pantalla3, FaceCode, clases, images

    # DB Faces
    # Accedemos a la carpeta
    images = []
    clases = []
    lista = os.listdir(OutFolderPathFace)

    # Leemos los rostros del DB
    for lis in lista:
        # Leemos las imagenes de los rostros
        imgdb = cv2.imread(f'{OutFolderPathFace}/{lis}')
        # Almacenamos imagen
        images.append(imgdb)
        # Almacenamos nombre
        clases.append(os.path.splitext(lis)[0])

    # Face Code
    FaceCode = Code_Face(images)

    # 3° Ventana
    pantalla3 = Toplevel(pantalla)
    pantalla3.title("BIOMETRIC SIGN")
    pantalla3.geometry("1280x720")

    back2 = Label(pantalla3, image=imagenB, text="Back")
    back2.place(x=0, y=0, relwidth=1, relheight=1)

    # Video
    lblVideo = Label(pantalla3)
    lblVideo.place(x=0, y=0)

    # Elegimos la camara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)
    Sign_Biometric()


# Register Function
def Log():
    global RegName, RegUser, RegPass, InputNameReg, InputUserReg, InputPassReg, cap, lblVideo, pantalla2
    # Name, User, PassWord
    RegName, RegUser, RegPass = InputNameReg.get(), InputUserReg.get(), InputPassReg.get()

    if len(RegName) == 0 or len(RegUser) == 0 or len(RegPass) == 0:
        # Info incompleted
        print(" FORMULARIO INCOMPLETO ")

    else:
        # Info Completed
        # Check users
        UserList = os.listdir(PathUserCheck)
        # Name Users
        UserName = []
        for lis in UserList:
            # Extract User
            User = lis
            User = User.split('.')
            # Save
            UserName.append(User[0])

        # Check Names
        if RegUser in UserName:
            # Registred
            print("USUARIO REGISTRADO ANTERIORMENTE")

        else:
            # No Registred
            # Info
            info.append(RegName)
            info.append(RegUser)
            info.append(RegPass)

            # Save Info
            f = open(f"{OutFolderPathUser}/{RegUser}.txt", 'w')
            f.writelines(RegName + ',')
            f.writelines(RegUser + ',')
            f.writelines(RegPass + ',')
            f.close()

            # Clean
            InputNameReg.delete(0, END)
            InputUserReg.delete(0, END)
            InputPassReg.delete(0, END)

            # Ventana principal
            pantalla2 = Toplevel(pantalla)
            pantalla2.title("BIOMETRIC REGISTER")
            pantalla2.geometry("1280x720")

            back = Label(pantalla2, image=imagenB, text="Back")
            back.place(x=0, y=0, relwidth=1, relheight=1)

            # Video
            lblVideo = Label(pantalla2)
            lblVideo.place(x=0, y=0)
            #lblVideo.place(x=320, y=115)

            # Elegimos la camara
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cap.set(3, 1280)
            cap.set(4, 720)
            Log_Biometric()

            pantalla2.wait_variable('image_path')
            image_path = pantalla2.getvar('image_path')

            if image_path is not None:
                userRepository.create(
                    name=RegName,
                    password=RegPass,
                    user=RegUser,
                    file_path=image_path,
                )


# Path
OutFolderPathUser = (os.getcwd()+'/DataBase/Users').replace("\\","/")
PathUserCheck = (os.getcwd()+'/DataBase/Users/').replace("\\","/")
OutFolderPathFace = (os.getcwd()+'/DataBase/Faces').replace("\\","/")
OutFolderPathEntrace = (os.getcwd()+'/DataBase/Entraces').replace("\\","/")


# List
info = []

# Variables
parpadeo = False
conteo = 0
muestra = 0
step = 0

# Margen
offsety = 30
offsetx = 20

# Umbral
confThreshold = 0.5
blurThreshold = 15

# Tool Draw
mpDraw = mp.solutions.drawing_utils
ConfigDraw = mpDraw.DrawingSpec(thickness=1, circle_radius=1) #Ajustamos la configuracion de dibujo

# Object Face Mesh
FacemeshObject = mp.solutions.face_mesh
FaceMesh = FacemeshObject.FaceMesh(max_num_faces=1) #Creamos el objeto (Ctrl + Click)

# Object Detect
FaceObject = mp.solutions.face_detection
detector = FaceObject.FaceDetection(min_detection_confidence= 0.5, model_selection=1)

# Img OpenCV
# Leer imagenes
img_check = cv2.imread((os.getcwd()+'/SetUp/check.png').replace("\\","/"))
img_step0 = cv2.imread((os.getcwd()+'/SetUp/Step0.png').replace("\\","/"))
img_step1 = cv2.imread((os.getcwd()+'/SetUp/Step1.png').replace("\\","/"))
img_step2 = cv2.imread((os.getcwd()+'/SetUp/Step2.png').replace("\\","/"))
img_liche = cv2.imread((os.getcwd()+'/SetUp/LivenessCheck.png').replace("\\","/"))


# Ventana principal
pantalla = Tk()
pantalla.title("FACE RECOGNITION SYSTEM")
pantalla.geometry("1280x720")

# Fondo
imagenF = PhotoImage(file = (os.getcwd()+'/SetUp/Inicio.png').replace("\\","/"))
background = Label(image = imagenF, text = "Inicio")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Fondo 2
imagenB = PhotoImage(file = (os.getcwd()+'/SetUp/Back2.png').replace("\\","/"))

# Input Text
# Register
# Name
InputNameReg = Entry(pantalla)
InputNameReg.place(x= 110, y = 320)
# User
InputUserReg = Entry(pantalla)
InputUserReg.place(x= 110, y = 430)
# Pass
InputPassReg = Entry(pantalla, show="*")
InputPassReg.place(x= 110, y = 540)

# Botones
# Registro
imagenBR = PhotoImage(file=(os.getcwd()+'/SetUp/BtSign.png').replace("\\","/"))
BtReg = Button(pantalla, text="Registro", image=imagenBR, height="40", width="200", command=Log)
BtReg.place(x = 300, y = 580)

# Inicio de sesion
imagenBL = PhotoImage(file=(os.getcwd()+'/SetUp/Btlogin.png').replace("\\","/"))
BtSign = Button(pantalla, text="Sign", image=imagenBL, height="40", width="200", command=Sign)
BtSign.place(x = 850, y = 580)

# Eject
pantalla.mainloop()
