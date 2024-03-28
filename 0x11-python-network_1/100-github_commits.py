#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for k in range(10):
            print("{}: {}".format(
                commits[k].get("sha"),
                commits[k].get("commit").get("author").get("name")))
    except IndexError:
        pass
