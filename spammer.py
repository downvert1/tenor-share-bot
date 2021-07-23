import requests, threading

done = 0

def lmfao():
    global done
    while True:
        try:
            r = requests.get('https://api.tenor.com/v1/registershare?platform=web&key=JJHDC7UK73EH&locale=en&anonid=MjYzNjE5MjE1Ng&id=22435017')
            done += 1
            print(f'Successfully added a share | This post now has been botted {done} shares. {r.status_code}')
        except:
            continue
while True:
    try:
        threading.Thread(target=lmfao).start()
    except:
        pass
