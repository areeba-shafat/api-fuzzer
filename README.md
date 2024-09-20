##### API Fuzzer (for KALI LINUX) ######

This project is a custom API fuzzer developed to test the robustness and security of RESTful APIs. The fuzzer sends various inputs to specified endpoints and analyzes the responses to identify potential vulnerabilities and unexpected behaviors.

### Features
Automated Testing: Sends GET requests to API endpoints with various inputs.
Error Handling: Logs different HTTP status codes and handles errors.
Formatted Output: Prints JSON responses in a readable format.
Endpoint Validation: Skips endpoints that return a 404 Not Found status.
Clear Logging: Provides structured output for easy analysis.

### Installation

# Prerequisites
Python 3.x
requests library

# Steps
# Clone the Repository:
```
git clone https://github.com/areeba-shafat/api-fuzzer.git
cd api-fuzzer
```
# Install Dependencies:
```
pip install requests
```

### Usage
Prepare Input Data:
you can use your own set of data (for demonstration purposes example.txt is given)

# Run the Script:
Use the following command to run the script with the input file:
```
cat example.txt | python3 api-fuzzer.py
```


### CODE OVERVIEW ###
api-fuzzer.py
```
import requests
import sys

def fuzz_api():
    for word in sys.stdin:
        word = word.strip()
        try:
            res = requests.get(url=f"https://jsonplaceholder.typicode.com/posts{word}")
            if res.status_code == 404:
                print(f"404 Not Found: {word}")
                continue
            else:
                try:
                    data = res.json()
                    print(f"Endpoint: {word}")
                    print(f"Status Code: {res.status_code}")
                    print("Response Data:")
                    print_json(data)
                    print("-" * 40)
                except ValueError:
                    print(f"Endpoint: {word}")
                    print("Response is not in JSON format")
                    print("-" * 40)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for endpoint {word}: {e}")
            print("-" * 40)

def print_json(data, indent=4):
    import json
    print(json.dumps(data, indent=indent))

if __name__ == "__main__":
    fuzz_api()
```

Feel free to customize this README.md file to better fit your project and preferences.

