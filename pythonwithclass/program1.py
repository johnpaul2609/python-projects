from sqlalchemy import create_engine,text
engine=create_engine("mysql+pymysql://root:johnpaul%40123@localhost:3306/pythonclass")
id=int(input("enter your id"))
name=input("enter your name")
mark1=int(input("enter your mark1"))
mark2=int(input("enter your mark2"))
mark3=int(input("enter your mark3"))
total=mark1+mark2+mark3
average=total/3
if total>=275:
    grade="A"
elif total>=200:
    grade="B"
elif total>=150:
    grade="C"
else:
    grade="D"
print(id,name,mark1,mark2,mark3,total,average,grade)
with engine.connect() as conn:
    conn.execute(text("insert into student values(:id,:name,:mark1,:mark2,:mark3,:total,:average,:grade)"),{"id":id,"name":name,"mark1":mark1,"mark2":mark2,"mark3":mark3,"total":total,"average":average,"grade":grade})
    conn.commit()
print("record inserted")