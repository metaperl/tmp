# Core
import ConfigParser

# 3rd Party
import argh
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Local

config = ConfigParser.RawConfigParser()


def rpc_connection(config, wallet):
    rpc_user = config.get(wallet, 'rpcuser')
    rpc_password = config.get(wallet, 'rpcpassword')
    port = config.get(wallet, 'port')
    rpc_connection = AuthServiceProxy(
        "http://{}:{}@127.0.0.1:{}".format(rpc_user, rpc_password, port))
    return rpc_connection

def current_balance(connection):
    return connection.getbalance()

def max_check(connection):
    pass

def main(config_file, wallet):

    config.read(config_file)

    connection = rpc_connection(config, wallet)

    max_check(connection)
    min_check(connection)


if __name__ == '__main__':
    argh.dispatch_command(main)
