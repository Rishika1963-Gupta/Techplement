#User Registration System
from tkinter import * 
import tkinter as tk
from tkinter import messagebox
import signup
import pymysql as mysql
from PIL import Image,ImageTk

class Login:

    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600")
        self.root.configure(bg = "white")
        self.root.attributes("-fullscreen",True)

       
        def exit(event):
            root.attributes("-fullscreen",False)
            

        self.root.bind("<Escape>",exit)

        #self.root.overrideredirect(1)

        self.l_img = Image.open("signin3.png")
        self.sz = (1600,850)
        self.l_img = self.l_img.resize(self.sz)
        self.limg = ImageTk.PhotoImage(self.l_img)
        self.l_img = tk.Label(root, image = self.limg)
        self.l_img.place(x=0,y=0)



        self.frame = tk.Frame(root, bg="#96e6e9" ,relief=tk.GROOVE , bd = 5 )
        self.frame.place(x=1000, y=100, width=440, height=600)

        self.state_label = tk.Label(root , text = "SIGN IN" , font=("Arial Narrow" , "20" , "bold") , bd=10, bg = "white")
        self.state_label.place(x = 1175, y = 120)

        self.state_label = tk.Label(root, text = "Username" , font = ("Arial Black" , "15"  ))
        self.state_label.place(x = 1020 , y = 255)
        self.u_entry = tk.Entry(root , bd = 2 , width = 15 , fg = "black" , bg = "#fbf4f4" , font = ("Arial Black" , "12") )
        self.u_entry.place(x=1020 , y=320)

        
        self.state_label = tk.Label(root , text = "Password" ,font = ("Arial Black" , "15") , bd = 3)
        self.state_label.place(x = 1020 , y = 405)
        self.p_entry = tk.Entry(root , bd = 2 , width = 15 , fg = "black" , bg = "#fbf4f4" , font = ("Arial Black" , "12") , show= "*" )
        self.p_entry.place(x=1020,y=470)

        self.login_button = tk.Button(root, text="Login" , font = ("Arial Black" , "15") ,bd = 2,width = 25 , bg = "#004aad", fg = "white", command = self.login)
        self.login_button.place(x = 1050 ,y = 530)

        self.l2 = Label(root , text = "Don't have an Account?" , fg = "black" , bg = "#96e6e9" , font = ("Aptos Display" , "13", "bold"))
        self.l2.place(x=1056 , y=620)

        self.sign_up = Button(root , width = 6 , text = "Sign up" ,font = ("Aptos Display" , "15", "bold"), border =0 , bg = "#96e6e9" , cursor = "hand2" , fg = "#004aad" , command = self.signup_page) 
        self.sign_up.place(x=1254,y=613)

    def login(self):
        username = self.u_entry.get()
        password = self.p_entry.get()

        if not username or not password:
            messagebox.showerror("Error" , "All Fields are Required !")
            return
        
           
        else:
            try:
                self.myconn = mysql.connect(host = "localhost" , user = "root" , password = "root" , port= 3306 , charset = "utf8")
                self.cur = self.myconn.cursor()
            except:
                messagebox.showerror("Error" , "Connection is not Established try Again")
                return
            
            self.qry = 'use userdata'
            self.cur.execute(self.qry)
            
            self.qry = "Select * from data where username = %s and password = %s"
            self.cur.execute(self.qry , (self.u_entry.get() , self.p_entry.get()))
            self.row = self.cur.fetchone()
            
            if self.row==None:
                messagebox.showerror("Error" ,"Invalid Username or Password!")
 
            else:
                messagebox.showinfo("Welcome" , "Login Successful!")




    def signup_page(self):
        self.root.destroy()
        root = Tk()
        signup.Register(root)
        root.mainloop()



if __name__ == "__main__":
    root = tk.Tk()
    app=Login(root)
    root.mainloop()


