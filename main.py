# main.py
from scraper import Scraper

def main():
    url = "http://learn-co-curriculum.github.io/site-for-scraping/courses"
    scraper = Scraper()
    scraper.scrape_courses(url)
    scraper.print_courses()

if __name__ == "__main__":
    main()
