import requests
import sys

def fuzz_api():
    for word in sys.stdin:
        word = word.strip()
        try:
            res = requests.get(url=f"https://jsonplaceholder.typicode.com/posts{word}") #replace url with api you want to test.
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
