import socket
from collections import namedtuple
import connect4

ConnectFourConnection = namedtuple('ConnectFourConnection' , ['socket', 'wordsIn', 'wordsOut'])

class ConnectFourProtocolError(Exception):
    pass

_SHOW_BUG_TRACE = False

HELLO = 0
NO_USER = 1

def make_connection(host:str, port:int)->ConnectFourConnection:
    connect_four_socket = socket.socket()
    print('connecting...')

    connect_four_socket.connect((host,port))
    print('connected')
    connect_four_input = connect_four_socket.makefile('r')
    connect_four_output = connect_four_socket.makefile('w')
    connect_four_socket.close()

    return ConnectFourConnection(socket = connect_four_socket, wordsIn = connect_four_input, wordsOut = connect_four_output)



def first_line(connection:ConnectFourConnection, username:str)-> HELLO:
    _write_line(connection, 'I32CFSP_HELLO ' + username)

    response = _read_line(connection)

    if response.startswith('WELCOME '):
        return HELLO
    else:
        raise ConnectFourProtocolError()

    
def input_message() -> str:
    '''asks the user for message to send to the host
    '''
    return input('send message: ') 

def send_message_to_server(connection: ConnectFourConnection, message:str) -> None:
    _write_line(connection, message)
    connection.words.out.flush()

def print_server_response(connection: ConnectFourConnection ) -> None:
    '''prints readable response from server'''
    print(_read_line(connection))
def close_connection(connection: ConnectFourConnection ) -> None:
    '''
    closes connect 4 game connection
    '''
    connection.wordsIn.clos()
    connection.wordsOut.close()
    connection.socket.close()


def _read_line(connection: 'ConnectFourConnection') -> None:
    '''
    Reads a line of text sent from the server and gets rid of the new line character
    '''
    line = connection.wordsIn.readline()[:-1]
    
    if _SHOW_BUG_TRACE:
        print('RCVD: ' + line)
        
    return line

def _write_line(connection: 'connection', line:str ) ->None:
    '''
    writes text to the server
    '''
    connectfour_socket, connectfour_socket_input, connectfour_socket_output = connection
    connect_four_socket_output.write(line + '\r\n')
    connect_four_socket_output.flush()
    

    if _SHOW_BUG_TRACE:
        print('SENT: ' + line)


def _read_host()-> str:
    while True:
        host = input('Host: ' )
        if host == '':
            print('Please specify a host (either an IP address or a name)')
        else:
            return host
        
def _read_port() -> int:
    while True:
        try:
            port = int(input('Port: ' ))
            if port<0 or port>65535:
                 print('Ports must be integers within these values')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

if __name__ == '__main__':
    make_connection(_read_host(), _read_port())
    username = input()
    first_line(ConnectFourConnection,'boo')
    print_server_response()
