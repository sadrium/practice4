import socket

sock = socket.socket()

username = input('Логин: ')
password = input('Пароль: ')

port = input('Порт (Enter - по умолчанию): ')

if not port:
    port = 9090
else:
    port = int(port)

addr = input('Адрес(Enter - по умолчанию): ')

if not addr:
    addr = 'localhost'

sock.connect((addr, port))
sock.send((username + '/' + password).encode())

resAutorization = sock.recv(1024).decode()
print(resAutorization, end='')

while True:
    data = input(f'{username} >>> ')
    sock.send(data.encode())

    if data == 'Выход':
        break
    elif data == 'Напомни мой username' or data == 'Время':
        answer = sock.recv(1024).decode()
        print(f'Server: {answer}')

sock.close()