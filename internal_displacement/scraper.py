import newspaper
import csv
from internal-displacement import Article
class Scraper(object):
    '''Scraper that accepts a url (or urls) and returns an instance of Article
    Parameters
    ----------
    urls: a url to be scraped

    Returns
    -------
    article: instance of Article containing body text and 
    '''

        # Helper Functions #

    def remove_newline(self,text):
        ''' Removes new line and &nbsp characters.
        '''
        text = text.replace('\n', ' ')
        text = text.replace('\xa0', ' ')
        return text


    # Class Functions #

    def html_article(self, url):
        '''Downloads and extracts content plus metadata for html page
        Parameters
        ----------
        url: url of page to be scraped 

        Returns
        -------
        report: dictionary containing page content and metadata
        '''

        a = newspaper.Article(url)
        a.download()
        a.parse()
        article_domain = a.source_url
        article_title = a.title
        article_authors = a.authors
        article_pub_date = a.publish_date
        article_text = self.remove_newlines(a.text)
        # tag the type of article
        ## currently default to text but should be able to determine img/video etc
        article_type = 'text'
        article = Article
        return article

    def scrape(self, urls):
        '''Scrapes content and metadata from all pages in a list
        ** Currently skips pdfs and only calls html_report
        Parameters
        ----------
        urls: list of urls of pages to be scraped 

        Returns
        -------
        reports: list of dictionaries containing all reports
        '''
        articles = []
        for url in urls:
            if url[-3:] == 'pdf':
                continue
            else:
                article = html_article(url)
                articles.append(article)
                
        return articles



    def __init__(self, urls):
        if isinstance(urls, list):
            self.urls = urls
        if isinstance(urls, pd.Series):
            self.urls = list(urls)
        if isinstance(urls, str):
            self.urls = [urls]

