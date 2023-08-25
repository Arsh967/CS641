import paramiko

# create an SSH client
client = paramiko.SSHClient()

# automatically add the host key (not recommended in production)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the SSH server
client.connect(hostname='172.27.26.188', port=22, username='student', password='cs641')

# open an SFTP session to transfer files
sftp = client.open_sftp()

# navigate to a directory
sftp.chdir('/path/to/directory')

# execute a command and get the output
stdin, stdout, stderr = client.exec_command('ls')
output = stdout.read().decode()

# close the connection
client.close()
