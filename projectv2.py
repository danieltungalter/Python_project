import cx_Oracle
from tkinter import *

def item_A_show_customer_info():
    window_01 = Toplevel(window_00)
    window_01.geometry("800x600")
    centre_window(window_01)
    window_01.title('Information of All Customers')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Show Information of All Customers')
    label.pack(padx=30, pady=10)

    listbox = Listbox(window_01,font='consolas')
    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    listbox.insert(END, "{:<20s}❙{:<20s}❙{:<30s}".format("Account No.", "Customer Name", "Address"))

    cur.execute('Select * from customer')

    for row in cur.fetchall():
        listbox.insert(END, "{:<20s}❙{:<20s}❙{:<30s}".format(row[0], row[1], row[2]))

def item_A_show_meter_info():
    window_01 = Toplevel(window_00)
    window_01.geometry("800x600")
    centre_window(window_01)
    window_01.title('Information of All Electric Meter')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Show Information of All Electric Meter')
    label.pack(padx=30, pady=10)

    listbox = Listbox(window_01,font='consolas')
    listbox.pack(side=LEFT, fill=BOTH, expand=1)
    listbox.insert(END, "{:<20s}❙{:<20s}❙{:<30s}❙{}".format("Meter No.", "Reading Date", "Reading Value", "Units"))
    cur.execute('Select meter_num, to_char(reading_date, \'MON-YY\'), reading_value, units from reading')

    for row in cur.fetchall():
        listbox.insert(END, "{:<20s}❙{:<20s}❙{:<30d}❙{}".format(row[0], row[1], row[2], row[3]))


def item_B1_action():
    def search_fuel_charge():
        window_02 = Toplevel(window_01)
        window_02.geometry("800x600")
        centre_window(window_02)
        window_02.title('Result of Fuel Charge of that Month')
        window_02.resizable(width=False, height=False)

        algebra1 = val_01.get()
        algebra2 = val_02.get()
        if algebra1 == '':
            algebra1 = "Insert Day"
            sql = "Select to_char(fuel_date, \'MON-YY\'), fuel_charge FROM fuel_charge WHERE to_char(fuel_date, 'YYYY') = '" + algebra2 + "'"
        elif algebra2 == '':
            algebra2 = "Insert Month"
            sql = "Select to_char(fuel_date, \'MON-YY\'), fuel_charge FROM fuel_charge WHERE to_char(fuel_date, 'MM') = '" + algebra1 + "'"
        else:
            sql = "Select to_char(fuel_date, \'MON-YY\'), fuel_charge FROM fuel_charge WHERE to_char(fuel_date, 'MM-YYYY') = '" + algebra1 + "-"+ algebra2 + "'"

        listbox = Listbox(window_02)
        listbox = Listbox(window_02, font='consolas')
        listbox.pack(side=LEFT, fill=BOTH, expand=1)
        cur.execute(sql)

        listbox.insert(END, "{:<20s}❙{}".format("Month  Year", "Fuel Charge"))
        for row in cur.fetchall():
            listbox.insert(END, "{:<20s}❙{}".format(row[0], row[1]))


    window_01 = Toplevel(window_00)
    window_01.geometry("320x100")
    centre_window(window_01)
    window_01.title('Search Fuel Charge')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Fuel Charge')

    Label(window_01, text="Please Insert Month (01-12): ").grid(row=0,column=0,sticky=W)
    Label(window_01, text="Please Insert Year (201X): ").grid(row=1,sticky=W)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)
    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)

    Button(window_01, text='Search', command=search_fuel_charge).grid(row=2, column=1)



def item_B2_action():
    def meter_belongs_to_cust():
        window_02 = Toplevel(window_01)
        window_02.geometry("800x600")
        centre_window(window_02)
        window_02.title('Result')
        window_02.resizable(width=False, height=False)

        algebra1 = val_01.get()
        if algebra1 != '':
            algebra1 = algebra1.upper()
        else:
            algebra1 = "Account No. Incorrect"


        algebra2 = val_02.get()
        if algebra2 !='':
            algebra2 = algebra2.upper()
        else:
            algebra2 = "Name Incorrect"

        sql = "Select * from customer where account_num  = '" + algebra1 + "' OR UPPER(cust_name) LIKE '%" + algebra2 + "%'"

        listbox = Listbox(window_02)
        listbox = Listbox(window_02, font='consolas')
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        cur.execute(sql)
        listbox.insert(END, "{:<20s}❙{:<20s}❙{}".format("Account No.", "Customers\' Name", "Address"))
        for row in cur.fetchall():
            listbox.insert(END, "{:<20s}❙{:<20s}❙{}".format(row[0], row[1], row[2]))
            listbox.insert(END, "")
            sql1 = "Select meter_num from meter where account_num = '{}'".format(row[0])
            cur1.execute(sql1)
            listbox.insert(END, "{:<12s}: ".format("Meters\' of customer"))
            for row1 in cur1.fetchall():
                listbox.insert(END, "{} ".format(row1[0]))
            listbox.insert(END, " ")

    window_01 = Toplevel(window_00)
    window_01.geometry("630x80")
    centre_window(window_01)
    window_01.title('Search Meter Belongs to Customer by Account No or Customers\' Name')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Search Meter Belongs to Customer by Account No or Customers\' Name')

    Label(window_01, text="Please Insert Account  No. :").grid(row=0,column=0,sticky=W)
    Label(window_01, text="Please Insert Name :").grid(row=1,sticky=W)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)

    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)

    Button(window_01, text='Search', command=meter_belongs_to_cust).grid(row=2, column=1)

def item_C1_action():
    def meter_history():
        window_02 = Toplevel(window_01)
        window_02.geometry("800x600")
        centre_window(window_02)
        window_02.title('Result')
        window_02.resizable(width=False, height=False)

        algebra1 = val_01.get()
        if algebra1 != '':
            algebra1 = algebra1.upper()
        else:
            algebra1 = "NO AC NUM"

        listbox = Listbox(window_02)
        listbox = Listbox(window_02, font='consolas')
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

        if algebra1 == "NO AC NUM":
            listbox.insert(END, "Please Input a Correct Account Number")
        else:
            order_method = var.get()
            if order_method == 1:
                sql = "Select meter_num,to_char(reading_date,'MON-YY'), reading_value " \
                      "From reading Where meter_num In (Select meter_num FROM meter Where Upper(account_num) = '" + algebra1 + "') Order by reading_date"
            elif order_method == 2:
                sql = "Select meter_num,to_char(reading_date,'MON-YY'), reading_value " \
                      "From reading Where meter_num In (Select meter_num " \
                      "From meter Where Upper(account_num) = '" + algebra1 + "') Order by meter_num"
            elif order_method == 3:
                sql = "Select meter_num,to_char(reading_date,'MON-YY'), reading_value " \
                      "From reading Where meter_num In (Select meter_num " \
                      "FROM meter Where Upper(account_num) = '" + algebra1 + "') Order by reading_value"
            else:
                sql = "Select meter_num,to_char(reading_date,'MON-YY'), reading_value " \
                      "From reading Where meter_num In (Select meter_num FROM meter Where Upper(account_num) = '" + algebra1 + "')"

            cur.execute(sql)
            row = cur.fetchall()

            if cur.rowcount == 0:
                listbox.insert(END, "Sorry, No Data of this Account No.")
                listbox.insert(END, "")
                listbox.insert(END, "Please Insert Correct Account No.")
            else:
                # print(cur.rowcount)
                sql1 = "Select cust_name from customer where account_num = '" + algebra1 + "'"
                cur1.execute(sql1)
                row1 = cur1.fetchone()
                listbox.insert(END, "Here are the meter history  of {} ({}):".format(row1[0], algebra1))
                listbox.insert(END, "")
                if order_method == 1:
                    listbox.insert(END, "Results are Sort by Reading Date")
                elif order_method == 2:
                    listbox.insert(END, "Results are Sort by Meter No.")
                elif order_method == 3:
                    listbox.insert(END, "Results are Sort by Reading")
                listbox.insert(END, "{:<15s}❙{:<15s}❙{}".format("Meter No.", "Reading Date", "Reading Value"))
                for row in row:
                    listbox.insert(END, "{:<15s}❙{:<15s}❙{}".format(row[0], row[1], row[2]))


    window_01 = Toplevel(window_00)
    window_01.geometry("300x100")
    centre_window(window_01)
    window_01.title('Search customer by Account No.')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Search customer by Account No.')

    Label(window_01, text="Account  No: ").grid(row=0, column=0, sticky=W)
    val_01 = Entry(window_01)
    val_01.grid(row=0, column=1)

    Label(window_01, text="Sort by: ").grid(row=1, column=0, sticky=W)
    var = StringVar(window_01)
    choices = { 'Reading Date', 'Meter No.', 'Reading Value'}
    var.set('Reading Date')
    ChoiceMenu = OptionMenu(window_01, var, *choices)
    Label(window_01, text = 'Sort by: ')
    ChoiceMenu.grid(row = 1, column = 1)


    Button(window_01, text='Search', command=meter_history).grid(row=3, column=1)

def item_C2_action():
    def electric_bills():
        window_02 = Toplevel(window_01)
        window_02.geometry("1500x600")
        centre_window(window_02)
        window_02.title('Result')
        window_02.resizable(width=False, height=False)

        algebra1 = val_01.get()
        if algebra1 != '':
            algebra1 = algebra1.upper()
        else:
            algebra1 = "Incorrect Account No. "


        algebra2 = val_02.get()
        if algebra2 != '':
            algebra2 = algebra2.upper()
        else:
            algebra2 = "Incorrect Date (MM-YYYY)"

        sql1 = "Select c.bill_num,c.account_num,to_char(c.bill_date),to_char(c.before_pay), r.meter_num,to_char(r.reading_date),to_char(r.reading_value),to_char(r.units * fc.fuel_charge/100) From reading r " \
              "Join fuel_charge fc On (to_char(r.reading_date,'MM-YYYY') = to_char(fc.fuel_date,'MM-YYYY')) Join meter m On (r.meter_num = m.meter_num) " \
              "inner join customer_bill c on m.account_num = c.account_num and to_char(r.reading_date,'MM-YYYY') = to_char(c.bill_date,'MM-YYYY') " \
              "Where m.account_num = '" + algebra1 + "' And to_char(r.reading_date,'MM-YYYY') = '" + algebra2 + "' Order by r.meter_num"
        cur.execute(sql1)
        result_set1 = cur.fetchall()
        #print(sql)
        sql2 = "Select SUM(r.units * fc.fuel_charge/100) From reading r " \
              "Join fuel_charge fc On (to_char(r.reading_date,'MM-YYYY') = to_char(fc.fuel_date,'MM-YYYY')) Join meter m On (r.meter_num = m.meter_num) " \
              "inner join customer_bill c on m.account_num = c.account_num and to_char(r.reading_date,'MM-YYYY') = to_char(c.bill_date,'MM-YYYY') " \
              "Where m.account_num = '" + algebra1 + "' And to_char(r.reading_date,'MM-YYYY') <= '" + algebra2 + "' Order by r.meter_num"
        cur.execute(sql2)
        result_set2 = cur.fetchall()

        listbox = Listbox(window_02)
        listbox = Listbox(window_02, font='consolas')
        listbox.pack(side=LEFT, fill=BOTH, expand=1)
        listbox.insert(END, "{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{}".format("Bill Number", "Account Number", "Date of bill", "Due date of bill","Meter No.", "Reading Date", "Reading Value", "Charge"))

        for row in result_set1:
            listbox.insert(END, "{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{}".format(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7]))

        listbox.insert(END, " ")
        listbox.insert(END, "Total amounts: ")
        listbox.insert(END, result_set2)

    window_01 = Toplevel(window_00)
    window_01.geometry("350x100")
    centre_window(window_01)
    window_01.title('Search Electric Bill by Account No and Date.')
    window_01.resizable(width=False, height=False)
    label = Label(window_01, text='Search Electric Bill by Account No and Date.')

    Label(window_01, text="Please Insert Account  No. :").grid(row=0,column=0,sticky=W)
    Label(window_01, text="Please Insert Date (MM-YYYY) :").grid(row=1,sticky=W)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)

    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)

    Button(window_01, text='Search', command=electric_bills).grid(row=2, column=1)

def item_C3_action():
    def search_by_date():
        window_02 = Toplevel(window_01)
        window_02.geometry("1500x600")
        centre_window(window_02)
        sql1 = "Select  coalesce(sum(r.units * f.fuel_charge/100),0)  from reading r " \
              "inner join fuel_charge f on to_char(r.reading_date,'MM-YYYY') = to_char(f.fuel_date,'MM-YYYY')" \
              "inner join meter m on r.meter_num = m.meter_num " \
              "inner join customer_bill c on m.account_num = c.account_num and to_char(r.reading_date,'MM-YYYY') = to_char(c.bill_date,'MM-YYYY') " \
              "where m.account_num = '" + val_01.get() + "' and to_char(add_months(r.reading_date,1),'MM-YYYY') <= '" + val_02.get() + "'  and c.paid_date is null " \
              "order by r.meter_num asc"
        cur.execute(sql1)
        arrears = cur.fetchall()

        sql2 ="Select c.bill_num,c.account_num,to_char(c.bill_date),to_char(c.before_pay), r.meter_num,to_char(r.reading_date),to_char(r.reading_value),to_char(r.units * f.fuel_charge/100) From reading r " \
              "inner join fuel_charge f on to_char(r.reading_date,'MM-YYYY') = to_char(f.fuel_date,'MM-YYYY')" \
              "inner join meter m on r.meter_num = m.meter_num " \
              "inner join customer_bill c on m.account_num = c.account_num and to_char(r.reading_date,'MM-YYYY') = to_char(c.bill_date,'MM-YYYY') " \
              "where m.account_num = '" + val_01.get() + "' and to_char(r.reading_date,'MM-YYYY') <= '" + val_02.get() + "' and c.paid_date is null   " \
              "order by c.bill_date,r.meter_num asc"
        cur.execute(sql2)
        result_set = cur.fetchall()

        sql3 ="Select coalesce(sum(r.units * f.fuel_charge/100),0) from  reading r " \
              "inner join fuel_charge f on to_char(r.reading_date,'MM-YYYY') = to_char(f.fuel_date,'MM-YYYY')" \
              "inner join meter m on r.meter_num = m.meter_num " \
              "inner join customer_bill c on m.account_num = c.account_num and to_char(r.reading_date,'MM-YYYY') = to_char(c.bill_date,'MM-YYYY') " \
              "where m.account_num = '" + val_01.get() + "' and to_char(r.reading_date,'MM-YYYY') = '" + val_02.get() + "'  " \
              "order by r.meter_num asc"
        cur.execute(sql3)
        amounts = cur.fetchall()

        listbox = Listbox(window_02)
        listbox = Listbox(window_02, font='consolas')
        listbox.pack(side=LEFT, fill=BOTH, expand=1)
        listbox.insert(END, "{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{}".format("Bill Number","Account Number","Date of bill","Due date of bill","Meter No.","Reading Date","Reading Value","Charge"))

        for row in result_set:
            listbox.insert(END,"{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{:<20s}❙{}".format(row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7]))

        listbox.insert(END, "")
        listbox.insert(END, "Arrears  of previous month: ")
        listbox.insert(END, arrears)
        listbox.insert(END, "Amount  of this month: ")
        listbox.insert(END, amounts)
        listbox.insert(END, "Please pay this amounts: ")
        listbox.insert(END, list(x + y for x, y in zip(arrears[0], amounts[0])))

    def update_paid_date():
        sql3 = "Update customer_bill set paid_date = to_date('" + val_03.get() + "','DD-MM-YYYY') where account_num  = '" + val_01.get() + "' and to_char(bill_date,'MM-YYYY') = '" + val_02.get() + "'  "
        cur.execute(sql3)

    window_01 = Toplevel(window_00)
    window_01.geometry("300x120")
    centre_window(window_01)
    window_01.title('')
    label = Label(window_01, text='Search by Date')

    Label(window_01, text="Account Number").grid(row=0)
    Label(window_01, text=" Month & Year (MM-YYYY)").grid(row=1)
    Label(window_01, text=" Update Paid date").grid(row=3)

    val_01 = Entry(window_01)
    val_02 = Entry(window_01)
    val_03 = Entry(window_01)

    val_01.grid(row=0, column=1)
    val_02.grid(row=1, column=1)
    val_03.grid(row=3, column=1)

    Button(window_01, text='Search', command=search_by_date).grid(row=2, column=1)
    Button(window_01, text='Update', command=update_paid_date).grid(row=4, column=1)

def centre_window(window):
    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

def create_menu(window):

    my_menu = Menu(window)
    window.config(menu=my_menu)

    # ----Item A----#
    item_A = Menu(my_menu)
    my_menu.add_cascade(label="Records", menu=item_A)
    item_A.add_command(label="Show Information of All Customers", command=item_A_show_customer_info)
    item_A.add_command(label="Show Information of all Electric Meter", command=item_A_show_meter_info)
    item_A.add_separator()
    item_A.add_command(label="Exit", command=window.quit)

    # ----Item B----#
    item_B = Menu(my_menu)
    my_menu.add_cascade(label="Search", menu=item_B)
    item_B.add_command(label="Fuel Charge of Month", command=item_B1_action)
    item_B.add_command(label="Meters Information of Customer", command=item_B2_action)

    # ----Item C----#
    item_C = Menu(my_menu)
    my_menu.add_cascade(label="Check Data", menu=item_C)
    item_C.add_command(label="Meter Data with History", command=item_C1_action)
    item_C.add_command(label="Electric Bills", command=item_C2_action)
    item_C.add_command(label="Paid Bill", command=item_C3_action)



"""Main Program"""
#----Connect Oracle----#
conn = cx_Oracle.connect('team004/ceteam004@144.214.178.70/xe')
cur = conn.cursor()
cur1 = conn.cursor()

window_00 = Tk()
x = PhotoImage(file="F:\\PycharmProjects\\206cdepj\\HK_Electric_Bill.png")
w1 = Label(window_00, image = x,bg = "white").pack(fill=BOTH, expand=1)
window_00.geometry('500x500')
window_00.title('206CDE Project - HK Electric Bills')
window_00.resizable(width=False, height=False)
centre_window(window_00)
create_menu(window_00)


mainloop()


