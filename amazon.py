class product:
    def __init__(self, product_id,product_name, product_price, product_count):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_count = product_count ###Need to add the product count into the product object, for checking out of stock info
    def get_product_info(self):
        print("Product Id: ",self.product_id)
        print("Product Name: ",self.product_name)
        print("Product Price: ",self.product_price)
        print("Note : Current stock of this product :=", self.product_count)
        ### Need not display the stock details, only used at the backened for the cart management
    def update_product_info(self,pro_name,pro_price, prod_stock_count):
        self.product_name = pro_name
        self.product_price = pro_price
        print("\n\n",prod_stock_count)
        self.product_count = prod_stock_count
        # print("Enter the corresponding number to update attributes \n 1: Product Name \n 2: Product Price \n")
        # choice = int(input())
        # if(choice == 1):
        #     print("Enter new product name: ")
        #     product_name = input()
        #     self.product_name = product_name
        
        # elif(choice == 2):
        #     print("Enter new product price: ")
        #     product_price_updated = float(input())
        #     self.product_price = product_price_updated
        
        # else:
        #     print("Incorrect choice entered!")

        
class inventory:
    def __init__(self):
        self.inventory_count = 0
        self.inventory_products = {}

    def add_product_to_inventory(self,product_id,product_name,product_price, product_stock):
        # list_of_product_ids = list(self.inventory_products.keys())
        # print("Enter product Id: ")
        # product_id = int(input())
        # if(product_id not in list_of_product_ids):
        #     print("Enter product Name: ")
        #     product_name = input()
        #     print("Enter product price: ")
        #     product_price = float(input())
        # else:
        #     print("Product Id already exists ,Please enter valid product Id: ")
        #     return
        product_id = int(product_id)
        product_price = float(product_price)
        product_count = int(product_stock)
        composite_product = product(product_id,product_name,product_price, product_count)
        self.inventory_products[product_id] = composite_product
        self.inventory_count +=1

    def get_product_info_from_inventory(self,product_id):
        # product_id = int(input("Enter the product Id to get info about:"))
        list_of_product_ids = list(self.inventory_products.keys())
        if(product_id in list_of_product_ids):
            req_prod = self.inventory_products[product_id]
            req_prod.get_product_info()
            # print("product Id: ",req_prod.product_id)
            # print("product name: ",req_prod.product_name)
            # print("product price: ",req_prod.product_price)
        else:
            print("Product Id does not exists ,Please enter valid product Id: ")
            return

    def update_product_in_inventory(self,product_id,product_name,product_price, prod_stock_increm, prod_stock_decrem):
        # product_id = int(input("Enter the product Id to update info about:"))
        product_id = int(product_id)
        list_of_product_ids = list(self.inventory_products.keys())
        if(product_id in list_of_product_ids):
            req_prod = self.inventory_products[product_id]
            if(product_name == ""):
                arg_product_name = req_prod.product_name
            else:
                arg_product_name = product_name
            if(product_price == ""):
                arg_product_price = req_prod.product_price
            else:
                arg_product_price = float(product_price)
            ### (cart_managing - aps)
            if(prod_stock_increm == ""):
                arg_product_count = req_prod.product_count
            else:
                arg_product_count = req_prod.product_count + int(prod_stock_increm)
            if(prod_stock_decrem == "" and prod_stock_increm == ""):
                arg_product_count = req_prod.product_count
            elif(prod_stock_increm == ""):
                if(int(prod_stock_decrem) > req_prod.product_count):
                    print("Error: update value increases beyond current stock")
                else:
                    arg_product_count = req_prod.product_count - int(prod_stock_decrem)
                    ############################################################################(aps)
                    ### Also call a function here to check whether the products in the cart have to removed because the stock has become 0 now ###
                    #############################################################################
            elif(prod_stock_decrem != "" and prod_stock_increm != ""):
                arg_product_count = arg_product_count - int(prod_stock_increm)
                print("Please enter either increase stock or decrease stock")

            req_prod.update_product_info(arg_product_name,arg_product_price, arg_product_count)
        else:
            print("Product Id does not exists ,Please enter valid product Id: ")
            return

    def list_all_products_in_inventory(self):
        print("Number of products in inventory: ",self.inventory_count,"\nThe products in inventory are:\n")
        for id in self.inventory_products:
            self.inventory_products[id].get_product_info()
            # print("Product count :",self.inventory_products[id].product_count)
    
    def delete_product_in_inventory(self,product_id):
        # product_id = int(input("Enter the product Id of the product to be deleted: "))
        self.inventory_products.pop(product_id)
        print("Product with Id = ",product_id," deleted")
        self.inventory_count -= 1

class cart:
    def __init__(self):
        self.cart_count = 0
        self.cart_products_ids = []

    def add_product_to_cart(self,product_id):
        ### Before adding to the cart check the stock of the item to be added to the cart
        product_id = int(product_id)
        self.cart_products_ids.append(product_id)
        self.cart_count +=1

    def list_all_products_in_cart(self):
        # print("Number of products in cart: ",self.cart_count,"\nThe products in cart are:\n")
        # for id in self.cart_products_ids:
            # prod = inventory_p.inventory_products[id]
            # inventory1.inventory_products[id].get_product_info()
        return list(self.cart_products_ids)
    
    def delete_product_in_cart(self,product_id):
        self.cart_products_ids.remove(product_id)
        # print("Product with Id = ",product_id," deleted")
        self.cart_count -= 1

def print_cart_products():
    print("The products in you cart are")
    cart_pro_ids = cart1.list_all_products_in_cart()
    for id in cart_pro_ids:
        inventory1.get_product_info_from_inventory(id)  ###(aps) Also prints the stock details notifing the user about the current status of the product
# product1 = product(123,"watch",1500.00)
# product1.get_product_info()
# product1.update_product_info()
# product1.get_product_info()

# inventory1 = inventory()
# inventory1.add_product_to_inventory()
# inventory1.add_product_to_inventory()
# inventory1.add_product_to_inventory()
# inventory1.get_product_info_from_inventory()
# inventory1.update_product_in_inventory()
# inventory1.get_product_info_from_inventory()
# inventory1.delete_product_in_inventory()
# inventory1.list_all_products_in_inventory()

# cart1 = cart()
# cart1.add_product_to_cart(123)
# cart1.add_product_to_cart(124)
# cart1.add_product_to_cart(125)
# print_cart_products()

# Import Required Module
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
inventory1 = inventory()
inventory1.add_product_to_inventory(8,"Curry flow8",1000, 20)
inventory1.add_product_to_inventory(3,"AirJordan3",2000, 10)
inventory1.add_product_to_inventory(18,"LeBron 18",3000, 30)
inventory1.add_product_to_inventory(7,"Kobe 7",4000, 55)

cart1 = cart()
# Create Root Object
root = tk.Tk()
# Set Geometry(widthxheight)
root.geometry('500x500')

# Create style Object-----------------------------------------------------------
style = Style()
style.configure('TButton', font =('calibri', 20, 'bold'),borderwidth = '1')

style_A_label = Style()
style_A_label.configure('TLabel', font =('calibri', 40, 'bold'),borderwidth = '4',padx = 500,pady = 200)
#-------------------------------------------------------------------------------

#Required Variables-------------------------------------------------------------
product_id_var=tk.StringVar()
product_name_var=tk.StringVar()
product_price_var=tk.StringVar()
product_count_var = tk.StringVar()

update_product_id_var=tk.StringVar()
update_product_name_var=tk.StringVar()
update_product_price_var=tk.StringVar()
update_increm_count_var=tk.StringVar()
update_decrem_count_var=tk.StringVar()

delete_product_id_var=tk.StringVar()
#-------------------------------------------------------------------------------


Amazon_label = Label(root, text = "Amazon",style = 'TLabel')

# btn_insert = Button(root, text = 'Insert Product', command = root.destroy)
# btn_insert.grid(row = 2, column = 1, padx = 10,pady = 65)
# btn_update = Button(root, text = 'Update Product', command = root.destroy)
# btn_update.grid(row = 3, column = 1, padx = 10,pady = 0)
# btn_delete = Button(root, text = 'Delete Product', command = root.destroy)
# btn_delete.grid(row = 4, column = 1, padx = 10,pady = 10)
#command functions--------------------------------------------------------------
def submit():
    
    id = product_id_var.get()
    name=product_name_var.get()
    price=product_price_var.get()
    count=product_count_var.get()
    
    ### The below prints are just for verification, printed on the terminal, replace with the success or failure notification popup ###
    print("The id is : " + id)
    print("The name is : " + name)
    print("The price is : " + price)
    print("The stock quantity is : " + count)

    inventory1.add_product_to_inventory(id,name,price, count)
    inventory1.list_all_products_in_inventory()

    product_id_var.set("")
    product_name_var.set("")
    product_price_var.set("")
    product_count_var.set("")

    product_id_entry.delete(0,"end")
    product_name_entry.delete(0,"end")
    product_price_entry.delete(0,"end")
    product_count_entry.delete(0,"end")

def update_submit():
    id = update_product_id_var.get()
    name=update_product_name_var.get()
    price=update_product_price_var.get()
    increased_quant = update_increm_count_var.get()
    decreased_quant = update_decrem_count_var.get()

    ### The below prints are just for verification, printed on the terminal, replace with the success or failure notification popup ###
    print("The id is : " + id)
    print("The name is : " + name)
    print("The price is : " + price)

    inventory1.update_product_in_inventory(id,name,price, increased_quant, decreased_quant)
    inventory1.list_all_products_in_inventory()

    update_product_id_var.set("")
    update_product_name_var.set("")
    update_product_price_var.set("")
    update_increm_count_var.set("")
    update_decrem_count_var.set("")

    ### To clear the entry in the GUI
    update_product_id_entry.delete(0,"end")
    update_product_name_entry.delete(0,"end")
    update_product_price_entry.delete(0,"end")
    update_increm_count_entry.delete(0,"end")
    update_decrem_count_entry.delete(0,"end")

def delete_submit():
    id = delete_product_id_var.get()
    
    # print("The id is : " + id)
    id = int(id)
    inventory1.delete_product_in_inventory(id)
    inventory1.list_all_products_in_inventory()

    delete_product_id_var.set("")
    delete_product_id_entry.delete(0,"end")

#-------------------------------------------------------------------------------

#labels----------------------------------------
insert_label = tk.Label(root, text = 'Insert Product', font=('calibre',10, 'bold'))
update_label = tk.Label(root, text = 'Update Product', font=('calibre',10, 'bold'))
#----------------------------------------------
#insert product--------------------
product_id_label = tk.Label(root, text = 'Product Id', font=('calibre',10, 'bold'))
product_id_entry = tk.Entry(root,textvariable = product_id_var, font=('calibre',10,'normal'))

product_name_label = tk.Label(root, text = 'Product Name', font=('calibre',10, 'bold'))
product_name_entry = tk.Entry(root,textvariable = product_name_var, font=('calibre',10,'normal'))

product_price_label = tk.Label(root, text = 'Product Price', font=('calibre',10, 'bold'))
product_price_entry = tk.Entry(root,textvariable = product_price_var, font=('calibre',10,'normal'))

### added for the cart management feature(aps)
product_count_label = tk.Label(root, text = 'Product Stock qty.', font=('calibre',10, 'bold'))
product_count_entry = tk.Entry(root,textvariable = product_count_var, font=('calibre',10,'normal'))
#----------------------------------

#update product--------------------
update_product_id_label = tk.Label(root, text = 'Product Id', font=('calibre',10, 'bold'))
update_product_id_entry = tk.Entry(root,textvariable = update_product_id_var, font=('calibre',10,'normal'))

update_product_name_label = tk.Label(root, text = 'Update Product Name', font=('calibre',10, 'bold'))
update_product_name_entry = tk.Entry(root,textvariable = update_product_name_var, font=('calibre',10,'normal'))

update_product_price_label = tk.Label(root, text = 'UpdateProduct Price', font=('calibre',10, 'bold'))
update_product_price_entry = tk.Entry(root,textvariable = update_product_price_var, font=('calibre',10,'normal'))

### added for the cart management feature(aps)
update_increm_count_label = tk.Label(root, text = 'Increase Stock', font=('calibre',10, 'bold'))
update_increm_count_entry = tk.Entry(root,textvariable = update_increm_count_var, font=('calibre',10,'normal'))

update_decrem_count_label = tk.Label(root, text = 'Reduce Stock', font=('calibre',10, 'bold'))
update_decrem_count_entry = tk.Entry(root,textvariable = update_decrem_count_var, font=('calibre',10,'normal'))
#----------------------------------
#delete product-----------------------
delete_label = tk.Label(root, text = 'Delete Product', font=('calibre',10, 'bold'))
delete_product_id_entry = tk.Entry(root,textvariable = delete_product_id_var, font=('calibre',10,'normal'))
#-------------------------------------

#Buttons------------------------------
sub_btn_insert=tk.Button(root,text = 'Submit', command = submit)
sub_btn_update=tk.Button(root,text = 'Submit', command = update_submit)
sub_btn_delete=tk.Button(root,text = 'Submit', command = delete_submit)
btn1 = tk.Button(root, text = 'Quit !', command = root.destroy)
#-------------------------------------
#Image labels-------------------------------------
im0_label = tk.Label(root, text = 'Products you might be interested', font=('calibre',10, 'bold'))
im1_label = tk.Label(root, text = 'Curry 8  P_ID : 8 ', font=('calibre',10, 'bold'))
im2_label = tk.Label(root, text = 'Air Jordan3 P_ID : 3', font=('calibre',10, 'bold'))
im3_label = tk.Label(root, text = 'Le Bron 18 P_ID : 18', font=('calibre',10, 'bold'))
im4_label = tk.Label(root, text = 'Kobe 7 P_ID : 7', font=('calibre',10, 'bold'))
#----------------------------------------------------------

#image functions-------------------------------------
def curry():
    cart1.add_product_to_cart(8)
    print_cart_products()
def air_jordan():
    cart1.add_product_to_cart(3)
    print_cart_products()
def leBron():
    cart1.add_product_to_cart(18)
    print_cart_products()
def kobe():
    cart1.add_product_to_cart(7)
    print_cart_products()
#----------------------------------------------------------

#image buttons-------------------------------------
im1_btn = tk.Button(root,text = 'Add To Cart ❤', command = curry)
im2_btn = tk.Button(root,text = 'Add To Cart ❤', command = air_jordan)
im3_btn = tk.Button(root,text = 'Add To Cart ❤', command = kobe)
im4_btn = tk.Button(root,text = 'Add To Cart ❤', command = leBron)

#images----------------------------------------------------
image1 = Image.open("curry.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
# Position image
# label1.grid(row=2,column=0)

image2 = Image.open("air_jordan.jpg")
test2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=test2)
label2.image = test2
# Position image
# label2.grid(row=2,column=1)

image3 = Image.open("kobe.jpg")
test3 = ImageTk.PhotoImage(image3)
label3 = tk.Label(image=test3)
label3.image = test3
# Position image
# label3.grid(row=3,column=0)

image4 = Image.open("leBron.jpg")
test4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(image=test4)
label4.image = test4
# Position image
# label4.grid(row=3,column=0)
#----------------------------------------------------------


# placing the label and entry in
# the required position using grid
# method-----------------------------------------
Amazon_label.grid(row=0,column=0,padx = 50)
insert_label.grid(row=1,column=0)
product_id_label.grid(row=2,column=0)
product_id_entry.grid(row=2,column=1)
product_name_label.grid(row=3,column=0)
product_name_entry.grid(row=3,column=1)
product_price_label.grid(row=4,column=0)
product_price_entry.grid(row=4,column=1)
###
product_count_label.grid(row=5,column=0)
product_count_entry.grid(row=5,column=1)
###
sub_btn_insert.grid(row=6,column=1)

update_label.grid(row=7,column=0)
update_product_id_label.grid(row=8,column=0)
update_product_id_entry.grid(row=8,column=1)
update_product_name_label.grid(row=9,column=0)
update_product_name_entry.grid(row=9,column=1)
update_product_price_label.grid(row=10,column=0)
update_product_price_entry.grid(row=10,column=1)
###
update_increm_count_label.grid(row=11,column=0)
update_increm_count_entry.grid(row=11,column=1)
update_decrem_count_label.grid(row=12,column=0)
update_decrem_count_entry.grid(row=12,column=1)
###
sub_btn_update.grid(row=13,column=1)

delete_label.grid(row=14,column=0)
delete_product_id_entry.grid(row=14,column=1)
sub_btn_delete.grid(row=15,column=1)

im0_label.grid(row=16,column = 0)
label1.grid(row=17,column=0)
label2.grid(row=17,column=1)
im1_label.grid(row=18,column = 0)
im2_label.grid(row=18,column = 1)
im1_btn.grid(row=19,column = 0)
im2_btn.grid(row=19,column = 1)

label3.grid(row=17,column=2)
label4.grid(row=17,column=3)
im3_label.grid(row=18,column = 2)
im4_label.grid(row=18,column = 3)
im3_btn.grid(row=19,column = 2)
im4_btn.grid(row=19,column = 3)

btn1.grid(row = 20, column = 5)
# -------------------------------------------------


# Execute Tkinter
root.mainloop()



