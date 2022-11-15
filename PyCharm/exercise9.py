#===================================AKBAR PADHKE SUNAO===========================================#
# this is going to provide daily news
# visit site News API
# visit news API - documentation - refer snapshot
# install pywin32 module
# harry ne speak func dilay, to code use kra
# task is - daily top 10 news it should speak meaning read it to u like:
# 1st news is:
# 2nd news is:
# esa top 10 news
# json ani request module use krun news reader banvay
# and daily it shld read differnt news , same news shld not be repeated

# newsapi.org - jui username, pass - MAYmay@27
# Your API key is: 3bb508106b514ae99b088d411d20d5f7

# DO NOT FORGET TO INSTALL JSON EXTENSION IN CHROME - done

#~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~Solution~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json

    speak('news for today. lets begin')

    news = requests.get('https://newsapi.org/v2/top-headlines?country=in&'
                        'pageSize=10&apiKey=3bb508106b514ae99b088d411d20d5f7')
    # print(news.text)
    # print(type(news.text), type(news))

    parsed = json.loads(news.text)
    print(type(parsed))  #<class 'dict'>
    # # for key in parsed.keys():
    # #     if key == 'articles':
    # #         print(parsed[key])
    # #         print(type(key))
    #
    i=1
    # while i<11:
    #     for key in parsed.keys():
    #         if key == 'articles':
    #             text = str(parsed[key][i])
    #             print(text.split(''''description':''')[1])
    #             # speak(f"news {i} is {parsed[key][i].split(''''description':''')[1]}")
    #             speak(f"news {i} is {text.split(''''description':''')[1]}")
    #             i+=1

#-----------------------below is harry's code (very simple!)-------------------------------------------
    arts=  parsed["articles"]
    for news in arts:
        print(news["title"])
        speak(f" news {i} is {news['title']}")
        i+=1
