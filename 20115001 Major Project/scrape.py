import requests
# from bs4 import BeautifulSoup

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

# url = "https://www.vlr.gg/248277/paper-rex-vs-evil-geniuses-valorant-champions-2023-playoffs-gf"

# url = "https://www.vlr.gg/248282/fnatic-vs-loud-valorant-champions-2023-playoffs-lr3"

# url = "https://www.vlr.gg/167391/loud-vs-drx-champions-tour-2023-lock-in-s-o-paulo-sf"

# url = "https://www.vlr.gg/team/matches/11001/m80/"

# url = "https://www.vlr.gg/team/matches/188/cloud9/"

# url = "https://www.vlr.gg/team/matches/5248/evil-geniuses/"

# url = "https://www.vlr.gg/team/matches/1034/nrg-esports/"

# url = "https://www.vlr.gg/team/matches/2593/fnatic/"

# url = "https://www.vlr.gg/team/matches/11479/apeks/"

# url = "https://www.vlr.gg/team/matches/13188/moist-x-shopify/"

# url = "https://www.vlr.gg/team/matches/624/paper-rex/"

# url = "https://www.vlr.gg/team/matches/6387/bleed/"

# url = "https://www.vlr.gg/team/matches/6961/loud/"

# url = "https://www.vlr.gg/team/matches/2406/furia/"

# url = "https://www.vlr.gg/team/matches/7386/mibr/"

# url = "https://www.vlr.gg/team/matches/8185/drx/"

# url = "https://www.vlr.gg/team/matches/8185/drx/?page=2"

# url = "https://www.vlr.gg/team/matches/11348/dplus-esports/"

# url = "https://www.vlr.gg/team/matches/17/gen-g/"

# url = "https://www.vlr.gg/team/matches/1120/edward-gaming/"

# url = "https://www.vlr.gg/team/matches/4210/made-in-thailand/"

# url = "https://www.vlr.gg/team/matches/8304/talon-esports/"

# url = "https://www.vlr.gg/team/matches/878/rex-regum-qeon/"

# url = "https://www.vlr.gg/team/matches/918/global-esports/"

# url = "https://www.vlr.gg/team/matches/2/sentinels/"

# url = "https://www.vlr.gg/team/matches/2359/leviat-n/"

# url = "https://www.vlr.gg/team/matches/4915/natus-vincere/"

# url = "https://www.vlr.gg/team/matches/474/team-liquid/"

# url = "https://www.vlr.gg/team/matches/1184/fut-esports/"

# url = "https://www.vlr.gg/team/matches/6882/fokus/"

# url = "https://www.vlr.gg/team/matches/1001/team-heretics/"

# url = "https://www.vlr.gg/team/matches/120/100-thieves/"

# url = "https://www.vlr.gg/team/matches/1837/attacking-soul-esports/"

# url = "https://www.vlr.gg/team/matches/282/scarz/"

# url = "https://www.vlr.gg/team/matches/5448/zeta-division/"

# url = "https://www.vlr.gg/team/matches/6199/team-secret/"

# url = "https://www.vlr.gg/team/matches/14/t1/"

# url = "https://www.vlr.gg/team/matches/8877/karmine-corp/"

# url = "https://www.vlr.gg/team/matches/2304/giants-gaming/"

# url = "https://www.vlr.gg/team/matches/7035/koi/"

url = "https://www.vlr.gg/team/matches/2059/team-vitality/"

fetchAndSaveToFile(url, "Datasets/team.html")