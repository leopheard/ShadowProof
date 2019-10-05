from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://unauthorizeddisclosure.libsyn.com/rss"
url2 = "http://beyondprison.libsyn.com/rss"
url3 = "http://aroundtheempire.libsyn.com/rss"
url4 = "http://deleteyouraccount.libsyn.com/showrss"
url5 = "http://shadowproof.libsyn.com/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts4/v4/a7/bf/01/a7bf01e4-5460-e701-c2be-25caca2fe925/mza_1508240927169116112.png/600x600bb.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/1f/ce/0f/1fce0fc2-69aa-113c-6ad1-3db65a633acd/mza_8390794261141807829.png/600x600bb.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts82/v4/b3/24/5c/b3245cbe-3b95-eae5-b15b-0a1ef125da0a/mza_3044980588654316779.png/600x600bb.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/c/b/4/bcb40c2322a7a520/Pr984-Dl.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/db/51/79/db5179d6-1cfc-1df2-837d-99bb1ac9eaa0/mza_4841854697771669414.png/600x600bb.jpg"},

    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

if __name__ == '__main__':
    plugin.run()
