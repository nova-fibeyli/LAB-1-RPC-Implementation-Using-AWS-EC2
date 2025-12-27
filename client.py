import socket
import json
import uuid

SERVER_IP = "44.222.203.88"
PORT = 5000
TIMEOUT = 2
RETRIES = 3

request = {
    "request_id": str(uuid.uuid4()),
    "method": "add",
    "params": {"a": 5, "b": 7}
}

for attempt in range(RETRIES):
    try:
        print(f"Attempt {attempt + 1}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            s.connect((SERVER_IP, PORT))
            s.sendall(json.dumps(request).encode())
            response = s.recv(1024)
            print("Response:", response.decode())
            break
    except socket.timeout:
        print("Timeout occurred, retrying...")
