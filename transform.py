import json

raw = json.load(open('raw-fantasy.json'))['data']['value']['playerList']

POS = {1: 'GK', 2: 'DEF', 3: 'MID', 4: 'FWD'}

players = [{
    'id': p['id'],
    'name': p['pDName'],
    'fullName': p['pFName'],
    'club': p['tName'],
    'clubCode': p['cCode'],
    'clubId': p['tId'],
    'position': POS.get(p['skill'], 'UNK'),
    'value': p['value'],
    'points': p.get('totPts', 0),
    'goals': p.get('gS', 0),
    'assists': p.get('assist', 0),
    'mins': p.get('minsPlyd', 0),
    'owner': None,
    'price': None,
    'status': 'available',
} for p in raw if p.get('isActive') == 1]

json.dump(players, open('players.json', 'w'), indent=2, ensure_ascii=False)

print(f"{len(players)} players")
from collections import Counter
print(Counter(p['position'] for p in players))
print(Counter(p['club'] for p in players).most_common(5))