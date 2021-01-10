import subprocess, os, requests

def main():
    server = os.getenv('SERVER')
    server_port = os.getenv('SERVER_PORT')
    timeout = os.getenv('TIMEOUT')
    containerid = os.getenv('CONTAINER_ID')
    tcpdump_port = os.getenv('TCPDUMP_PORT')
    tcpdump_host = os.getenv('TCPDUMP_HOST')
   
    http_url = server + ":" + server_port + "?timeout=" + timeout + "&containerid=" + containerid + "&port=" + tcpdump_port + "&host=" + tcpdump_host
    HttpGetTesting(http_url)

def HttpGetTesting(http_url):
    print("HTTP GET test started:",http_url)
    r = requests.get(http_url)
    print("HTTP GET test finished:", r.status_code, r.reason, r.text)

if __name__ == "__main__":
    main()
