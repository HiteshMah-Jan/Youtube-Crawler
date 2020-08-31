
from selenium import webdriver

'''This is a simple (youtube.com) crawler which gives out Top 10 tracks
   and Top albums of your favorite Artist.
   It also suggests you similar Artists to try out'''

PATH = 'C:\Program Files (x86)\chromedriver.exe'
searchArtist = input('Tell me your favorite Song Artist :')

driver = webdriver.Chrome(PATH)
driver.maximize_window()

url = 'https://www.youtube.com/results?search_query='+ searchArtist
driver.get(url)

####################################################

topTracks = driver.find_elements_by_xpath("//a/div/div/yt-formatted-string/a[@class='yt-simple-endpoint style-scope yt-formatted-string']")
print("Top Tracks by " + driver.title + " :")
top_tracks = []
for tt in topTracks:
    top_tracks.append(tt.text)

####################################################

trackDetails = driver.find_elements_by_xpath("//yt-formatted-string[@class='subtitle style-scope ytd-watch-card-compact-video-renderer']")
track_details = []

for td in trackDetails:
    track_details.append(td.text)

tracks = dict(zip(top_tracks, track_details))
for tt, td in tracks.items():
    print("{:<35} {:<25}".format(tt,td))

####################################################

albums = driver.find_elements_by_xpath("//div[@id='items']/ytd-search-refinement-card-renderer/a/div[@id='card-title']/div[@class='style-scope ytd-search-refinement-card-renderer']")
print('\nThese are the top albums by ' + searchArtist + ' :')
for a in albums[-4:]:
    print(a.text)

print('\nHere are some similar artists you may like:')
for a in albums[:7]:
    print(a.text)


########################################################

driver.quit()
