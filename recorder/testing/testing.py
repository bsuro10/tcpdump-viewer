import subprocess, os, requests

def main():
    server = os.getenv('SERVER')
    timeout = os.getenv('TIMEOUT')
    containerid = os.getenv('CONTAINER_ID')
    tcpdump_port = os.getenv('TCPDUMP_PORT')
    tcpdump_host = os.getenv('TCPDUMP_HOST')
   
    http_url = server + "?timeout=" + timeout + "&containerid=" + containerid + "&port=" + tcpdump_port + "&host=" + tcpdump_host
    status_code = HttpGetTesting(http_url)
    if (status_code != 200):
        exit(1)

def HttpGetTesting(http_url):
    print("HTTP GET test started:",http_url)
    r = requests.get(http_url)
    print("HTTP GET test finished:", r.status_code, r.reason, r.text)
    return r.status_code

if __name__ == "__main__":
    main()
