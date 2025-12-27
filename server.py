import socket
import json
import time

HOST = "0.0.0.0"
PORT = 5000

def handle_request(data):
    request = json.loads(data)
    request_id = request["request_id"]
    method = request["method"]
    params = request["params"]

    # Artificial delay to demonstrate timeout and retry
    time.sleep(1)

    if method == "add":
        result = params["a"] + params["b"]
        return {
            "request_id": request_id,
            "result": result,
            "status": "OK"
        }

    return {
        "request_id": request_id,
        "status": "ERROR"
    }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("RPC Server listening on port 5000")

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            response = handle_request(data.decode())
            conn.sendall(json.dumps(response).encode())
