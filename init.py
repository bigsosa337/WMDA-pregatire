from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Setup Firefox options
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Run headless Firefox
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Path to your WebDriver
webdriver_path = 'path/to/your/geckodriver'

# Setup WebDriver
service = Service(webdriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# List of movie URLs to scrape
movie_urls = [
    'https://www.metacritic.com/movie/young-woman-and-the-sea/',
    'https://www.metacritic.com/movie/backspot/',
    # Add more movie URLs here
]

# Function to scrape movie details
def scrape_movie_details(url):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Extract movie details
    try:
        title = driver.find_element(By.CSS_SELECTOR, 'h1').text
        director = driver.find_element(By.XPATH, "//b[contains(text(), 'Directed By')]/following-sibling::a").text
        critics_score = driver.find_element(By.CSS_SELECTOR, 'div.c-productScoreInfo_scoreNumber.u-float-right span').text
        users_score = driver.find_element(By.CSS_SELECTOR, 'div.c-siteReviewScore_background-user span').text
        # duration = driver.find_element(By.XPATH, "//li[contains(text(), 'h')]").text
        duration = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[6]/div/div[1]/div[1]/div[2]/div/div[3]/span[2]").text
        rating = driver.find_element(By.CSS_SELECTOR, 'div.c-movieDetails_sectionContainer:nth-child(4) > span:nth-child(2)').text


        return {
            'Title': title,
            'Director': director,
            'Critics Score': critics_score,
            'Users Score': users_score,
            'Duration': duration,
            'Rating': rating
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Scrape details for each movie
movie_details_list = []
for url in movie_urls:
    details = scrape_movie_details(url)
    if details:
        movie_details_list.append(details)

# Print the results
for details in movie_details_list:
    print(details)

# Close the WebDriver
driver.quit()
