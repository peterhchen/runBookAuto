import requests
url = 'http://master/api/run'
data = '{
  "server": [
     {"server-name": "s1", "sshKey": "000001", "run-cmd": "ls"},
     {"server-name": "s2", "sshKey": "000002", "run-cmd": "mkdir"},
     {"server-name": "s3", "sshKey": "000003", "run-cmd": "cp"},
     {"server-name": "s4", "sshKey": "000004", "run-cmd": "cat"},
     {"server-name": "s5", "sshKey": "000005", "run-cmd": "pipe (|)"},
  ]
}'
response = requests.post(url, data=data)
