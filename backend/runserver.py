import socket, subprocess

PORT = '8000'

def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def main():
    '''Run'''
    subprocess.call(f'python manage.py runserver { PORT }', shell=True)


if __name__ == '__main__':
    main()