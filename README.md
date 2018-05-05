# SSH Decorator 

## Basic Usage
Install with

    pip3 install ssh_decorate

Running code on a remote server is as simple as

    from ssh_decorate import ssh_connect
    ssh = ssh_connect('user','password','server')
    
    # Run a python function
    @ssh
    def python_pwd():
        import os
        return os.getcwd()
    
    print (python_pwd())
    
    # Run a bash command
    ssh >> "ls"

Custom private key path or port ? no problem !

    ssh = ssh_connect('user','password','server',
          privateKeyFile = "path/to/key", port=22)
## Manual code execution

    # Remote shell/bash command
    ssh.exec_cmd("ls")
    
    # Remote python command
    ssh.exec_code("print ('hello world')")
    
## File Transfer

    # Download
    ssh.get_file("remote.name", "local.name")
    
    # Upload
    ssh.put_file("local.name", "remote.name")    
    
## Running on a pool of servers

    from ssh_decorate import ssh_pool
    pool = ssh_pool([
       {"server": "server1", "user": "user1", "password": "pass1"},
       {"server": "server2", "user": "user2", "password": "", "privateKeyFile": "~/.ssh/id_rsa"},
    ])
    
    @pool
    def pool_ls():
       import os
       return os.listdir(".")

    print (pool_ls())