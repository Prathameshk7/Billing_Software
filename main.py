from tkinter import *
import math,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#800000"
        title =Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),pady=2,fg="white",bd=10,bg=bg_color,relief=GROOVE).pack(fill=X)

        #=============================Variables========================================
        # =============================cosmetics========================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        # =============================grocery========================================
        self.rice=IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # =============================Cold drinks========================================
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # =============================Total product price and tax variable========================================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # =============================Customer========================================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill= StringVar()

        #p=========================Customer Details++++++++++++++++++++++++++++++++++++
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name:",font=("times new roman",15,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,pady=5,padx=20)
        cname_txt=Entry(F1,width=15,font=("Arial",15),textvariable=self.c_name,bd=6,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=20)

        cphn_lbl = Label(F1, text="Customer Phone:", font=("times new roman", 15, "bold"), fg="white",bg=bg_color).grid(row=0, column=2, pady=5, padx=20)
        cphn_txt = Entry(F1, width=15, font=("Arial", 15),textvariable=self.c_phone, bd=6, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=20)

        c_bill = Label(F1, text="Bill Number:", font=("times new roman", 15, "bold"), fg="white",bg=bg_color).grid(row=0, column=4, pady=5, padx=20)
        c_bill = Entry(F1, width=15, font=("Arial", 15),textvariable=self.bill_no ,bd=6, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=20)

        bill_btn=Button(F1,text="Search",width=10,textvariable=self.search_bill ,bd=7,font="arial 12 bold",fg="black").grid(row=0,column=6,pady=10,padx=10)
        #===========================Cosmetics Frame=========================================
        F2 = LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F2.place(x=5,y=170,width=325,height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 15, "bold"), fg="white",bg=bg_color).grid(row=0, column=0, pady=10, padx=20,sticky="w")
        bath_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.soap ,bd=6, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        facec_lbl = Label(F2, text="Face Cream", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(row=1, column=0, pady=10, padx=20,sticky="w")
        facec_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.face_cream ,bd=6, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        facew_lbl = Label(F2, text="Face Wash", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(row=2, column=0, pady=10, padx=20,sticky="w")
        facew_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.face_wash ,bd=6, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        hairs_lbl = Label(F2, text="Hair Spray", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(row=3, column=0, pady=10, padx=20,sticky="w")
        hairs_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.spray ,bd=6, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        hairg_lbl = Label(F2, text="Hair Gel", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(row=4, column=0, pady=10, padx=20,sticky="w")
        hairg_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.gell ,bd=6, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        bodyl_lbl = Label(F2, text="Body Lotion", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(row=5, column=0, pady=10, padx=20,sticky="w")
        bodyl_txt = Entry(F2, width=10, font=("Arial", 15),textvariable=self.loshan ,bd=6, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # ===========================Grocery Frame=========================================
        F3 = LabelFrame(self.root, text="Grocery", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color,bd=10, relief=GROOVE)
        F3.place(x=330, y=170, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=0, column=0, pady=10, padx=20, sticky="w")
        rice_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.rice ,bd=6, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        foodoil_lbl = Label(F3, text="Food Oil", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=1, column=0, pady=10, padx=20, sticky="w")
        foodoil_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.food_oil ,bd=6, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        daal_lbl = Label(F3, text="Daal", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=2, column=0, pady=10, padx=20, sticky="w")
        daal_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.daal ,bd=6, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        wheat_lbl = Label(F3, text="Wheat", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=3, column=0, pady=10, padx=20, sticky="w")
        wheat_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.wheat ,bd=6, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        sugar_lbl = Label(F3, text="Sugar", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=4, column=0, pady=10, padx=20, sticky="w")
        sugar_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.sugar ,bd=6, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        tea_lbl = Label(F3, text="Tea", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=5, column=0, pady=10, padx=20, sticky="w")
        tea_txt = Entry(F3, width=10, font=("Arial", 15),textvariable=self.tea ,bd=6, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # ===========================Cold drinks Frame=========================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, bd=10,
                        relief=GROOVE)
        F4.place(x=655, y=170, width=325, height=380)

        maza_lbl = Label(F4, text="Maza", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=0, column=0, pady=10, padx=20, sticky="w")
        maza_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.maza ,bd=6, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        coke_lbl = Label(F4, text="Coke", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=1, column=0, pady=10, padx=20, sticky="w")
        coke_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.cock ,bd=6, relief=SUNKEN).grid(row=1, column=1, pady=10,
                                                                                        padx=10)

        frooti_lbl = Label(F4, text="Frooti", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=2, column=0, pady=10, padx=20, sticky="w")
        frooti_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.frooti ,bd=6, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        thums_lbl = Label(F4, text="Thumsup", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=3, column=0, pady=10, padx=20, sticky="w")
        thums_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.thumbsup ,bd=6, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        limca_lbl = Label(F4, text="Limca", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=4, column=0, pady=10, padx=20, sticky="w")
        limca_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.limca ,bd=6, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        sprite_lbl = Label(F4, text="Sprite", font=("times new roman", 15, "bold"), fg="white", bg=bg_color).grid(
            row=5, column=0, pady=10, padx=20, sticky="w")
        sprite_txt = Entry(F4, width=10, font=("Arial", 15),textvariable=self.sprite ,bd=6, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)
        #===============================Bill area====================================================
        F5 =Frame(self.root,relief=GROOVE,bd=10)
        F5.place(x=1000, y=170, width=335, height=380)

        bill_title=Label(F5,text="Bill Area",bd=7,font="arial 15 bold",relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======================Button frame==================================================
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color,
                        bd=10,
                        relief=GROOVE)
        F6.place(x=0, y=560, relwidth=1, height=140 )

        m1_lbl=Label(F6,text="Total Cosmetic price",font=("times new roman", 14, "bold"), fg="white", bg=bg_color).grid(row=0, column=0, pady=1, padx=20, sticky="w")
        m1_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.cosmetic_price ,bd=6, relief=SUNKEN).grid(row=0, column=1, pady=1,padx=10)

        m2_lbl = Label(F6, text="Total Grocery price", font=("times new roman", 14, "bold"), fg="white",bg=bg_color).grid(row=1, column=0, pady=1, padx=20, sticky="w")
        m2_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.grocery_price ,bd=6, relief=SUNKEN).grid(row=1, column=1, pady=1,padx=10)

        m3_lbl = Label(F6, text="Total Cold Drink price", font=("times new roman", 14, "bold"), fg="white",bg=bg_color).grid(row=2, column=0, pady=1, padx=20, sticky="w")
        m3_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.cold_drink_price ,bd=6, relief=SUNKEN).grid(row=2, column=1, pady=1,padx=10)

        c1_lbl = Label(F6, text="Cosmetic Tax", font=("times new roman", 14, "bold"), fg="white",
                            bg=bg_color).grid(row=0, column=2, pady=1, padx=20, sticky="w")
        c1_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.cosmetic_tax ,bd=6, relief=SUNKEN).grid(row=0, column=3, pady=1,
                                                                                        padx=10)

        c2_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 14, "bold"), fg="white",
                            bg=bg_color).grid(row=1, column=2, pady=1, padx=20, sticky="w")
        c2_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.grocery_tax ,bd=6, relief=SUNKEN).grid(row=1, column=3, pady=1,
                                                                                        padx=10)

        c3_lbl = Label(F6, text="Cold Drink Tax", font=("times new roman", 14, "bold"), fg="white",
                             bg=bg_color).grid(row=2, column=2, pady=1, padx=20, sticky="w")
        c3_txt = Entry(F6, width=18, font=("Arial", 10),textvariable=self.cold_drink_tax ,bd=6, relief=SUNKEN).grid(row=2, column=3, pady=1,
                                                                                         padx=10)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn = Button(btn_f,text="Total",bg="#805500",command=self.total,fg="white",pady=15,width=9,font="arial 14 bold",bd=5).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_f, text=" Generate Bill",command=self.bill_area, bg="#805500", fg="white", pady=15, width=11, font="arial 14 bold",bd=5).grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_f, text="Clear", bg="#805500", fg="white", pady=15, width=9, font="arial 14 bold",bd=5).grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_f, text="Exit", bg="#805500", fg="white", pady=15, width=9, font="arial 14 bold",bd=5).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fc_p=(self.face_cream.get()*70)
        self.c_fw_p=(self.face_wash.get()*50)
        self.c_sp_p =(self.spray.get()*140)
        self.c_g_p=(self.gell.get()*60)
        self.c_l_p=(self.loshan.get()*45)
        self.total_cosmetic_price=(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_sp_p+
            self.c_g_p+
            self.c_l_p
        )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs."+str(round((self.total_cosmetic_price*0.05),2)))

        self.g_r_p=(self.rice.get() * 28)
        self.g_fo_p=(self.food_oil.get() * 150)
        self.g_d_p=(self.daal.get() * 32)
        self.g_w_P=(self.wheat.get() * 34)
        self.g_s_p=(self.sugar.get() * 40)
        self.g_t_p=(self.tea.get() * 50)
        self.total_grocery_price = (
                self.g_r_p +
                self.g_fo_p +
                self.g_d_p +
                self.g_w_P +
                self.g_s_p +
                self.g_t_p
        )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.grocery_tax.set("Rs."+str(round((self.total_grocery_price * 0.07),2)))

        self.cd_m_p=(self.maza.get() * 28)
        self.cd_c_p=(self.cock.get() * 40)
        self.cd_f_p=(self.frooti.get() * 39)
        self.cd_th_P=(self.thumbsup.get() * 34)
        self.cd_l_p=(self.limca.get() * 26)
        self.cd_s_p=(self.sprite.get() * 40)

        self.total_cold_drink_price = (
                self.cd_m_p+
                self.cd_c_p+
                self.cd_f_p+
                self.cd_th_P+
                self.cd_l_p +
                self.cd_s_p
        )
        self.cold_drink_price.set("Rs."+str(self.total_cold_drink_price))
        self.cold_drink_tax.set("Rs."+str(round((self.total_cold_drink_price * 0.09),2)))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"******Welcome Prathamesh Retail*****\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n====================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n====================================")



    def bill_area(self):
        self.welcome_bill()
        if self.soap.get()!=0 :
            self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
        if self.face_cream.get()!=0 :
            self.txtarea.insert(END, f"\nFace cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
        if self.face_wash.get()!=0 :
            self.txtarea.insert(END, f"\nFace wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
        if self.spray.get()!=0 :
            self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t{self.c_sp_p}")
        if self.gell.get()!=0 :
            self.txtarea.insert(END, f"\nHair Gel\t\t{self.gell.get()}\t{self.c_g_p}")
        if self.loshan.get()!=0 :
            self.txtarea.insert(END, f"\nLotion\t\t{self.loshan.get()}\t{self.c_l_p}")
        if self.rice.get()!=0 :
            self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t{self.g_r_p}")
        if self.food_oil.get()!=0 :
            self.txtarea.insert(END, f"\nFood OIl\t\t{self.food_oil.get()}\t{self.g_fo_p}")
        if self.daal.get()!=0 :
            self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t{self.g_d_p}")
        if self.wheat.get()!=0 :
            self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t{self.g_w_P}")
        if self.sugar.get()!=0 :
            self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t{self.g_s_p}")
        if self.tea.get()!=0 :
            self.txtarea.insert(END, f"\nTea\t\t{self.soap.get()}\t{self.g_t_p}")
        if self.maza.get()!=0 :
            self.txtarea.insert(END, f"\nMaza\t\t{self.maza.get()}\t{self.cd_m_p}")
        if self.cock.get()!=0 :
            self.txtarea.insert(END, f"\nCoke\t\t{self.cock.get()}\t{self.cd_c_p}")
        if self.frooti.get()!=0 :
            self.txtarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t{self.cd_f_p}")
        if self.thumbsup.get()!=0 :
            self.txtarea.insert(END, f"\nThumbs Up\t\t{self.thumbsup.get()}\t{self.cd_th_P}")
        if self.limca.get()!=0 :
            self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t{self.cd_l_p}")
        if self.sprite.get()!=0 :
            self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t{self.cd_s_p}")
        self.txtarea.insert(END, f"\n====================================")
        self.total_price=(self.total_cosmetic_price.get())+(self.total_grocery_price.get())+(self.total_cold_drink_price.get())
        self.txtarea.insert(END, f"\nTotal Bill : {self.total_price}")
        self.txtarea.insert(END, f"\n====================================")






root=Tk()
obj=Bill_App(root)
root.mainloop()
