import os
from tkinter import messagebox
import tkinter
os.chdir('c:\\users\\jivan\\desktop\\test')
while True:    
        for f in os.listdir() :
               if not f.startswith('.'):
                        file_object=open("\\Users\\jivan\\Desktop\\Renamer\\number.txt","r")
                        number=file_object.read()
                        file_object.close()
                        file_name,file_ext=os.path.splitext(f)
                        if file_name[0]!='m':
                                new_name='m '+ str(number)
                                os.rename(f,new_name + ".jpg")
                                number1=int(number)+1
                                file_object=open("\\Users\\jivan\\Desktop\\Renamer\\number.txt","w")
                                file_object.write(str(number1))
                                root = tkinter.Tk()
                                root.withdraw()
                                messagebox.showinfo('Note This',new_name)
                                file_object.close()
                                
