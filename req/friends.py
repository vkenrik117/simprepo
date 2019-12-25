import requests as r
import datetime as y



def calc_age(uid):
    response = r.get('https://api.vk.com/method/friends.get?v=5.71&access_token=10c48c8710c48c8710c48c87a610aa444c110c410c48c874ec71a602ea4918fe4b0c801&user_id=475705115&fields=bdate')
    json = response.json()
    seychas = y.datetime.now()
    gotovo = {}
    for user in json['response']['items']:
        if 'bdate' in user:
            s = user['bdate']
            if(len(s) == 9):
                #print(str(-(int(s[-4:])-int(seychas.year))), str(-(int(s[-4:])-int(seychas.year))) in gotovo)
                if str(-(int(s[-4:])-int(seychas.year))) in gotovo:
                    gotovo[str(-(int(s[-4:])-int(seychas.year)))] += 1
                else:
                    gotovo[str(-(int(s[-4:])-int(seychas.year)))] = 1
    return gotovo.items()

        

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
