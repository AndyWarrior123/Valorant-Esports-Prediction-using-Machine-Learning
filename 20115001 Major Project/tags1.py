import requests
import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup


# ________________________________________________________
def custom_replace(a):
    val = a.replace("\\t","")
    val = val.replace("\\n", "")
    val = val.replace("['","")
    val = val.replace("']","")
    return val

def custom_replace1(my_str):
    my_str = my_str.replace("{'title': '", "")
    my_str = my_str.replace("'}","")
    my_str = my_str.replace("', 'style': 'padding-left: 14px;","")
    my_str = my_str.replace("', 'style': 'padding-left: 1px;","")
    my_str = my_str.replace("', 'style': 'padding-left: 9px;","")
    my_str = my_str.replace("', '","")
    my_str = my_str.replace("': '","")
    my_str = my_str.replace('"','')
    my_str = my_str.replace("{}","")
    return my_str

def custom_replace2(my_str):
    my_str = my_str.replace('%','')
    my_str = my_str.replace('+', '')
    my_str = my_str.replace('-','')
    return my_str

def custom_replace3(my_str):
    my_str = my_str.replace('\t','')

    return my_str

def compare_rows(row_a, row_b):
  # Sort by the first value in the row.
  if row_a[0] < row_b[0]:
    return -1
  elif row_a[0] > row_b[0]:
    return 1
  else:
    # If the first values are equal, sort by the second value in the row.
    if row_a[1] < row_b[1]:
      return -1
    elif row_a[1] > row_b[1]:
      return 1
    else:
      return 0
# __________________________________________________________

with open("url.txt", "r", encoding="UTF-8") as f:
    url_lines = f.read()

url_arr = url_lines.splitlines()

# print(type(url_lines))
# print(url_arr)


"""
# url1 = "https://www.vlr.gg/248277/paper-rex-vs-evil-geniuses-valorant-champions-2023-playoffs-gf"

# url2 = "https://www.vlr.gg/248282/fnatic-vs-loud-valorant-champions-2023-playoffs-lr3"

# url3 = "https://www.vlr.gg/167391/loud-vs-drx-champions-tour-2023-lock-in-s-o-paulo-sf"

# url_arr = []
# url_arr.append(url1)
# url_arr.append(url2)
# url_arr.append(url3)

"""

# def read_game_ID(u):
#     page = requests.get(u)
#     soup = BeautifulSoup(page.text, 'html.parser')

#     for i in soup.find_all(class_ = 'vm-stats-gamesnav-item js-map-switch'):
#         game_ID.append(str(i.get('data-game-id')))

"""
def performance(u, perf2):
    page = requests.get(u + "/?game=all&tab=performance")
    soup = BeautifulSoup(page.text, 'html.parser')

    names = []
    arr = []
    maps = []
    perf = []

    for games in soup.find_all('div', {'data-game-id': game_ID[0]}):
        for i in games.find_all('div', {'class': 'team'}):
            s = str(i.find('div').get_text())
            s = s.strip()
            s = custom_replace3(s)
            names.append(s)
    
    for i in range(len(names)):
        l = names[i].find('\n')
        names[i] = names[i][0:l]

    names = names[-10:]
    # print(names[-10:])

    for i in soup.find_all('tr'):
        for j in i.find_all('td'):
            for stats in j.find_all(class_='stats-sq'):
                arr.append(str(stats.get_text()).replace('\t','').replace('\n',''))

    for i in range(len(arr)):
        if(len(arr[i]) > 3):
            arr[i] = arr[i][0]

    for i in range(len(arr)):
        if(arr[i] == ''):
            arr[i] = 0

    n = ''
    new_arr = arr[355:]
    n = len(game_ID)
    i = 0
    cnt = 0

    while(cnt < n):
        temp = np.array_split(new_arr[i+225: i + 355], 10)
        for val in range(len(temp)):
            temp[val][0] = names[val%10]
            # print(temp[val])
        perf.extend(temp)

        i += 355
        cnt += 1

    # for i in perf:
        # print(i)

    perf1 = np.array_split(perf, n)
    perf2 = []
    for i in range(n):
        temp = []
        for j in np.array_split(perf1[i], 2):
            temp.append(sorted(j, key=lambda x: x[0]))
        perf2.extend(temp)

    print(perf2)


def overview(u):

    page = requests.get(u)
    soup = BeautifulSoup(page.text, 'html.parser')

    page1 = BeautifulSoup()

    x = []
    for i in  soup.find_all(class_="match-header-vs-note"):
        x.append(str(i.get_text()).strip())

    # print(x[1])

    # Map
    maps = []
    # Team Names:
    team_name = []
    # Scores
    scores = []
    # No of played Maps
    n = ""

    # player Name
    player_names_arr = []

    # Player Agent
    player_agent_arr = []

    # Player Stats
    player_stats_arr=[]

    # Matches
    match = []

    # Naming
    naming = []

    # -----------------------------------------------------------------
    for map in soup.find_all(class_="map"):
        for i in map.find_all("span", {"style":"position: relative;"}):
            my_str = str(i.contents[0])
            maps.append(my_str.strip())


    n = len(maps)


    for name in soup.find_all(class_="team-name"):
        my_string = str(name.contents)
        val = custom_replace(my_string)
        team_name.append(val)
        # print(val)

    team_name = team_name[0:2]



    for score in soup.find_all(class_="score"):
        scores.append(int(score.get_text()))
        # print(score.get_text())

    scores = np.array_split(scores, n)


    for name in soup.find_all("div", {"style": "font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;"}):
        my_str = str(name.contents)
        val = custom_replace(my_str)
        # print(val)
        player_names_arr.append(val)

    player_names_arr = player_names_arr[0:10] + player_names_arr[(n-1)*(-10):]


    for agent in soup.find_all(class_ = "stats-sq mod-agent small"):
        player_agent_arr.append(agent.find("img").get("title"))

    player_agent_arr = player_agent_arr[0:10] + player_agent_arr[(n-1)*(-10):]


    for i in soup.find_all('td',{'class':'mod-stat'}):
        my_str = str(i.find("span", {'class': 'side'}).contents)
        my_str = custom_replace(my_str)
        my_str = custom_replace2(my_str)
        # print(my_str)
        player_stats_arr.append(float(my_str))

    player_stats_arr = player_stats_arr[0:120] + player_stats_arr[(n-1)*(-120):]

    newArr = np.array_split(player_stats_arr, n*10)
    player_stats_arr1 = []
    test_arr = []
    for i in newArr:
        test_arr = i
        player_stats_arr1.append(test_arr)

    # print(player_stats_arr1)
    player_stats_arr2 = player_stats_arr1[0:10]+player_stats_arr1[(n-1)*(-10):]

    for i in range(0,n*10):
        test_arr = []
        test_arr.append(player_names_arr[i])
        test_arr.append(player_agent_arr[i])
        test_arr.extend(player_stats_arr2[i])
        # print(test_arr)
        match.append(test_arr)

    match = np.array(match)
    match = np.array_split(match, n)

    match1 = []
    for i in match:
        for j in (np.array_split(i, 2)):
            temp = sorted(j, key=lambda x: x[0])
            match1.extend(temp)
            # print(temp, '\n')
            # print(j)
    
    # print(match1)
    match = np.array_split(match1, n)

    for i in range(0,n):
        # print(type(match[i]))
        match[i] = match[i].flatten()
        match[i] = np.insert(match[i], 0, maps[i])
        match[i] = np.insert(match[i], 1, team_name[0])
        match[i] = np.insert(match[i], 2, team_name[1])
        match[i] = np.insert(match[i], 3, scores[i][0])
        match[i] = np.insert(match[i], 4, scores[i][1])
        # print(match[i], "\n")


    df = pd.DataFrame(match)

    # print(n)
    # print(maps)
    # print(team_name)
    # print(scores)
    # print(player_names_arr)
    # print(len(player_names_arr))
    # print(player_agent_arr)
    # print(len(player_agent_arr))
    # print(player_stats_arr)
    # print(len(player_stats_arr))
    # print(player_stats_arr2)
    # print(len(player_stats_arr2))
    # print(match)
    # print(df)

    if(len(df.columns) == 265):
        print(df)

        # df.to_csv('Datasets/match1.csv', mode='a', index=False, header=False)
    
"""

def ov(u):

    page = requests.get(u + '/?game=all&tab=overview')
    soup = BeautifulSoup(page.text, 'html.parser')

    page1 = requests.get(u + "/?game=all&tab=performance")
    soup1 = BeautifulSoup(page1.text, 'html.parser')

    x = []
    # Global Variables
    game_ID = []

    for i in  soup.find_all(class_="match-header-vs-note"):
        x.append(str(i.get_text()).strip())

    for i in soup.find_all(class_ = 'vm-stats-gamesnav-item js-map-switch'):
        game_ID.append(str(i.get('data-game-id')))

    # print(x[1])

    # Map
    maps = []
    # Team Names:
    team_name = []
    # Scores
    scores = []
    # No of played Maps
    n = ""

    # player Name
    player_names_arr = []

    # Player Agent
    player_agent_arr = []

    # Player Stats
    player_stats_arr=[]

    # Matches
    match = []

    # Naming
    naming = []

    names = []
    arr = []
    perf = []
    # -----------------------------------------------------------------
    for map in soup.find_all(class_="map"):
        for i in map.find_all("span", {"style":"position: relative;"}):
            my_str = str(i.contents[0])
            maps.append(my_str.strip())


    n = len(maps)


    for name in soup.find_all(class_="team-name"):
        my_string = str(name.contents)
        val = custom_replace(my_string)
        team_name.append(val)
        # print(val)

    team_name = team_name[0:2]

    for score in soup.find_all(class_="score"):
        scores.append(int(score.get_text()))
        # print(score.get_text())

    scores = np.array_split(scores, n)


    for name in soup.find_all("div", {"style": "font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;"}):
        my_str = str(name.contents)
        val = custom_replace(my_str)
        # print(val)
        player_names_arr.append(val)

    player_names_arr = player_names_arr[0:10] + player_names_arr[(n-1)*(-10):]


    for agent in soup.find_all(class_ = "stats-sq mod-agent small"):
        player_agent_arr.append(agent.find("img").get("title"))

    player_agent_arr = player_agent_arr[0:10] + player_agent_arr[(n-1)*(-10):]


    for i in soup.find_all('td',{'class':'mod-stat'}):
        my_str = str(i.find("span", {'class': 'side'}).contents)
        my_str = custom_replace(my_str)
        my_str = custom_replace2(my_str)
        # print(my_str)
        player_stats_arr.append(float(my_str))

    player_stats_arr = player_stats_arr[0:120] + player_stats_arr[(n-1)*(-120):]

    newArr = np.array_split(player_stats_arr, n*10)
    player_stats_arr1 = []
    test_arr = []
    for i in newArr:
        test_arr = i
        player_stats_arr1.append(test_arr)

    # print(player_stats_arr1)
    player_stats_arr2 = player_stats_arr1[0:10]+player_stats_arr1[(n-1)*(-10):]

    for i in range(0,n*10):
        test_arr = []
        test_arr.append(player_names_arr[i])
        test_arr.append(player_agent_arr[i])
        test_arr.extend(player_stats_arr2[i])
        # print(test_arr)
        match.append(test_arr)

    match = np.array(match)
    # print(match)
    match = np.array_split(match, n)

    match1 = []
    for i in match:
        for j in (np.array_split(i, 2)):
            temp = sorted(j, key=lambda x: x[0])
            match1.extend(temp)
            # print(temp, '\n')
            # print(j)
    
    # print(match1)

    # print(n)
    # print(maps)
    # print(team_name)
    # print(scores)
    # print(player_names_arr)
    # print(len(player_names_arr))
    # print(player_agent_arr)
    # print(len(player_agent_arr))
    # print(player_stats_arr)
    # print(len(player_stats_arr))
    # print(player_stats_arr2)
    # print(len(player_stats_arr2))
    # print(match)



    for games in soup1.find_all('div', {'data-game-id': game_ID[0]}):
        # for i in games.find_all('th'):
        #     print(i)
        for i in games.find_all('div', {'class': 'team'}):
            s = str(i.find('div').get_text())
            s = s.strip()
            s = custom_replace3(s)
            names.append(s)
            # print(s)
            # print(str(i.find('div').get_text()).strip())
    
    for i in range(len(names)):
        l = names[i].find('\n')
        names[i] = names[i][0:l]

    names = names[-10:]
    # print(names)

        
    for i in soup1.find_all('tr'):
        for j in i.find_all('td'):
            for stats in j.find_all(class_='stats-sq'):
                arr.append(str(stats.get_text()).replace('\t','').replace('\n',''))

    # print(arr)

    for i in range(len(arr)):
        if(len(arr[i]) > 3):
            arr[i] = arr[i][0]

    for i in range(len(arr)):
        if(arr[i] == ''):
            arr[i] = 0

    # print(arr) 
    # print(arr[0:225])
    # print()
    # print(arr[225: 355])

    new_arr = arr[355:]

    i = 0
    cnt = 0
    while(cnt < n):
        temp = np.array_split(new_arr[i+225: i + 355], 10)
        for val in range(len(temp)):
            temp[val][0] = names[val%10]
            # print(temp[val])
        perf.extend(temp)

        i += 355
        cnt += 1

    # print(arr[365])
    # for i in perf:
    #     print(i)

    # print(perf)
    # print(len(perf))

    # for i in range(n):
    perf1 = np.array_split(perf, n)
    # print(perf1, '\n')
    perf2 = []
    for i in range(n):
        # perf1[i] = sorted(perf1[i], key=lambda x: x[0])
        temp = []
        for j in np.array_split(perf1[i], 2):
            # a = sorted(j, key=lambda x: x[0])
            temp.append(sorted(j, key=lambda x: x[0]))
        # print()
        perf2.extend(temp)

    perf3 = []
    for i in perf2:
        for j in i:
            perf3.append(j)
    
    # print(perf3)
    # perf1 = sorted(perf, key=lambda x: x[0])
    # print(perf1)
    # print(perf2)
    match2 = []

    # for i in range(len(perf2)):
    #     a = match1[i]
    #     b = perf2[i][1:]
        # print(a)
        # print(b)
        # match2.append(np.concatenate([a, b]))

    for i in range(len(perf3)):
        match2.append(np.concatenate( [match1[i] , perf3[i][1:]]))

    match = np.array_split(match2, n)

    for i in range(0,n):
        # print(type(match[i]))
        match[i] = match[i].flatten()
        match[i] = np.insert(match[i], 0, maps[i])
        match[i] = np.insert(match[i], 1, team_name[0])
        match[i] = np.insert(match[i], 2, team_name[1])
        match[i] = np.insert(match[i], 3, scores[i][0])
        match[i] = np.insert(match[i], 4, scores[i][1])
        # print(match[i], "\n")


    df = pd.DataFrame(match)
    # print(df)

    if(len(df.columns) == 265):
        print(df)
        df.to_csv('Datasets/match1.csv', mode='a', index=False, header=False)
        


for u in url_arr:
    try:
        # read_game_ID(u)
        # print(u)
        ov(u)
        
    except:
        continue
