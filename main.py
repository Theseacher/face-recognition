import face_recognition as fr 
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


Tk().withdraw()
load_image = askopenfilename()

target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)


def main():


    def encode_faces(folder):
        list_people_encoding = []
        
        for filename in os.listdir(folder):
            known_image = fr.load_image_file(f'{folder}{filename}')
            known_encoding = fr.face_encodings(known_image)[0]
            
            
            list_people_encoding.append((known_encoding,filename))
            
        return list_people_encoding

    def find_target_face():
        face_location = fr.face_locations(target_image)
        
        for persons in encode_faces("YOUR DIRECTORY"):
            encoded_face = persons[0]
            filename = persons[1]
            
            
            is_target_face = fr.compare_faces(encoded_face,target_encoding,tolerance=0.5)
            print(f'{is_target_face}{filename}')
            
            if face_location:
                face_number = 0
                for location in face_location:
                    if is_target_face[face_number]:
                        label = filename
                        create_frame(location,label)
                    
                    face_number +=1
                    
                    
    def create_frame(location,label):
        top,right,bottom,left = location
        cv.rectangle(target_image,(left,top),(right,bottom),(145,143,211),2)
        cv.rectangle(target_image,(left,bottom +20),(right,bottom),(145,143,211,cv.FILLED))
        cv.putText(target_image,label , (left + 3,bottom + 14),cv.FONT_HERSHEY_DUPLEX, 0.9, (115,123,152), 1)
        
        
        
    def render_image():
        rgp_img = cv.cvtColor(target_image,cv.COLOR_BGR2RGB)
        resized_img = cv.resize(rgp_img, (500, 500))
        cv.imshow("face", resized_img)
        cv.waitKey(0)
        


    find_target_face()
    render_image()
    
