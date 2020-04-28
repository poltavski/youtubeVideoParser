# youtubeVideoParser
Simple terminal python youtube video parser by given query with use of pytube library 

## Installation
Install requirements by:

```pip install -r requirements.txt```

### Usage
#### script arguments
```shell script
'--query', type=str, default='None',
help='query for downloading'
'--output-folder', type=str, default='data',
help='output folder name'
'--verbose', type=bool, default=False,
help='give detailed description of processing'
'--text-queries', type=str, default='example.txt',
help='.txt file with queries, check example.txt'
```
#### run solution
From command line or IDE with additional parameters:

``` python youtube_parser.py --text-queries="my_txt_queries.txt" --output_folder="downloads"```

