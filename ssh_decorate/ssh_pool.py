try:
    from .ssh_connect import ssh_connect
except:
    from ssh_connect import ssh_connect
import multiprocessing

class ssh_pool:
    """This class wraps the ssh_connect for multiple connections
    """

    def __init__(self, connection_list):
        self.conns = [ssh_connect(**args) for args in connection_list]
        self.processes = multiprocessing.Pool(len(connection_list))

    def __call__(self, func):
        """Runs a function on multiple servers"""
        ret_funcs = [conn.py(func) for conn in self.conns]

        def pool_func(*args, **kwargs):
            return [f(*args, **kwargs) for f in ret_funcs]
        return pool_func

    def __rshift__(self, cmd):
        """Runs a bash command on multiple servers"""
        return [conn.exec_cmd(cmd) for conn in self.conns]


if __name__ == "__main__":
    pool = ssh_pool([
       {"server": "127.0.0.1", "user": "ec2-user", "password": "", "privateKeyFile": "~/.ssh/id_rsa"}
    ])
    @pool
    def ls():
       import os
       return os.listdir(".")

    print (ls())

    pool >> "pwd"

