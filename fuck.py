import requests, random, string

url = "https://social-logins.com/ABC/D4/check.php"

headers = {
  "Origin" : "https://social-logins.com",

  "User-Agent" : "Mozilla/5.0 (Linux; Android 10; M2006C3LI Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/ 4.0 Chrome/96.0.4664.45 Mobile Safari/537.36",

  "Referer" : "https://social-logins.com/ABC/D4/?id=5791241724",

  "Accept" : "text/html,application/ xhtml+xml,application/xml;q=0.9,image/ avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

  "Upgrade-Insecure-Requests" : "1",

  "Content-Type": "application/x-www-form-urlencoded",
}

def rando():
  letters = string.ascii_lowercase
  result = "".join(random.choice(letters) for i in range(6))
  return result

def login(i):
  req = requests.Session()
  req.headers.update(headers)
  
  x = rando()
  email = x+"@gmail.com"
  password = rando()
  
  data = {
    "id" : "5791241724",
    "form_token" : "63c7d5fec1376",
    "email" : email,
    "password" : password,
    "login" : "Facebook",
  }
  
  resp=req.post(url,data=data,allow_redirects=True,timeout=300)
  
  print(i,email,password,resp)

i = 0
while True : 
  login(i)
  i+=1