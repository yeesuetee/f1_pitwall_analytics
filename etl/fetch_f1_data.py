import requests
import pandas as pd

def get_race_results(year=2023, round_num=1):
    url = f"https://ergast.com/api/f1/{year}/{round_num}/results.json"
    resp = requests.get(url)
    data = resp.json()

    races = data['MRData']['RaceTable']['Races']
    if not races:
        return pd.DataFrame()

    results = races[0]['Results']

    rows = [
        {
            'position': r['position'],
            'driver': f"{r['Driver']['givenName']} {r['Driver']['familyName']}",
            'constructor': r['Constructor']['name'],
            'time': r.get('Time', {}).get('time'),
            'status': r['status']
        }
        for r in results
    ]

    return pd.DataFrame(rows)


# df = get_race_results(2023,1)
# print(df.head())