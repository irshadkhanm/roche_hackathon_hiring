We are creating a REST server, fizz-buzz, that follows the classic Fizz-Buzz logic. The server should expose a REST API endpoint, with the additional feature of a statistical endpoint.

Fizz-Buzz Logic
The Fizz-Buzz algorithm involves replacing all multiples of 3 with "fizz", all multiples of 5 with "buzz" and all multiples of 15 with "fizzbuzz". Your output should look like this:
Example: “1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,..."
Requirements

Your server should adhere to the following specifications:

1. REST API Endpoint
•	Accept five parameters: three integers (int1, int2, and limit) and two strings (str1 and str2).
•	Return a list of strings containing numbers from 1 to limit.
•	Replace multiples of int1 with str1, multiples of int2 with str2, and multiples of both int1 and int2 with str1str2

2. Production Ready
•	Ensure that the server is ready for production use.
•	Prioritize clean and maintainable code to facilitate future development by other developers.

3. Statistics Endpoint:
•	Add a statistics endpoint that accepts no parameters.
•	Return the parameters corresponding to the most used request.
•	Include the number of hits for the most frequent request.

4. Unit Tests:
•	Develop comprehensive unit tests to validate the functionality of your server.

to achieve this we will follow below instruction, code for which is saved in fizzapp.py file.

1. importing necessary classes and functions
2. we will import <Flask> to create web aplication, <request> to access data from the HTTP request, and <jsonify> to convert Python data structures to JSON format
3. <Counter> is imported from collections module of python to count the occurences of elements" 

then we will create an instance of Flask class and then we have created In-memory storage for statistics, will be used to count the occurences 
  
FizzBuzz Logic is created to generate a fizzbuzz sequennce and returns it as a list

FizzBuzz Endpoint is created to define the route for the fizzbuzz endpoint

now, we have created fizzbuzz function 

1. The function retrieves parameters from the query string using request.args.get() with default values provided. It then updates the statistics and returns the FizzBuzz sequence as JSON
   
Statistics Endpoint is created to define route for the statistics endpoint

statistics function is created to check if there are any statistics. If not, it returns a JSON response indicating no requests have been made. Otherwise, it returns the most common set of parameters and the number of hits." 

if __name__  is created to check if script is run directly and not imported as module" 


app.run(debug=True) will start the flask development server. 
True parameter enables debugging mode, providing detailed error messages and ability to auto-reload the server on code changes during development." 


Use the App and its Flask:

1. we need to ensure that Flask is installed
2. Verify that your fizzapp module contains a Flask application named app
3. we will use <waitress-serve --host=0.0.0.0 --port=8000 fizzapp:app> code to use the fizzapp using waitress server
4. flask app can be accessed at http://localhost:8000/
5. Once the server is running, you can interact with the FizzBuzz API by making requests to the /fizzbuzz endpoint. For example, you can open a new terminal or use a tool like curl or Postman to make a GET request
   code < curl "http://localhost:8000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz"> 
