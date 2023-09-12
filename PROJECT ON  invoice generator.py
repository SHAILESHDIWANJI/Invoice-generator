from tkinter import *
from fpdf import FPDF
import PyPDF2
window=Tk()
window.title("invoice generator")

medicines={
    "medicine A":10,
    "medicine B":20,
    "medicine C":30,
    "medicine D":40
}
invoice_items=[]


def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)
    quantity=int(quantity_entry.get())
    price=medicines[selected_medicine]
    item_total=price*quantity
    invoice_items.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total + item[2]
    return total
    
def update_invoice_text():
    invoice_text.delete(1.0,END)
    for item in invoice_items:
        invoice_text.insert(END,f"medicine:{item[0]},quntity:{item[1]},total:{item[2]}")
medicine_label=Label(window,text="medicine: ")

def generate_invoice():
    custome_name=custome_entry.get()
    
    
    pdf=FPDF()
    pdf.add_page()
    
    pdf.cell(0,10,txt="invoice",new_x="LMARGIN",new_y="NEXT",align="C")
    pdf.cell(0,10,txt="customer name: "+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,txt="",new_x="LMARGIN",new_y="NEXT")
    
    for item in invoice_items:
        medicine_name,quantity,item_total=total
        pdf.cell(0,10,txt=f"medicine:{medicine_name},quantity: {quantity},total:{item_total}",new_x="LMARGINE",new_y="NEXT",align="L")
    pdf.cell(0,10,txt="total amount: "+str(calculate_total()),new_x="LMARGIN",new_y="NEXT",align="L")

    pdf.output("invoice.pdf")
medicine_label.pack()
medicine_listbox=Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)
medicine_listbox.pack()


quantity_label=Label(window,text="quantity")
quantity_label.pack()
quantity_entry=Entry()
quantity_entry.pack()

add_button=Button(window,text="add medicine",command=add_medicine)
add_button.pack()


total_amount_label=Label(window,text="total amount")
total_amount_label.pack()

total_amount_entry=Entry()
total_amount_entry.pack()

custome_label=Label(window,text="customer name: ")
custome_label.pack()
custome_entry=Entry(window)

custome_entry.pack()

generate_button=Button(window,text="generate invoice",command=generate_invoice)
generate_button.pack()

invoice_text=Text(window,height=10,width=50)
invoice_text.pack()

window.mainloop()