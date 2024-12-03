from selenium import webdriver
from selenium.webdriver.common.by import By

global driver
driver = webdriver.Chrome()

global url 
url = 'https://newtoxic.com/New_Movies/'

def movie_names():
    driver.get(url)
    movies = driver.find_elements(By.TAG_NAME, 'li')
    movie_list = [movie.text.replace(' ', '') for movie in movies]
    return movie_list

def next_pages():
    page_list = ['00455', '00454', '00453', '00452', '00451',]
    for num in page_list:
        driver.get(url + f'{num}.php')
        movies = driver.find_elements(By.TAG_NAME, 'li')
        movie_list = [movie.text.replace(' ', '') for movie in movies]
        compiled_list = movie_names() + movie_list
    return compiled_list


def action_genres():
    action_movies = []
    for movie in next_pages(): 
        driver.get(url+ f'/2024/{movie}.php')
        font_list = driver.find_elements(By.TAG_NAME, 'font')
        for item in font_list:
            if 'Action' in item.text:
                action_movies.append(movie)
    return action_movies

with open('action_movies.txt', 'w') as action:
    for movie in action_genres():
        action.write('movie\n')