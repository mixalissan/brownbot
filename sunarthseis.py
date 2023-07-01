import requests

"""sunarthseis"""


#sunarthsh gia office quote api
def get_quote():
    response = requests.get("https://officeapi.dev/api/quotes/random")
    quote = response.json()
    return (quote['data']['content'] + "\n - " +
            quote['data']['character']['firstname'] + " " +
            quote['data']['character']['lastname'])

def get_episode():
    response = requests.get("https://officeapi.dev/api/episodes/random")
    quote = response.json()
    return ("**" + quote['data']['title'] + "**" + "\n" + "Description: ||" + quote['data']['description'] 
    + "||")

        
#sunarthsh gia cat photos api
def get_cat():
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search?api_key=e2dec158-0a3c-4f01-a7a5-fd29ea207b92"
    )
    cat = response.json()[0]['url']
    return (cat)

#returns name of message author
def get_name(messageauthor):
    userfullname = str(messageauthor)
    name = ''
    tag = ''
    for i in range(0, len(userfullname)):
      if i < (len(userfullname)-5):
        name += userfullname[i]
      else:
        tag += userfullname[i]
    if tag == '#7161':
      return('michael')
    elif tag == '#9839':
      return('andrew')
    else:
      return(name)
