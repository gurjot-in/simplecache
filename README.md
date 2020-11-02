

# simplecache
A simple, thread-safe in memory cache store written in Python.

## Installation

[Python 3.8](https://www.python.org/downloads/release/python-380/)  is required

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Features

- A caller facing API that allows others to use your library
- Verification that all functional requirements are present
- Verification that all functional requirements were met and work
- Documentation addressing the performance characteristics and memory usage



## How to run app 

```bash
uvicorn main:app --reload
```
Web server will be running at `http://127.0.0.1:8000/`


## API Doc
 
 HOST - http://127.0.0.1:8000
 
##### List all keys

	  GET /cache
    Status 200  OK
    
    Response JSON
    ["key1", "key2"]
    

##### Get key

    GET /cache/<key>
    Status 200  OK
    
    Response JSON
    "value"

##### Insert new key

    POST /cache
    Status 201  Created
    
    Request JSON
    {
    "key": "log",
    "value": "kafka"
	 }
  

##### Delete key

    DELETE /cache/<key>
    Status 204  No Content


