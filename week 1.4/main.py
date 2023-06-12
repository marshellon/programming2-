from crawler import WebCrawler

# Create an instance of the WebCrawler class
crawler = WebCrawler()

# Call the crawl_site() method to start crawling
crawler.crawl_site()

# Use the crawler as an iterator to get the next crawled website
for website in range(5):
    print(str(next(crawler)))