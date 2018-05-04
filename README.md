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

## Manual code execution

    # Remote shell/bash command
    ssh.exec_cmd("ls")
    
    # Remote python command
    ssh.exec_cmd("print 'hello world'")
    
## File Transfer

    # Download
    ssh.get_file("remote.name", "local.name")
    
    # Upload
    ssh.get_file("local.name", "remote.name")    