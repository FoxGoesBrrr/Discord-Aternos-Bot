from python_aternos import Client

aternos_client = Client()

user = ENTER_YOUR_USERNAME
passw = ENTER_YOUR PASSWORD
#hashpassw = ENTER_YOUR_MD5_HASHED_PASSWORD
#atcookie = ATERNOS_SESSION_COOKIE_VALUE

aternos_client.login(user, passw)
#aternos_client.login_hashed(user, hashpassw)
#aternos_client.login_with_session(atcookie)
aternos = aternos_client.account

servs = aternos.list_servers()
serv = servs[0]
serv.fetch()
lol = serv.status
print(lol)