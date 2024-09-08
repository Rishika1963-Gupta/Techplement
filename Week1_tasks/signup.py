from tkinter import *
import tkinter as tk
from tkinter import messagebox 
import pymysql as mysql
import signin
from PIL import Image,ImageTk

class Register :

    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x1000")
        self.root.configure(bg = "#cdc2c2")
        self.root.attributes("-fullscreen",True)

        def exit(event):
            root.attributes("-fullscreen",False)
            

        self.root.bind("<Escape>",exit)


        self.r_img = Image.open("signin4.png")
        self.sz = (1650,850)
        self.r_img = self.r_img.resize(self.sz)
        self.rimg = ImageTk.PhotoImage(self.r_img)
        self.r_img = tk.Label(root, image = self.rimg)
        self.r_img.place(x=0,y=0)


        self.frame = tk.Frame(root, bg="#d9d9d9" , border = 3 ,relief=tk.GROOVE , bd = 5)
        self.frame.place(x=1000, y=100, width=440, height=600)

        self.state_label = tk.Label(root , text = "SIGN UP" , font=("Arial Narrow" , "20" , "bold") , bd=10)
        self.state_label.place(x = 1165, y = 120)

        self.u_label = tk.Label(root, text = "Username" , font = ("Arial Black" , "15"  ))
        self.u_label.place(x = 1020 , y = 225)
        self.u_entry = tk.Entry(root , bd = 4 , width = 20 , font = ("Arial" , "12" , "bold"))
        self.u_entry.place(x=1020 , y=270)

        self.p_label = tk.Label(root , text = "Password" ,font = ("Arial Black" , "15"))
        self.p_label.place(x = 1020 , y = 325)
        self.p_entry = tk.Entry( root , bd = 4 , width = 30 , show = "*", font = ("Arial" , "12" , "bold"))
        self.p_entry.place(x=1020,y=370)

        self.state_label = tk.Label(root , text = "Confirm Password" ,font = ("Arial Black" , "15"))
        self.state_label.place(x = 1020 , y = 425)
        self.p1_entry = tk.Entry(root , bd = 4 , width = 30 , show = "*" , font = ("Arial" , "12" , "bold"))
        self.p1_entry.place(x=1020,y=470)


        self.login_button = tk.Button(root, text="Register" , font = ("Arial Black" , "15") ,bd = 2,width = 25 , bg = "#004aad", fg = "white" , command = self.connect_database)
        self.login_button.place(x = 1036 ,y = 560)

        self.l2 = Label(root , text = "Back to  " , fg = "black" , bg = "#d9d9d9" , font = ("Aptos Display" , "15", "bold"))
        self.l2.place(x=1225 , y=620)

        self.sign_in = Button(root , width = 6 , text = "SIGN IN" ,font = ("Aptos Display" , "15", "bold" ), border = 2 , bg = "#d9d9d9" , cursor = "hand2" , fg = "black" , command = self.signin_page) 
        self.sign_in.place(x=1314,y=616)



    def connect_database(self):
        unm = self.u_entry.get()
        pwd = self.p_entry.get()
        cpwd = self.p1_entry.get()

        if not unm or not pwd or not cpwd :
            messagebox.showerror("Error" , "All Fields are Required!")
            return
        
        elif pwd!=cpwd:
            messagebox.showerror("Error" , "Passwords do not match!")
            return
    
        else:
            try:
                self.myconn = mysql.connect(host='localhost' ,port = 3306, user = 'root' , password = 'root' , charset="utf8")
                self.cur = self.myconn.cursor()
            except mysql.MySQLError as e:
                messagebox.showerror("error" , "Database Connectivity Issue.Please Try again!")
                print(e)
                return
            
            try:    
                self.qry = 'create database if not exists userdata'
                self.cur.execute(self.qry)
                self.qry = 'use userdata'
                self.cur.execute(self.qry)
                self.qry = 'create table if not exists data(id int auto_increment primary key not null ,username varchar(50) unique key , password varchar(255) , confirm_password varchar(255))'
                self.cur.execute(self.qry)

                self.qry = "select * from data where username=%s"
                self.cur.execute(self.qry,(self.u_entry.get()))

                self.row=self.cur.fetchone()

                if self.row!=None:
                    messagebox.showerror("Error" , "Username Already Exists")

                else:   

                    self.qry = "insert into data (username , password , confirm_password) values (%s,%s,%s)"
                    self.cur.execute(self.qry , (unm,pwd,cpwd))
                    self.myconn.commit()

        
                    self.clear_fields()
                    messagebox.showinfo("Successful" , "Registration is Successful!")


            except mysql.MySQLError as e:
                messagebox.showerror("Error" , f"Sql Error :{str(e)}")
                print(e)
                return
            
            finally:
                self.cur.close()
                self.myconn.close()

        
    def clear_fields(self):
        self.u_entry.delete(0,END)
        self.p_entry.delete(0,END)
        self.p1_entry.delete(0,END)


    def signin_page(self):
        self.root.destroy()
        root = Tk()
        signin.Login(root)
        root.mainloop()

        



if __name__ == "__main__":
    root = tk.Tk()
    app = Register(root)
    root.mainloop()