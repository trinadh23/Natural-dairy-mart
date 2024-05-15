import mysql.connector as mysql

#create database

mydb = mysql.connect(host="localhost", user="root", passwd="Kommineni@2000",port=3307)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS ndm")

mydb.commit()


#create account table

mycursor.execute('''CREATE TABLE IF NOT EXISTS ndm.user(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), phonenumber VARCHAR(255), password VARCHAR(255))''')


#create items table

mycursor.execute('''
        CREATE TABLE IF NOT EXISTS ndm.items(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255), 
            price VARCHAR(255),
            description VARCHAR(255),
            category VARCHAR(255),
            image VARCHAR(255))
                 ''')

#cart table

mycursor.execute('''
        CREATE TABLE IF NOT EXISTS ndm.cart(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            item_id INT,
            quantity INT,
            status VARCHAR(255) DEFAULT 'pending',
            FOREIGN KEY (user_id) REFERENCES ndm.user(id),
            FOREIGN KEY (item_id) REFERENCES ndm.items(id))
                 ''')

#orders table

mycursor.execute('''
        CREATE TABLE IF NOT EXISTS ndm.orders(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            order_id INT,   
            user_id INT, 
            item_id INT,
            quantity INT,
            price INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES ndm.user(id),
            FOREIGN KEY (item_id) REFERENCES ndm.items(id))
                 ''')

print("Table created successfully")

#create orders table

mydb.commit()
