VIDEO_PREFIX = "/video/lifetime"
EPISODES_URL = "http://www.mylifetime.com/watch-full-episodes-online"
MOVIES_URL = "http://www.mylifetime.com/watch-full-movies-online"
BASE_URL = "http://www.mylifetime.com"

NAME = L('Title')
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    HTTP.CacheTime = CACHE_1HOUR

def MainMenu():
    dir= MediaContainer(viewGroup = 'List')
    dir.Append(Function(DirectoryItem(ShowFinder, title='Full Episodes'),url = EPISODES_URL, title='Full Episodes'))
    dir.Append(Function(DirectoryItem(ShowFinder, title='Full Movies'),url = MOVIES_URL, title='Full Movies'))
    return dir

def ShowFinder(sender,url,title):
    dir = MediaContainer(viewGroup = 'List', title2 = title)
    page = HTML.ElementFromURL(url, cacheTime=1200)
    
    for s in page.xpath('//h2'):
        title = s.xpath("../div[@class='photo-title']/a").text
        url = s.xpath("../div[@class='photo-title']/a")[0].get('href')
        thumb = s.xpath("../div[@class='photo']/a/img")[0].get('src')
        dir.Append(Function(DirectoryItem(GetShows, title=title, thumb=Function(GetThumb, path=thumb)),path=BASE_URL +url,title = title))
    return dir

def GetThumb(path):
    return DataObject(HTTP.Request(path),'image/jpeg')
    
  
