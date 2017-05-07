
# Core
import ConfigParser
import logging
import traceback

# 3rd Party
import argh
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Local
import exception
import mymailer


class Wallet(object):

    def __init__(self, config, wallet_config_label):

        self.config, self.wallet_config_label = config, wallet_config_label


    @property
    def connection(self):
        rpc_user = self.config.get(self.wallet_config_label, 'rpcuser')
        rpc_password = self.config.get(self.wallet_config_label, 'rpcpassword')
        port = self.config.get(self.wallet_config_label, 'port')
        ip = self.config.get(self.wallet_config_label, 'ip')

        rpc_connection = AuthServiceProxy(
            "http://{}:{}@{}:{}".format(rpc_user, rpc_password, ip, port))

        return rpc_connection

    @property
    def max_allowed(self):
        m = self.config.getfloat(self.wallet_config_label, 'max')
        logging.debug("max allowed: %.8f", m)
        return m

    @property
    def min_allowed(self):
        return self.config.getfloat(self.wallet_config_label, 'min')

    @property
    def balance(self):
        b = self.connection.getbalance()
        f = float(b)
        logging.debug("balance: %.8f", f)
        return f

    def error_msg(self, text):
        return self.wallet_config_label + ": " + text


    def max_check(self):
        if self.balance > self.max_allowed:
            e = exception.BalanceTooLarge
            error_msg = self.error_msg(e.error_msg(
                self.balance, self.max_allowed))
            logging.debug(error_msg)
            raise e(error_msg)
        else:
            logging.debug("No Max violation.")

    def min_check(self):

        if self.balance < self.min_allowed:
            e = exception.BalanceTooSmall
            error_msg = self.error_msg(e.error_msg(
                self.balance, self.max_allowed))
            raise e(error_msg)

def notify_admin(app_instance, e, subject):
    error_msg = traceback.format_exc()
    logging.info('Aborting on error: %s', error_msg)
    mymailer.send_email(app_instance, subject, error_msg)

def main(config_file, wallet):

    try:
        config = ConfigParser.RawConfigParser()
        config.read(config_file)

        wallet  = Wallet(config, wallet)

        wallet.max_check()
        wallet.min_check()

    except exception.BalanceTooLarge as e:
        pass # sweep, whatever that is

    except exception.BalanceTooSmall as e:
        notify_admin(wallet, e, "Balance too Small")


if __name__ == '__main__':
    argh.dispatch_command(main)
