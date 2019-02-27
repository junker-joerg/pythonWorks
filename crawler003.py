# -*- coding: utf-8 -*-
# ! git push https://github.com/junker-joerg/pythonworks [jeden Abend]
# ! Das Beste aus den Vorversionen NLP_CIO_Tool2.py,  NLP_CIO_Tool.py...
# ! ... corpusclean.py und CorpUniC01.py übernehmen
# ToDO: über alle Dateien - aus jeder Datei wird mit PDFminer der Text gezogen und ín eine neue Datei kopiert   
# ToDO: in einem zweiten Schritt werden die .txt-Dateien durch die Cleaner-Funktionen geschickt und dann wird
# ToDO: die REIN-Datei für den Corpus geschrieben - es wird im LogFile vermerkt, wieviel Sätze / Worte geschrieben
# ToDO: wurden
import feedparser
import pandas

# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])   
    return headlines


# A list to hold all headlines
allheadlines = []
 
# List of RSS feeds that we will fetch and combine
newsurls = {
    'CIO_1':            'https://www.cio.de/feed/at/1',
    'CIO_2':            'https://www.cio.de/feed/p/3932',
    'vs_foren_it':      'https://www.versicherungsforen.net/portal/de/system/rss/news.rss',
    'techChrunch_1':    'http://feeds.feedburner.com/Techcrunch/europe',
    'MIT_Technology':   'https://www.technologyreview.com/topnews.rss'     
                        
}
 
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
 
 
# Iterate over the allheadlines list and print each headline
for hl in allheadlines:
    print(hl)
