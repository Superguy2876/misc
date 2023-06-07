
# import required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json

# function to get the unique item data from poedb website
def get_unique_items_from_DB():

    # create a new Chrome session chrome driver is in chromedriver_win32 folder
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    # go to the website that we want to scrape
    driver.get('https://poedb.tw/us/Unique_item#WeaponUnique')

    # get the page source
    html = driver.page_source

    # pretty print the html
    soup = BeautifulSoup(html, 'html.parser')

    # find all tags with the class name 'item_unique'
    items = soup.find_all('a', class_='item_unique')

    # create a set to store the text data of each tag
    unique_items = set()
    # print the text in each tag then append it to the set
    for item in items:
        if item.text == 'Whakawairua Tuahu Strand Map':
            break
        print(item.text)
        unique_items.add(item.text)

    # close the driver
    driver.quit()
    return unique_items

# function to serialize and save the unique item data to a json file
def save_unique_items(complete_items, incomplete_items):
    # create a json file to store the unique items with overwrite permission
    with open('unique_items.json', 'w') as file:
        # dictionary to store the unique items
        unique_items = {
            'complete_items': list(complete_items),
            'incomplete_items': list(incomplete_items)
        }
        # serialize the dictionary and save it to the json file
        json.dump(unique_items, file)

    
        

# function to read the unique item data from a file
def read_unique_items():
    # create a set to store the unique items
    complete_items = set()
    incomplete_items = set()
    # open the json file if it exists otherwise return empty sets
    try:
        with open('unique_items.json', 'r') as file:
            # deserialize the json file
            unique_items = json.load(file)
            # add the unique items to the set
            complete_items.update(unique_items['complete_items'])
            incomplete_items.update(unique_items['incomplete_items'])
    except FileNotFoundError:
        pass
    return complete_items, incomplete_items

def print_data(complete_items, incomplete_items):
    print(f'There are {len(complete_items)} complete items')
    print(f'There are {len(incomplete_items)} incomplete items')
    

# function to display a menu
def menu(complete_items, incomplete_items):
    print('1. get one random unique item')
    print('2. list all complete unique items')
    print('3. list all incomplete unique items')
    print('4. display data on items')
    print('5. get all unique items from poedb')
    print('6. exit')

    # get the user's choice
    choice = input('Enter your choice: ')

    if choice == '1':
        complete_items, incomplete_items = get_one_random_item(incomplete_items, complete_items)
    elif choice == '2':
        list_items(complete_items)
    elif choice == '3':
        list_items(incomplete_items)
    elif choice == '4':
        print_data(complete_items, incomplete_items)
    elif choice == '5':
        unique_items = get_unique_items_from_DB()
        incomplete_items.update([item for item in unique_items if item not in complete_items])
        save_unique_items(complete_items, incomplete_items)
    elif choice == '6':
        exit()
    
    input()

    menu(complete_items, incomplete_items)

# function to get one random unique item display it move it to the complete set, then save the data
def get_one_random_item(incomplete_items, complete_items):
    # get a random item from the incomplete set
    random_item = incomplete_items.pop()
    # display the random item
    print(random_item)
    # add the random item to the complete set
    complete_items.add(random_item)
    # save the unique items
    save_unique_items(complete_items, incomplete_items)
    return complete_items, incomplete_items

# list items in passed set
def list_items(items):
    for item in items:
        print(item)

# main function
if __name__ == '__main__':
    # get the unique items
    complete_items, incomplete_items = read_unique_items()
    # display a menu
    menu(complete_items, incomplete_items)
