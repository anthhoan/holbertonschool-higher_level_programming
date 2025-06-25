#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
Python script to fetch posts from JSONPlaceholder using requests.get()
"""

import csv
import requests


def fetch_and_print_posts():
    """
    fetch posts from JSONPlaceholder
    """
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])
        else:
            print("Failed to retrieve posts.")
    except requests.Timeout:
        print("The request timed out")
    except requests.RequestException as e:
        print(f"An error occured: {e}")

def fetch_and_save_posts():
    """
    fetch posts from JSONPlaceholder
    """
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5)
        if response.status_code == 200:
            posts = response.json()
            structured_data = [
                {'id': post['id'], 'title': post['title'], 'body': post['body']}
                for post in posts
            ]
            with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(structured_data)
            print("Successful data is saved to posts.csv.")
        else:
            print("Failed to retrieve posts. Status code:", response.status_code)
    except requests.Timeout:
        print("The request timed out.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")