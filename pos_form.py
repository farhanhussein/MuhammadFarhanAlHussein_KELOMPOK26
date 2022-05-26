from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from random import randint
from PIL import Image,ImageTk
import locale
from tkinter.font import Font

window = Tk()
class Pos:
    def __init__(self, window):
        self.window = window
        # Membuat tampilan GUI(ukuran, dll)
        window.geometry("1220x900")
        window.title("Pizza Corner")
        color = "sky blue"
        window.resizable(width=1, height=1)
        window.configure(bg=color)

                
        # Membuat Frame atas yang akan ditempatkan label
        bigfont = Font(
			family = "Comic Sans MS",
			size = 25, 
			weight = "bold",
			slant = "roman",
			underline = 0,
			overstrike=0)
        top_frame = Frame(window, bg=color, width=1200, height=50, relief="raise")
        top_frame.pack(side=TOP)
        # Membuat label/judul di frame
        title_label = Label(top_frame, text="Pizza Corner", font=bigfont, bg=color,
                            pady=0)
        title_label.grid(row=0, column=0)                    
        # Membuat frame kiri untuk tabs
        left_frame = Frame(window, bg="skyblue", width=600, height=520)
        left_frame.place(x=30+0.49, y=50)
        title_label.pack(side=TOP)
        # Membuat frame bawah untuk button nantinya
        bottom_frame = Frame(window, bg="grey", height=120, width=1210, relief="raise")
        bottom_frame.place(x=30, y=607)
        
        # Membuat Notebook yang ditampung oleh tabs_parent
        tabs_parent = ttk.Notebook(window, height=520, width=595)
        tabs_parent.place(x=31, y=50)
        # Membuat tab 1,2,3,4 untuk judul menu
        tab1 = Frame(tabs_parent, bg="grey", relief="raise")
        # Membuat label flavour
        label = Label(tab1, text="Flavour", font="arial 15 bold italic", bg="grey", fg="black")
        label.place(x=0, y=0)
        tab2 = Frame(tabs_parent, bg="grey", relief="raise")
        tab3 = Frame(tabs_parent, bg="grey", relief="raise")
        tab4 = Frame(tabs_parent, bg="grey", relief="raise")
        tab1.pack(fill="both", expand=1)
        tab2.pack(fill="both", expand=1)
        tab3.pack(fill="both", expand=1)
        tab4.pack(fill="both", expand=1)
        tabs_parent.add(tab1, text="Pizza")
        tabs_parent.add(tab2, text="Beverages")
        tabs_parent.add(tab3, text="Desserts")
        tabs_parent.add(tab4, text="Package")

        # Membuat checkbuttons untuk pizza di tab1 yang berada di tab_parent
        self.piz_ch_bt_1 = IntVar()
        piz1 = Checkbutton(tab1, text="Fajita", variable=self.piz_ch_bt_1, font="Helvetica 12 bold italic", 
                            bg="grey")
        piz1.place(x=0, y=40)

        self.piz_ch_bt_2 = IntVar()
        piz2 = Checkbutton(tab1, text="Chicken Tikka", variable=self.piz_ch_bt_2, font="Helvetica 12 bold italic",
                           bg="grey")
        piz2.place(x=0, y=90)

        self.piz_ch_bt_3 = IntVar()
        piz3 = Checkbutton(tab1, text="Cheese Lover", variable=self.piz_ch_bt_3, font="Helvetica 12 bold italic",
                           bg="grey")
        piz3.place(x=0, y=140)

        self.piz_ch_bt_4 = IntVar()
        piz4 = Checkbutton(tab1, text="Chicken Supreme", variable=self.piz_ch_bt_4, font="Helvetica 12 bold italic",
                           bg="grey")
        piz4.place(x=0, y=190)

        self.piz_ch_bt_5 = IntVar()
        piz5 = Checkbutton(tab1, text="Spicy Ranch", variable=self.piz_ch_bt_5, font="Helvetica 12 bold italic",
                           bg="grey")

        piz5.place(x=0, y=240)

        self.piz_ch_bt_6 = IntVar()
        piz6 = Checkbutton(tab1, text="Double Cheese Margherita", variable=self.piz_ch_bt_6,
                           font="Helvetica 12 bold italic", bg="grey")

        piz6.place(x=0, y=290)

        # Membuat widget optionmenu untuk menampilkan berapa banyak pizza yang dipesan di tab1 dan bisa di dropdown
        global list_menu
        list_menu = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.drop_op_piz_1 = StringVar()
        self.drop_op_piz_1.set(list_menu[0])
        drop1 = OptionMenu(tab1, self.drop_op_piz_1, *list_menu)

        self.drop_op_piz_2 = StringVar()
        self.drop_op_piz_2.set(list_menu[0])
        drop2 = OptionMenu(tab1, self.drop_op_piz_2, *list_menu)

        self.drop_op_piz_3 = StringVar()
        self.drop_op_piz_3.set(list_menu[0])
        drop3 = OptionMenu(tab1, self.drop_op_piz_3, *list_menu)

        self.drop_op_piz_4 = StringVar()
        self.drop_op_piz_4.set(list_menu[0])
        drop4 = OptionMenu(tab1, self.drop_op_piz_4, *list_menu)

        self.drop_op_piz_5 = StringVar()
        self.drop_op_piz_5.set(list_menu[0])
        drop5 = OptionMenu(tab1, self.drop_op_piz_5, *list_menu)

        self.drop_op_piz_6 = StringVar()
        self.drop_op_piz_6.set(list_menu[0])
        drop6 = OptionMenu(tab1, self.drop_op_piz_6, *list_menu)

        drop1.place(x=180, y=40)
        drop2.place(x=180, y=90)
        drop3.place(x=180, y=140)
        drop4.place(x=180, y=190)
        drop5.place(x=180, y=240)
        drop6.place(x=250, y=290)

        # Membuat widget optionmenu untuk menampilkan ukuran pizza yang dipesan di tab1
        self.s1 = StringVar()
        self.s1.set("size")
        list_menu2 = ["Small", "Medium", "Large"]
        size_opt1 = OptionMenu(tab1, self.s1, *list_menu2)
        size_opt1.place(x=270, y=40)
        self.s2 = StringVar()
        self.s2.set("Size")
        size_opt2 = OptionMenu(tab1, self.s2, *list_menu2)
        size_opt2.place(x=270, y=90)
        self.s3 = StringVar()
        self.s3.set("Size")
        size_opt3 = OptionMenu(tab1, self.s3, *list_menu2)
        size_opt3.place(x=270, y=140)
        self.s4 = StringVar()
        self.s4.set("Size")
        size_opt4 = OptionMenu(tab1, self.s4, *list_menu2)
        size_opt4.place(x=270, y=190)
        self.s5 = StringVar()
        self.s5.set("Size")
        size_opt5 = OptionMenu(tab1, self.s5, *list_menu2)
        size_opt5.place(x=270, y=240)
        self.s6 = StringVar()
        self.s6.set("Size")
        size_opt6 = OptionMenu(tab1, self.s6, *list_menu2)
        size_opt6.place(x=330, y=290)

        # Membuat checkbutton untuk minuman di tab2 
        label_2 = Label(tab2, text="Drinks", font="Helvetica 15 bold italic", bg="grey", fg="black")
        label_2.place(x=0, y=0)
        self.d_ch_bt_1 = IntVar()
        cd1 = Checkbutton(tab2, text="Orange Juice", variable=self.d_ch_bt_1, font="Helvetica 12 bold italic", bg="grey")
        cd1.place(x=0, y=40)
        self.d_ch_bt_2 = IntVar()
        cd2 = Checkbutton(tab2, text="Ice Tea", variable=self.d_ch_bt_2, font="Helvetica 12 bold italic", bg="grey")
        cd2.place(x=0, y=90)
        self.d_ch_bt_3 = IntVar()
        cd3 = Checkbutton(tab2, text="Pepsi", variable=self.d_ch_bt_3, font="Helvetica 12 bold italic", bg="grey")
        cd3.place(x=0, y=140)
        self.d_ch_bt_4 = IntVar()
        cd4 = Checkbutton(tab2, text="Sprite", variable=self.d_ch_bt_4, font="Helvetica 12 bold italic", bg="grey")
        cd4.place(x=0, y=190)
        self.d_ch_bt_5 = IntVar()
        cd5 = Checkbutton(tab2, text="Coca Cola", variable=self.d_ch_bt_5, font="Helvetica 12 bold italic", bg="grey")
        cd5.place(x=0, y=240)
        self.d_ch_bt_6 = IntVar()
        cd6 = Checkbutton(tab2, text="Ice Choco", variable=self.d_ch_bt_6, font="Helvetica 12 bold italic", bg="grey")
        cd6.place(x=0, y=290)

        # Membuat widget optionmenu untuk menampilkan berapa banyak yang dipesan di tab2
        self.drop_op_d_1 = StringVar()
        self.drop_op_d_1.set(list_menu[0])
        drop1b = OptionMenu(tab2, self.drop_op_d_1, *list_menu)
        self.drop_op_d_2 = StringVar()
        self.drop_op_d_2.set(list_menu[0])
        drop2b = OptionMenu(tab2, self.drop_op_d_2, *list_menu)
        self.drop_op_d_3 = StringVar()
        self.drop_op_d_3.set(list_menu[0])
        drop3b = OptionMenu(tab2, self.drop_op_d_3, *list_menu)
        self.drop_op_d_4 = StringVar()
        self.drop_op_d_4.set(list_menu[0])
        drop4b = OptionMenu(tab2, self.drop_op_d_4, *list_menu)
        self.drop_op_d_5 = StringVar()
        self.drop_op_d_5.set(list_menu[0])
        drop5b = OptionMenu(tab2, self.drop_op_d_5, *list_menu)
        self.drop_op_d_6 = StringVar()
        self.drop_op_d_6.set(list_menu[0])
        drop6b = OptionMenu(tab2, self.drop_op_d_6, *list_menu)

        drop1b.place(x=180, y=40)
        drop2b.place(x=180, y=90)
        drop3b.place(x=180, y=140)
        drop4b.place(x=180, y=190)
        drop5b.place(x=180, y=240)
        drop6b.place(x=180, y=290)

        # Membuat checkbutton untuk desserts di tab3 
        label_3 = Label(tab3, text="Dessert", font="Helvetica 15 bold italic", bg="grey", fg="black")
        label_3.place(x=0, y=0)
        self.s_ch_bt_1 = IntVar()
        sal1 = Checkbutton(tab3, text="Strawberry Ice Cream", variable=self.s_ch_bt_1, font="Helvetica 12 bold italic",
                           bg="grey")
        sal1.place(x=0, y=40)
        self.s_ch_bt_2 = IntVar()
        sal2 = Checkbutton(tab3, text="Strawberry Cake", variable=self.s_ch_bt_2, font="Helvetica 12 bold italic",
                           bg="grey")
        sal2.place(x=0, y=90)
        self.s_ch_bt_3 = IntVar()
        sal3 = Checkbutton(tab3, text="Chocolate Pie", variable=self.s_ch_bt_3, font="Helvetica 12 bold italic",
                           bg="grey")
        sal3.place(x=0, y=140)
        self.s_ch_bt_4 = IntVar()
        sal4 = Checkbutton(tab3, text="Chocolate Ice Cream", variable=self.s_ch_bt_4,
                           font="Helvetica 12 bold italic", bg="grey")
        sal4.place(x=0, y=190)
        self.s_ch_bt_5 = IntVar()
        sal5 = Checkbutton(tab3, text="Cheese Cake", variable=self.s_ch_bt_5, font="Helvetica 12 bold italic",
                           bg="grey")
        sal5.place(x=0, y=240)

        # Membuat optionmenu untuk desserts untuk memilih berapa banyak desserts yang dibeli di tab3
        global list_menu_s
        list_menu_s = ["0", "1", "2", "3", "4", "5"]
        self.drop_op_s1 = StringVar()
        self.drop_op_s1.set(list_menu_s[0])
        drop1s = OptionMenu(tab3, self.drop_op_s1, *list_menu_s)
        self.drop_op_s2 = StringVar()
        self.drop_op_s2.set(list_menu_s[0])
        drop2s = OptionMenu(tab3, self.drop_op_s2, *list_menu_s)
        self.drop_op_s3 = StringVar()
        self.drop_op_s3.set(list_menu_s[0])
        drop3s = OptionMenu(tab3, self.drop_op_s3, *list_menu_s)
        self.drop_op_s4 = StringVar()
        self.drop_op_s4.set(list_menu_s[0])
        drop4s = OptionMenu(tab3, self.drop_op_s4, *list_menu_s)
        self.drop_op_s5 = StringVar()
        self.drop_op_s5.set(list_menu_s[0])
        drop5s = OptionMenu(tab3, self.drop_op_s5, *list_menu_s)

        drop1s.place(x=220, y=40)
        drop2s.place(x=220, y=90)
        drop3s.place(x=220, y=140)
        drop4s.place(x=220, y=190)
        drop5s.place(x=220, y=240)

        # Membuat button dan label paket di tab4
        label_4 = Label(tab4, text="Package", font="Helvetica 18 bold italic", bg="grey", fg="black")
        label_4.place(x=240, y=0)
        deal1 = Button(tab4, text="Package 1", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal1_b())
        deal2 = Button(tab4, text="Package 2", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal2_b())
        deal3 = Button(tab4, text="Package 3", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal3_b())
        deal4 = Button(tab4, text="Package 4", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal4_b())
        deal5 = Button(tab4, text="Package 5", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal5_b())

        deal1.place(x=240, y=60)
        deal2.place(x=240, y=150)
        deal3.place(x=240, y=240)
        deal4.place(x=240, y=330)
        deal5.place(x=240, y=420)

        self.receipt_made = Text(window, width=73, height=30)
        self.receipt_made.place(x=650, y=110)


        # Membuat label struk di dalam textbox 
        title_label2 = Label(window, text="Receipt", font=("Aisha Latin Semibold", 18, "bold"), bg="grey", fg="black",
                             pady=10, padx=250)
        title_label2.place(x=650, y=50)
        #  Membuat button total, receipt, dan reset di frame bawah
        total = Button(bottom_frame, text="Total", font="Helvetica 12 bold italic", bg="grey",
                       command=lambda: self.total())
        total.place(x=50, y=6)

        receipt = Button(bottom_frame, text="Receipt", font="Helvetica 12 bold italic", bg="grey",
                         command=lambda: self.print_receipt())
        receipt.place(x=250, y=6)

        reset = Button(bottom_frame, text="Reset", font="Helvetica 12 bold italic", bg="grey",
                       command=lambda: self.reset_sales())
        reset.place(x=420, y=6)
        # Membuat label total yang ada di samping entry dan membuat entry
        total_x = Label(bottom_frame, text="Total:", font="Helvetica 12 bold italic", bg="grey")
        total_x.place(x=550, y=6)
        self.total_a = StringVar()
        self.total_x_e = Entry(bottom_frame, textvariable=self.total_a)
        self.total_x_e.place(x=600, y=6)

        # Membuat tanggal di dalam entry
        now = datetime.now()
        self.dt = now.strftime("%d-%m-%Y")
        self.tym = now.strftime("%H:%M")
        date_str = StringVar()
        date_str.set(str(self.dt))
        lbl_date = Label(bottom_frame, text="Date", font="Helvetica 12 bold italic", bg="grey")
        lbl_date.place(x=850, y=6)
        lbl_date = Entry(bottom_frame, textvariable=date_str)
        lbl_date.place(x=900, y=6)

        self.total_deals = 0
        self.deal1_p = 0
        self.deal2_p = 0
        self.deal3_p = 0
        self.deal4_p = 0
        self.deal5_p = 0

    global item_quantity_price
    item_quantity_price = []

    def error_handling(self, msg):
        if msg == "error!":
            messagebox.showerror("Error", "No Digits to compute!")
        elif msg == "division by zero!":
            messagebox.showerror("Error", "You can not divide a digit by zero!")

    # Method untuk total semua pesanan
    def total(self):
        try:
            # untuk pizza 1
            if self.piz_ch_bt_1.get() == 1:
                if self.s1.get() == "Large":
                    fajita_result = int(self.drop_op_piz_1.get()) * 100000
                    p1_t = ("Fajita Pizza", str(self.drop_op_piz_1.get()), "Rp100.000")
                elif self.s1.get() == "Medium":
                    fajita_result = int(self.drop_op_piz_1.get()) * 75000
                    p1_t = ("Fajita Pizza", str(self.drop_op_piz_1.get()), "Rp75.000")
                else:
                    fajita_result = int(self.drop_op_piz_1.get()) * 50000
                    p1_t = ("Fajita Pizza", str(self.drop_op_piz_1.get()), "Rp50.000")
                item_quantity_price.append(p1_t)
            else:
                fajita_result = 0
            # untuk pizza 2
            if self.piz_ch_bt_2.get() == 1:
                if self.s2.get() == "Large":
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 100000
                    p2_t = ("Chicken Tikka Pizza", str(self.drop_op_piz_2.get()), "Rp100.000")
                elif self.s2.get() == "Medium":
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 75000
                    p2_t = ("Chicken Tikka Pizza", str(self.drop_op_piz_2.get()), "Rp75.000")
                else:
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 50000
                    p2_t = ("Chicken Tikka Pizza", str(self.drop_op_piz_2.get()), "Rp50.000")
                item_quantity_price.append(p2_t)
            else:
                ch_tikka_result = 0
            # untuk pizza 3
            if self.piz_ch_bt_3.get() == 1:
                if self.s3.get() == "Large":
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 100000
                    p3_t = ("Cheese Lover Pizza", str(self.drop_op_piz_3.get()), "Rp100.000")
                elif self.s3.get() == "Medium":
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 75000
                    p3_t = ("Chesse Lover Pizza", str(self.drop_op_piz_3.get()), "Rp75.000")
                else:
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 50000
                    p3_t = ("Chesse Lover Pizza", str(self.drop_op_piz_3.get()), "Rp50.000")
                item_quantity_price.append(p3_t)
            else:
                chs_lover_result = 0
            # untuk pizza 4
            if self.piz_ch_bt_4.get() == 1:
                if self.s4.get() == "Large":
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 100000
                    p4_t = ("Chicken Supreme Pizza", str(self.drop_op_piz_1.get()), "Rp100.000")
                elif self.s4.get() == "Medium":
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 75000
                    p4_t = ("Chicken Supreme Pizza", str(self.drop_op_piz_4.get()), "Rp75.000")
                else:
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 50000
                    p4_t = ("Chicken Supreme Pizza", str(self.drop_op_piz_4.get()), "Rp50.000")
                item_quantity_price.append(p4_t)
            else:
                ch_supreme_result = 0
            # untuk pizza 5
            if self.piz_ch_bt_5.get() == 1:
                if self.s5.get() == "Large":
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 100000
                    p5_t = ("Spicy Ranch Pizza", str(self.drop_op_piz_5.get()), "Rp100.000")
                elif self.s5.get() == "Medium":
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 75000
                    p5_t = ("Spicy Ranch Pizza", str(self.drop_op_piz_5.get()), "Rp75.000")
                else:
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 50000
                    p5_t = ("Spicy Ranch Pizza", str(self.drop_op_piz_5.get()), "Rp50.000")
                item_quantity_price.append(p5_t)
            else:
                sp_ranch_result = 0
            # untuk pizza 6
            if self.piz_ch_bt_6.get() == 1:
                if self.s6.get() == "Large":
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 100000
                    p6_t = ("Double Cheese Margerita Pizza", str(self.drop_op_piz_6.get()), "Rp100.000")
                elif self.s6.get() == "Medium":
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 75000
                    p6_t = ("Double Cheese Margerita Pizza", str(self.drop_op_piz_6.get()), "Rp75.000")
                else:
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 50000
                    p6_t = ("Double Cheese Margerita Pizza", str(self.drop_op_piz_6.get()), "Rp50.000")
                item_quantity_price.append(p6_t)
            else:
                db_chs_marg_result = 0

            global total_all_pizzas
            self.total_all_pizzas = (
                        fajita_result + ch_tikka_result + chs_lover_result + sp_ranch_result + db_chs_marg_result + ch_supreme_result)
            # untuk minuman
            if self.d_ch_bt_1.get() == 1:
                d1r = int(self.drop_op_d_1.get()) * 20000
                d1_t = ("Orange Juice", str(self.drop_op_d_1.get()), "Rp20.000")
                item_quantity_price.append(d1_t)
            else:
                d1r = 0
            if self.d_ch_bt_2.get() == 1:
                d2r = int(self.drop_op_d_2.get()) * 10000
                d2_t = ("Ice Tea", str(self.drop_op_d_2.get()), "Rp10.000")
                item_quantity_price.append(d2_t)
            else:
                d2r = 0
            if self.d_ch_bt_3.get() == 1:
                d3r = int(self.drop_op_d_3.get()) * 10000
                d3_t = ("Pepsi", str(self.drop_op_d_3.get()), "Rp10.000")
                item_quantity_price.append(d3_t)
            else:
                d3r = 0
            if self.d_ch_bt_4.get() == 1:
                d4r = int(self.drop_op_d_1.get()) * 10000
                d4_t = ("Sprite", str(self.drop_op_d_4.get()), "10.000")
                item_quantity_price.append(d4_t)
            else:
                d4r = 0
            if self.d_ch_bt_5.get() == 1:
                d5r = int(self.drop_op_d_5.get()) * 10000
                d5_t = ("Coca cola", str(self.drop_op_d_5.get()), "Rp10.000")
                item_quantity_price.append(d5_t)
            else:
                d5r = 0
            if self.d_ch_bt_6.get() == 1:
                d6r = int(self.drop_op_d_6.get()) * 15000
                d6_t = ("Ice Chocolate", str(self.drop_op_d_6.get()), "Rp15.000")
                item_quantity_price.append(d6_t)
            else:
                d6r = 0

            global t_drink
            self.t_drink = (d1r + d2r + d3r + d4r + d5r + d6r)
            # untuk desserts
            if self.s_ch_bt_1.get() == 1:
                s1r = int(self.drop_op_s1.get()) * 25000
                s1_t = ("Strawberry Ice Cream", str(self.drop_op_s1.get()), "Rp25.000")
                item_quantity_price.append(s1_t)
            else:
                s1r = 0

            if self.s_ch_bt_2.get() == 1:
                s2r = int(self.drop_op_s2.get()) * 25000
                s2_t = ("Strawberry Cake", str(self.drop_op_s2.get()), "Rp25.000")
                item_quantity_price.append(s2_t)
            else:
                s2r = 0
            if self.s_ch_bt_3.get() == 1:
                s3r = int(self.drop_op_s3.get()) * 25000
                s3_t = ("Chocolate Pie", str(self.drop_op_s3.get()), "Rp25.000")
                item_quantity_price.append(s3_t)
            else:
                s3r = 0
            if self.s_ch_bt_4.get() == 1:
                s4r = int(self.drop_op_s4.get()) * 25000
                s1_4 = ("Chocolate Ice Cream", str(self.drop_op_s4.get()), "Rp25.000")
                item_quantity_price.append(s1_4)
            else:
                s4r = 0
            if self.s_ch_bt_5.get() == 1:
                s5r = int(self.drop_op_s5.get()) * 25000
                s5_t = ("Cheese Cake", str(self.drop_op_s5.get()), "Rp25.000")
                item_quantity_price.append(s5_t)
            else:
                s5r = 0

            global t_dessert
            self.t_dessert = (s1r + s2r + s3r + s4r + s5r)
            global total_all

            self.total_all = (self.total_deals + self.t_dessert + self.total_all_pizzas + self.t_drink)
            global sub_total

            global tax
            global service_charge

            self.tax = self.total_all * 0.01
            self.service_charge = self.total_all * 0.001
            self.sub_total = self.tax + self.service_charge + self.total_all
            
            if self.sub_total == 0:
                pass
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.sub_total)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.total_x_e.insert(0, str(currency))
            
        except NameError:
            self.error_handling("error!")

    def print_receipt(self):
        x = randint(390000, 500000)
        try:
            self.receipt_made.delete("1.0", END)
            self.receipt_made.insert(END, "\t\t\t   Farhan Pizza" + "\n")
            self.receipt_made.insert(END, "\t\t\t   Sale Receipt" + "\n")
            self.receipt_made.insert(END, " " + "\n")
            self.receipt_made.insert(END, "Invoice# " + str(x) + "\n\n")

            self.receipt_made.insert(END, "Operator name: Farhan\n\n")
            self.receipt_made.insert(END, "Date:{}\t\t\tTime:{}\n".format(self.dt, self.tym))

            x = 0
            y = 1
            while True:
                self.receipt_made.insert(END, "Item {}: {} \nquantity: {:.2}, price 1: {:.5}000\n\n".format(y,
                                                                                                   item_quantity_price[
                                                                                                       x][0],
                                                                                                   item_quantity_price[
                                                                                                       x][1],
                                                                                                   item_quantity_price[
                                                                                                       x][2]))

                x += 1
                y += 1

                if x < len(item_quantity_price):
                    continue
                else:
                    break

            self.receipt_made.insert(END, " " + "\n")
            if self.total_all_pizzas == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.total_all_pizzas)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Total of pizzas: "+currency+ "\n")

            if self.t_drink == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.t_drink)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Total of drinks: "+currency+ "\n")

            if self.t_dessert == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.t_dessert)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Total of desserts: "+currency+ "\n")

            if self.total_deals == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.total_deals)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Total of package: "+currency+ "\n")

            if self.total_all == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.tax)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Tax: "+currency+ "\n")
                
            if self.service_charge == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.service_charge)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Service charges: "+currency+ "\n")

            if self.sub_total == 0:
                self.receipt_made.insert(END, "")
            else:
                thousands_separator = "."
                fractional_separator = ","
                currency = "Rp{:,.2f}".format(self.sub_total)
                if thousands_separator == ".":
                    main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
                    new_main_currency = main_currency.replace(",", ".")
                    currency = new_main_currency + fractional_separator + fractional_currency
                    self.receipt_made.insert(END, "Total: "+currency+ "\n")

            
            self.receipt_made.insert(END, " " + "\n")
            self.receipt_made.insert(END, "\t\t\t***** THANK YOU *****" + "\n")
        except IndexError:
            messagebox.showerror("Error!", "select items first! Thank you!")
        except NameError:
            messagebox.showerror("Error!", "select items first! Thank you!")

    def deal1_b(self):
        global total_deals
        global deal1_p
        # package 1
        deal1_p = 125000
        tup_d1 = ("1 Large Pizza + 1 Orange Juice + 6 Chicken Nuggets", "1", "Rp125.000")
        item_quantity_price.append(tup_d1)
        self.total_deals += deal1_p

    def deal2_b(self):
        global total_deals
        global deal2_p
        # package 2
        deal2_p = 90000
        tup_d2 = ("1 Medium Pizza + 1 Coca cola + 6 Chicken Nuggets", "1", "Rp90.000")
        item_quantity_price.append(tup_d2)
        self.total_deals += deal2_p

    def deal3_b(self):
        global total_deals
        global deal3_p
        # package 3
        deal3_p = 75000
        tup_d3 = ("1 Small Pizza + 6 Chicken Nuggets", "1", "Rp75.000")
        item_quantity_price.append(tup_d3)
        self.total_deals += deal3_p

    def deal4_b(self):
        global total_deals
        global deal4_p
        # package 4
        deal4_p = 65000
        tup_d4 = ("3 Small Pizza + 1 Desserts + 1 Coca-cola", "1", "Rp65.000")
        item_quantity_price.append(tup_d4)
        self.total_deals += deal4_p

    def deal5_b(self):
        global total_deals
        global deal5_p
        # package 5
        deal5_p = 73000
        tup_d4 = ("2 Medium Pizza + 1 Desserts + 2 Sprite", "1", "Rp73.000")
        item_quantity_price.append(tup_d4)
        self.total_deals += deal5_p

    # untuk reset
    def reset_sales(self):

        try:
            self.piz_ch_bt_1.set(0)
            self.piz_ch_bt_2.set(0)
            self.piz_ch_bt_3.set(0)
            self.piz_ch_bt_4.set(0)
            self.piz_ch_bt_5.set(0)
            self.piz_ch_bt_6.set(0)

            self.drop_op_piz_1.set(list_menu[0])
            self.drop_op_piz_2.set(list_menu[0])
            self.drop_op_piz_3.set(list_menu[0])
            self.drop_op_piz_4.set(list_menu[0])
            self.drop_op_piz_5.set(list_menu[0])
            self.drop_op_piz_6.set(list_menu[0])

            self.s1.set("size")
            self.s2.set("size")
            self.s3.set("size")
            self.s4.set("size")
            self.s5.set("size")
            self.s6.set("size")

            self.d_ch_bt_1.set(0)
            self.d_ch_bt_2.set(0)
            self.d_ch_bt_3.set(0)
            self.d_ch_bt_4.set(0)
            self.d_ch_bt_5.set(0)
            self.d_ch_bt_6.set(0)

            self.drop_op_d_1.set(list_menu[0])
            self.drop_op_d_2.set(list_menu[0])
            self.drop_op_d_3.set(list_menu[0])
            self.drop_op_d_4.set(list_menu[0])
            self.drop_op_d_5.set(list_menu[0])
            self.drop_op_d_6.set(list_menu[0])

            self.s_ch_bt_1.set(0)
            self.s_ch_bt_2.set(0)
            self.s_ch_bt_3.set(0)
            self.s_ch_bt_4.set(0)
            self.s_ch_bt_5.set(0)

            self.drop_op_s1.set(list_menu_s[0])
            self.drop_op_s2.set(list_menu_s[0])
            self.drop_op_s3.set(list_menu_s[0])
            self.drop_op_s4.set(list_menu_s[0])
            self.drop_op_s5.set(list_menu_s[0])

            global total_deals
            self.total_deals = 0
            global deal1_p, deal2_p, deal3_p, deal4_p, deal5_p
            global total_all_pizzas, t_drink, t_dessert
            self.total_all_pizzas = 0
            self.t_drink = 0
            self.t_dessert = 0
            global item_quantity_price
            item_quantity_price.clear()
            self.total_x_e.delete(0, END)
            self.receipt_made.delete("1.0", END)
            
            
            messagebox.showinfo("Next Customer!", "Serve the next customer please!")
        except NameError:
            messagebox.showerror("error nothing to clear")


ob = Pos(window)
window.mainloop()

