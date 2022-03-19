import pymysql 

username = "root"
host="localhost"
password=""
dbname = "amazon"

def connect():
    db = pymysql.connect(user=username,host=host,password=password,db=dbname)
    return db

# ADD CUSTOMER
def insert_customer(order_no,customer_name, product_info, contact_number, delivery, location):
    try:
        db = connect()
        cs = db.cursor()
        sql = "insert into customer (order_no,customer_name, product_info, contact_number, delivery, location) values (%s,%s,%s,%s,%s,%s)"
        values = (order_no,customer_name, product_info, contact_number, delivery, location)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()

# SHOW CUSTOMER
def get_customers():
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from customer"
        cs.execute(sql)
        tasks = cs.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()

# Get one customer
def get_one_customer(order_no):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from customer where order_no=%s"
        value = (order_no,)
        cs.execute(sql,value)
        task = cs.fetchone()
        return task
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()

# UPDATE CUSTOMER
def update_customer(order_no, customer_name, product_info, contact_number, delivery, location):
    try:
        db = connect()
        cs = db.cursor()
        sql = "update customer set customer_name=%s, product_info=%s, contact_number=%s, delivery=%s, location=%s where order_no=%s"
        values = (customer_name, product_info, contact_number, delivery, location,order_no)
        cs.execute(sql,values)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()   

# DELETE CUSTOMER
def delete_customer(order_no):
    try:
        db = connect()
        cr = db.cursor()
        sql = "delete from customer where order_no= %s"
        value= (order_no,)
        cr.execute(sql, value)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close() 
        