# import mysql.connector as connection
# mydb=connection.connect(host='localhost',use_pure=True,user='kishor',password='mysql123')
# print(mydb)
# cur=mydb.cursor()
# cur.execute("create table kishor.iNeuron(employee_id int(10),emp_name varchar(80),emp_mailid varchar(80),emp_salary int(7),emp_attendenc int(20))")
# cur.execute("insert into kishor.ineuron values(101,'kishor kumar','kishordev36@gmail.com',100,3000)")
# mydb.commit()
# cur.execute(("select * from kishor.ineuron"))
# for i in cur.fetchall():
#    print(i)
# cur.execute('select employee_id,emp_mailid from kishor.ineuron')
# l=[]
# for i in cur.fetchall():
#     l.append(i)

# print(l)
# print(type(l[0]))
import pymongo
client = pymongo.MongoClient("mongodb+srv://kishor:mongodb@cluster0.4xwrt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "Name":"kishor",
    "email":"kishor@gmail.com",
    "surname":"Devaragudi"

}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)

