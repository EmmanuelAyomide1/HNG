# E-R model of relationships between endpoints and view functions
![e-r model](https://github.com/EmmanuelAyomide1/HNG/blob/main/ERmodel/graphviz.png?raw=true "e-r model")
# Documentation
## Sample Requests and Responses
#### 1. Create Operation:
+ ##### Request
	+ Request Method: `POST`
	
	+ Endpoint :`https://hng-stage2-e6ly.onrender.com/api` 
	
    + Request body: 
	```json
	 {
        "name": "Emmanuel_Ayomide"
    }
	```
+ ##### Response
    + Status code `201`
	
    + Response message
     ```json
     {
        "name": "Emmanuel_Ayomide"
    }
  ```

#### 2. READ Operation(ALL)
+ ##### Description
  + This returns a list of all Stored Persons on the database
+ ##### Request
	+ Request Method: `GET`
	
	+ Endpoint: `https://hng-stage2-e6ly.onrender.com/api` 
	
+ ##### Response
    + Status code: `200`
	
    + Response message:
     ```
     [
    {
        "id": 1,
        "name": "Emmanuel_Ayomide"
    },
    {
        "id": 3,
        "name": "Emmy_test345"
    }
    ]
  ```

#### 3.  READ Operation(ID)
+ ##### Description
  + This returns information about the user-id passed in the endpoint
+ ##### Request
	+ Request Method: `GET`
	
	+ Endpoint :`https://hng-stage2-e6ly.onrender.com/api/1` 
	
+ ##### Response
    + Status code: `200`
	
    + Response message:
     ```json
   {
    "id": 1,
    "name": "Emmanuel_Ayomide"
    }
   ```

#### 4. UPDATE Operation
+ ##### Request
	+ Request Method: `PATCH`
	
	+ Endpoint: `https://hng-stage2-e6ly.onrender.com/api/1` 
	
	+ Request body: 
	```json
	 {
        "name": "Emmy_Ayo"
    }
  ```
+ ##### Response

    + Status code: `200`
	
    + Response message:
     ```json
   {
    "id": 1,
    "name": "Emmy_Ayo"
}
    ```

#### 5.  DELETE Operation
+ ##### Request
	+ Request Method: `DELETE`
	
	+ Endpoint: `https://hng-stage2-e6ly.onrender.com/api/1` 
	
+ ##### Response
    + Status code: `204`


# Installation Guide
Follow these steps to use this project on your Local device . Make sure you have python installed already,if not download from the [python website](http://www.python.org/downloads/ "python website") .
### Steps:
##### 1.  Clone the Repository:
+ Copy and paste the command below in your local device terminal

 ```bash
git clone https://github.com/your_username/your_django_project.git
```

##### 2. Change directory to  the Projects  directory and Create a .env file 
+ Copy and paste this in your .env file

     ```plaintext
  secretkey='django-insecure-ec=fvq-o!*@jwtnjzzlhaf9_^ono^jl=j%gt)n1_(757_n0at4'
   ```

##### 3. Install Required Packages: 
+ Your project should have a requirements.txt file that lists all the dependencies. Run the command below in the terminal

 ```bash
pip install -r requirements.txt
```

##### 4. Set up the database:
+ Apply migrations to create database tables by running the command below in your terminal

 ```bash
python manage.py migrate
```

##### 5. Run the Server:
+ Copy and paste the command below in the command prompt to run the server

 ```bash
python manage.py runserver
```