AirBnB Clone Command Interpreter
This is a command line interpreter for managing objects in the AirBnB clone project.
The interpreter supports creating, retrieving, updating, and deleting objects.

Background Context
The AirBnB clone project aims to build a full web application that can be used to manage bookings and rentals.
The project has several tasks, and this is the first step towards building the application.

The goal of this project is to create a parent class called BaseModel, which will take care of the initialization, 
serialization, and deserialization of future instances. The project also involves creating a flow of serialization/
deserialization between instances, dictionaries, JSON strings, and files.

Other classes that inherit from BaseModel will also be created, such as User, State, City, and Place. 
Additionally, an abstracted storage engine for the project will be created, called "File storage".
Finally, unit tests will be created to validate all classes and the storage engine.

How to Start
To start the interpreter, first clone the repository from GitHub:

bash
git clone https://github.com/your-username/airbnb-clone.git
Next, navigate to the project directory and run the following command to start the interpreter:

javascript
python3 console.py
How to Use
Once the interpreter is started, you can start entering commands. Commands should be entered on a 
single line, with arguments separated by spaces.

Here are some example commands you can use:

Create a new user:
sql
create User email="john.doe@example.com" password="password" first_name="John" last_name="Doe"

Retrieve a user:
sql
show User 1234-1234-1234

Update a user's last name:
sql
update User 1234-1234-1234 last_name "Smith"

Delete a user:
sql
destroy User 1234-1234-1234
For a full list of available commands and their usage, enter help or ?.
