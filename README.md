python3 fuzzer.py https://<example.com?id= <path_to_file>

Make sure you put url with https otherwise it'll give you an error.
Path to file is a list for example with LFI payloads or XSS. The idea is to provide the response from the server to the requests with the payloads

This tool is to quickly fuzz a web app with huge lists of payloads
