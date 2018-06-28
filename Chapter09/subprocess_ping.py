import subprocess


def ping_destination(ip):
    p = subprocess.Popen(['ping', '-c', '3'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(input=ip)
    if p.returncode == 0:
        print("Host is alive")
        return True, stdout
    else:
        print("Host is down")
        return False, stderr


while True:
    print(ping_destination(raw_input("Please enter the host:")))

# print(ping_destination('HostNotExist'))
