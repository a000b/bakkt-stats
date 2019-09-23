from requests_html import HTMLSession


url = 'https://www.theice.com/products/72035464/Bakkt-Bitcoin-USD-Monthly-Futures-Contract/data?marketId=6137541'


def get_info():
    l = {}
    session = HTMLSession()
    try:
        r = session.get(url)
        r.html.render()
        table = r.html.find('table', first=True)
        data = [element.text for element in r.html.find('td')]
        data[2] = data[2].replace("\n", " ")
        
        mesg = (
            f"BAKKT stats:\n"
            f"Czas :{data[2]}\n"
            f"Źródło : {url}\n"
            f"Kontrakt :{data[0]}\n"
            f"Cena :{data[1]}\n"
            f"Zmiana :{data[3]}%\n"
            f"Wolumen :{data[4]} BTC\n"

                )
    except:
        mesg ='err'
        
    return(mesg)

print(get_info())