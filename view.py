import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, source_url):
    result = search.kimetsu_search(word, source_url)
    return result

    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)