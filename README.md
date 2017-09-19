SSH Decorator 
---
Install with

    pip3 install ssh_decorate

Running code on a remote server is as simple as

    from ssh_decorate import ssh_connect
    ssh=ssh_connect('user','password','server')
    
    #Run a python function
    @ssh
    def python_pwd():
        import os
        return os.getcwd()
    
    print (python_pwd())
    
    #Run a bash command
    ssh>>"ls"

