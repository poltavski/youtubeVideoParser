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
        '--query', type=str, default='None',
        help='query for downloading'
    )

    parser.add_argument(
        '--output-folder', type=str, default='data',
        help='output folder name'
    )

    parser.add_argument(
        '--verbose', type=bool, default=False,
        help='give detailed description of processing'
    )

    parser.add_argument(
        '--text-queries', type=str, default='example.txt',
        help='.txt file with queries, check example.txt'
    )

    return parser.parse_args()


def process_query(download_folder, query, verbose):
    """
    process single query
    :param download_folder: str path to download folder
    :param query: str search query
    :return: downloads files in download_folder directory
    """
    download_path = download_folder + '/' + query

    os.makedirs(download_path, exist_ok=True)
    url_list = get_url_list(query)

    if len(os.listdir(download_path)) > len(url_list)/2:
        print('Query: ' + query + ' already downloaded, skip')
        return

    for i in tqdm(range(len(url_list))):
        try:
            YouTube(url_list[i]) \
                .streams \
                .get_by_resolution('720p') \
                .download(download_path)
        except:
            if verbose:
                print('no 720p quality, pass: ', url_list[i])


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
    text_queries = args.text_queries
    verbose = args.verbose

    queries = []
    if query != 'None':
        queries.append(query)

    file = open(text_queries, "r")
    queries.extend(file.read().splitlines())
    print('Queries to process: ', len(queries))
    for q in queries:
        print('Process query: ', q)
        process_query(download_folder=download_folder, query=q, verbose=verbose)


if __name__ == '__main__':
    main()
