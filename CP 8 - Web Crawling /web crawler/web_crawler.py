import logging
import sys
import requests
import re
import csv

def get_category_list(content):
    """get_category_list takes content of home page
    and returns a list of categories and their urls"""
    return category_pat.findall(content)

def get_book_list(content):
    """get_book_list takes content of a book list page
    and returns a list of book (name and url)
    """
    pass

def get_product_details(content):
    """get_product_details takes content of a book list page
    and returns a list of categories and their urls
    """
    pass

def get_page_content(url):
    """get_page_content takes a url and returns the content os the pass"""
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e) 

    if response.ok:
        return response.text     

    logging.error("Can not get content from url:" + url)

    return None

def get_next_page(content):
    """Checks the content of a book list page and returns link
     of the next page, returns None, if there is no more next page"""
    pass

def scrape_book_info(book_info, category_name):
    """ gets the content of a book details page,
    and parses different components and stores the info"""
    pass


def crawl_category(category_name, category_url):
    """crawls a particular category of books"""
    while True:
        content = get_page_content(category_url)
        book_list = get_book_list(content)

        for book in book_list:
            scrape_book_info(book, category_name)

        if get_next_page(content) is None:
            break

def crawl_website():
    """crawl_website() is the main function 
    that coordinates the whole crawling task"""

    url = "http://books.toscrape.com/index.html"
    host_name = "books.toscrape.com"

    content = get_page_content(url)
    if content is None:
        logging.critical("Failed to get content from " + url)
        sys.exit(1)

    category_list = get_category_list(content)

    for category in category_list:
        category_url, category_name = category
        print(category_url)
        sys.exit(1)
        crawl_category(category_name, category_url)



if __name__ == "__main__":
    # Compile different reguler expresion patterns
    category_pat = re.compile(r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M |re.DOTALL)

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S: %p', filename='bookstore_crawler.log', level=logging.DEBUG)

    with open("book_list.csv", "w") as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability", "Description"])
        csv_writer.writeheader()
        
        crawl_website()
