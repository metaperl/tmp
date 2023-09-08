from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_user = 'uname'
rpc_password = 'passwd'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:6969"%(rpc_user, rpc_password))

print rpc_connection
print rpc_connection.getbalance()
