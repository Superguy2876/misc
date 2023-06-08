from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

# Set the chromedriver path as per your system configuration
driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

# URL of the webpage you want to access
url = input('Enter the URL: ')

# get the top level domain name, from https to the first /
domain = re.search(r'https://.*?/', url).group()

# Open the file to write to
with open('forums/output.txt', 'w', encoding='utf-8') as f:
    while True:
        driver.get(url)
        time.sleep(2)
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all divs with class 'bbWrapper'
        divs = soup.find_all('div', {'class': 'bbWrapper'})

        # Loop over each div
        for div in divs:
            # Get the text of the div
            text = div.get_text(separator='\n')

            # Replace excess newlines following sentence endings with a single <#>
            text = re.sub(r'([.!?]"?)\n+', r'\1<#>', text)

            # Replace all other newlines with a space
            text = re.sub(r'\n', ' ', text)

            # Replace <#> with a newline
            text = re.sub(r'<#>', '\n', text)

            # Remove lines starting with [] or -[]
            text = re.sub(r'^\[.*\].*|^-\[.*\].*', '', text, flags=re.MULTILINE)

            # Remove everything after ===== including it
            text = re.sub(r'=====.*', '', text, flags=re.DOTALL)

            # Ensure opening and closing quotes are on the same line by removing any newlines between them
            text = re.sub(r'"(.*?)"', lambda m: m.group().replace('\n', ' '), text, flags=re.DOTALL)

            # Write the cleaned text to the file, with "===" between each block of text
            f.write(text)
            f.write('\n===\n')

        # Try to click the next button, if it exists
        try:
            aref = soup.find_all('a', {'class': 'pageNav-jump--next'})[0]
            url_end = aref.get('href')
            url = domain + url_end
            # url = next_button.get_attribute('href')
        except Exception as e:
            # If the next button doesn't exist, break the loop
            print(e)
            break

# Close the driver after use
driver.quit()