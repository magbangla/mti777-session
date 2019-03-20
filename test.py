import requests
def test():
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',

        'Host': 'www.kangalou.com',
        'Origin': 'https://www.kangalou.com',
        'Referer':'https://www.kangalou.com/fr/location/montreal/cote-des-neiges?q=S1Y1dTJQNXWxNTEwUCvIzcyzNTQAsxIrbI1BrGLbvNTy1OISAA%3D%3D',
        'Connection': 'keep-alive'
        }

    response = requests.get('https://www.kangalou.com/fr/location/montreal/cote-des-neiges?q=S1Y1dTJQNXWxNTEwUCvIzcyzNTQAsxIrbI1BrGLbvNTy1OISAA%3D%3D', headers=headers)
    print response.content


if __name__ == '__main__':
    # Start app
    test()
