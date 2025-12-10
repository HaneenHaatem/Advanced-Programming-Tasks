# ========================================================
# Problem 1: (Basic SQLite CRUD):

import sqlite3

con=sqlite3.connect("school.db")
c=con.cursor()
c.execute("create table students(id integer primary key, name text, grade real)")
c.execute("insert into students values(1,'Ali', 85)")
c.execute("insert into students values(2,'Sara', 92)")
c.execute("insert into students values(3,'Mohamed', 78.3)")
con.commit()
con.close()

c.execute("select * from students")
for i in c.fetchall():
    print(i)


# ========================================================
# Problem 2: (Paramitrized queries):

import sqlite3

id = int(input("Enter id: "))
name = str(input("Enter name: "))
grade = float(input("Enter grade: "))
 
c.execute("insert into students values(?,?,?)", (id,name,grade))
c.execute("select * from students")
for i in c.fetchall():
    print(i)
con.commit()
con.close()


# ========================================================
# Problem 3: (Transactions):

import sqlite3

try:
    c.execute("insert into students VALUES(4, 'Noura', 88.0)")
    c.execute("insert into students VALUES(5, 'Khalid', 95.0)")
    
    result = 10 / 0
    con.commit()
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    con.rollback()
    print("Transaction rolled back.")

except Exception as e:
    print(f"Other error: {e}")
    con.rollback()

finally:
    c.execute("select * from students")
    for i in c.fetchall():
        print(i)
con.close()



# ========================================================
# Problem 4: (ORM):

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"

engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

book1 = Book(title='Python Basics', author='Guido')
book2 = Book(title='AI with Python', author='Mohamed')

session.add_all([book1, book2])
session.commit()

print("All books in database:")
books = session.query(Book).all()
for book in books:
    print(book)
session.close()