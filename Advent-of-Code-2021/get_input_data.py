"""Helper functions for fetching personal Advent of Code data inputs."""

import requests
from decouple import config

AOC_SESSION = config("AOC_SESSION")

def get_response_data(url):
    """Get text data from response object."""
    response = requests.request(
      method="GET",
      url=url,
      headers={"cookie": f"session={AOC_SESSION}"}
    )

    if response.status_code == 200:
        return response.text

    print(f"Error: {response.status_code}")

    return None

def write_data(day, path="data.txt"):
    """Write personal input data from given day
    to a file determinedby given path."""
    url = f"https://adventofcode.com/2021/day/{day}/input"

    data = get_response_data(url)

    if data is None:
        print("No data available")
        return

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(data)
