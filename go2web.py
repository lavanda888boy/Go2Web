import argparse
from urllib.parse import urlparse
import socket
import ssl

HTTPS_PORT = 443
HTTP_PORT = 80

def parse_url(url):
    parsed_url = urlparse(url)

    scheme = parsed_url.scheme
    host = parsed_url.netloc
    path = parsed_url.path

    return scheme, host, path


def send_http_get_request(host, port, path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    if port == 443:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=host)

    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())

    response = b""
    while True:
        data = sock.recv(2048)
        if not data:
            break
        response += data

    sock.close()
    return response.decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Make an HTTP request to the specified URL and print the response')
    parser.add_argument('-s', nargs='+', help='Make an HTTP request to search the term using your favorite search engine and print top 10 results')

    args = parser.parse_args()

    if args.u:
        scheme, host, path = parse_url(args.u)
        if scheme == 'https':
            print(send_http_get_request(host, HTTPS_PORT, path))
        else:
            print(send_http_get_request(host, HTTP_PORT, path))
    else:
        pass


if __name__ == "__main__":
    main()
