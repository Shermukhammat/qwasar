import requests
from bs4 import BeautifulSoup as BS 

# sahifa = requests.get('https://github.com/trending') 
# shurva = BS(sahifa.text, "html.parser")
# top = shurva.find_all("article")
# chiqar = top[0].select_one("a.Link--muted.d-inline-block.mr-3").text
# ruyxat = chiqar.split()
# print(ruyxat)
# print(" ".join(ruyxat))



def request_github_trending(url):
    return requests.get(url)

def extract(page):
    shurva = BS(page.text, 'html.parser')
    repolar = shurva.find_all('article')
    return repolar

def transform(html_repos):
    javob = list()
    for repo in html_repos:
        #Repozitoriylar nomini aniqlab olamiz;
        repozitory_nomi = repo.select_one("h1.h3.lh-condensed").text
        repozitory_nomi = repozitory_nomi.split()
        repozitory_nomi = "".join(repozitory_nomi)
        
        #Yulduzlar sonnini aniqlaymiz!
        yul_son = repo.select_one("span.d-inline-block.float-sm-right").text
        yul_son = yul_son.split()
        yul_son = " ".join(yul_son)
        
        #Dasturchi ismni aniqlaymiz
        d_ism = repo.select_one("img.avatar.mb-1.avatar-user")['alt']
        #Javob ruyxatiga repozitory nomi, dasturchi nomi va yulduzlar sonnini lug'at ko'rnshda qushamiz;
        qush = {
            'developer' : d_ism,
            'repository_name' : repozitory_nomi,
            'nbr_stars' : yul_son
            }
        javob.append(qush)
    return javob

def format(repositories_data):
    
    javob = 'Developer,Repository Name,Number of Stars\\n'
    for repodata in repositories_data:
        dasturchi = repodata['developer']
        repo = repodata['repository_name']
        yul_son =  repodata['nbr_stars']
        qush = dasturchi+','+repo+yul_son+'\\n'
        javob+=qush
    return javob
    
    



#TEST

# link = request_github_trending("https://github.com/trending")
# repolar = extract(link)
# repodata = transform(repolar)
# format(repodata)