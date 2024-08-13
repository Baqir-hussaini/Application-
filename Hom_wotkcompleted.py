#1. Create a class called Person with attributes name and age. Create an object of the class and print its attributes.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def show(self):
		print("name: ",self.name)
		print("age: ",self.age)
		
Ahmad = Person("Ahamd",16)
Ahmad.show()

#2. Add a method called greet to the Person class that prints a greeting message including the person's name.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def show(self):
		print("name: ",self.name)
		print("age: ",self.age)
	def greet(self):
		print("Hello, How you doing?")
		
Ahmad = Person("Ahamd",16)
Ahmad.show()
Ahmad.greet()

#3. Create a class called Car with attributes make, model, and year. Include a method to print out the car's details.
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def show(self):
		print("make: ",self.make)
		print("model: ",self.model)
		print("year: ",self.year)
Lamborghini = Car("Lamborghini","Miura P400",2020)
Lamborghini.show()

#4. Create a class Circle with a method to compute the area. Initialize the class with the radius.
class Circle:
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		a = 3.14 * ((self.radius) ** 2)
		print("The area is: ",a)
C1 = Circle(12)
C1.area()

#5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length and width.
class Rectangle:
	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		a = self.length * self.width
		print("the area is: ",a)
	def perimeter(self):
		p = (self.length * 2) + (self.width * 2)
		print("the perimeter is: ",p)
R1 = Rectangle(10,5)
R1.area()
R1.perimeter()

#6. Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method.
class Animal:
	def speak(self):
		print("speak")

class Dog(Animal):
	def speak(self):
		print("bark")
		
class Cat(Animal):
	def speak(self):
		print("Meow")
		
#7. Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area method.
class Shape:
	def area(self):
		a = self.width * self.length
		print("the area is: ",a)

class Square(Shape):
	def __init__(self,width,length):
		self.width = width
		self.length = length

class Triangle(Shape):
	def __init__(self,base,height):
		self.base = base
		self.height = height
	def area(self):
		a = (1/2) * self.base * self.height
		print("thr area is: ",a)
		
s1 = Square(10,10)
s1.area()

t1 = Triangle(4,3)
t1.area()

#8. Create a class Employee with attributes name and salary. Create a derived class Manager with an additional attribute department.
class Employee:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

class Manager(Employee):
	def __init__(self,name,salary,department):
		self.name = name
		self.salary = salary
		self.department = department
		
#9. Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that override the drive method.
class Vehicle:
	def drive(self):
		pass

class Bike(Vehicle):
	def ride(self):
		pass
		
class Truck(Vehicle):
	def drive(self):
		pass
		
#10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly.
class Bird:
	def fly(self):
		print("fly")

class Eagle(Bird):
	pass
class Penguin(Bird):
	def fly(self):
		print("walk")
		
#11. Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money.

class Account:
	def __init__(self, balance):
		self.balance = balance
		print("the balance is: ",self.balance)
		
	def deposit(self, amount):
		self.balance += amount
		print("the balance after the",amount, "deposit is: ",self.balance)
		
	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			print("the balance after", amount,"withdraw is: ",self.balance)
		else:
			print("insufficient funds")
			
ahmad_account = Account(100)
ahmad_account.deposit(10)
ahmad_account.withdraw(35)

#12. Create a class Book with private attributes title, author, and pages. Provide public methods to get and set these attributes.
class Book:
	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages
	def get_title(self):
		print("the title of the book is: ", self.title)
	def get_author(self):
		print("the author of the book is: ", self.author)
	def get_pages(self):
		print("the number of pages of the book is: ",self.pages)
		
#13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply a discount and a method to display laptop details.

class Laptop:
	def __init__(self, brand, model, price):
		self.brand = brand
		self.model = model
		self.price = price
	def discount(self, amount):
		self.price -= amount
		print("laptop price after discount is ",self.price)
	def details(self):
		print("laptop brand is ",self.brand)
		print("laptop model is ",self.model)
		print("laptop price is ",self.price)
		
l1 = Laptop("dell", "core i9", 17000)
l1.details()
l1.discount(2000)

#14. Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check the balance.
class BankAccount:
	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
		else:
			print("insuficient funds!!!")
	def check(self):
		print("AccountNumber: ", self.account_number)
		print("balnce: ", self.balance)
		
ba1 = BankAccount(12345678, 20000)
ba1.withdraw(30)
ba1.deposit(60)
ba1.check()

#15. Create a class Student with private attributes name, grade, and age. Provide methods to get and set these attributes and a method to display the student's details.
class Student:
	def __init__(self, name, grade, age):
		pass
	def get_name(self):
		self.name = input("enter your name: ")
	def get_grade(self):
		self.grade = input("enter your grade: ")
	def get_age(self):
		self.age = input("enter your age: ")
	def details(self):
		print("your name is: ", self.name)
		print("your grade is: ", self.grade)
		print("your age is: ", self.age)
s1 = Student("ahmad", 12, 18)
s1.get_name()
s1.get_grade()
s1.get_age()
s1.details()

#16. Create a class Library with attributes name and books (a list of Book objects). Provide methods to add and remove books.
class Library:
	def __init__(self, name, books):
		self.name = name
		self.books = books
		print("the library books: ", self.books)
	def add(self, item):
		self.books.append(item)
		print("the library books after", item, "added: ", self.books)
	def remove(self, item1):
		if item1 in self.books:
			self.books.remove(item1)
			print("the library books after", item1, "removed: ",self.books)
		else:
			print("does not exist!!")
l1 = Library("Eqra", ["Python", "javascript"])
l1.add("atomic habits")
l1.remove("Python")

#17. Create a class School with attributes name and students (a list of Student objects). Provide methods to add and remove students.
class School:
	def __init__(self, name, students):
		self.name = name
		self.students = students
		print("the students: ", self.students)
	def add(self, person):
		self.students.append(person)
		print("the students after", person, "added: ", self.students)
	def remove(self, person):
		if person in self.students:
			self.students.remove(person)
			print("the students after", person, "removed: ",self.students)
		else:
			print("does not exist!!")
s1 = School("Ghazi", ["Ahmad", "Ali"])
s1.add("Mohammad")
s1.remove("Ahmad")

#18. Create a class Team with attributes name and members (a list of Person objects). Provide methods to add and remove members.
class Team:
	def __init__(self, name, members):
		self.name = name
		self.members = members
		print("the", self.name, "members: ", self.members)
	def add(self, person):
		self.members.append(person)
		print("the members after", person, "added: ", self.members)
	def remove(self, person):
		if person in self.members:
			self.members.remove(person)
			print("the members after", person, "removed: ",self.members)
		else:
			print("does not exist!!")
t1 = Team("Hewad", ["Ahmad", "Ali"])
t1.add("Mohammad")
t1.remove("Ahmad")

#19. Create a class Company with attributes name and employees (a list of Employee objects). Provide methods to add and remove employees.
class Company:
	def __init__(self, name, employees):
		self.name = name
		self.employees = employees
		print("the", self.name, "employees: ", self.employees)
	def add(self, person):
		self.employees.append(person)
		print("the employees after", person, "added: ", self.employees)
	def remove(self, person):
		if person in self.employees:
			self.employees.remove(person)
			print("the employees after", person, "removed: ",self.employees)
		else:
			print(person,"does not exist!!")
c1 = Company("Apple", ["Smith", "John"])
c1.add("Mohammad")
c1.remove("Smith")

#20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods to add and remove animals.
class Zoo:
	def __init__(self, name, animals):
		self.name = name
		self.animals = animals
		print("the", self.name, "animals: ", self.animals)
	def add(self, animal):
		self.animals.append(animal)
		print("the animals after", animal, "added: ", self.animals)
	def remove(self, animal):
		if animal in self.animals:
			self.animals.remove(animal)
			print("the animals after", animal, "removed: ",self.animals)
		else:
			print(animal,"does not exist!!")
z1 = Zoo("Kabul Zoo", ["Snake", "Lion"])
z1.add("Bear")
z1.remove("Snake")

#21. Create a class FileManager with methods to read from and write to a file.

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


if __name__ == "__main__":
    fm = FileManager("example.txt")
    
    fm.write("Hello, World!")
   
    content = fm.read()
    print(content)
		
o1 = FileManager
o1.read()
o1.write()

#22. Create a class Log with methods to write error messages to a log file.

from datetime import datetime

class Log:
    def __init__(self, filename="error_log.txt"):
        self.filename = filename

    def write_error(self, message):
        with open(self.filename, 'a') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] ERROR: {message}\n")

if __name__ == "__main__":
    logger = Log()
    logger.write_error("This is an error message.")

#23. Create a class Config that reads configuration settings from a file and provides methods to access these settings.

import json

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config: {e}")
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)

if __name__ == "__main__":
    config = Config()
    db_host = config.get('db_host', 'localhost')
    db_port = config.get('db_port', 5432)

    print(f"Database Host: {db_host}")
    print(f"Database Port: {db_port}")

#25. Create a class Report that generates a report from data in a file. Provide methods to handle exceptions if the file does not exist or cannot be read.

class Report:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = file.read()
                print("Data read successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' does not exist.")
        except IOError:
            print(f"Error: The file '{self.file_path}' cannot be read.")

    def generate_report(self):
        if self.data is not None:
            print("Generating report...")
            print(self.data)
        else:
            print("No data available to generate the report.")

report = Report('data.txt')
report.read_data()
report.generate_report()

#26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price. Provide methods to display ticket details and apply discounts.
class Ticket:
	def __init__(self, movie_name, seat_number, price):
		self.m = movie_name
		self.s = seat_number
		self.p = price
	def details(self):
		print("Movie name: ",self.m)
		print("Seat number: ",self.s)
		print("Ticket price: ", self.p)
	def discount(self):
		self.p -= 10
		print("Ticket price after 10 discount: ", self.p)
t1 = Ticket("Harry potter", 12, 100)
t1.details()
t1.discount()

#27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should be an object of a class Item with attributes name and price.
class Item:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class ShoppingCart:
	def __init__(self):
		self.items = []
	def add(self, item):
		self.items.append(item)
	def remove(self, item):
		self.items.remove(item)
	def display(self):
		for item in self.items:
			print("name: ",item.name, "price: ",item.price)
			
i1 = Item("bread", 20)
i2 = Item("apple", 30)

cart = ShoppingCart()
cart.add(i1)
cart.add(i2)
cart.remove(i1)
cart.display()

#28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide methods to add and remove items from the menu.
class Item:
	def __init__(self, name, price):
		self.name  = name
		self.price = price
class Restaurant:
	def __init__(self):
		self.menu = []
	def add(self, item):
		self.menu.append(item)
	def remove(self, item):
		self.menu.remove(item)
	def display(self):
		for item in self.menu:
			print("name: ", item.name, "price: ", item.price)
		
i1 = Item("Burger", 100)
i2 = Item("Kabab", 200)

m = Restaurant()
m.add(i1)
m.add(i2)
m.remove(i1)
m.display()

#29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person objects). Provide methods to add and remove passengers.
class Person:
	def __init__(self, flight_number, destination, name):
		self.f = flight_number
		self.d = destination
		self.n = name
class Flight:
	def __init__(self):
		self.passengers = []
	def add(self, passenger):
		self.passengers.append(passenger)
	def remove(self, passenger):
		self.passengers.remove(passenger)
	def dispaly(self):
		for passenger in self.passengers:
			print("flight number: ",passenger.f,"  ","destination: ",passenger.d,"  ","name: ",passenger.n)

p1 = Person(2216, "America", "Mohammad")
p2 = Person(2217, "Canada", "Ali")

f1 = Flight()
f1.add(p1)
f1.add(p2)
f1.remove(p1)
f1.dispaly()

#30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room should have attributes room_number and is_occupied. Provide methods to book and checkout rooms.

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

    def book(self):
        if not self.is_occupied:
            self.is_occupied = True
            return True
        return False

    def checkout(self):
        if self.is_occupied:
            self.is_occupied = False
            return True
        return False


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number):
        room = Room(room_number)
        self.rooms.append(room)

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.book():
                    print(f"Room {room_number} booked successfully.")
                    return True
                else:
                    print(f"Room {room_number} is already occupied.")
                    return False
        print(f"Room {room_number} does not exist.")
        return False

    def checkout_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.checkout():
                    print(f"Checked out of room {room_number} successfully.")
                    return True
                else:
                    print(f"Room {room_number} is not occupied.")
                    return False
        print(f"Room {room_number} does not exist.")
        return False
        
hotel = Hotel("Grand Hotel")
hotel.add_room(101)
hotel.add_room(102)

hotel.book_room(101) 
hotel.book_room(101) 
hotel.checkout_room(101)
hotel.checkout_room(101)

#36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and decrement buttons.

import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        master.title("Counter App")

        self.counter = 0
        
        self.label = tk.Label(master, text=str(self.counter), font=("Arial", 24))
        self.label.pack()

        self.increment_button = tk.Button(master, text="Increment", command=self.increment)
        self.increment_button.pack()

        self.decrement_button = tk.Button(master, text="Decrement", command=self.decrement)
        self.decrement_button.pack()

    def increment(self):
        self.counter += 1
        self.label.config(text=str(self.counter))

    def decrement(self):
        self.counter -= 1
        self.label.config(text=str(self.counter))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
    
#37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and remove tasks.

import tkinter as tk

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            pass

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
   
#38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.

 import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, width=16, font=('Arial', 24), bd=10, insertwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(master, text=button, padx=20, pady=20, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
        else:
            current = self.result_var.get()
            self.result_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
    
#39. Create a class LoginApp that uses tkinter to create a login form GUI.

import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login Form")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Invalid Credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
    
#40. Create a class WeatherApp that uses tkinter to create a weather information GUI.

import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")
        self.title_label = tk.Label(master, text="Weather Information", font=("Arial", 16))
        self.weather_label = tk.Label(master, text="Weather: Unknown", font=("Arial", 14))
        self.weather_label.pack(pady=20)
        self.fetch_button = tk.Button(master, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack(pady=10)

    def fetch_weather(self):
        simulated_weather = "Sunny, 25°C"
        self.weather_label.config(text=f"Weather: {simulated_weather}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()