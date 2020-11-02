


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

##### Insert key

    POST /cache
    Status 201  Created
    
    Request JSON
    {
    "key": "log",
    "value": "kafka"
	 }
	 

##### Insert self expiry key

    POST /cache
    Status 201  Created
    
    Request JSON
    {
    "key": "log",
    "value": "kafka",
    "ttl": 3
	 }

##### Delete key

    DELETE /cache/<key>
    Status 204  No Content

## Performance Testing
[ApacheBench](https://httpd.apache.org/docs/2.4/programs/ab.html) 
```bash
ab -n 1000 -c 5  http://127.0.0.1:8000/cache/key
```
![ScreenShot](/docs/perf_ss.png)


