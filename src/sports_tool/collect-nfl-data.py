# Collect the past 5 years of nfl data

from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

URL = "https://github.com/nflverse/nflverse-data/releases/download"
OUTPUT_DIR = Path("data/raw/nfl")
RANGE = range(2020, 2027)
OVERWRITE = False # <- True when refreshing data

def download():



def main():



if __name__ == "__main__":
    main()