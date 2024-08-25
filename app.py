from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# Utility function to check if a string is an alphabet
def is_alphabet(s):
    return s.isalpha()

@app.route('/bfhl', methods=['POST'])
def process_request():
    try:
        # Parse the request body as JSON
        request_data = request.get_json()

        # Initialize response object with user details
        response = {
            "is_success": True,
            "user_id": "tisha_mahajan_29112002",   # Replace with actual user id
            "email": "tisha.mahajan2021@vitstudent.ac.in",  # Replace with actual email
            "roll_number": "21BBS0086",           # Replace with actual roll number
            "numbers": [],
            "alphabets": [],
            "highest_lowercase_alphabet": ""
        }

        # Initialize data structures to hold numbers and alphabets
        numbers = []
        alphabets = []
        highest_lowercase = ""

        # Iterate through input data to separate numbers and alphabets
        for item in request_data.get("data", []):
            if item.isdigit():
                # Item is a number
                numbers.append(item)
            elif is_alphabet(item):
                # Item is an alphabet
                alphabets.append(item)
                # Check for highest lowercase alphabet
                if item.islower() and (highest_lowercase == "" or item > highest_lowercase):
                    highest_lowercase = item

        # Populate the response object with filtered data
        response["numbers"] = numbers
        response["alphabets"] = alphabets
        response["highest_lowercase_alphabet"] = highest_lowercase

        # Return the response as JSON
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": "Invalid JSON format or other error", "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # Return hardcoded operation code
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


