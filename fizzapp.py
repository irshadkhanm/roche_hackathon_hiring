
# importing necessary classes and functions
# <Flask> to create web aplication
# <request> to access data from the HTTP request, and
# <jsonify> to convert Python data structures to JSON format

from flask import Flask, request, jsonify

# <Counter> is imported from collections module of python to count the occurences of elements

from collections import Counter

# an instance of Flask class is created

app = Flask(__name__)

# In-memory storage for statistics, will be used to count the occurences

request_stats = Counter()

# FizzBuzz Logic

# this will generate a fizzbuzz sequennce and returns it as a list

def fizz_buzz(int1, int2, limit, str1, str2):
    result = []
    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            result.append(str1 + str2)
        elif i % int1 == 0:
            result.append(str1)
        elif i % int2 == 0:
            result.append(str2)
        else:
            result.append(str(i))
    return result

# FizzBuzz Endpoint

# to define the route for the fizzbuzz endpoint

@app.route('/fizzbuzz', methods=['GET'])

# The function retrieves parameters from the query string using request.args.get()
# with default values provided. It then updates the statistics and returns the FizzBuzz sequence as JSON

def fizzbuzz():
    try:
        int1 = int(request.args.get('int1', 3))
        int2 = int(request.args.get('int2', 5))
        limit = int(request.args.get('limit', 100))
        str1 = request.args.get('str1', 'fizz')
        str2 = request.args.get('str2', 'buzz')

        # Update statistics
        request_stats[(int1, int2, limit, str1, str2)] += 1

        return jsonify(fizz_buzz(int1, int2, limit, str1, str2))
    except ValueError:
        return jsonify({"error": "Invalid input parameters"}), 400

# Statistics Endpoint

# to define route for the statistics endpoint

@app.route('/statistics', methods=['GET'])

# The function checks if there are any statistics. If not, it returns a JSON response indicating no requests have been made.
# Otherwise, it returns the most common set of parameters and the number of hits.

def statistics():
    if not request_stats:
        return jsonify({"error": "No requests made yet"}), 404
    most_common = request_stats.most_common(1)[0]
    return jsonify({
        "parameters": most_common[0],
        "hits": most_common[1]
    })

# to check if script is run directly and not imported as module

if __name__ == '__main__':

# this will start the flask development server.
# True parameter enables debugging mode, providing detailed error messages and ability to
# auto-reload the server on code changes during development.

    app.run(debug=True)