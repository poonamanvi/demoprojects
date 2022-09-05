#!/usr/bin/env python
# coding: utf-8

# # 1) Write a python program to display all the header tags from wikipedia.org.¶

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[4]:


soup = BeautifulSoup(page.content)


# In[5]:


soup


# In[6]:


html = requests.get("https://en.wikipedia.org/wiki/Main_Page")
titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[ ]:





# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)and make data frame.

# In[7]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[8]:



from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[9]:


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# In[10]:



movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]


# In[11]:


list = []


# In[12]:


for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            }
    list.append(data)


# In[13]:


for movie in list:
    
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'],')','-', movie['rating'])
    


# In[14]:


df = pd.DataFrame(list)
df.to_csv('imdb_top__movies.csv',index=False)


# In[15]:


df.head(100)


# # 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[16]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[17]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[18]:


url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# In[19]:


movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]


# In[20]:


list =[]


# In[21]:


for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            }
    list.append(data)


# In[22]:


df.head(100)


# In[23]:


for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'],')','-', movie['rating'])
    


# In[24]:


df = pd.DataFrame(list)
df.to_csv('imdb_top__movies.csv',index=False)


# In[25]:


df.head(100)


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[4]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[5]:


soup = BeautifulSoup(page.content)


# In[6]:


soup


# In[7]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[8]:


scraped_formerPresidents = soup.find_all('div',class_='presidentListing')
scraped_formerPresidents


# In[9]:


formerPresidents = []
for formerPresident in scraped_formerPresidents:
    print(formerPresident.get_text())


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.
# 

# # a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[5]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[8]:


#Scraping ODI teams
scraped_odi_teams = soup.find_all('span',class_='u-hide-phablet')
scraped_odi_teams

#creating empty list to store Data
odi_teams = []


#parsing ODI teams
for odi_team in scraped_odi_teams[:10]:
    odi_team = odi_team.get_text().replace('\n',"")
    odi_team = odi_team.strip("")
    odi_teams.append(odi_team)
odi_teams    


# In[9]:


df = pd.DataFrame({'Teams':odi_teams})
df


# In[10]:


top_bteam_matches = []
top_bteam_points = []
top_bteam_rating = []
name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_matches.append(name.text)

name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_points.append(name.text.strip())

name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_rating.append(name.text.strip())


# In[11]:


df1 = pd.DataFrame({'Matches':top_bteam_matches,'Points':top_bteam_points,'Rating':top_bteam_rating})
df1


# In[12]:


matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[:18]:
    matches.append(i.text)
matches


match1 = []
for i in range(0,len(matches),2)[:18]:
    match1.append(matches[i])
match1        


# In[13]:


points = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[:20]:
    points.append(i.text)
points


points1 = []
for i in range(1,len(matches),2)[:20]:
    points1.append(matches[i])
points1        


# In[14]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[:9]:
    ratings.append(i.text)
ratings


# In[15]:


print(len(match1),len(points1),len(ratings))


# In[16]:


df2 = pd.DataFrame({'Matches':match1,'Points':points1,'Rating':ratings})
df2


# In[17]:


df3 = pd.concat([df1[:1],df2[:10]])
df3


# # b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[18]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[19]:


soup = BeautifulSoup(page.content)
soup


# In[20]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[21]:


rank=soup.find_all("span",attrs={"class":["rankings-block__pos-number","rankings-table__pos-number"]})
rank

ranks=[]
for ranking in rank:
    ranking=ranking.get_text().replace('\n',"")
    ranking=ranking.strip()
    ranks.append(ranking)
ranks=ranks[0:10]
ranks


# In[22]:


player_name=soup.find_all('td',class_='table-body__cell name')
player_name.insert(0,(soup.find('div',class_='rankings-block__banner--name')))
player_name


# In[23]:


name=[]
for player in player_name:
    player=player.get_text().replace('\n',"")
    player=player.strip()
    name.append(player)
name=name[0:10]
name


# In[24]:


team=soup.find_all(attrs={"class":["table-body__logo-text"]})
team=team[2:3]
team


# In[25]:


top=[]
for m in team:
    m=m.get_text().replace('\n',"")
    top.append(m)
top    


# In[26]:


team1=soup.find_all(attrs={"class":["table-body__logo-text"]})
team1=team1[0:9]
team1


# In[27]:


teams=[]
for tm in team1:
    tm=tm.get_text().replace('\n',"")
    teams.append(tm)
teams    


# In[28]:


team_name=top+teams
team_name


# In[29]:


ratings=soup.find_all(attrs={"class":["rankings-block__banner--rating","table-body__cell u-text right"]})
ratings


# In[30]:


rating=[]
for rate in ratings:
    rate=rate.get_text().replace('\n',"")
    rate=rate.strip()
    rating.append(rate)
rating=rating[0:10]
rating


# In[31]:


df = pd.DataFrame(list(zip(ranks,name,team_name,rating)),columns=['Ranks','Name','Team','Rating'])
df


# # c) Top 10 ODI bowlers along with the records of their team and rating.

# In[32]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[33]:


soup = BeautifulSoup(page.content)
soup


# In[34]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[35]:


bowl=soup.select("tr.table-body a")
bowl=bowl[9:18]
bowl


# In[36]:


top=soup.find_all(class_="rankings-block__banner--name")[1]
top


# In[37]:


bowl.insert(0,top)
bowl


# In[38]:


name=[]
for nm in bowl:
    nm=nm.get_text().replace('\n',"")
    nm=nm.strip()
    name.append(nm)
name    


# In[39]:


team=soup.select("span.table-body__logo-text")
team=team[9:18]
team


# In[40]:


teams=[]
for tm in team:
    tm=tm.get_text().replace('\n',"")
    teams.append(tm)
teams    


# In[41]:


top2=soup.select("span.table-body__logo-text")[16:17]
top2


# In[42]:


team1=[]
for tm in top2:
    tm=tm.get_text().replace('\n',"")
    team1.append(tm)
team1    


# In[43]:


team_name=team1+teams
team_name


# In[44]:


rate=soup.find_all("td",class_="table-body__cell u-text-right rating")[9:18]
rate


# In[45]:


top3=soup.select("div.rankings-block__banner--rating")[1]
top3


# In[46]:


rate.insert(0,top3)
rate


# In[47]:


ratings=[]
for rt in rate:
    rt=rt.get_text().replace('\n',"")
    rt=rt.strip()
    ratings.append(rt)
ratings    


# In[49]:


df=pd.DataFrame({"Players":name,"Team":team_name,"Rating:ratings"})
df


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating

# # a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[96]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[97]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[99]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[100]:


soup = BeautifulSoup(page.content)
soup


# In[101]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[102]:


#Scraping ODI teams
scraped_odi_teams = soup.find_all('span',class_='u-hide-phablet')
scraped_odi_teams

#creating empty list to store Data
odi_teams = []


#parsing ODI teams
for odi_team in scraped_odi_teams[:10]:
    odi_team = odi_team.get_text().replace('\n',"")
    odi_team = odi_team.strip("")
    odi_teams.append(odi_team)
odi_teams    


# In[103]:


df = pd.DataFrame({'Teams':odi_teams})
df


# In[104]:


top_bteam_matches = []
top_bteam_points = []
top_bteam_rating = []
name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_matches.append(name.text)

name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_points.append(name.text.strip())

name=soup.find('td',class_="rankings-block__banner--matches")
top_bteam_rating.append(name.text.strip())


# In[105]:


df1 = pd.DataFrame({'Matches':top_bteam_matches,'Points':top_bteam_points,'Rating':top_bteam_rating})
df1


# In[106]:


matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[:18]:
    matches.append(i.text)
matches


match1 = []
for i in range(0,len(matches),2)[:18]:
    match1.append(matches[i])
match1        


# In[107]:


points = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[:20]:
    points.append(i.text)
points


points1 = []
for i in range(1,len(matches),2)[:20]:
    points1.append(matches[i])
points1        


# In[108]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[:9]:
    ratings.append(i.text)
ratings


# In[109]:


print(len(match1),len(points1),len(ratings))


# In[110]:


df2 = pd.DataFrame({'Matches':match1,'Points':points1,'Rating':ratings})
df2


# In[111]:


df3 = pd.concat([df1[:1],df2[:10]])
df3


# # b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[112]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[113]:


soup = BeautifulSoup(page.content)
soup


# In[114]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[116]:


rank=soup.find_all("span",attrs={"class":["rankings-block__pos-number","rankings-table__pos-number"]})
rank

ranks=[]
for ranking in rank:
    ranking=ranking.get_text().replace('\n',"")
    ranking=ranking.strip()
    ranks.append(ranking)
ranks=ranks[0:10]
ranks


# In[ ]:





# # 7.Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :i) Headline ii) Time iii) News Link

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[3]:


page = requests.get('https://www.cnbc.com/world/?region=world')
page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[6]:


for link in soup.findAll("a"):
    print("Headlines : {}".format(link.text))


# In[7]:


for link in soup.findAll('time',{'class' : 'LatestNews-timestamp'}):
    print("Times : {}".format(link.text))


# In[8]:


cnbc_url="https://www.cnbc.com/world"


# In[9]:


page = requests.get('https://www.cnbc.com/world')
page


# In[10]:


soup = BeautifulSoup(page.content)
soup


# In[11]:


links_list = soup.find_all('a')


# In[12]:


for link in links_list:
    if 'href'in link.attrs:
        print(str(link.attrs['href']))


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details : i) Paper Title ii) Authors iii) Published Date iv) Paper URL

# In[13]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[14]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[15]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[16]:


soup = BeautifulSoup(page.content)
soup


# In[17]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[18]:


for link in soup.findAll("h2"):
    print("PaperTitle : {}".format(link.text))


# In[19]:


author = []

for i in soup.find_all('span',{'class' : "sc-1w3fpd7-0 pgLAT"}):
    author.append(i.text)


# In[20]:


author


# In[21]:


date = []

for i in soup.find_all('span',{'class' : 'sc-1thf9ly-2 bKddwo'}):
    date.append(i.text)


# In[22]:


date


# In[23]:


url = "https://www.journals.elsevier.com"


# In[24]:


page = requests.get('https://www.journals.elsevier.com') 
page


# In[25]:


soup = BeautifulSoup(page.content)
soup


# In[26]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[27]:


links_list = soup.find_all('a')


# In[28]:


for link in links_list:
    if 'href'in link.attrs:
        print(str(link.attrs['href']))


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name ii) Cuisine iii) Location iv) Ratings v) Image URL

# In[63]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[64]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[65]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[66]:


soup = BeautifulSoup(page.content)
soup


# In[67]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[68]:


# RESTAURANT NAME
scraped_restaurant_name = soup.find_all('a',class_="restnt-name ellipsis")
scraped_restaurant_name


# In[69]:


#EMPTY LIST
restaurant_name = []


# In[70]:


#Restaurant name
for rn in scraped_restaurant_name:
    rn = rn.get_text().replace('\n','')
    restaurant_name.append(rn)
restaurant_name


# In[71]:


# Cuisine 
scraped_cuisines = soup.find_all('div',class_="filter-component-wrap cuisine-wrap")
scraped_cuisines


# In[72]:


#EMPTY LIST
cuisines = []


# In[73]:


for c in scraped_cuisines:
    c = c.get_text().replace('\n',' ')
cuisines.append(c)
cuisines


# In[74]:


scraped_location = soup.find_all('div',class_="restnt-loc ellipsis")
scraped_location


# In[75]:


location = []


# In[76]:


#Location
for l in scraped_location :
    l = l.get_text().replace('\n',' ')
location.append(l)
location


# In[77]:


scraped_ratings = soup.find_all('div',class_="restnt-rating rating-4")
scraped_ratings


# In[78]:


ratings = []


# In[79]:


for r in scraped_ratings :
    r = r.get_text().replace('\n',' ')
ratings.append(r)
ratings


# In[80]:


scraped_image_url = soup.find_all('img',class_= "no-img")
scraped_image_url


# In[81]:


image_url = []


# In[82]:


for i in scraped_image_url :
    i = i.get_text().replace('\n',' ')
image_url.append(i)
image_url


# In[ ]:





# # 10) Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en i) Rank ii) Publication iii) h5-index iv) h5-median

# In[83]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[84]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[85]:


page = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[86]:


soup = BeautifulSoup(page.content)
soup


# In[87]:


rank = []
publication = []


# In[88]:


for i in soup.find_all('td',class_="gsc_mvt_p"):
    rank.append(i.text)


# In[89]:


rank


# In[90]:


for i in soup.find_all('td',class_="gsc_mvt_t"):
    publication.append(i.text)


# In[91]:


publication


# In[92]:


citation = []


# In[93]:


for i in soup.find_all('td',class_="gsc_mvt_n"):
    citation.append(i.text)


# In[94]:


citation


# In[95]:


data = list(zip(rank,publication,citation))
df = pd.DataFrame(data,columns = ['Rank','Publication','Citation'])
df 


# In[ ]:





# In[ ]:




