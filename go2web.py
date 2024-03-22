import argparse
import socket
import ssl

HTTPS_PORT = 443
HTTP_PORT = 80

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
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-u', help='Make an HTTP request to the specified URL and print the response')
    # parser.add_argument('-s', nargs='+', help='Make an HTTP request to search the term using your favorite search engine and print top 10 results')

    # args = parser.parse_args()
    # print(args.s)

    print(send_http_get_request('utm.md', HTTPS_PORT, '/'))

if __name__ == "__main__":
    main()
