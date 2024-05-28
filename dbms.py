from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x400")

conn = sqlite3.connect('mydb.db')

c = conn.cursor()

# c.execute("CREATE TABLE employee (empid integer, name text, age integer, salary integer)")

empid_label = Label(root, text="Employee ID: ")
empid_label.grid(row=0, column=0)
empid_entry = Entry(root)
empid_entry.grid(row=0, column=1)

name_label = Label(root, text="Name: ")
name_label.grid(row=1, column=0)
name_entry = Entry(root)
name_entry.grid(row=1, column=1)

age_label = Label(root, text="Age: ")
age_label.grid(row=2, column=0)
age_entry = Entry(root)
age_entry.grid(row=2, column=1)

salary_label = Label(root, text="Salary: ")
salary_label.grid(row=3, column=0)
salary_entry = Entry(root)
salary_entry.grid(row=3, column=1)


def submit():

    conn = sqlite3.connect('mydb.db')

    c = conn.cursor()

    c.execute("INSERT INTO employee VALUES(:id, :name, :age, :salary)",
            {
                'id': empid_entry.get(),
                'name': name_entry.get(),
                'age': age_entry.get(),
                'salary': salary_entry.get()

            }
    )

    c.execute("SELECT *, oid FROM employee")
    data = c.fetchall()
    print(data)

    conn.commit()

    conn.close()

    empid_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    salary_entry.delete(0, END)

def show():
    conn = sqlite3.connect('mydb.db')

    c = conn.cursor()

    c.execute("SELECT * FROM employee")
    records = c.fetchall()
    
    print(records)
    x = 8
    for record in records:
        id = Label(root, text="ID: " + "\t" + str(record[0]))
        id.grid(row=x, column=0)
        x += 1
        name = Label(root, text="Name: " + "\t" + str(record[1]))
        name.grid(row=x, column=0)
        x += 1
        age = Label(root, text="Age: " + "\t" + str(record[2]))
        age.grid(row=x, column=0)
        x += 1
        Salary = Label(root, text="Salary: " + "\t" + str(record[3]) + "\n")
        Salary.grid(row=x, column=0)
        x += 1
        


    conn.commit()

    conn.close()

submitButton = Button(root, text="Add Record", command=submit)
submitButton.grid(row=4, column=1)



showButton = Button(root, text="Show Record", command=show)
showButton.grid(row=5, column=1)

deleteLabel = Label(root, text="Delete ID: ")
deleteLabel.grid(row=6, column=0)

deleteEntry = Entry(root)
deleteEntry.grid(row=6, column=1)

def delete():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    c.execute("DELETE FROM employee WHERE empid = " + deleteEntry.get())

    conn.commit()
    conn.close()

    deleteEntry.delete(0, END)
    show()


deletebutton = Button(root, text="Delete", command=delete)
deletebutton.grid(row=7, column=1)
conn.commit()

conn.close()



root.mainloop()