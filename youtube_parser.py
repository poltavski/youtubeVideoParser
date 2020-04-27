import urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube
import os
from tqdm import tqdm
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description='Downloads youtube videos by query'
    )

    parser.add_argument(
        '--query', type=str, required=True, default='hello world',
        help='query for downloading'
    )

    parser.add_argument(
        '--output-folder', type=str, default='data',
        help='output folder name'
    )
    return parser.parse_args()


def get_url_list(query):
    """
    gets url list by given query
    :param query: name of search youtube query
    :return: list of url videos
    """
    url_list = []
    textToSearch = query
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        url = 'https://www.youtube.com' + vid['href']
        url_list.append(url)
    return url_list


def main():
    args = parse_args()

    query = args.query
    download_folder = args.output_folder
    download_path = download_folder+'/'+query
    os.makedirs(download_path, exist_ok=True)
    url_list = get_url_list(query)
    for i in tqdm(range(len(url_list))):
        YouTube(url_list[i])\
            .streams\
            .get_by_resolution('720p')\
            .download(download_path)


if __name__ == '__main__':
    main()
