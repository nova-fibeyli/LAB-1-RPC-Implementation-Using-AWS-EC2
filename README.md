# **LAB-1-RPC-Implementation-Using-AWS-EC2**

This repository contains a minimal Remote Procedure Call (RPC) implementation using Python, TCP sockets, and JSON. The system consists of two AWS EC2 instances: one server and one client.

# **Environment and infrastructure:**

Two AWS EC2 instances were used.

**Instance 1:**
Name: rpc-server-node
AMI: Ubuntu Server 22.04 LTS
Instance type: t2.micro
Public IPv4 address: enabled

**Instance 2:**
Name: rpc-client-node
AMI: Ubuntu Server 22.04 LTS
Instance type: t2.micro
Public IPv4 address: enabled

Both instances were placed in the same VPC.

Security group configuration

A single security group was created with the following inbound rules:
- SSH, TCP port 22, source 0.0.0.0/0
- Custom TCP, port 5000, source 0.0.0.0/0

Port 5000 is used for RPC communication between the client and server.

# **Prerequisites on both instances:**

The following packages must be installed on both the server and client instances:

```
sudo apt update
```
```
sudo apt install python3 python3-pip -y
```

**Python version used:**
python3 (system default on Ubuntu 22.04)

**Files:**
1) server.py
Implements the RPC server. The server listens on TCP port 5000, accepts JSON requests, executes a simple add(a, b) function, and returns the result. An artificial delay is introduced to demonstrate timeout and retry behavior.

2) client.py
Implements the RPC client. The client connects to the server on port 5000, sends a request with a unique request_id, waits for a response with a timeout, and retries the request if a timeout occurs.

# **How to run?**

**1. On the server EC2 instance, start the server:**

```
python3 server.py
```

The server will begin listening on port 5000.

**2. On the client EC2 instance, edit client.py and set the SERVER_IP value to the public IPv4 address of the server instance.**

**3. Run the client:**
   
```
python3 client.py
```

**Expected behavior:**

The client sends a request to the server to execute a remote add operation.
The server introduces a short delay before responding.
The client may experience a timeout and retry the request.
A successful response is eventually received.
This behavior demonstrates timeout handling, retry logic, and at-least-once RPC semantics.

