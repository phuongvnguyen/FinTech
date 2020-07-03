#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pickle
filename = 'CreditCardRFC_model.sav'
loaded_CreditCardRFC_model = pickle.load(open(filename, 'rb'))

class Main_window:
    def __init__(self, window):
        
        self.window = window
        self.window.title("PhuongCCDP Dashboard")
        self.window.geometry("900x920") #(width,heigth)
        self.window.resizable(0, 0)
        

        self.label = tk.Label(self.window, text = "Welcome To The Phuong Fintech",
                             font = ('Arial' , 12, 'bold'), fg = 'blue',height = 1)#, width = 11,  
                              #borderwidth = 1, relief = 'solid')
        self.label.pack()

        
        self.label = tk.Label(self.window, text = "The Phuong Credit Card Default Prediction System",
                             font = ('Arial' , 15, 'bold'), fg = 'green',height = 1)#, width = 11,  
                              #borderwidth = 1, relief = 'solid')
        self.label.pack()
        

        
        self.label = tk.Label(self.window, text = " A Machine Learning-integrated Application For The Banking Industry",
                             font=("Helvetica", 11, "bold italic"), fg = 'blue')
        self.label.pack()
        
        
        self.label = tk.Label(self.window, text = "Demo Version ",
                             font=("Time", 10, "bold italic"), fg = 'red')
        self.label.pack()
        
        self.label = tk.Label(self.window, text = "Copyright @ Phuong V. Nguyen",
                             font=("Helvetica", 9, "bold"), fg = 'magenta')
        self.label.pack()
        
        
         # Optional step: insert an image
        self.icon = tk.PhotoImage(file = "Mybank.PNG")
        self.label = tk.Label(self.window, image = self.icon)
        self.label.pack()
        
        # The functional buttoms
        self.label = tk.Label(self.window, text = "Please, enter your customer information into the areas below",
                             font=("Times", 11, "bold"), fg = 'blue')
        self.label.pack()
        
        


        
        ## SubFrame 1: Personal information
        
        ## Subframe
        self.label = tk.Label(self.window, text = "Personal Information",
                              font=("Times", 12, "bold"), fg = 'green')
        self.label.pack(side = TOP)
        self.frm_entry = tk.Frame(self.window,width=800, height=100,borderwidth = 1,relief='solid') 
        self.frm_entry.pack()
        
        # Variables 
        self.temp_name = tk.StringVar()
        self.temp_id = tk.IntVar()#StringVar()#tk.DoubleVar()
        self.age =tk.IntVar()#StringVar()
        self.temp_sex = tk.IntVar()#StringVar()
        self.temp_address = tk.StringVar()
        self.temp_educ= tk.IntVar()
        self.temp_marri= tk.IntVar()
        
        
        
        #1. name
        self.label_name = tk.Label(self.frm_entry, text="Full Name:",font=("Times", 9, "bold"))
        self.label_name.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_name = tk.Entry(self.frm_entry, width=30, textvariable=self.temp_name)
        self.entry_name.grid(row=0, column=2, padx=5, pady=5)
        
        # 2. ID
        self.label_ID = tk.Label(self.frm_entry, text="ID Number:",font=("Times", 9, "bold"))
        self.label_ID.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_ID= tk.Entry(self.frm_entry, width=20, textvariable=self.temp_id )
        self.entry_ID.grid(row=0, column=4, padx=5, pady=5)
        
        # 3. Age
        self.label_age = tk.Label(self.frm_entry, text="Age:",font=("Times", 9, "bold"))
        self.label_age.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_age= tk.Entry(self.frm_entry, width=20, textvariable=self.age)
        self.entry_age.grid(row=1, column=2, padx=5, pady=5)
        
        # 4. Sex
        self.label_sex = tk.Label(self.frm_entry, text="Sex:",font=("Times", 9, "bold"))
        self.label_sex.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_sex= tk.Entry(self.frm_entry, width=20, textvariable=self.temp_sex )
        self.entry_sex.grid(row=1, column=4, padx=5, pady=5)

        # 5. Address
        self.label_address = tk.Label(self.frm_entry, text="Address:",font=("Times", 9, "bold"))
        self.label_address.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_address= tk.Entry(self.frm_entry, width=20, textvariable=self.temp_address )
        self.entry_address.grid(row=2, column=2, padx=5, pady=5)
        
        # 6. Education
        self.label_education = tk.Label(self.frm_entry, text="Education:",font=("Times", 9, "bold"))
        self.label_education.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_education= tk.Entry(self.frm_entry, width=20, textvariable=self.temp_educ )
        self.entry_education.grid(row=2, column=4, padx=5, pady=5)
        
         #7. Marriage
        self.label_marri = tk.Label(self.frm_entry, text="Marital status:",font=("Times", 9, "bold"))
        self.label_marri.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_marri = tk.Entry(self.frm_entry, width=20, textvariable=self.temp_marri)
        self.entry_marri.grid(row=5, column=2, padx=5, pady=5)
        
        ## SubFrame 2: Financial condition

        
        ## Subframe
        self.label = tk.Label(self.window, text = "Financial Condition",
                              font=("Times", 12, "bold"), fg = 'green')
        self.label.pack(side = TOP)
        self.frm_finentry = tk.Frame(self.window,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_finentry.pack()
        
        # Repayment Status
        self.label_RePaySta = tk.Label(self.frm_finentry, text="Repayment Status:",font=("Times", 9, "bold"),fg = 'blue')
        self.label_RePaySta.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.frm_RePayentry = tk.Frame(self.frm_finentry,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_RePayentry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Variables 
        self.pay_6 =tk.IntVar()
        self.pay_5 =tk.IntVar()
        self.pay_4 =tk.IntVar()
        self.pay_3 =tk.IntVar()
        self.pay_2 =tk.IntVar()
        self.pay_0 =tk.IntVar()
        
        self.label_pay_6 = tk.Label(self.frm_RePayentry, text="April:",font=("Times", 9, "bold"))
        self.label_pay_6.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_6 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_6)
        self.entry_pay_6.grid(row=0, column=2, padx=5, pady=5)
        
        self.label_pay_5 = tk.Label(self.frm_RePayentry, text="May:",font=("Times", 9, "bold"))
        self.label_pay_5.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_5 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_5)
        self.entry_pay_5.grid(row=0, column=4, padx=5, pady=5)
        
        self.label_pay_4 = tk.Label(self.frm_RePayentry, text="June:",font=("Times", 9, "bold"))
        self.label_pay_4.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_4 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_4)
        self.entry_pay_4.grid(row=1, column=2, padx=5, pady=5)
        
        self.label_pay_3 = tk.Label(self.frm_RePayentry, text="July:",font=("Times", 9, "bold"))
        self.label_pay_3.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_3 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_3)
        self.entry_pay_3.grid(row=1, column=4, padx=5, pady=5)
        
        self.label_pay_2 = tk.Label(self.frm_RePayentry, text="Ausgust:",font=("Times", 9, "bold"))
        self.label_pay_2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_2 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_2)
        self.entry_pay_2.grid(row=2, column=2, padx=5, pady=5)
        
        
        self.label_pay_0 = tk.Label(self.frm_RePayentry, text="September:",font=("Times", 9, "bold"))
        self.label_pay_0.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_pay_0 = tk.Entry(self.frm_RePayentry, width=20, textvariable=self.pay_0)
        self.entry_pay_0.grid(row=2, column=4, padx=5, pady=5)
        
        
        # Amount of bill statement
        self.label_BillState = tk.Label(self.frm_finentry, text="Amount of bill statement:",font=("Times", 9, "bold"),fg = 'blue')
        self.label_BillState.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.frm_BillStatEntry = tk.Frame(self.frm_finentry,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_BillStatEntry.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        
        
         # Variables 
        self.BILL_AMT6 =tk.IntVar()
        self.BILL_AMT5 =tk.IntVar()
        self.BILL_AMT4 =tk.IntVar()
        self.BILL_AMT3 =tk.IntVar()
        self.BILL_AMT2 =tk.IntVar()
        self.BILL_AMT0 =tk.IntVar()
        
        self.label_BILL_AMT6 = tk.Label(self.frm_BillStatEntry, text="April:",font=("Times", 9, "bold"))
        self.label_BILL_AMT6.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT6 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT6)
        self.entry_BILL_AMT6.grid(row=0, column=2, padx=5, pady=5)
        
        self.label_BILL_AMT5 = tk.Label(self.frm_BillStatEntry, text="May:",font=("Times", 9, "bold"))
        self.label_BILL_AMT5.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT5 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT5)
        self.entry_BILL_AMT5.grid(row=0, column=4, padx=5, pady=5)
        
        self.label_BILL_AMT4 = tk.Label(self.frm_BillStatEntry, text="June:",font=("Times", 9, "bold"))
        self.label_BILL_AMT4.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT4 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT4)
        self.entry_BILL_AMT4.grid(row=1, column=2, padx=5, pady=5)
        
        self.label_BILL_AMT3 = tk.Label(self.frm_BillStatEntry, text="July:",font=("Times", 9, "bold"))
        self.label_BILL_AMT3.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT3 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT3)
        self.entry_BILL_AMT3.grid(row=1, column=4, padx=5, pady=5)
        
        self.label_BILL_AMT2 = tk.Label(self.frm_BillStatEntry, text="Ausgust:",font=("Times", 9, "bold"))
        self.label_BILL_AMT2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT2 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT2)
        self.entry_BILL_AMT2.grid(row=2, column=2, padx=5, pady=5)
        
        
        self.label_BILL_AMT0 = tk.Label(self.frm_BillStatEntry, text="September:",font=("Times", 9, "bold"))
        self.label_BILL_AMT0.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_BILL_AMT0 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.BILL_AMT0)
        self.entry_BILL_AMT0.grid(row=2, column=4, padx=5, pady=5)
        
        
        
        
        # Amount of previous payment

        self.label = tk.Label(self.frm_finentry, text = "Amount of previous payment:",
                              font=("Times", 9, "bold"),fg = 'blue')
        self.label.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)#pack(side = TOP)
        self.frm_BillStatEntry = tk.Frame(self.frm_finentry,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_BillStatEntry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        
         # Variables 
        self.PAY_AMT6 =tk.IntVar()
        self.PAY_AMT5 =tk.IntVar()
        self.PAY_AMT4 =tk.IntVar()
        self.PAY_AMT3 =tk.IntVar()
        self.PAY_AMT2 =tk.IntVar()
        self.PAY_AMT1 =tk.IntVar()
        
        self.label_PAY_AMT6 = tk.Label(self.frm_BillStatEntry, text="April:",font=("Times", 9, "bold"))
        self.label_PAY_AMT6.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT6 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT6)
        self.entry_PAY_AMT6.grid(row=0, column=2, padx=5, pady=5)
        
        self.label_PAY_AMT5 = tk.Label(self.frm_BillStatEntry, text="May:",font=("Times", 9, "bold"))
        self.label_PAY_AMT5.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT5 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT5)
        self.entry_PAY_AMT5.grid(row=0, column=4, padx=5, pady=5)
        
        self.label_PAY_AMT4 = tk.Label(self.frm_BillStatEntry, text="June:",font=("Times", 9, "bold"))
        self.label_PAY_AMT4.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT4 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT4)
        self.entry_PAY_AMT4.grid(row=1, column=2, padx=5, pady=5)
        
        self.label_PAY_AMT3 = tk.Label(self.frm_BillStatEntry, text="July:",font=("Times", 9, "bold"))
        self.label_PAY_AMT3.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT3 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT3)
        self.entry_PAY_AMT3.grid(row=1, column=4, padx=5, pady=5)
        
        self.label_PAY_AMT2 = tk.Label(self.frm_BillStatEntry, text="Ausgust:",font=("Times", 9, "bold"))
        self.label_PAY_AMT2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT2 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT2)
        self.entry_PAY_AMT2.grid(row=2, column=2, padx=5, pady=5)
        
        
        self.label_PAY_AMT0 = tk.Label(self.frm_BillStatEntry, text="September:",font=("Times", 9, "bold"))
        self.label_PAY_AMT0.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_PAY_AMT0 = tk.Entry(self.frm_BillStatEntry, width=20, textvariable=self.PAY_AMT1)
        self.entry_PAY_AMT0.grid(row=2, column=4, padx=5, pady=5)
        
        
        # Other financial information

        self.label = tk.Label(self.frm_finentry, text = "Other related information:",
                              font=("Times", 9, "bold"),fg = 'blue')
        self.label.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)#pack(side = TOP)
        self.frm_OtherFinEntry = tk.Frame(self.frm_finentry,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_OtherFinEntry.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
        
         # Variables 
        self.Job_Status =StringVar()#tk.IntVar()
        self.Limit_Balance   = tk.IntVar()#StringVar()
        
        self.House_Owner =StringVar()
        self.House_Value =tk.IntVar()
        self.Month_Income=tk.IntVar()
        self.Credit_Score =tk.IntVar()
        
        self.label_Job_Status = tk.Label(self.frm_OtherFinEntry, text="Employ. Status:",font=("Times", 9, "bold"))
        self.label_Job_Status.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_Job_Status = tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.Job_Status)
        self.entry_Job_Status.grid(row=0, column=2, padx=5, pady=5)
        
        self.label_Month_Income = tk.Label(self.frm_OtherFinEntry, text="Month Income:",font=("Times", 9, "bold"))
        self.label_Month_Income.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_Month_Income = tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.Month_Income)
        self.entry_Month_Income.grid(row=0, column=4, padx=5, pady=5)
        
     
        self.label_House_Owner = tk.Label(self.frm_OtherFinEntry, text="House Onwer (Y/N):",font=("Times", 9, "bold"))
        self.label_House_Owner.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_House_Owner = tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.House_Owner)
        self.entry_House_Owner.grid(row=1, column=2, padx=5, pady=5)
        
        self.label_House_Value= tk.Label(self.frm_OtherFinEntry, text="House Value:",font=("Times", 9, "bold"))
        self.label_House_Value.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_House_Value= tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.House_Value)
        self.entry_House_Value.grid(row=1, column=4, padx=5, pady=5)
        
        
        
        self.label_Limit_Bal = tk.Label(self.frm_OtherFinEntry, text="Limit Balance:",font=("Times", 9, "bold"))
        self.label_Limit_Bal.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_Limit_Bal = tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.Limit_Balance)
        self.entry_Limit_Bal.grid(row=2, column=2, padx=5, pady=5)
        
        self.label_Credit_Score = tk.Label(self.frm_OtherFinEntry, text="Credit Score:",font=("Times", 9, "bold"))
        self.label_Credit_Score.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_Credit_Score = tk.Entry(self.frm_OtherFinEntry, width=15, textvariable=self.Credit_Score)
        self.entry_Credit_Score.grid(row=2, column=4, padx=5, pady=5)
          
        
        # Button
        self.label = tk.Label(self.window, text = "Do you want to predict the probability of credit card default of this customer next month?",
                              font=("Times", 12, "bold"), fg = 'green')
        self.label.pack(side = TOP)

        self.frm_button = tk.Frame(self.window,width=420, height=100,borderwidth = 1,relief='solid') 
        self.frm_button.pack()
        
        
        self.ok_button = tk.Button(self.frm_button, text="Yes",
                                          font=("Times", 9, "bold"), fg = 'blue', height = 1, width = 10,#)#,#bg='green')
                                       command=self.get_entry)
        self.ok_button.grid(row=0, column=2, padx=5, pady=5)
       
    
        

        self.quit_button = tk.Button(self.frm_button, text="No",
                                          font=("Times", 9, "bold"), fg = 'red', height = 1, width = 10,
                                       command=self.ExitApplication)
        self.quit_button.grid(row=0, column=1, padx=5, pady=5)# pack(side = BOTTOM)
        
       
    
    
    
    
        # showing the results
        self.label = tk.Label(self.window, text = "Result:",font=("Times", 12, "bold"), fg = 'green')
        self.label.pack()
#         self.pridict_class = tk.Label(self.window, text=" ") 
#         self.pridict_class.pack()
        
        self.text_loadDat = tk.Text(self.window, height=3, width=200)
        self.text_loadDat.pack()

        
    def get_entry(self):
        # Generate the Entry value to the data pandasframe:
#         self.entry_value['text'] =self.entry_sex.get()#[[self.entry_sex.get(),]]
        self.entry_value=[[self.entry_Limit_Bal.get(), self.entry_sex.get(),self.entry_education.get(), self.entry_marri.get(),
                           self.entry_age.get(), self.entry_pay_0.get(),self.entry_pay_2.get(),self.entry_pay_3.get(),
                          self.entry_pay_4.get(),self.entry_pay_5.get(),self.entry_pay_6.get(),
                          self.entry_BILL_AMT0.get(),self.entry_BILL_AMT2.get(),self.entry_BILL_AMT3.get()
                          ,self.entry_BILL_AMT4.get(),self.entry_BILL_AMT5.get(),self.entry_BILL_AMT6.get()
                          ,self.entry_PAY_AMT0.get(),self.entry_PAY_AMT2.get(),self.entry_PAY_AMT3.get()
                          ,self.entry_PAY_AMT4.get(),self.entry_PAY_AMT5.get(),self.entry_PAY_AMT6.get()]]
        self.col = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1', 'PAY_2',
       'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
        x_test=pd.DataFrame(data=self.entry_value, columns=self.col)
#         self.pridict_class['text']=loaded_CreditCardRFC_model.predict(x_test)
#         self.text_loadDat.insert('end', str(loaded_CreditCardRFC_model.predict(x_test)) + '\n') 
        self.text_loadDat.insert('end', str(x_test) + '\n') 
        predict=loaded_CreditCardRFC_model.predict(x_test)
        if predict== 0:
#             tk.messagebox.showwarning("Warning","Hey! be careful the prob of credit card default of this customer is high")
            tk.messagebox.showwarning("Warning","Này, hãy cẩn thận với khách hàng " +self.entry_name.get()+" này, khả năng vỡ nợ rất cao")
    
    def ExitApplication(self):
        self.MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the PhuongCCDP System?',
                                            icon = 'warning')
        if self.MsgBox == 'yes':
             self.window.destroy()
        else:
            tk.messagebox.showinfo('Return','Welcome to the PhuongCCDP System')



def main(): 
    root = tk.Tk()
    app = Main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
