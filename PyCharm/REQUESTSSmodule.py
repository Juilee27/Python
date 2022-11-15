# search -requests http for humans- on net
import requests

# r= requests.get('https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=quarter&limit=400&apikey=YOUR_API_KEY')
# print(r.text) #this is giving me content of r i.e. above api/url
# print(r.status_code) #google http status code



# --------------------------POST REQUEST---------------------------#
#NOTE- PASSWORDS VGERE URL VER NAI PATHVAT. POST REQ NE SEND HOTAT
# url = "www.something.com" #random ghetlay, DO NOT RUN THIS PART
# data = {
#     'p1':2, 'p2':9
# }
#
# r2 = requests.post(url = url, data= data)

# -------------------------------------TASK-------------------------------------#
# take any free api , send post requests
url = 'https://reqbin.com/echo/post/form'
data = {"userid":123, 'pincode': 300675}
r = requests.post(url, data)
print(r.text)
print(r.status_code)



