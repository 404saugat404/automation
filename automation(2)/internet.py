import requests
import subprocess
import sys

def check_internet():
    try:
        # Try to make a request to a well-known website (in this case, Google)
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def run_online_script():
    try:
        subprocess.run([sys.executable, "online.py"], check=True)
    except subprocess.CalledProcessError:
        print("Error running online.py")

def main_function_code():
    if check_internet():
        print("Internet is available. Running online.py...")
        run_online_script()
    else:
        print("Check your Internet connection")

if __name__ == "__main__":
    main_function_code()    