# Collect the past 5 years of nfl data

from pathlib import Path
from shutil import copyfileobj
from urllib.error import HTTPError
from urllib.request import Request, urlopen

URL = "https://github.com/nflverse/nflverse-data/releases/download"
OUTPUT_DIR = Path("data/raw/nfl")
RANGE = range(2020, 2027)
OVERWRITE = False # <- True when refreshing data

def download(tag, filename, folder):
    destination = OUTPUT_DIR / folder / filename
    destination.parent.mkdir(parents=True, exist_ok=True) 

    if destination.exists() and not OVERWRITE:
        print(f"Skip: {destination}")
        return

    url =  f"{URL}/{tag}/{filename}"
    temp = destination.with_suffix(".parquet.part")
    print(f"Download: {destination}")

    try:
        request = Request(url, headers={"User-Agent": "SportsStat-491Final"})
        with urlopen(request, timeout=60) as response:
            with temp.open("wb") as file:
                copyfileobj(response, file)

        with temp.open("rb") as file:
            if temp.stat().st_size < 8 or file.read(4) != b"PAR1":
                raise ValueError(f"Invalid Parquet download: {filename}")
            file.seek(-4, 2)
            if file.read(4) != b"PAR1":
                raise ValueError(f"Incomplete Parquet download: {filename}")

        temp.replace(destination)
        print(f"Saved to: {destination}")

    except HTTPError as error:
        if error.code == 404:
            print(f"Not available: {filename}")
        else:
            raise
    finally:
        temp.unlink(missing_ok=True)


def main():
    



if __name__ == "__main__":
    main()