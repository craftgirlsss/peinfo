![1733279476617](images/readme/1733279476617.png)

**PeInfo is Information gathering for port scanner and Flood requst or DDoS Attack with TCP and UDP created by Putra Budianto**

*I recommended to use Unix Like Operating System like Linux or macOS because this using bash, you can use Windows operating system, but you must have git application and running this code with git bash*

**How to install?**

```
python3 -m venv ./
cd bin && source ./activate
cd ..
pip install -r requirements.txt
```

**Example for execution Port Scanner**

`./pinfo.py -n -p80 -sV target.com`

1. `-n` Port Scanner Method
2. `-p80` Port 80
3. `-sV` Service Version
4. `target.com` target you want to gathering information

**Example for execution DDoS attack for TCP Method**

`./pinfo.py -d -tC -t 1000 -p 80 -s 90 target.com`

1. `-d` DDoS Attack Method
2. `-tC` TCP Method
3. `-p` Port of target
4. `-t` Thread Count
5. `-s` Time for execution (second) default 60s
6. `target.com` Target you want to attack

**Example for execution DDoS attack for UDP Method**

`./pinfo.py -d -uD -t 1000 -p 80 -s 90 target.com`

1. `-d` DDoS Attack Method
2. `-uD` UDP Method
3. `-p` Port of target
4. `-t` Thread Count
5. `-s` Time for execution (second) default 60s
6. `target.com` Target you want to attack

We hope you can contribute to this project to make it even better. Thanks
