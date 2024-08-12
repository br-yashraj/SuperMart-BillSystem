from tkinter import *
from tkinter import messagebox
from tkinter import Text
from PIL import Image, ImageTk
import random, os, tempfile
# smtplib to send Gmail
import smtplib
from datetime import datetime

# Functionality part..........

# !generate billnumber
billnumber = random.randint(1,1000)

# !adding date and time
# Get the current date and time
now = datetime.now()
# Format date as MM/DD/YYYY
date_str = now.strftime("%m/%d/%Y")
# Format time as 12-hour format with AM/PM
time_str = now.strftime("%I:%M %p")

# ! If SuperMart bills fill doesnt exist it will create then save the bills
if not os.path.exists('SuperMart bills'):
    os.mkdir('SuperMart bills')

# !Saving bill in system file
def save_bill():
    global billnumber
    result = messagebox.askyesno('Save', 'Do you want to Save this Bill')
    if(result):
        bill_content = textarea.get(1.0, END)
        file = open(f'SuperMart bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill Number {billnumber} is saved successfully')

def bill_area():
    if NameEntry.get == '' or PhoneEntry.get() == '':
        messagebox.showerror('Invalide Customer Details', 'Customer Details Are Required*')
    elif dailyEss_Price_Entry.get() == '' and Fruit_Vegees_Price_Entry.get() == '' and Grocery_Price_Entry.get() == '':
        messagebox.showerror('Error','No Product are Selected')
    elif dailyEss_Price_Entry.get() == '0 Rs' and Fruit_Vegees_Price_Entry.get() == '0 Rs' and Grocery_Price_Entry.get() == '0 Rs':
        messagebox.showerror('Error','No Product are Selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f"\nBill Number: {billnumber}\t\t\t\t   {date_str}")
        textarea.insert(END, f"\nCustomer Name: {NameEntry.get()}\t\t\t\t   {time_str}")
        textarea.insert(END, f"\nCustomer Phone: {PhoneEntry.get()}")
        textarea.insert(END,'\n______________________________________________\n')
        textarea.insert(END, f"\n")
        textarea.insert(END, ' Product\t\t\tQuantity\t\tPrice ')
        textarea.insert(END,'\n______________________________________________')
        textarea.insert(END, f"\n")

        # ! Daily Essential Itmes
        if dailyEss_Entry[0].get() != '0':
            textarea.insert(END, f' Milk(0.5L)\t\t\t{dailyEss_Entry[0].get()}\t\t{Milk_Price} Rs\n')
        if dailyEss_Entry[1].get() != '0':
            textarea.insert(END, f' Brown Bread\t\t\t{dailyEss_Entry[1].get()}\t\t{BrownBread_Price} Rs\n')
        if dailyEss_Entry[2].get() != '0':
            textarea.insert(END, f' White Bread\t\t\t{dailyEss_Entry[2].get()}\t\t{WhiteBread_Price} Rs\n')
        if dailyEss_Entry[3].get() != '0':
            textarea.insert(END, f' Dahi 200g\t\t\t{dailyEss_Entry[3].get()}\t\t{Dahi_Price} Rs\n')
        if dailyEss_Entry[4].get() != '0':
            textarea.insert(END, f' Atta (5kg)\t\t\t{dailyEss_Entry[4].get()}\t\t{Atta_Price} Rs\n')
        if dailyEss_Entry[5].get() != '0':
            textarea.insert(END, f' Daal(1kg)\t\t\t{dailyEss_Entry[5].get()}\t\t{Dal_Price} Rs\n')
        if dailyEss_Entry[6].get() != '0':
            textarea.insert(END, f' Rice(1kg)\t\t\t{dailyEss_Entry[6].get()}\t\t{Rice_Price} Rs\n')
        if dailyEss_Entry[7].get() != '0':
            textarea.insert(END, f' Tata Salt(1kg)\t\t\t{dailyEss_Entry[7].get()}\t\t{Salt_Price} Rs\n')
        
        # ! Fruits & Vegetables Items
        if Fruit_Vegge_Entry[0].get() != '0':
            textarea.insert(END, f' Mango (1kg)\t\t\t{Fruit_Vegge_Entry[0].get()}\t\t{Mango_Price} Rs\n')
        if Fruit_Vegge_Entry[1].get() != '0':
            textarea.insert(END, f' Banana (12P)\t\t\t{Fruit_Vegge_Entry[1].get()}\t\t{Banana_Price} Rs\n')
        if Fruit_Vegge_Entry[2].get() != '0':
            textarea.insert(END, f' Apple (1kg)\t\t\t{Fruit_Vegge_Entry[2].get()}\t\t{Apple_Price} Rs\n')
        if Fruit_Vegge_Entry[3].get() != '0':
            textarea.insert(END, f' Orange (1kg)\t\t\t{Fruit_Vegge_Entry[3].get()}\t\t{Orange_Price} Rs\n')
        if Fruit_Vegge_Entry[4].get() != '0':
            textarea.insert(END, f' Aaloo(1kg)\t\t\t{Fruit_Vegge_Entry[4].get()}\t\t{Aaloo_Price} Rs\n')
        if Fruit_Vegge_Entry[5].get() != '0':
            textarea.insert(END, f' Onion(1kg)\t\t\t{Fruit_Vegge_Entry[5].get()}\t\t{Onion_Price} Rs\n')
        if Fruit_Vegge_Entry[6].get() != '0':
            textarea.insert(END, f' Bindi(1kg)\t\t\t{Fruit_Vegge_Entry[6].get()}\t\t{Bindi_Price} Rs\n')
        if Fruit_Vegge_Entry[7].get() != '0':
            textarea.insert(END, f' Paneer(100g)\t\t\t{Fruit_Vegge_Entry[7].get()}\t\t{Paneer_Price} Rs\n')

        # ! Grocery Items
        if Grocery_Entry[0].get() != '0':
            textarea.insert(END, f' Maggie\t\t\t{Grocery_Entry[0].get()}\t\t{Maggie_Price} Rs\n')
        if Grocery_Entry[1].get() != '0':
            textarea.insert(END, f' Butter\t\t\t{Grocery_Entry[1].get()}\t\t{Butter_Price} Rs\n')
        if Grocery_Entry[2].get() != '0':
            textarea.insert(END, f' Cheese (5p)\t\t\t{Grocery_Entry[2].get()}\t\t{Cheese_Price} Rs\n')
        if Grocery_Entry[3].get() != '0':
            textarea.insert(END, f' Fortune Oil\t\t\t{Grocery_Entry[3].get()}\t\t{Fortune_Oil_Price} Rs\n')
        if Grocery_Entry[4].get() != '0':
            textarea.insert(END, f' Hair Oil\t\t\t{Grocery_Entry[4].get()}\t\t{Hair_Oil_Price} Rs\n')
        if Grocery_Entry[5].get() != '0':
            textarea.insert(END, f' Shampoo\t\t\t{Grocery_Entry[5].get()}\t\t{Shampoo_Price} Rs\n')
        if Grocery_Entry[6].get() != '0':
            textarea.insert(END, f' Soup\t\t\t{Grocery_Entry[6].get()}\t\t{Soup_Price} Rs\n')
        if Grocery_Entry[7].get() != '0':
            textarea.insert(END, f' Surf (1kg)\t\t\t{Grocery_Entry[7].get()}\t\t{Surf_Price} Rs\n')
        textarea.insert(END,'______________________________________________\n')
        textarea.insert(END, f"\n")
        textarea.insert(END, f' Gross Amount:\t\t\t\t   {Total_Bill_Before_Tax} Rs\n')
        textarea.insert(END, f' Total GST Amount:\t\t\t\t   {Tax_amt} Rs\n')
        textarea.insert(END, f"\n")

        # !Adding of Carry Bag
        Carry_Bag = messagebox.askyesno('Additional', 'Want a Carry Bag for just 5 Rs')
        if(Carry_Bag):
            textarea.insert(END, f'\t\t\tCarry Bag: 5 Rs\n')
            textarea.insert(END,'\t\t\t\t______________\n')
            textarea.insert(END, f' Total Net Amount:\t\t\t\t   {Total_Bill + 5} Rs\n')
            textarea.insert(END,'\t\t\t\t______________\n')
        else:
            textarea.insert(END,'\t\t\t\t______________\n')
            textarea.insert(END, f' Total Net Amount:\t\t\t\t   {Total_Bill} Rs\n')
            textarea.insert(END,'\t\t\t\t______________\n')

        # ! Saving bill at the end...
        save_bill()

# Command for Total Button
def total():
    # & Total For Daily Essential Products 
    global Milk_Price, BrownBread_Price, WhiteBread_Price, Dahi_Price, Atta_Price, Dal_Price, Rice_Price, Salt_Price

    Milk_Price = int((dailyEss_Entry[0].get())) * 32
    BrownBread_Price = int((dailyEss_Entry[1].get())) * 50
    WhiteBread_Price = int((dailyEss_Entry[2].get())) * 23
    Dahi_Price = int((dailyEss_Entry[3].get())) * 20
    Atta_Price = int((dailyEss_Entry[4].get())) * 215
    Dal_Price = int((dailyEss_Entry[5].get())) * 140
    Rice_Price = int((dailyEss_Entry[6].get())) * 80
    Salt_Price = int((dailyEss_Entry[7].get())) * 24

    Total_DailyEss_Price = Milk_Price + BrownBread_Price + WhiteBread_Price + Dahi_Price + Atta_Price + Dal_Price + Rice_Price + Salt_Price
    
    # First we will delete any values before Inserting
    # This will update the Price everytime we click on total button 
    dailyEss_Price_Entry.delete(0, END)
    #  Inserting Total Amount inside Entry of DailyESs
    dailyEss_Price_Entry.insert(0,f"{Total_DailyEss_Price} Rs")

    # & Total For Fruits and Vegetables 
    global Mango_Price, Banana_Price, Apple_Price, Orange_Price, Aaloo_Price, Onion_Price, Bindi_Price, Paneer_Price

    Mango_Price = int((Fruit_Vegge_Entry[0].get())) * 110
    Banana_Price = int((Fruit_Vegge_Entry[1].get())) * 60
    Apple_Price = int((Fruit_Vegge_Entry[2].get())) * 170
    Orange_Price = int((Fruit_Vegge_Entry[3].get())) * 80
    Aaloo_Price = int((Fruit_Vegge_Entry[4].get())) * 24
    Onion_Price = int((Fruit_Vegge_Entry[5].get())) * 30
    Bindi_Price = int((Fruit_Vegge_Entry[6].get())) * 60
    Paneer_Price = int((Fruit_Vegge_Entry[7].get())) * 45

    Total_Fruit_Vegges_Price = Mango_Price + Banana_Price + Apple_Price + Orange_Price + Aaloo_Price + Onion_Price + Bindi_Price + Paneer_Price

    # First we will delete any values before Inserting
    # This will update the Price everytime we click on total button 
    Fruit_Vegees_Price_Entry.delete(0, END)
    #  Inserting Total Amount inside Entry of Fruits_Vegges
    Fruit_Vegees_Price_Entry.insert(0, f"{Total_Fruit_Vegges_Price} Rs")

    # & Total For Grocery
    global Maggie_Price, Butter_Price, Cheese_Price, Fortune_Oil_Price, Hair_Oil_Price, Shampoo_Price, Soup_Price, Surf_Price

    Maggie_Price = int((Grocery_Entry[0].get())) * 14
    Butter_Price = int((Grocery_Entry[1].get())) * 56
    Cheese_Price = int((Grocery_Entry[2].get())) * 80
    Fortune_Oil_Price = int((Grocery_Entry[3].get())) * 140
    Hair_Oil_Price = int((Grocery_Entry[4].get())) * 60
    Shampoo_Price = int((Grocery_Entry[5].get())) * 160
    Soup_Price = int((Grocery_Entry[6].get())) * 20
    Surf_Price = int((Grocery_Entry[7].get())) * 134

    Total_Grocery_Price = Maggie_Price + Butter_Price + Cheese_Price + Fortune_Oil_Price + Hair_Oil_Price + Shampoo_Price + Soup_Price + Surf_Price

    # First we will delete any values before Inserting
    # This will update the Price everytime we click on total button 
    Grocery_Price_Entry.delete(0, END)
    #  Inserting Total Amount inside Entry of Grocery 
    Grocery_Price_Entry.insert(0, f"{Total_Grocery_Price} Rs")

    # & Excluding Taxes total bill
    global Total_Bill, Total_Bill_Before_Tax
    Total_Bill = Total_DailyEss_Price + Total_Fruit_Vegges_Price + Total_Grocery_Price
    Total_Bill_Before_Tax = (Total_Bill) / 1.05
    Total_Bill_Before_Tax = round(Total_Bill_Before_Tax)

    Tax_before_GST_Entry.delete(0,END)
    Tax_before_GST_Entry.insert(0, f"{Total_Bill_Before_Tax} Rs")

    # # & Tax Amount
    global Tax_amt
    Tax_amt = Total_Bill - Total_Bill_Before_Tax

    Total_GST_Amount_Entry.delete(0, END)
    Total_GST_Amount_Entry.insert(0, f"{Tax_amt} Rs")

    # # & Final Bill

    Total_Amount_Entry.delete(0, END)
    Total_Amount_Entry.insert(0, f"{Total_Bill} Rs")

# Command for Search button in Customer details
def search_Bill():
    for i in os.listdir('SuperMart bills/'):
        if i.split('.')[0] == BillEntry.get():
            f = open(f'SuperMart bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')

# Command for Printing the Bill
def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', "Bill is Empty")
    else:
       file = tempfile.mktemp('.txt')
       open(file, 'w').write(textarea.get(1.0, END))
       os.startfile(file, 'print')

# Command to send bill through Email
def send_email():

    def send_Gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(SenderEntry.get(), PasswordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(SenderEntry.get(), RecipientEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=email_window)
        except:
            messagebox.showerror('Error', "Something Went Wrong, Please Try Again", parent=email_window)


    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', "Bill is Empty")
    else:
        # creating a new tkinter window
        email_window = Toplevel()
        email_window.title('Send To Email')
        email_window.config(bg="#010005")
        email_window.resizable(0,0)
        
        SenderFrame = LabelFrame(email_window, text='SENDER', font=('arial',14,'bold'), bd=5, bg='#010005', fg='white')
        SenderFrame.grid(row=0, column=0, padx=20, pady=20)

        SenderLabel = Label(SenderFrame, text="Sende's Email", font=('arial',10,'bold'), bg='#010005', fg='white')
        SenderLabel.grid(row=0, column=0, padx=10, pady=8)

        SenderEntry = Entry(SenderFrame, font=('arial',10,'bold'), bd=2, width=23, relief=RIDGE)
        SenderEntry.grid(row=0, column=1, padx=10, pady=8)
        SenderEntry.insert(0, 'br.yashraj16@gmail.com')

        PasswordLabel = Label(SenderFrame, text="Password", font=('arial',10,'bold'), bg='#010005', fg='white')
        PasswordLabel.grid(row=1, column=0, padx=10, pady=8)

        PasswordEntry = Entry(SenderFrame, font=('arial',10,'bold'), bd=2, width=23, relief=RIDGE, show="*")
        PasswordEntry.grid(row=1, column=1, padx=10, pady=8)
        PasswordEntry.insert(0, 'xuls bkbp ipru vrhs')
        

        RecipientFrame = LabelFrame(email_window, text='RECIPIENT', font=('arial',14,'bold'), bd=5, bg='#010005', fg='white')
        RecipientFrame.grid(row=1, column=0, padx=20, pady=20)

        RecipientLabel = Label(RecipientFrame, text="Email Address", font=('arial',10,'bold'), bg='#010005', fg='white')
        RecipientLabel.grid(row=0, column=0, padx=10, pady=8)

        RecipientEntry = Entry(RecipientFrame, font=('arial',10,'bold'), bd=2, width=23, relief=RIDGE)
        RecipientEntry.grid(row=0, column=1, padx=10, pady=8)

        MessageLabel = Label(RecipientFrame, text="Message", font=('arial',10,'bold'), bg='#010005', fg='white')
        MessageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(RecipientFrame, font=('arial',10,'bold'), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('_', '').replace('\t\t', '\t'))

        sendButton = Button(email_window, text='SEND', font=('arail', 16, 'bold'), width=12, command=send_Gmail)
        sendButton.grid(row=2, column=0, pady=10)

    email_window.mainloop()

# command for Reset button
def clearAll():
    value = messagebox.askyesno('Clear All', 'Do You Want to Clear All')

    if (value == TRUE) :
        # Customer Fields
        NameEntry.delete(0, END)
        PhoneEntry.delete(0, END)
        BillEntry.delete(0, END)
        # For Daily Essential Entry field
        for entry1 in dailyEss_Entry:
            entry1.delete(0, END)
            entry1.insert(0, 0)
            # For Fruits & Veggetable Entry field
        for entry2 in Fruit_Vegge_Entry:
            entry2.delete(0, END)
            entry2.insert(0, 0)
            # For Grocery Items Entry field
        for entry3 in Grocery_Entry:
            entry3.delete(0, END)
            entry3.insert(0, 0)
        # Reseting Bill Area
        textarea.delete(1.0, END)
        # Reseting Bill Menu
        dailyEss_Price_Entry.delete(0, END)
        Fruit_Vegees_Price_Entry.delete(0, END)
        Grocery_Price_Entry.delete(0, END)
        Tax_before_GST_Entry.delete(0, END)
        Total_GST_Amount_Entry.delete(0, END)
        Total_Amount_Entry.delete(0, END)

# Command to get QR Code
def QR_Code():
    global original_text, photo
    original_text = textarea.get("1.0", END)
    textarea.delete("1.0", END)
    textarea.image_create(END, image=photo)

# Command to Back to Bill in textarea
def goBack():
    textarea.delete("1.0", END)
    textarea.insert(END, original_text)
         
# GUI part..........    
# Object of tkinter
root = Tk()
root.geometry('1430x740')
root.resizable(0,0)
root.config(bg="black")

# Load an image and convert it to a PhotoImage object
# image = Image.open("QR Code.jpg")  # Update this path to your image
# photo = ImageTk.PhotoImage(image)

# Store the original text
original_text = ""

# ! 1.Heading Frame
headingLabel = Label(root,text='स्वागतम् है • Welcome to Barnwal SuperMart', font=('times new roman', 25, 'bold'), fg='gold', bg='#010005', bd=7, relief=GROOVE)
headingLabel.pack(side='top', fill=X)

# ! 2.Customer Detail Frame
customer_details_frame = LabelFrame(root, text="Customer Detail's", font=('times new roman', 15, 'bold'),bg = '#010005', fg='gold', bd=5, relief=GROOVE)
customer_details_frame.pack(pady=3, fill=X)

# Name label
NameLabel = Label(customer_details_frame, text="Customer Name :", font=('times new roman', 15, 'bold'), bg='#010005', fg='white')
NameLabel.grid(row=0, column=0, padx=8, pady=3)

NameEntry = Entry(customer_details_frame, textvariable='', font = ('arial', 15), bd=5, relief=GROOVE, width=20)
NameEntry.grid(row=0, column=1, padx=5, pady=3)

# Phone label
PhoneLabel = Label(customer_details_frame, text="Phone No:", font=('times new roman', 15, 'bold'), bg='#010005', fg='white')
PhoneLabel.grid(row=0, column=2, padx=8, pady=3)

PhoneEntry = Entry(customer_details_frame, textvariable='', font = ('arial', 15), bd=5, relief=GROOVE, width=20)
PhoneEntry.grid(row=0, column=3, padx=5, pady=5)

# Bill label
BillLabel = Label(customer_details_frame, text="Bill No:", font=('times new roman', 15, 'bold'), bg='#010005', fg='white')
BillLabel.grid(row=0, column=4, padx=8, pady=5)

BillEntry = Entry(customer_details_frame, textvariable='', font = ('arial', 15), bd=5, relief=GROOVE, width=20)
BillEntry.grid(row=0, column=5, padx=5, pady=5)

searchbtn = Button(customer_details_frame, text='Search', font=('times new roman', 12, 'bold'), bd=3, width=10, relief=GROOVE, command=search_Bill)
searchbtn.grid(row=0, column=6, padx=30, pady=10)

# ! 3.Products Main Frame
productsFrame = Frame(root)
productsFrame.pack()

#  Daily Essential Products inside Products
dailyEssentialFrame = LabelFrame(productsFrame, text="Daily Essentials", font=('times new roman', 15, 'bold'),bg = '#010005', fg='gold', bd=5, relief=GROOVE)
dailyEssentialFrame.grid(row=0, column=0)


dailyEss_list = ['1.Milk (.5L) • 32Rs', '2.Brown Bread • 50Rs', 
            '3.White Bread • 23Rs','4.Dahi (200g) • 20Rs', 
            '5.Atta (5kg) • 215Rs','6.Masoor Dal (1kg) • 140Rs', 
            '7.Rice (1kg) • 80Rs', '8.Salt(1kg) • 24Rs']

item_no = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8']

dailyEss_Entry = ['item1_Entry', 'item2_Entry', 'item3_Entry', 'item4_Entry', 'item5_Entry', 'item6_Entry', 'item7_Entry', 'item8_Entry']

for i in range(8):
    dailyEss_list[i] = Label(dailyEssentialFrame, text= dailyEss_list[i], font=('times new roman', 12, 'bold'),bg='#010005', fg='white')
    dailyEss_list[i].grid(row=i, column=0, pady=9, padx=9, sticky="w")

    # ^Entry field of dailyEssentialFrame
    dailyEss_Entry[i] = Entry(dailyEssentialFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    dailyEss_Entry[i].grid(row=i, column=1, pady=9, padx=10)
    # to make all the entry field initially Zero...
    # taki agar total ke time koi entry kahli ho(product nhi le) toh 
    # error throw nhi kre kyuki agar khali - null or
    # null * price is invalid so we do so.... 
    dailyEss_Entry[i].insert(0,0)

#  &Fruits and Vegetables Products inside Products
Fruit_VegeesFrame = LabelFrame(productsFrame, text="Fruits & Vegetables(kg)", font=('times new roman', 15, 'bold'),bg = '#010005', fg='gold', bd=5, relief=GROOVE)
Fruit_VegeesFrame.grid(row=0, column=1)

F_V_list = ['1.Mango • 110Rs', '2.Banana • 60Rs', 
            '3.Apple • 170Rs','4.Orange • 80Rs', 
            '5.Aaloo • 24Rs','6.Onion • 30Rs', 
            '7.Bindi • 60Rs', '8.Paneer(100g) • 45Rs']

item_no = ['item9', 'item10', 'item11', 'item12', 'item13', 'item14', 'item15', 'item16']

Fruit_Vegge_Entry = ['item9_Entry', 'item10_Entry', 'item11_Entry', 'item12_Entry', 'item13_Entry', 'item14_Entry', 'item15_Entry', 'item16_Entry']

for i in range(8):
    F_V_list[i] = Label(Fruit_VegeesFrame, text= F_V_list[i], font=('times new roman', 12, 'bold'),bg='#010005', fg='white')
    F_V_list[i].grid(row=i, column=0, pady=9, padx=9, sticky="w")

    # ^Entry field of Fruits_VeggesFrame

    Fruit_Vegge_Entry[i] = Entry(Fruit_VegeesFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    Fruit_Vegge_Entry[i].grid(row=i, column=1, pady=9, padx=10)

    # Setting initial value to 0
    Fruit_Vegge_Entry[i].insert(0,0)

#  &Grocery Products inside Products
GroceryFrame = LabelFrame(productsFrame, text="Grocery", font=('times new roman', 15, 'bold'),bg = '#010005', fg='gold', bd=5, relief=GROOVE)
GroceryFrame.grid(row=0, column=2)

Grocery_list = ['1.Maggie • 14Rs', '2.Butter • 56Rs', 
            '3.Cheese(5p) • 80Rs','4.Fortune Oil(1L) • 140Rs', 
            '5.Hair Oil • 60Rs','6.Shampoo • 160Rs', 
            '7.Soup • 20Rs', '8.Surf(1kg) • 134Rs']

item_no = ['item17', 'item18', 'item19', 'item20', 'item21', 'item22', 'item23', 'item24']

Grocery_Entry = ['item17_Entry', 'item18_Entry', 'item19_Entry', 'item20_Entry', 'item21_Entry', 'item22_Entry', 'item23_Entry', 'item24_Entry']

for i in range(8):
    Grocery_list[i] = Label(GroceryFrame, text= Grocery_list[i], font=('times new roman', 12, 'bold'),bg='#010005', fg='white')
    Grocery_list[i].grid(row=i, column=0, pady=9, padx=9, sticky="w")

    # ^Entry field of CosmaticFrame
    Grocery_Entry[i] = Entry(GroceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    Grocery_Entry[i].grid(row=i, column=1, pady=9, padx=10)
    # Setting initially 0 to all entry Field
    Grocery_Entry[i].insert(0,0)

# & Receipt & Bill Frame inside Products

BillFrame = Frame(productsFrame, bd=8, relief=GROOVE, bg='#010005')
BillFrame.grid(row=0, column=3)

billareaLabel = Label(BillFrame, text="Bill Area", font=('times new roman', 15, 'bold'), width=10, bd=5, relief=GROOVE, bg='#010005', fg='gold')
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(BillFrame, orient=VERTICAL, width=22, background='#edafb8')
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(BillFrame, height=25, width=46, yscrollcommand=scrollbar.set, bg='#ffffff')
textarea.pack()
scrollbar.config(command=textarea.yview)

# ! 4.Bill Menu
billMenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), bg='#010005', fg='gold', bd=5, relief=GROOVE)
billMenuFrame.pack(fill=X)

# ~Total Price of Daily Essential Products
 
dailyEss_Products_Price = Label(billMenuFrame, text='Daily Ess Products Price', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
dailyEss_Products_Price.grid(row=0, column=0, pady=3, padx=9, sticky="w")

# ~Entry of Total Price of Daily Essential Products 

dailyEss_Price_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
dailyEss_Price_Entry.grid(row=0, column=1, pady=3, padx=10)

# ~Total Price of Fruits_Veggess Products
 
Fruit_Vegees_Price = Label(billMenuFrame, text='Fruits / Vegetables Price', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
Fruit_Vegees_Price.grid(row=1, column=0, pady=3, padx=9, sticky="w")

# ~Entry of Total Price of Fruits_Veggess Products

Fruit_Vegees_Price_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
Fruit_Vegees_Price_Entry.grid(row=1, column=1, pady=3, padx=10)

# ~Total Price of Grocery Products
 
Grocery_Price = Label(billMenuFrame, text='Groceries Price', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
Grocery_Price.grid(row=2, column=0, pady=3, padx=9, sticky="w")

# ~Entry of Total Price of Fruits_Veggess Products

Grocery_Price_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
Grocery_Price_Entry.grid(row=2, column=1, pady=3, padx=10)

# ~Total bill Before GSt
 
Tax_before_GST = Label(billMenuFrame, text='Gross Amount', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
Tax_before_GST.grid(row=0, column=2, pady=3, padx=9, sticky="w")

# ~Entry of Total bill Before GSt 

Tax_before_GST_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
Tax_before_GST_Entry.grid(row=0, column=3, pady=3, padx=10)

# ~Total GSt Amount
 
Total_GST_Amount = Label(billMenuFrame, text='GST Amount', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
Total_GST_Amount.grid(row=1, column=2, pady=3, padx=9, sticky="w")

# ~Entry of Total GSt Amount

Total_GST_Amount_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
Total_GST_Amount_Entry.grid(row=1, column=3, pady=3, padx=10)

# ~Total bill amount
 
Total_Amount = Label(billMenuFrame, text='Grand Total', font=('times new roman', 14, 'bold'),bg='#010005', fg='white')
Total_Amount.grid(row=2, column=2, pady=3, padx=9, sticky="w")

# ~Entry of Total bill

Total_Amount_Entry = Entry(billMenuFrame, font=('times new roman', 12, 'bold'), width=14, bd=5)
Total_Amount_Entry.grid(row=2, column=3, pady=3, padx=25)

# ~ All Essential Buttons "Total", "Clear", "Print" and so on 
buttonFrame = Frame(billMenuFrame, bd=5, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

# ^Total Button
totalButton = Button(buttonFrame, text='Total', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=total)
totalButton.grid(row=0, column=0, pady=10, padx=5)

# ^ Bill Button
billButton = Button(buttonFrame, text='Bill', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=bill_area)
billButton.grid(row=0, column=1, padx=5)

# ^ Send Button
SendButton = Button(buttonFrame, text='Email', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=send_email)
SendButton.grid(row=0, column=2, padx=5)

# ^ Print Button
PrintButton = Button(buttonFrame, text='Print', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=print_bill)
PrintButton.grid(row=0, column=3, padx=5)

# ^ Clear Button
ClearButton = Button(buttonFrame, text='Clear', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=clearAll)
ClearButton.grid(row=0, column=4, padx=5)

# ^ QR Code Button
QrButton = Button(buttonFrame, text='QR Code', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=7, pady=5, relief=GROOVE, command=QR_Code)
QrButton.grid(row=0, column=5, padx=5)

# ^ Back Button
Back_Button = Button(buttonFrame, text='Back', font=('times new roman', 16, 'bold'), bg='#010005', fg='white',  bd=3, width=6, pady=3, relief=GROOVE, command=goBack)
Back_Button.grid(row=0, column=6, padx=5)

root.mainloop() 