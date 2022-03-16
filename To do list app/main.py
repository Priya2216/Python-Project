from flask import Flask , render_template, request
import sqlfile as s
      
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# function to insert customer details
@app.route("/customer_data", methods=["POST"])
def get_customer_data():
    order_no = request.form["order_no"]
    customer_name = request.form["customer_name"]
    product_info = request.form["product_info"]
    contact_number = request.form["contact_number"]
    delivery= request.form["delivery"]
    location = request.form["location"]
    
    if s.insert_customer(order_no,customer_name, product_info, contact_number, delivery, location):
        return "New Customer details added"
    else:
        return render_template("update.html")
    
    
# function to show customer details
@app.route("/show_customer")
def show_customer():
    tasks = s.get_customers()
    
    if tasks == False:
        return "Exception- contact developer"
    else:
        #print(tasks)
        #return "success"
        return render_template("update.html",data=tasks)

#function to update customer
@app.route("/update_customer/<order_no>")
def update_customer(order_no):
    # return order_no
    task = s.get_one_customer(order_no) 
    
    if task == False:
        return "Exception- contact developer"
    else:
        return render_template("delete.html",data=task) 

#function to edit order  
@app.route("/edit_customer/<order_no>", methods=["POST"])
def edit_customer(order_no):
      order_no = request.form["order_no"]
      customer_name = request.form["customer_name"]
      product_info = request.form["product_info"]
      contact_number = request.form["contact_number"]
      delivery= request.form["delivery"]
      location = request.form["location"]
      
      # print(order_no, customer_name, product_info, contact_number, delivery, location)
      # return "success"
      if s.update_customer(order_no, customer_name, product_info, contact_number, delivery, location):
           return render_template("home.html")
      else:
           return "Exception- contact developer"   
       
#function to delete order   
@app.route("/delete_order/<order_no>")
def delete_order(order_no):
    
    if s.delete_customer(order_no):
        return render_template("home.html")
    else:
        return "Exception- contact developer"

# using debug so that no need to stop and run again and again
app.run()    



















