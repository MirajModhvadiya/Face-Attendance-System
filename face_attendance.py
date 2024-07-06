from tkinter import*  
from tkinter import messagebox
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

base = Tk()  
base.geometry('500x300')  

def fun():
    entered_username = entry_1.get()
    entered_password = entry_02.get()

    expected_username = "Miraj"
    expected_password = "1234"

    if entered_username == expected_username and entered_password == expected_password:
        messagebox.showinfo("Login", "Login successful!")
        base = Tk() 
        base.geometry('800x600')  
        base.title("Face Attendance System")  
  
        labl_3 = Label(base, text="Face Attendance System",width=40,font=("bold", 30))
        labl_3.place(x=10,y=40)  
                
        Button(base, text='IT Attendance',command =IT,width=20,bg='brown',fg='white').place(x=300,y=140)  
        Button(base, text='BCom Attendance',command =BCom,width=20,bg='brown',fg='white').place(x=300,y=170)
        Button(base, text='BBA Attendance',command =BBA,width=20,bg='brown',fg='white').place(x=300,y=200)  
        Button(base, text='MCom Attendance',command =MCom,width=20,bg='brown',fg='white').place(x=300,y=230)  
        Button(base, text='B.sc Attendance',command =Bsc,width=20,bg='brown',fg='white').place(x=300,y=260)  
        Button(base, text='M.sc Attendance',command =Msc,width=20,bg='brown',fg='white').place(x=300,y=290)  
        Button(base, text='MscIT Attendance',command =MscIT,width=20,bg='brown',fg='white').place(x=300,y=320)  
        

        # it will be used for displaying the registration form onto the window  
        base.mainloop()        
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")

def IT():
    messagebox.showinfo("Wait", "Project is Running!")
        
    image_folder_path = "IT/"

    image_files = os.listdir(image_folder_path)

    video_capture = cv2.VideoCapture(0)

    Face_encoding = []
    Faces_names = []

    for image_file in image_files:
            image_path = os.path.join(image_folder_path, image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            Face_encoding.append(encoding)
            
            image_name = os.path.splitext(image_file)[0]
            Faces_names.append(image_name)

    students = Faces_names.copy()

    face_locations = []
    face_encodings = []
    face_names = []
    s = True

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    csv_file_path = 'IT-'+current_date + '.csv'
    f = open(csv_file_path, 'w+', newline='')
    lnwriter = csv.writer(f)

    while True:
            _, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            if s:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(Face_encoding, face_encoding)
                    name = ""
                    face_distance = face_recognition.face_distance(Face_encoding, face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = Faces_names[best_match_index]
                    face_names.append(name)

                    if name in Faces_names:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        bottomLeftCornerOfText = (10, 100)
                        fontScale = 1.5
                        fontColor = (255, 0, 0)
                        thickness = 3
                        lineType = 2

                        cv2.putText(frame, name + ' Present',
                                    bottomLeftCornerOfText,
                                    font,
                                    fontScale,
                                    fontColor,
                                    thickness,
                                    lineType)

                        if name in students:
                            students.remove(name)
                            print(students)

                            current_time = now.strftime("%H-%M-%S")
                            lnwriter.writerow([name, current_time])

            cv2.imshow("attendance system", frame)
            if cv2.waitKey(1) & 0xFF == ord('m'):
                break

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

def BCom():
    pass

def BBA():
    pass

def MCom():
    pass

def Bsc():
    pass

def MscIT():
    pass

def Msc():
    pass

base.title("Registration Form")  
  
labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  
  
  
labl_1 = Label(base, text="Username",width=20,font=("bold", 10))  
labl_1.place(x=68,y=130)  
  
entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  
  
labl_2 = Label(base, text="Password",width=20,font=("bold", 10))  
labl_2.place(x=68,y=180)  
  
entry_02 = Entry(base,show="*")  
entry_02.place(x=240,y=180)  

  
Button(base, text='Login',command = fun,width=20,bg='brown',fg='white').place(x=180,y=220)  
# it will be used for displaying the registration form onto the window  
base.mainloop()  
print("Attendance Save Seccussfully...") 