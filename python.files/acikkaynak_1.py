#IMPORTING ALL REQUIRED MODULES
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from datetime import *
#ESTABLISHING CONNECTIVITY WITH MYSQL
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1311",database="Project")
mycursor=mydb.cursor()
#CREATING ALL REQUIRED TABLES
mycursor.execute("CREATE TABLE Admin (Name CHAR(25) NOT NULL , Username VARCHAR (16) UNIQUE ,
Password VARCHAR (16) NOT NULL )")
mycursor.execute("CREATE TABLE Staff ( Name CHAR(25) NOT NULL , Department CHAR(20) , Post
CHAR(20) , Salary INTEGER NOT NULL , Age INTEGER , Gender CHAR NOT NULL , Mobile_No INTEGER
)")
mycursor.execute("CREATE TABLE Stock (Item_Code VARCHAR(20) UNIQUE , Item_Name VARCHAR(20) ,
Quantity INTEGER , Price_in_Rs INTEGER )")
mycursor.execute("CREATE TABLE Customer (Name CHAR(25) , Address VARCHAR(50) , Mobile_No
INTEGER , Total_Purchase_in_Rs INTEGER , Due_Amount_in_Rs INTEGER )")
mycursor.execute("CREATE TABLE Sales (Date DATE,Total_Sale INTEGER(4))")
#INSERTING VALUES INTO TABLES
#ADMIN TABLE
mycursor.execute("INSERT INTO Admin VALUES ('Anirudh Arora', 'anirudh', '1234') ")
mycursor.execute("INSERT INTO Admin VALUES ('Shubh Goyal', 'shubh', '1234') ")
mycursor.execute("INSERT INTO Admin VALUES ('Naman Mardia', 'naman', '1234') ")
#STAFF TABLE
mycursor.execute("INSERT INTO Staff VALUES ('Ram
Shukla','Finance','Head',15000,42,'M',1111111111)")
mycursor.execute("INSERT INTO Staff VALUES ('Shyam
Sharma','Finance','Cashier',12500,39,'M',1111111112)")
mycursor.execute("INSERT INTO Staff VALUES (' Prakash
Gupta','Stock','Head',13000,35,'M',1111111113)")
mycursor.execute("INSERT INTO Staff VALUES ('Rani
Mahajan','Stock','Assistant',10000,32,'F',1111111114)")
mycursor.execute("INSERT INTO Staff VALUES ('Manoj Singh
','Helper','Helper',5000,32,'M',1111111115)")
mycursor.execute("INSERT INTO Staff VALUES ('Disha
Patel','Helper','Helper',5000,28,'F',1111111116)")
mycursor.execute("INSERT INTO Staff VALUES ('Lakshmi Devi','Supporting
Staff','Peon',3000,42,'F',1111111117)")
#STOCK TABLE
mycursor.execute("INSERT INTO Stock VALUES('10FSTAR','5STAR',500,10)")
mycursor.execute("INSERT INTO Stock VALUES('20FSTAR','5STAR',500,20)")
mycursor.execute("INSERT INTO Stock VALUES('05GEMS','GEMS',1000,5)")
mycursor.execute("INSERT INTO Stock VALUES('10GEMS','GEMS',500,10)")
mycursor.execute("INSERT INTO Stock VALUES('50DETT','DETTOL',150,50)")
mycursor.execute("INSERT INTO Stock VALUES('25ODON','ODONIL',100,25)")
mycursor.execute("INSERT INTO Stock VALUES('30MAGHH','MAGGIE HOTHEAD',750,30)")
mycursor.execute("INSERT INTO Stock VALUES('12MAGG','MAGGIE',1000,12)")
mycursor.execute("INSERT INTO Stock VALUES('30THUP','THUMBS UP',100,30)")
mycursor.execute("INSERT INTO Stock VALUES('80NEXP','NESCAFE EXPRESSO',200,80)")
mycursor.execute("INSERT INTO Stock VALUES('2NESCL','NESCAFE CLASSIC',1500,2)")
#CUSTOMER TABLE
mycursor.execute("INSERT INTO Customer VALUES('Shubh Gupta','85,Ranga
Nagar',1111111111,25000,200)")
mycursor.execute("INSERT INTO Customer VALUES('Shubham Goyal','82,Ranga
Nagar',1111111112,18000,50)")
mycursor.execute("INSERT INTO Customer VALUES('Vijay Singh','96,Ranga
Nagar',1111111113,35000,100)")
mycursor.execute("INSERT INTO Customer VALUES('Sonu Verma','15,Ranga
Nagar',1111111114,24000,0)")
SOURCE CODE 
4
mycursor.execute("INSERT INTO Customer VALUES('Raja Babu','75,Ranga
Nagar',1111111115,12000,500)")
#DECLARATION OF TKINTER WINDOWS
global root , root_main , root_admin , root_stock , root_customer , root_staff , root_inv ,
root_finance
#DECLARATION OF IMAGE VARIABLES
global bg_icon , user_icon , logo_icon , customer , staff , stock , inv , finance , logout ,
bg_icon1
#-----------------------------------ADMIN CORNER---------------------------------------
#REQUIRED FUNCTIONS FOR ADMIN CORNER
def admin_corner(): #FUNCTION FOR CALLING ADMIN CORNER WINDOW
 global root_main , root_admin
 root_main.destroy() #FOR DESTROYING MENU SCREEN ON PRESSING ADMIN CORNER BUTTON
 root_admin = Tk()
 root_admin.title ("SUPERMART")
 root_admin.geometry("1350x700+0+0")
 #DECLARATION OF VARIABLES
 newuser= StringVar()
 newpsd = StringVar()
 cnfpsd = StringVar()
 deluser = StringVar()
 delpsd = StringVar()
 olduser = StringVar()
 oldpsd = StringVar()
 upduser = StringVar()
 updpsd = StringVar()
 newname=StringVar()

 #FUNCTIONS IN ADMIN CORNER
 #TO ADD USER
 def add_user():
 if newuser.get().isalnum() and newpsd.get().isalnum():
 if cnfpsd.get()==newpsd.get():
 add="INSERT INTO admin VALUES('%s','%s','%s')"%
 (newname.get(),newuser.get(),newpsd.get())
 nn,nu,np=newname.get(),newuser.get(),newpsd.get()
 mycursor.execute(add)
 mydb.commit()
 messagebox.showinfo("SUCCESSFUL","User Successfully Added")
 else:
 messagebox.showerror("ERROR!","Password Do Not Match")
 else:
 messagebox.showerror("ERROR!","All Fileds Are Required")

 #TO DELETE USER
 def delete_user():
 mycursor.execute("SELECT Username,Password FROM admin ")
 data=mycursor.fetchall()
 for row in data:
 if deluser.get() == row[0]:
 if delpsd.get() == row[1] :
 delete="DELETE FROM admin WHERE Username='%s'"
%(deluser.get(),)
 mycursor.execute(delete)
 mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!"
, "User Deleted Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Password")
 break
 else:
 messagebox.showerror("ERROR" , "User Does Not Exists")

 #TO UPDATE USER
 def update_user():
 if olduser.get().isalnum() and oldpsd.get().isalnum() and
 upduser.get().isalnum() and updpsd.get().isalnum():
 mycursor.execute("SELECT Username,Password FROM admin ")
 data=mycursor.fetchall()
 for row in data:
 if olduser.get() == row[0]:
5
 if oldpsd.get() == row[1] :
 update='''UPDATE admin SET Username='%s',Password='%s'
WHERE Username='%s' '''%(upduser.get(),
updpsd.get(),olduser.get())
mycursor.execute(update)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!"
, "User Updated Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Password")
 break
 else:
 messagebox.showerror("ERROR" , "User Does Not Exists")
 #FRAMES IN ADMIN CORNER
 #TO ADD USER
 add_user_frame = LabelFrame(root_admin , bg="white" , text="Add User" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 name_user_lbl = Label ( add_user_frame , text="Name ::" ,
 font = ("gill sans mt" , 18 , "bold") , bg="white")
 name_user_lbl.place ( x=100 , y=30)
 new_user_lbl = Label ( add_user_frame , text="New Username ::" ,
 font = ("gill sans mt" , 18 , "bold") , bg="white")
 new_user_lbl.place ( x=100 , y=90)
 new_psd_lbl = Label ( add_user_frame , text="New Password ::" ,
 font = ("gill sans mt" , 18 , "bold") , bg="white")
 new_psd_lbl.place ( x=100 , y=150)
 confirm_psd_lbl = Label ( add_user_frame , text="Confirm Password ::" ,
 font = ("gill sans mt" , 18 , "bold") , bg="white")
 confirm_psd_lbl.place ( x=100 , y=210)
 name_user_ent = Entry ( add_user_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newname)
 name_user_ent.place ( x=475 , y=30)
 new_user_ent = Entry ( add_user_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newuser)
 new_user_ent.place ( x=475 , y=90)
 new_psd_ent = Entry ( add_user_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newpsd)
 new_psd_ent.place ( x=475 , y=150)
 cnf_psd_ent = Entry ( add_user_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = cnfpsd)
 cnf_psd_ent.place ( x=475 , y=210)
 add_btn = Button ( add_user_frame , text = "ADD !" ,font =("gill sans mt",18,"bold"),
 padx=25 , bg="white" ,command=add_user)
 add_btn.place (x=475 , y=270)
 #TO DELETE USER
 delete_user_frame= LabelFrame(root_admin , bg="white" , text="Delete User" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 delete_user_lbl = Label ( delete_user_frame , text="Username ::",
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 delete_user_lbl.place ( x=100 , y=30)
 delete_psd_lbl = Label ( delete_user_frame , text="Password ::",
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 delete_psd_lbl.place ( x=100 , y=100)
 delete_user_ent = Entry ( delete_user_frame , font = ("gill sans mt" , 16 ),
 bd=5 , textvariable = deluser)
 delete_user_ent.place ( x=475 , y=30)
 delete_psd_ent = Entry ( delete_user_frame , font = ("gill sans mt" , 16 ),
 bd=5 , textvariable =delpsd)
 delete_psd_ent.place ( x=475 , y=100)
 delete_btn = Button ( delete_user_frame ,text ="DELETE !",font =("gill sans
 mt",18,"bold"),padx=25 , bg="white" , command = delete_user)
 delete_btn.place (x=475 , y=240)
 #TO UPDATE USER
 update_user_frame= LabelFrame(root_admin , bg="white" , text="Update User" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 old_user_lbl = Label ( update_user_frame , text="Old Username ::" ,
 font = ("gill sans mt" , 15 , "bold") , bg="white")
 old_user_lbl.place ( x=100 , y=20)
 update_user_lbl = Label ( update_user_frame , text="New Username ::" ,
 font = ("gill sans mt" , 15 , "bold") , bg="white")
 update_user_lbl.place ( x=100 , y=70)
6
 old_psd_lbl = Label ( update_user_frame , text="Old Password ::" ,
 font = ("gill sans mt" , 15 , "bold") , bg="white")
 old_psd_lbl.place ( x=100 , y=120)
 update_psd_lbl = Label ( update_user_frame , text="New Password ::" ,
 font = ("gill sans mt" , 15 , "bold") , bg="white")
 update_psd_lbl.place ( x=100 , y=170)
 old_user_ent = Entry ( update_user_frame , font = ("gill sans mt" , 16 ),
 bd=5 , textvariable = olduser)
 old_user_ent.place ( x=475 , y=20)
 update_psd_ent = Entry ( update_user_frame ,font = ("gill sans mt" , 16 ),
 bd=5 , textvariable = upduser)
 update_psd_ent.place ( x=475 , y=70)
 old_psd_ent = Entry ( update_user_frame ,font =("gill sans mt" , 16 ),
 bd=5 , textvariable = oldpsd)
 old_psd_ent.place ( x=475 , y=120)
 update_psd_ent = Entry ( update_user_frame , font = ("gill sans mt" ,16),
 bd=5 , textvariable=updpsd)
 update_psd_ent.place ( x=475 , y=170)
 update_btn = Button ( update_user_frame , text = "UPDATE !" , font = ("gill sans mt" ,
 18 , "bold") , padx=25 , bg="white" , command = update_user )
 update_btn.place (x=475 , y=240)
 #FUNCTION FOR SWAPPING FRAMES
 def swap(frame):
 frame.tkraise()
 for frame in (add_user_frame , delete_user_frame , update_user_frame):
 frame.place (x=200 , y=200)
 #ADMIN CORNER WINDOW
 global bg_icon
 bg_icon=ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl = Label(root_admin, image=bg_icon).pack()

 title = Label (root_admin , text = "ADMIN CORNER" , font=("lucida handwriting"
 , 40 ,"bold"), bg="yellow" , fg="black" , bd=5 , relief = GROOVE)
 title.place (x=0 , y=0 , relwidth=1)
 Add_User = Button (root_admin , text = "Add User" , font=("lucida handwriting"
 , 18 , "bold") , bg="white" , padx=15 , command = lambda: swap(add_user_frame))
 Add_User.place (x=200 , y=100)
 Delete_User = Button (root_admin , text = "Delete User" , font=("lucida handwriting"
 , 18 , "bold") , bg="white" , padx=15 , command = lambda: swap(delete_user_frame))
 Delete_User.place (x=550 , y=100)
 Update = Button (root_admin , text = "Update User" , font=("lucida handwriting"
 , 18 , "bold") , bg="white" , padx=15 , command = lambda: swap(update_user_frame))
 Update.place (x=925 , y=100)

 go_back = Button (root_admin , text = "<<< Go Back" , font=("lucida handwriting"
 , 18 , "bold") , bg="white" , padx=15 , command=Main_Screenadmin )
 go_back.place (x=1100 , y=640)
#FUNCTION TO GO BACK TO MAIN MENU FROM ADMIN CORNER
def Main_Screenadmin():
 global root_admin
 root_admin.destroy()
 Main_Screen()

#--------------------------------------------------CUSTOMER DATA MANAGEMENT-------------------
----------------------------
#REQUIRED FUNCTIONS FOR CUSTOMER
def customer_data():
 global root_customer , root_main
 root_main.destroy()
 root_customer = Tk()
 root_customer.title("SUPERMART")
 root_customer.geometry("1350x700+0+0")
 #DECLARATION OF VARIABLES
 cname=StringVar()
 cadd=StringVar()
 cmob=StringVar()
 delcn=StringVar()
 delcm=StringVar()
 cusname=StringVar()
 cusadd=StringVar()
 cusomob=StringVar()
7
 cusnmob=StringVar()
 cusdamt=StringVar()
 fmob=StringVar()
 #FUNCTIONS IN CUSTOMER DATA MANAGEMENT
 #TO ADD CUSTOMER
 def add_cus():
 add="INSERT INTO customer(Name,Address,Mobile_No) VALUES('%s','%s','%s')"
 %(cname.get(),cadd.get(),cmob.get())
 mycursor.execute(add)
 mydb.commit()
 messagebox.showinfo("SUCCESSFUL","Customer Successfully Added")

 #TO DELETE CUSTOMER
 def del_cus():
 mycursor.execute("SELECT Name,Mobile_No FROM customer")
 data=mycursor.fetchall()
 for row in data:
 if delcn.get()==row[0]:
 if delcm.get() == str(row[1]) :
 delete="DELETE FROM customer WHERE Mobile_No='%s'"%(delcm.get(),)
mycursor.execute(delete)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!" ,
 "Customer Deleted Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Mobile No.")
 break
 else:
 messagebox.showerror("ERROR" , "Customer Does Not Exists")
 #TO UPDATE CUSTOMER
 def upd_cus():
 if cusname.get().isalnum() and cusadd.get().isalnum() and
 cusomob.get().isalnum() and cusnmob.get().isalnum() and
 cusdamt.get().isalnum():
 mycursor.execute("SELECT Name,Mobile_No FROM customer ")
 data=mycursor.fetchall()
 for row in data:
 if cusname.get() == row[0]:
 if cusomob.get() ==str(row[1]):
 update='''UPDATE customer SET Mobile_No='%s',
Address='%s',Due_Amount_in_Rs='%s' WHERE (Name='%s'
AND Mobile_No='%s')'''%(cusnmob.get(),
cusadd.get(),cusdamt.get(),cusname.get(),cusomob.get())
mycursor.execute(update)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!" ,
 "Customer Updated Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Mobile Number")
 break
 else:
 messagebox.showerror("ERROR" , "Customer Does Not Exists")
 else:
 messagebox.showerror("ERROR","All Field Are Required")

 #TO FIND CUSTOMER
 def find_cus():
 if fmob.get().isalnum():
 mycursor.execute('''SELECT Name,Address,Mobile_No,
 Total_Purchase_in_Rs,Due_Amount_in_Rs FROM customer ''')
 data=mycursor.fetchall()
 for row in data:
 if fmob.get() ==str(row[2]):
 fname_label = Label(find_customer_frame , text ="NAME",
font = ("gill sans mt" , 14 , "bold"))
 fname_label.place(x=100 , y=150)
 fadd_label = Label(find_customer_frame , text ="ADDRESS",
 font = ("gill sans mt" , 14 , "bold"))
 fadd_label.place(x=100 , y=200)
 ftp_label = Label(find_customer_frame , text ="TOTAL PURCHASE",
 font = ("gill sans mt" , 14 , "bold"))
 ftp_label.place(x=100 , y=250)
 fda_label = Label(find_customer_frame , text ="DUE AMOUNT",
8
 font = ("gill sans mt" , 14 , "bold"))
 fda_label.place(x=100 , y=300)
 fname_label = Label(find_customer_frame , text =row[0],font =
("gill sans mt" , 14 , "bold"),bg="white",width=50,anchor=W)
 fname_label.place(x=400 , y=150)
 fadd_label = Label(find_customer_frame , text =row[1],font =
("gill sans mt" , 14 , "bold"),bg="white",width=50,anchor=W )
 fadd_label.place(x=400 , y=200)
 ftp_label = Label(find_customer_frame , text =row[3],font =
 ("gill sans mt" , 14 , "bold"),bg="white",width=50,anchor=W )
 ftp_label.place(x=400 , y=250)
 fda_label = Label(find_customer_frame , text =row[4],font =
("gill sans mt" , 14 , "bold"),bg="white",width=50,anchor=W)
 fda_label.place(x=400 , y=300)
 break
 else:
 messagebox.showerror("ERROR",'''Either Mobile No. Not Entered Correctly
 \n OR \nCustomer Does Not Exists''')

 #FRAMES IN CUSTOMER DATA MANAGMENT
 # TO ADD CUSTOMER
 add_customer_frame = LabelFrame(root_customer, bg="white",text="Add Customer",
 font=("agency fb", 29, "bold"), width=950,height=400)
 new_name_lbl = Label(add_customer_frame, text="Name ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 new_name_lbl.place(x=100, y=30)
 new_add_lbl = Label(add_customer_frame, text="Address ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 new_add_lbl.place(x=100, y=100)
 new_mob_lbl = Label(add_customer_frame, text="Mobile No. ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 new_mob_lbl.place(x=100, y=170)
 new_name_ent = Entry(add_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cname)
 new_name_ent.place(x=475, y=30)
 new_add_ent = Entry(add_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cadd)
 new_add_ent.place(x=475, y=100)
 new_mob_ent = Entry(add_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cmob)
 new_mob_ent.place(x=475, y=170)

 add_btn = Button(add_customer_frame, text="ADD !", font=("gill sans mt",
 18, "bold"), padx=25, bg="white",command=add_cus)
 add_btn.place(x=475, y=240)
 #TO DELETE CUSTOMER
 delete_customer_frame = LabelFrame(root_customer, bg="white",
 text="Delete Customer", font=("agency fb", 29, "bold"),width=950,height=400)
 delete_customer_lbl = Label(delete_customer_frame, text="Name ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 delete_customer_lbl.place(x=100, y=30)
 delete_customer_lbl = Label(delete_customer_frame, text="Mobile No. ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 delete_customer_lbl.place(x=100, y=100)
 delete_customer_ent = Entry(delete_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=delcn)
 delete_customer_ent.place(x=475, y=30)
 delete_customer_ent = Entry(delete_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=delcm)
 delete_customer_ent.place(x=475, y=100)

 delete_btn = Button(delete_customer_frame, text="DELETE !",
 font=("gill sans mt", 18, "bold"), padx=25, bg="white",command=del_cus)
 delete_btn.place(x=475, y=240)
 # TO UPDATE CUSTOMER
 update_customer_frame=LabelFrame(root_customer,bg="white",text="Update Customer"
 , font=("agency fb", 29, "bold"),width=950,height=400)
 name_customer_lbl = Label(update_customer_frame, text="Name ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 name_customer_lbl.place(x=100, y=20)
 add_customer_lbl = Label(update_customer_frame, text="Address ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 add_customer_lbl.place(x=100, y=70)
 oldmob_customer_lbl = Label(update_customer_frame, text="Old Mobile No. ::",
 font=("gill sans mt", 15, "bold"), bg="white")
9
 oldmob_customer_lbl.place(x=100, y=120)
 newmob_customer_lbl = Label(update_customer_frame, text="New Mobile No. ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 newmob_customer_lbl.place(x=100, y=170)
 dueamt_customer_lbl = Label(update_customer_frame, text="Due Amount ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 dueamt_customer_lbl.place(x=100, y=220)
 name_customer_ent = Entry(update_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cusname)
 name_customer_ent.place(x=475, y=20)
 add_customer_ent = Entry(update_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cusadd)
 add_customer_ent.place(x=475, y=70)
 oldmob_customer_ent = Entry(update_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cusomob)
 oldmob_customer_ent.place(x=475, y=120)
 newmob_customer_ent = Entry(update_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cusnmob)
 newmob_customer_ent.place(x=475, y=170)
 dueamt_customer_ent = Entry(update_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=cusdamt)
 dueamt_customer_ent.place(x=475, y=220)
 update_btn = Button(update_customer_frame, text="UPDATE !",
 font=("gill sans mt", 18, "bold"), padx=25, bg="white",command=upd_cus)
 update_btn.place(x=475, y=275)
 #TO FIND CUSTOMER
 find_customer_frame = LabelFrame(root_customer, bg="white",text="Find Customer",
 font=("agency fb", 29, "bold"), width=950, height=400)
 find_customer_lbl = Label(find_customer_frame, text="Mobile No. ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 find_customer_lbl.place(x=100, y=30)
 find_customer_ent = Entry(find_customer_frame, font=("gill sans mt", 16),
 bd=5,textvariable=fmob)
 find_customer_ent.place(x=475, y=30)
 find_btn = Button(find_customer_frame, text="FIND !",
 font=("gill sans mt", 18, "bold"), padx=25, bg="white",command=find_cus)
 find_btn.place(x=500, y=80)
 # FUNCTIONS FOR SWAPPING FRAMES
 def swap(frame):
 frame.tkraise()
 for frame in (add_customer_frame, delete_customer_frame,
 update_customer_frame,find_customer_frame):
 frame.place(x=200, y=200)
 #CUSTOMER DATA MANAGEMENT WINDOW
 global bg_icon
 bg_icon = ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl = Label(root_customer, image=bg_icon).pack()

 title = Label(root_customer, text="Customer Data", font=("lucida handwriting",
 40, "bold"), bg="yellow", fg="black", bd=5 , relief=GROOVE)
 title.place(x=0, y=0, relwidth=1)
 Add_Customer = Button(root_customer,text="Add Customer",font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(add_customer_frame))
 Add_Customer.place(x=50, y=100)
 Delete_Customer = Button(root_customer,text="Delete Customer",
 font=("lucida handwriting", 18, "bold"), bg="white", padx=15,
 command=lambda: swap(delete_customer_frame))
 Delete_Customer.place(x=375, y=100)
 Update_Customer = Button(root_customer,text="Update Customer",
 font=("lucida handwriting", 18, "bold"), bg="white", padx=15,
 command=lambda: swap(update_customer_frame))
 Update_Customer.place(x=700, y=100)
 Find = Button(root_customer, text="Find Customer", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(find_customer_frame))
 Find.place(x=1050, y=100)
 go_back = Button(root_customer, text="<<< Go Back", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=main_screencustomer)
 go_back.place(x=1100, y=640)
#FUNCTION TO GO BACK TO MAIN MENU FROM CUSTOMER MANAGEMENT
10
def main_screencustomer():
 global root_customer
 root_customer.destroy()
 Main_Screen()
#---------------------------------STAFF DATA MANAGEMENT--------------------------------------

#REQUIRED FUNCTIONS FOR STAFF DATA MANAGEMENT
def staff_data():
 global root_staff,root_main
 root_main.destroy()
 root_staff = Tk()
 root_staff.title("SUPERMART")
 root_staff.geometry("1350x700+0+0")
 # DECLARATION OF VARIABLES
 sn = StringVar()
 sd = StringVar()
 sp = StringVar()
 ss = StringVar()
 sa = StringVar()
 sg = StringVar()
 sm = StringVar()
 deln=StringVar()
 delm=StringVar()
 sname=StringVar()
 somob=StringVar()
 snpos=StringVar()
 snage=StringVar()
 snmob=StringVar()
 snsal=StringVar()
 fsmob=StringVar()

 #FUNCTIONS IN STAFF DATA MANAGEMENT
 #TO ADD STAFF
 def add_staff():
 if sn.get()=="" or sd.get()=="" or sp.get()=="" or ss.get()=="" or
 sa.get()=="" or sg.get()=="" or sm.get()=="" :
 messagebox.showerror("ERROR !" , "All fields are mandatory")
 else :
 add = "INSERT INTO staff VALUES ('%s','%s','%s',%s,%s,'%s',%s)"
 %(sn.get(),sd.get(),sp.get(),ss.get(),sa.get(),sg.get(),sm.get())
 mycursor.execute(add)
 mydb.commit()
 messagebox.showinfo("SUCCESSFUL !" , "Staff member added successfully !")

 #TO DELETE-STAFF
 def del_staff():
 mycursor.execute("SELECT Name,Mobile_No FROM staff")
 data=mycursor.fetchall()
 for row in data:
 if deln.get()==row[0]:
 if delm.get() == str(row[1]) :
 delete="DELETE FROM staff WHERE Mobile_No='%s'"%(delm.get(),)
mycursor.execute(delete)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!" ,
 "Staff Deleted Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Mobile No.")
 break
 else:
 messagebox.showerror("ERROR" , "Staff Member Does Not Exists")

 #TO UPDATE STAFF
 def upd_staff():
 if sname.get().isalnum() and somob.get().isalnum() and snpos.get().isalnum()
 and snsal.get().isalnum() and snage.get().isalnum() and snmob.get().isalnum():
 mycursor.execute("SELECT Name,Mobile_No FROM staff ")
 data=mycursor.fetchall()
 for row in data:
 if sname.get() == row[0]:
 if somob.get() ==str(row[1]):
 update="UPDATE staff SET Post='%s',Salary=%s,Age=%s,
 Mobile_No=%s WHERE (Name='%s' AND Mobile_No=%s)"%(snpos.get(),
 snsal.get(),snage.get(),snmob.get(),sname.get(),somob.get())
11
 mycursor.execute(update)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!" ,
 "Staff Updated Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Mobile Number")
 break
 else:
 messagebox.showerror("ERROR" , "Staff Does Not Exists")
 else:
 messagebox.showerror("ERROR","All Field Are Required")

 #TO FIND STAFF
 def find_sta():
 if fsmob.get().isalnum():
 mycursor.execute("SELECT Name,Department,Post,Salary,Age,
 Gender,Mobile_No FROM staff ")
 data=mycursor.fetchall()
 for row in data:
 if fsmob.get() ==str(row[6]):
 n_label = Label(find_staff_frame, text ="NAME :",
font = ("gill sans mt" , 14 , "bold"))
 n_label.place(x=100 , y=150)
 d_label = Label(find_staff_frame , text ="DEPARTMENT :",
font = ("gill sans mt" , 14 , "bold"))
 d_label.place(x=100 , y=200)
 p_label = Label(find_staff_frame , text ="POST :",
font = ("gill sans mt" , 14 , "bold"))
 p_label.place(x=100 , y=250)
 s_label = Label(find_staff_frame , text ="SALARY :",
font = ("gill sans mt" , 14 , "bold"))
 s_label.place(x=100 , y=300)
 a_label = Label(find_staff_frame , text ="AGE :",
font = ("gill sans mt" , 14 , "bold"))
 a_label.place(x=600 , y=150)
 g_label = Label(find_staff_frame , text ="GENDER :",
 font = ("gill sans mt" , 14 , "bold"))
 g_label.place(x=600 , y=200)

n_label = Label(find_staff_frame,text =row[0],font=("gill sans mt"
 , 14 , "bold"),bg="white",width=20,anchor=W)
 n_label.place(x=300 , y=150)
 d_label = Label(find_staff_frame,text =row[1],font=("gill sans mt"
 , 14 , "bold"),bg="white",width=15,anchor=W )
 d_label.place(x=300 , y=200)
 p_label = Label(find_staff_frame'text =row[2],font=("gill sans mt"
, 14 , "bold"),bg="white",width=15,anchor=W )
 p_label.place(x=300 , y=250)
 s_label = Label(find_staff_frame,text =row[3],font=("gill sans mt"
 , 14 , "bold"),bg="white",width=10,anchor=W)
 s_label.place(x=300 , y=300)
 a_label = Label(find_staff_frame,text =row[4],font=("gill sans mt"
 , 14 , "bold"),bg="white",width=3,anchor=W )
 a_label.place(x=800 , y=150)
 g_label = Label(find_staff_frame,text =row[5],font=("gill sans mt"
 , 14 , "bold"),bg="white",width=2,anchor=W)
 g_label.place(x=800 , y=200)
 break
 else:
 messagebox.showerror("ERROR", '''Either Mobile No. Not Entered Correctly \n
 OR \nStaff Does Not Exists''')
 #FRAMES IN STAFF DATA MANAGEMENT
 # TO ADD STAFF
 add_staff_frame = LabelFrame(root_staff, bg="white", text="Add Staff",
 font=("agency fb", 29, "bold"), width=950, height=400)
 name_lbl = Label(add_staff_frame, text="New Username ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 name_lbl.place(x=100, y=10)
 dep_lbl = Label(add_staff_frame, text="Department ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 dep_lbl.place(x=100, y=55)
 post_lbl = Label(add_staff_frame, text="Post ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 post_lbl .place(x=100, y=100)
 sal_lbl = Label(add_staff_frame, text="Salaray ::",
12
 font=("gill sans mt", 20, "bold"), bg="white")
 sal_lbl.place(x=100, y=145)
 age_lbl = Label(add_staff_frame, text="Age ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 age_lbl.place(x=100, y=190)
 gen_lbl = Label(add_staff_frame, text="Gender{M/F/O} ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 gen_lbl.place(x=100, y=235)
 mob_lbl = Label(add_staff_frame, text="Mobile No. ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 mob_lbl.place(x=100, y=280)
 name_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sn)
 name_ent.place(x=475, y=10)
 dep_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sd)
 dep_ent.place(x=475, y=55)
 post_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sp)
 post_ent.place(x=475, y=100)
 sal_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = ss)
 sal_ent.place(x=475, y=145)
 age_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sa)
 age_ent.place(x=475, y=190)
 gen_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sg)
 gen_ent.place(x=475, y=235)
 mob_ent = Entry(add_staff_frame, font=("gill sans mt", 16),
 bd=5 , textvariable = sm)
 mob_ent.place(x=475, y=280)
 add_btn = Button(add_staff_frame, text="ADD !", font=("gill sans mt",
 18, "bold"),padx=25, bg="white" , command = add_staff)
 add_btn.place(x=750, y=135)

 # TO DELETE STAFF
 delete_staff_frame = LabelFrame(root_staff, bg="white", text="Delete Staff",
 font=("agency fb", 29, "bold"),width=950,height=400)
 dname_staff_lbl = Label(delete_staff_frame, text="Name ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 dname_staff_lbl.place(x=100, y=30)
 dmob_staff_lbl = Label(delete_staff_frame, text="Mobile No. ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 dmob_staff_lbl.place(x=100, y=100)
 dname_staff_ent = Entry(delete_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=deln)
 dname_staff_ent.place(x=475, y=30)
 dmob_staff_ent = Entry(delete_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=delm)
 dmob_staff_ent.place(x=475, y=100)

 delete_btn = Button(delete_staff_frame, text="DELETE !",
 font=("gill sans mt", 18, "bold"), padx=25, bg="white",command=del_staff)
 delete_btn.place(x=475, y=240)
 # TO UPDATE STAFF
 update_staff_frame = LabelFrame(root_staff, bg="white", text="Update Staff",
 font=("agency fb", 29, "bold"),width=950,height=400)
 name_staff_lbl = Label(update_staff_frame, text="Name ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 name_staff_lbl.place(x=100, y=20)
 post_staff_lbl = Label(update_staff_frame, text="Post ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 post_staff_lbl.place(x=100, y=270)
 sal_staff_lbl = Label(update_staff_frame, text="Salary ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 sal_staff_lbl.place(x=100, y=120)
 age_staff_lbl = Label(update_staff_frame, text="Age ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 age_staff_lbl.place(x=100, y=170)
 omob_staff_lbl = Label(update_staff_frame, text="Old Mobile_No ::",
 font=("gill sans mt", 15, "bold"), bg="white")
 omob_staff_lbl.place(x=100, y=70)
 nmob_staff_lbl = Label(update_staff_frame, text="New Mobile_No ::",
 font=("gill sans mt", 15, "bold"), bg="white")
13
 nmob_staff_lbl.place(x=100, y=220)
 name_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=sname)
 name_staff_ent.place(x=475, y=20)
 post_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=snpos)
 post_staff_ent.place(x=475, y=270)
 sal_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=snsal)
 sal_staff_ent.place(x=475, y=120)
 age_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=snage)
 age_staff_ent.place(x=475, y=170)
 omob_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=somob)
 omob_staff_ent.place(x=475, y=70)
 nmob_staff_ent = Entry(update_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=snmob)
 nmob_staff_ent.place(x=475, y=220)
 update_btn = Button(update_staff_frame, text="UPDATE !",
 font=("gill sans mt", 18, "bold"), padx=25, bg="white",command=upd_staff)
 update_btn.place(x=735, y=135)
 # TO FIND STAFF
 find_staff_frame = LabelFrame(root_staff, bg="white", text="Find Staff",
 font=("agency fb", 29, "bold"), width=950 , height=400)
 find_staff_lbl = Label(find_staff_frame, text="Mobile_No ::",
 font=("gill sans mt", 20, "bold"), bg="white")
 find_staff_lbl.place(x=100, y=30)
 find_staff_ent = Entry(find_staff_frame, font=("gill sans mt", 16),
 bd=5,textvariable=fsmob)
 find_staff_ent.place(x=475, y=30)
 find_btn = Button(find_staff_frame, text="FIND !", font=("gill sans mt",
 18, "bold"), padx=25, bg="white",command=find_sta)
 find_btn.place(x=475, y=80)
 # FUNCTIONS FOR SWAPPING FRAMES
 def swap(frame):
 frame.tkraise()
 for frame in (add_staff_frame, delete_staff_frame, update_staff_frame,find_staff_frame):
 frame.place(x=200, y=200)
 #STAFF DATA MANAGEMENT WINDOW
 global bg_icon
 bg_icon = ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl = Label(root_staff, image=bg_icon).pack()

 title = Label(root_staff, text="Staff Data", font=("lucida handwriting",
 40, "bold"), bg="yellow", fg="black", bd=5, relief=GROOVE)
 title.place(x=0, y=0, relwidth=1)
 Add_User = Button(root_staff, text="Add Staff", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(add_staff_frame))
 Add_User.place(x=100, y=100)
 Delete_User = Button(root_staff, text="Delete Staff", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(delete_staff_frame))
 Delete_User.place(x=400, y=100)
 Update = Button(root_staff, text="Update Staff", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(update_staff_frame))
 Update.place(x=750, y=100)
 Find = Button(root_staff, text="Find Staff", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15, command=lambda: swap(find_staff_frame))
 Find.place(x=1100, y=100)
 go_back = Button(root_staff, text="<<< Go Back", font=("lucida handwriting",
 18, "bold"), bg="white", padx=15 , command=main_screenstaff)
 go_back.place(x=1100, y=640)
#FUNCTION TO GO BACK TO MAIN MENU FROM STAFF DATA MANAGEMENT
def main_screenstaff():
 global root_staff
 root_staff.destroy()
 Main_Screen()
#---------------------------FINANCE DATA MANAGEMENT------------------------------
14
#REQUIRED FUNCTIONS FOR FINANCE DATA MANAGEMENT
def Finance_Management():
 global root_finance , root_main
 root_main.destroy()
 root_finance=Tk()
 root_finance.title ("Finance Management")
 root_finance.geometry("1350x700+0+0")
 #FINANCE DATA MANAGEMENT WINDOW
 global bg_icon
 bg_icon=ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl=Label(root_finance,image=bg_icon).pack()

 title = Label (root_finance , text = "Account Management" ,
 font=("lucida handwriting" , 40 ,"bold"), bg="yellow" , fg="black"
 , bd=5 , relief = GROOVE)
 title.place (x=0 , y=0 , relwidth=1)
 Finance_Frame=Frame(root_finance,bg="white")
 Finance_Frame.place(x=525,y=150)
 go_back = Button (root_finance , text = " <<< Go Back" ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command=Main_Screenfinance)
 go_back.place (x=1100 , y=640)
 #FRAME IN FINANCE DATA MANAGEMENT
 frame1=LabelFrame(root_finance,bg="white",text="Monthly Account",
 font = ("agency fb" , 29 , "bold"),width=1000,height=400)
 frame1.place(x=175,y=175)
 #LABELS
 acc_ts_lbl = Label (frame1 , text="Today's Sale ::" ,
 font = ("gill sans mt" , 20 , "bold") )
 acc_ts_lbl.place ( x=200 , y=25)
 acc_ms_lbl = Label (frame1 , text="Monthly Sale ::" ,
 font = ("gill sans mt" , 20 , "bold") )
 acc_ms_lbl.place ( x=200 , y=100)
 acc_msal_lbl = Label (frame1 , text="Monthly Salary ::" ,
 font = ("gill sans mt" , 20 , "bold") )
 acc_msal_lbl.place ( x=200 , y=175)
 #TO SHOW TODAY'S SALE
 salinf="SELECT * FROM sales WHERE Date='%s'"%(datetime.now().date())
 mycursor.execute(salinf)
 data=mycursor.fetchone()
 if data is None:
 acc_t_lbl = Label (frame1 , text= "0" , font = ("gill sans mt" , 20 )
 ,borderwidth=5, relief="raised", width=10 ,anchor="center",bg="white")
 acc_t_lbl.place ( x=460 , y=25)
 else :
 acc_t_lbl = Label (frame1 , text=data[1] , font = ("gill sans mt" , 20 )
 ,borderwidth=5, relief="raised", width=10 ,anchor="center",bg="white")
 acc_t_lbl.place ( x=460 , y=25)
 #TO SHOW MONTHLY SALE
 salinf="SELECT * FROM sales WHERE Date LIKE '_____%s___'"%(str(datetime.now().date())[5:7])
 mycursor.execute(salinf)
 data=mycursor.fetchall()
 tamt=0
 for row in data:
 tamt=tamt+row[1]
 acc_m_lbl = Label (frame1 , text=tamt , font = ("gill sans mt" , 20 )
 ,borderwidth=5, relief="raised", width=10 ,anchor="center",bg="white")
 acc_m_lbl.place ( x=460 , y=100)
 #TO SHOW MONTHLY SALARY OF STAFF
 salin="SELECT Salary FROM staff"
 mycursor.execute(salin)
 data=mycursor.fetchall()
 tsal=0
 for row in data:
 tsal=tsal+row[0]
 acc_ms_lbl = Label (frame1 , text=tsal , font = ("gill sans mt" , 20 )
 ,borderwidth=5, relief="raised", width=10 ,anchor="center",bg="white")
 acc_ms_lbl.place ( x=460 , y=175)
#FUNCTION TO GO BACK TO MAIN MENU FROM FINANCE DATA MANAGEMENT
def Main_Screenfinance():
 global root_finance
 root_finance.destroy()
 Main_Screen()
15
#-------------------------------STOCK MANAGEMENT-----------------------------------------
#REQUIRED FUNCTIONS FOR STOCK MANAGEMENT
def stock_management():
 global root_stock , root_main
 root_main.destroy()
 root_stock=Tk()
 root_stock.title ("Stock Management")
 root_stock.geometry("1350x700+0+0")

 #DECLARATION OF VARIABLES
 newcode = StringVar()
 newname=StringVar()
 newprice=StringVar()
 newquantity = StringVar()
 delname = StringVar()
 delprice = StringVar()
 findstock= StringVar()
 ucode= StringVar()
 uprice=StringVar()
 uqua=StringVar()

 #FUNCTIONS IN STOCK MANAGEMENT
 #TO ADD STOCK
 def add_stock():
 if newname.get()=="" or newcode.get()=="" or newquantity.get()==""
 or newprice.get()=="":
 messagebox.showerror("ERROR !" , "All fields are mandatory")
 else :
 add = "INSERT INTO stock VALUES ('%s','%s',%s,%s)"%(newcode.get(),
 newname.get(),newquantity.get(),newprice.get())
 mycursor.execute(add)
 mydb.commit()
 messagebox.showinfo("SUCCESSFUL !" , "Item added successfully !")

 #TO DELETE STOCK
 def del_stock():
 mycursor.execute("SELECT Item_Name,Price_in_Rs FROM stock")
 data=mycursor.fetchall()
 for row in data:
 if delname.get()==row[0]:
 if delprice.get() == str(row[1]) :
 delete="DELETE FROM stock WHERE Price_in_Rs='%s'"
%(delprice.get(),)
mycursor.execute(delete)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!" ,
 "Item Deleted Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Item Does Not Exists")
 break
 else:
 messagebox.showerror("ERROR" , "Item Does Not Exists")

 #TO UPDATE STOCK
 def upd_stock():
 if ucode.get().isalnum() and uprice.get().isalnum() and uqua.get().isalnum():
 mycursor.execute("SELECT Item_Code FROM stock ")
 data=mycursor.fetchall()
 for row in data:
 if ucode.get() ==row[0]:
 update='''UPDATE stock SET Quantity='%s',Price_in_Rs=%s
WHERE Item_Code='%s''''
%(uqua.get(),uprice.get(),ucode.get())
mycursor.execute(update)
mydb.commit()
response = messagebox.showinfo("SUCCESSFUL!"
, "Stock Updated Successfully!")
break
 else :
 messagebox.showerror("ERROR" , "Item Does Not Exists")
 else:
 messagebox.showerror("ERROR","All Field Are Required")

 #TO FIND STOCK
 def find_stock():
16
 if findstock.get().isalnum():
 mycursor.execute("SELECT Item_Code,Item_Name,Quantity,Price_in_Rs FROM stock ")
 data=mycursor.fetchall()
 for row in data:
 if findstock.get() ==row[0]:
 code_label = Label(find_stock_frame , text ="CODE",
font = ("gill sans mt" , 14 , "bold"))
 code_label.place(x=100 , y=140)
 name_label = Label(find_stock_frame , text ="NAME",
font = ("gill sans mt" , 14 , "bold") )
 name_label.place(x=300 , y=140)
 qty_label = Label(find_stock_frame , text ="QUANTITY",
 font = ("gill sans mt" , 14 , "bold") )
 qty_label.place(x=500 , y=140)
 prc_label = Label(find_stock_frame , text ="PRICE",
font = ("gill sans mt" , 14 , "bold") )
 prc_label.place(x=750 , y=140)
 icode_label = Label(find_stock_frame , text =row[0],
 font = ("gill sans mt" ,14, "bold"),width=10,anchor=W,bg="white")
 icode_label.place(x=100 , y=180)
 iname_label = Label(find_stock_frame , text =row[1],
font = ("gill sans mt" ,14, "bold"),width=20,anchor=W,bg="white" )
 iname_label.place(x=300 , y=180)
 iqty_label = Label(find_stock_frame , text =row[2],
font = ("gill sans mt" ,14, "bold"),width=10,anchor=W,bg="white" )
 iqty_label.place(x=500 , y=180)
 iprc_label = Label(find_stock_frame , text =row[3],
 font = ("gill sans mt" ,14, "bold"),width=5,anchor=W,bg="white" )
 iprc_label.place(x=750 , y=180)
 break
 else:
 messagebox.showerror("ERROR",'''Either Name Not Entered Correctly
 \n OR \nItem Does Not Exists''')

 #FRAMES IN STOCK MANAGEMENT
 #TO DELETE STOCK
 delete_stock_frame= LabelFrame(root_stock , bg="white" ,
 text="Delete Stock" ,font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 delete_name_lbl = Label ( delete_stock_frame , text="Name ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 delete_name_lbl.place ( x=100 , y=30)
 delete_price_lbl = Label ( delete_stock_frame , text="Price ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 delete_price_lbl.place ( x=100 , y=100)
 delete_name_ent = Entry ( delete_stock_frame ,
 font = ("gill sans mt" , 16 ) , bd=5 , textvariable = delname)
 delete_name_ent.place ( x=475 , y=30)
 delete_price_ent = Entry ( delete_stock_frame ,
 font = ("gill sans mt" , 16 ) , bd=5 , textvariable =delprice)
 delete_price_ent.place ( x=475 , y=100)

 delete_btn = Button ( delete_stock_frame , text = "DELETE !" , font = ("gill sans mt",
 18 , "bold") , padx=25 , bg="white" ,command=del_stock)
 delete_btn.place (x=475 , y=240)

 #TO ADD STOCK
 add_stock_frame = LabelFrame(root_stock , bg="white" , text="Add Stock" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 new_price_lbl = Label ( add_stock_frame , text="Price ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 new_price_lbl.place ( x=100 , y=170)
 new_quantity_lbl = Label ( add_stock_frame , text="Quantity ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 new_quantity_lbl.place ( x=100 , y=120)
 new_ic_lbl = Label ( add_stock_frame , text="Item Code ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 new_ic_lbl.place ( x=100 , y=20)
 new_name_lbl = Label ( add_stock_frame , text="Name ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 new_name_lbl.place ( x=100 , y=70)
 new_ic_ent = Entry ( add_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newcode)
 new_ic_ent.place ( x=475 , y=20)
 new_name_ent = Entry ( add_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newname)
 new_name_ent.place ( x=475 , y=70)
 new_quantity_ent = Entry ( add_stock_frame , font = ("gill sans mt" , 16 ) ,
17
 bd=5 , textvariable = newquantity)
 new_quantity_ent.place ( x=475 , y=120)
 new_price_ent = Entry ( add_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = newprice)
 new_price_ent.place ( x=475 , y=170)

 add_stock_btn = Button ( add_stock_frame , text = "ADD !" , font = ("gill sans mt"
 , 18 , "bold") , padx=25 , bg="white" ,command=add_stock)
 add_stock_btn.place (x=475 , y=240)
 #TO FIND STOCK
 find_stock_frame = LabelFrame(root_stock , bg="white" , text="Find Stock" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 iname_stock_lbl = Label( find_stock_frame , text="Item Code ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 iname_stock_lbl.place ( x=100 , y=20)
 iname_stock_ent = Entry (find_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = findstock)
 iname_stock_ent.place ( x=475 , y=20)

 find_stock_btn = Button ( find_stock_frame , text = "FIND !" ,
 font = ("gill sans mt" , 18 , "bold") , padx=25 , bg="white",command=find_stock)
 find_stock_btn.place (x=475 , y=70)

 #TO UPDATE STOCK
 update_stock_frame = LabelFrame(root_stock , bg="white" , text="UPDATE Stock" ,
 font=("agency fb" , 29 ,"bold") , width = 950 , height=400)
 code_stock_lbl = Label ( update_stock_frame , text="Code ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 code_stock_lbl.place ( x=100 , y=30)
 price_stock_lbl = Label ( update_stock_frame , text=" Price ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 price_stock_lbl.place ( x=100 , y=100)
 qua_stock_lbl = Label ( update_stock_frame , text=" Quantity ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 qua_stock_lbl.place ( x=100 , y=170)
 code_stock_ent = Entry ( update_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = ucode)
 code_stock_ent.place ( x=475 , y=30)
 price_stock_ent = Entry ( update_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = uprice)
 price_stock_ent.place ( x=475 , y=100)
 qua_stock_ent = Entry ( update_stock_frame , font = ("gill sans mt" , 16 ) ,
 bd=5 , textvariable = uqua)
 qua_stock_ent.place ( x=475 , y=170)

 update_stock_btn = Button ( update_stock_frame , text = "UPDATE !" ,
 font = ("gill sans mt" , 18 , "bold") , padx=25 , bg="white",command=upd_stock)
 update_stock_btn.place (x=475 , y=240)

 #FUNCTION TO SWAP FRAMES
 def swap(frame):
 frame.tkraise()
 for frame in (add_stock_frame , delete_stock_frame ,
 find_stock_frame , update_stock_frame):
 frame.place (x=200 , y=200)

 #STOCK MANAGEMENT WINDOW
 global bg_icon
 bg_icon=ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl=Label(root_stock,image=bg_icon).pack()
 title = Label (root_stock , text = "Stock Management" , font=("lucida handwriting",
 40 ,"bold"), bg="yellow" ,fg="black" , bd=5 , relief = GROOVE)
 title.place (x=0 , y=0 , relwidth=1)
 Stock_Frame=Frame(root_stock,bg="white")
 Stock_Frame.place(x=525,y=150)
 Add_Stock = Button (root_stock , text = "Add Stock" , font=("lucida handwriting" ,
 18 , "bold") , bg="white" , padx=15 ,command = lambda: swap(add_stock_frame) )
 Add_Stock.place (x=150 , y=125)
 delete_stock_but = Button (root_stock,text = "Delete Stock",font=("lucida handwriting",
 18 , "bold") , bg="white" , padx=15, command = lambda: swap(delete_stock_frame) )
 delete_stock_but.place (x=425 , y=125)
 Find_Stock = Button (root_stock,text = "Find Stock" , font=("lucida handwriting" ,
 18 , "bold") , bg="white" , padx=15, command = lambda: swap(find_stock_frame))
 Find_Stock.place (x=725 , y=125) 
18
 Update_Stock = Button (root_stock,text = "Update Stock" , font=("lucida handwriting" ,
 18 , "bold") , bg="white" , padx=15 , command = lambda: swap(update_stock_frame))
 Update_Stock.place (x=1000 , y=125)

 go_back = Button (root_stock , text = " <<< Go Back" , font=("lucida handwriting" ,
 18 , "bold") , bg="white" , padx=15 , command=Main_Screenstock)
 go_back.place (x=1100 , y=640)
#FUNCTION TO GO BACK TO MAIN MENU FROM STOCK MANAGEMENT
def Main_Screenstock():
 global root_stock
 root_stock.destroy()
 Main_Screen()

#-----------------------------SELF INVOICE CREATOR----------------------------------
#REQUIRED FUNCTIONS FOR INVOICE CREATION
def inv_management():
 global root_inv, root_main
 root_main.destroy()
 root_inv=Tk()
 root_inv.title ("Invoice")
 root_inv.geometry("1350x700+0+0")
 #DECLARATION OF VARIABLES
 invname=StringVar()
 invmob=StringVar()
 invic=StringVar()
 invqua=StringVar()
 #FUNCTIONS IN SELF INVOICE CREATOR
 #TO ADD INVOICE
 def add_inv():
 response= 0
 #TO CHECK WHETHER CUSTOMER EXISTS OR NOT
 mycursor.execute("SELECT Name,Mobile_No FROM customer")
 data=mycursor.fetchall()
 for row in data:
 if invname.get()==row[0]:
 if invmob.get() == str(row[1]) :
 response = "ok"
break
 else :
 messagebox.showerror("ERROR" , "Incorrect Mobile No.")
 break
 else:
 messagebox.showerror("ERROR" , "Customer Does Not Exists")

 #TO ADD ITEM IN INVOICE
 if response == "ok" :
 if invic.get().isalnum() and invqua.get().isalnum():
 mycursor.execute("SELECT * FROM stock ")
 data=mycursor.fetchall()
 for row in data:
 if invic.get() == row[0] :
 add="INSERT INTO invoice VALUES('%s','%s',%s,%s,%s)"
%(invic.get(),row[1],row[3],invqua.get(),
 (row[3])*(int(invqua.get())))
 mycursor.execute(add)
mydb.commit()
inv_ic_ent.delete(0,END)
inv_qua_ent.delete(0,END)
break
 else :
 messagebox.showerror("ERROR" , "Item Does Not Exist")
 else:
 messagebox.showerror("ERROR" , "All fields are necessary.")

 #TO SHOW DETAILS
 def det_inv():
 mycursor.execute("SELECT * FROM invoice")
 data=mycursor.fetchall()
 tqty = 0
 tamt=0
 for row in data:
 tqty = tqty + row[3]
 tamt = tamt + row[4]
19

 #TO REDUSE QUANTITY OF STOCK IN STOCK TABLE
 mycursor.execute("SELECT Item_Code , Quantity FROM invoice")
 data=mycursor.fetchall()
 for row in data:
 qtyupd='''UPDATE stock SET Quantity=Quantity-'%s'
 WHERE Item_Code='%s''''
 %(row[1] , row[0])
 mycursor.execute(qtyupd)
 mydb.commit()

 #TO ADD AMOUNT IN TOTAL SALE IN SALES TABLE
 mycursor.execute("SELECT * FROM sales")
 data = mycursor.fetchall()
 for row in data:
 if row[0] == datetime.now().date():
 updsale = '''UPDATE sales SET Total_Sale=Total_Sale + '%s'
 WHERE Date='%s''''
 %( tamt , datetime.now().date())
 mycursor.execute(updsale)
 mydb.commit()
 break
 else :
 saleadd = "INSERT INTO sales VALUES('%s' , '%s')"%(datetime.now().date() , tamt)
 mycursor.execute(saleadd)
 mydb.commit()

 #TO SHOW INFORMATION OF CUSTOMER
 cusn="SELECT * FROM customer WHERE Mobile_No='%s'"%(invmob.get())
 mycursor.execute(cusn)
 data=mycursor.fetchall()
 for row in data:
 code_label = Label(frame3 , text ="Name ::",font = ("gill sans mt" ,
 14 , "bold"))
 code_label.place(x=100 , y=20)
 name_label = Label(frame3 , text ="Mobile No. ::",font = ("gill sans mt" ,
 14 , "bold") )
 name_label.place(x=600 , y=20)
 qty_label = Label(frame3 , text ="Address ::",font = ("gill sans mt" ,
 14 , "bold") )
 qty_label.place(x=100 , y=60)
 top_label = Label(frame3 , text ="Total Purchase ::",font = ("gill sans mt" ,
 14 , "bold") )
 top_label.place(x=100 , y=100)
 da_label = Label(frame3 , text ="Due Amount ::",font = ("gill sans mt" ,
 14 , "bold") )
 da_label.place(x=600 , y=100)
 ca_label = Label(frame3 , text ="Current Amount ::",font = ("gill sans mt" ,
 14 , "bold") )
 ca_label.place(x=100 , y=140)
 cq_label = Label(frame3 , text ="Current Quantity ::",font = ("gill sans mt" ,
 14 , "bold") )
 cq_label.place(x=600 , y=140)

 icode_label = Label(frame3 , text =row[0],font = ("gill sans mt" ,
 14 , "bold"),bg="white")
 icode_label.place(x=185 , y=20)
 iname_label = Label(frame3 , text =row[2],font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 iname_label.place(x=725 , y=20)
 iqty_label = Label(frame3 , text =row[1],font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 iqty_label.place(x=200 , y=60)
 itop_label = Label(frame3 , text =row[3],font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 itop_label.place(x=260, y=100)
 ida_label = Label(frame3 , text =row[4],font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 ida_label.place(x=750 , y=100)
 ica_label = Label(frame3 , text =tqty,font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 ica_label.place(x=780 , y=140)
 icq_label = Label(frame3 , text =tamt,font = ("gill sans mt" ,
 14 , "bold"),bg="white" )
 icq_label.place(x=265 , y=140)

 #TO ADD AMOUNT TO TOTAL PURCHASE OF CUSTOMER
20
 topur='''UPDATE customer SET Total_Purchase_in_Rs=Total_Purchase_in_Rs+'%s'
 WHERE Mobile_No='%s''''
 %(tamt , invmob.get())
 mycursor.execute (topur)
 mydb.commit()

 #TO CLEAR THE ENTRY BOX
 inv_name_ent.delete(0,END)
 inv_mob_ent.delete(0,END)
 #TO DELETE INVOICE TABLE
 mycursor.execute("DELETE FROM invoice")
 mycursor.execute("DROP TABLE invoice")
 mydb.commit()
 #SELF INVOICE CREATER WINDOW
 global bg_icon
 bg_icon=ImageTk.PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 bg_lbl=Label(root_inv , image=bg_icon).pack()
 title = Label (root_inv , text = "INVOICE" , font=("lucida handwriting" ,
 40 ,"bold"), bg="yellow" , fg="black" , bd=5 , relief = GROOVE)
 title.place (x=0 , y=0 , relwidth=1)
 go_back = Button (root_inv , text = "<<< Go Back" , font=("lucida handwriting" ,
 18 , "bold") , bg="white" , padx=15 , command=Inv_Goback)
 go_back.place (x=1100 , y=640)

 #FRAMES IN SELF INVOICE CREATOR
 #CUSTOMER INFORMATION FRAME
 frame1=LabelFrame(root_inv,bg="white",width=1250,height=150)
 frame1.place(x=50,y=100)
 inv_name_lbl = Label ( frame1 , text="Customer Name ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 inv_name_lbl.place ( x=100 , y=25)
 inv_mob_lbl = Label ( frame1 , text="Mobile No ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 inv_mob_lbl.place ( x=100 , y=85)
 inv_name_ent = Entry ( frame1, font = ("gill sans mt" , 16 ) ,
 bd=5,textvariable=invname)
 inv_name_ent.place ( x=475 , y=25)
 inv_mob_ent = Entry ( frame1 , font = ("gill sans mt" , 16 ) ,
 bd=5,textvariable=invmob)
 inv_mob_ent.place ( x=475 , y=85)

 #FRAME FOR ADDING ITEMS IN INVOIVE TABLE
 frame2=LabelFrame(root_inv,bg="white",width=1250,height=150)
 frame2.place(x=50,y=255)
 inv_ic_lbl = Label ( frame2 , text="Item Code ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 inv_ic_lbl.place ( x=100 , y=25)
 inv_qua_lbl = Label ( frame2 , text="Quantity ::" ,
 font = ("gill sans mt" , 20 , "bold") , bg="white")
 inv_qua_lbl.place ( x=100 , y=85)
 inv_ic_ent = Entry ( frame2, font = ("gill sans mt" , 16 ) ,
 bd=5,textvariable=invic)
 inv_ic_ent.place ( x=475 , y=25)
 inv_qua_ent = Entry ( frame2 , font = ("gill sans mt" , 16 ) ,
 bd=5,textvariable=invqua)
 inv_qua_ent.place ( x=475 , y=85)
 inv_add_btn = Button ( frame2, text = "ADD !" , font = ("gill sans mt" ,
 14 , "bold") , padx=25 , bg="white",command=add_inv)
 inv_add_btn.place (x=800 , y=25)
 inv_det_btn = Button ( frame2 , text = "FINAL DETAIL !" , font = ("gill sans mt" ,
 14 , "bold") , padx=25 , bg="white" , command = det_inv)
 inv_det_btn.place (x=800 , y=85)
 #FRAME FOR DISPLAYING CUSTOMER & PURCHASE DETAILS
 frame3=LabelFrame(root_inv,bg="white",width=1250,height=200)
 frame3.place(x=50,y=410)

 #CREATING INVOICE TABLE
 mycursor.execute('''CREATE TABLE invoice (Item_Code VARCHAR(20) , Item_Name CHAR(20) ,
 Price INTEGER ,Quantity INTEGER ,Total INTEGER(20))''')
 mydb.commit()

#FUNCTION TO GO BACK TO MAIN MENU FROM INVOICE CREATOR
def Inv_Goback():
21
 global root_inv
 root_inv.destroy()
 Main_Screen()
#------------------------------------MAIN SCREEN--------------------------------------
def Main_Screen():
 global root_main
 root_main = Tk()
 root_main.title("SUPERMART")
 root_main.geometry("1350x700+0+0")
 global bg_icon , user_icon , logo_icon , customer , staff , stock , inv , finance , logout

 bg_icon=PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
 user_icon = PhotoImage(file="D:\\New Folder\\projectimg\\admin.gif")
 logo_icon = PhotoImage(file="D:\\New Folder\\projectimg\\userimage.gif")
 customer = PhotoImage(file="D:\\New Folder\\projectimg\\customer.gif")
 staff = PhotoImage(file="D:\\New Folder\\projectimg\\staff.gif")
 stock = PhotoImage(file="D:\\New Folder\\projectimg\\stock.gif")
 inv = PhotoImage(file="D:\\New Folder\\projectimg\\inv.gif")
 finance = PhotoImage(file="D:\\New Folder\\projectimg\\finance.gif")
 logout = PhotoImage(file="D:\\New Folder\\projectimg\\logout.gif")

 bg_lbl = Label(root_main , image=bg_icon).pack()
 title = Label (root_main , text = "MAIN MENU" , font=("lucida handwriting" ,
 40 ,"bold"), bg="yellow" , fg="black" , bd=5 , relief = GROOVE)
 title.place (x=0 , y=0 , relwidth=1)
 #FRAME IN MAIN SCREEN
 admin_frame= Frame(root_main , bg="white")
 admin_frame.place(x=526 , y=125)
 logolbl=Label(admin_frame , bd=0 , image=logo_icon).grid(row=0,pady=20 , padx=20)
 welcome = Label (admin_frame , text = "Welcome To \nSUPERMARKET !!!" ,
 font= ("agency fb" , 25, "bold" ), bg="white" , fg= "black" )
 welcome.grid ( row=1 , column =0 , padx=5)
 admin_name = Label (admin_frame , text = "Admin" ,
 font= ("lucida handwriting" , 30, "bold" ), bg="white" , fg= "blue" )
 admin_name.grid ( row=2, column =0 , padx=5)
 #BUTTONS IN MAIN SCREEN
 Admin_corner= Button(root_main ,text=" ADMIN \n CORNER " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command=admin_corner , image=user_icon , compound = LEFT)
 Admin_corner.place(x = 155, y= 150)
 Customer_data = Button(root_main ,text=" CUSTOMER \nDATABASE " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command = customer_data , image=customer , compound = LEFT)
 Customer_data.place( x = 139, y= 300)
 Staff_data = Button(root_main ,text=" STAFF \n DATABASE " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command=staff_data, image=staff , compound = LEFT )
 Staff_data.place( x = 143, y= 450)
 Finance = Button(root_main ,text=" FINANCE \n DEPARTMENT " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command=Finance_Management , image=finance , compound = LEFT )
 Finance.place( x = 943, y= 150)
 Stock = Button(root_main ,text=" STOCK \n DEPARTMENT " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white", padx=15 ,
 command=stock_management , image=stock , compound = LEFT )
 Stock.place( x =936, y= 300)
 Shipping = Button(root_main ,text=" SELF \n INVOICE " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command=inv_management, image=inv , compound = LEFT)
 Shipping.place( x = 980, y= 450)
 Logout = Button(root_main ,text=" LOGOUT !!! " ,
 font=("lucida handwriting" , 18 , "bold") , bg="white" , padx=15 ,
 command = root_main.destroy , image=logout , compound = LEFT)
 Logout.place( x = 544, y= 580)
#FUNCTION FOR LOGING IN
def login():
 response = 0
 mycursor.execute("SELECT Username,Password FROM admin")
 data = mycursor.fetchall()

 #CHECKING LOGIN INFORMATION
22
 if userid.get()=="" and password.get()=="" :
 messagebox.showerror("ERROR" , "Please enter username and password")
 elif userid.get()=="" and password.get() != "":
 messagebox.showerror("ERROR" , "Please enter username")
 elif password.get()=="" and userid.get() != "":
 messagebox.showerror("ERROR" , "Please enter password")
 else:
 for row in data:
 if userid.get() == row[0]:
 if password.get() == row[1] :
 response = messagebox.showinfo("LOGGED IN !!!" , "Login Successful !")
 break
 else :
 messagebox.showerror("ERROR" , "Incorrect Password")
 break
 else:
 messagebox.showerror("ERROR" , "Incorrect Username")

 #LOGING IN
 if response=="ok":
 root.destroy()
 Main_Screen()
#LOGIN SCREEN WINDOW
root = Tk()
root.title("SUPERMART")
root.geometry("1350x700+0+0")

global bg_icon
bg_icon=PhotoImage(file="D:\\New Folder\\projectimg\\BG.gif")
user_icon=PhotoImage(file="D:\\New Folder\\projectimg\\admin.gif")
pass_icon =PhotoImage(file="D:\\New Folder\\projectimg\\password.gif")
logo_icon = PhotoImage(file="D:\\New Folder\\projectimg\\userimage.gif")
#DECLARATION OF VARIABLES
userid=StringVar()
password=StringVar()
#LOGIN SCREEN BODY
bg_lbl = Label(root, image=bg_icon).pack()
title=Label(root,text="Welcome To SUPERMART",font=("lucida handwriting",
40,"bold"),bg="yellow",fg="black",bd=5,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)
#FRAME IN LOGIN SCREEN
Login_Frame=Frame(root,bg="white")
Login_Frame.place(x=400,y=150)
logolbl=Label(Login_Frame,image=logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
userlbl=Label(Login_Frame,text=" Username :",font=("lucida handwriting",20,"bold"),
bg="white" , image=user_icon,compound=LEFT).grid(row="1",column="0",padx=20,pady=10) ,
txtid=Entry(Login_Frame, bd=5 , textvariable=userid ,
relief=GROOVE,font=("",15)).grid(row="1",column="1",padx=20)
passlbl=Label(Login_Frame,text=" Password :",compound=LEFT,font=("lucida
handwriting",20,"bold"image=pass_icon,),bg="white").grid(row="2",column="0",padx=20,pady=10)
txtpass = Entry(Login_Frame, bd=5,textvariable=password, relief=GROOVE, font=("",
15)).grid(row="2", column="1", padx=20)
b_login=Button(Login_Frame,text="Login !",width=15,font=("lucida
handwriting",14,"bold"),bg="white",fg="black" , command =login).grid(row="3",column=1,pady=10)