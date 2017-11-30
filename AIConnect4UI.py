import AIConnect4

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
            port = input('Port: ' )
            if port<0 or port>65535:
                 print('Ports must be integers within these values')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that is non-empty, as
    the Polling server requires.
    '''
    while True:
        username = input('Username: ').strip()

        if len(username) > 0:
            return username
        else:
            print('That username is blank; please try again')

def _run_user_interface() -> None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    _show_welcome_banner()
    connection = AIConnect4.connect(POLLING_HOST, POLLING_PORT)

    try:
        while True:
            username = _ask_for_username()

            response = AIConnect4.hello(connection, username)

            if response == polling.NO_USER:
                print('That user does not exist')
            else:
                break

        # Notice how _handle_command returns False only when there are
        # no more commands to be processed.  That gives us the ability
        # to get out of this loop.
        while _handle_command(connection):
            pass

    finally:
        # No matter what, let's make sure we close the Polling connection
        # when we're done with it.
        polling.close(connection)
def _show_welcome_banner() -> None:
    '''
    Shows the welcome banner
    '''
    print('Welcome to the Connect 4 client!')
    print()
    print('Please login with your username.')
    print()
