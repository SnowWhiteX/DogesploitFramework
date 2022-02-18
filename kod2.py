import paramiko

sshipinput=input("ssh ip enter: ")
userinput=input("username enter: ")
passwordinput=input("password enter: ")
s = input("command enter:  ")
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(sshipinput,username=userinput,password=passwordinput)
stdin, stdout, stderr = ssh.exec_command(s)
print(stdout.read())
