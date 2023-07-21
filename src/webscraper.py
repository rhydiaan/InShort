import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    '''
    Scrape a url for the paragraphs.

    Parameters:
    url (str): The target url.
    '''
    try:
        # Fetch the HTML content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main article content based on the HTML structure of the website
        article_content = ""
        article_paragraphs = soup.find_all('p')  # Adjust this based on the specific website's structure
        for paragraph in article_paragraphs:
            paragraph_text = paragraph.get_text()
            article_content += str(paragraph_text) + " "

        # Return the extracted information as a dictionary
        return {
            'content': article_content
        }
    except Exception as e:
        return {'error': str(e)}

# Example usage
def webscraper():
    input_url = input("Enter the URL of the news article: ")
    scraped_data = scrape_article(input_url)

    if 'error' in scraped_data:
        print("Error:", scraped_data['error'])
    else:
        return scraped_data['content']
