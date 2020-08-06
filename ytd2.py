import webbrowser
import pytube
from subprocess import call

key = input('Input what you want to download: ')
a_website = "https://www.youtube.com/results?search_query="+key
webbrowser.open_new(a_website)

open('url.txt', 'w')
call(['notepad', 'url.txt'])

start = input('Press enter when ready to download >>> ')
with open('url.txt','r') as f:
    urls = f.readlines()
number = len(urls)
num = 0
for url in urls:
    num += 1
    print('Downloading video',num,'of',number)
    yt = pytube.YouTube(url)
    stream = yt.streams.first()
    stream.download()

open('url.txt', 'w')