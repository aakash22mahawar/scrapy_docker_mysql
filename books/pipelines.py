
from itemadapter import ItemAdapter
import mysql.connector
import traceback
# import logging as log

class BooksPipeline:
    
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                user="admin",
                password="Sana946#z",
                database="aws_db1",
                port="3306",
                host="aws-1.ckqzeg9ewa9h.us-east-1.rds.amazonaws.com",
                autocommit=True)

            print(f"Msg :Connection Established.")
            # log.info(f"Msg :Connection Established.")
            self.cur = self.mydb.cursor()

        except:

            # log.error(traceback.print_exc(), exc_info=True)
            print("Error in DB connection")

    def process_item(self, item, spider):
        sql = f"""INSERT Ignore INTO books (name,image) VALUES ("{item['name']}","{item['image']}")"""
        #val = (item['name'], item['image'])
        self.cur.execute(sql)
        print(sql)
        print('insertion successful')

    def close(self):
        self.cur.close()
        self.mydb.close()