import requests
import csv
import os

TOP_LEVEL_FIELDS_TO_IMPORT = ["state", "url", "created_at", "updated_at", "closed_at", "merged_at"]

def repostats(url = "", out_csv_location = ""):
    stat_arr = []
    # BC im lazy, default to the Ace editor
    if url is "":
        url = "https://api.github.com/repos/ajaxorg/ace/pulls"
    else:
        url = "https://api.github.com/repos/" + url + "/pulls"

    if out_csv_location is "":
        out_csv_location = "lol.csv"

    # TODO(add a different kind of auth so that other people can use my package)
    params = {"state":"all"}
    r = requests.get(url, auth=('lisunshiny', os.environ.get('GITHUB_SECRET_KEY')), params=params)
    pulls = r.json()

    # TODO: replace with commented out line, its so i dont get rate limited while developing
    for pull in [pulls[1]]:
    # for pull in pulls:
        stats = {}

        stats["author"] = pull["user"]["login"]
        stats["probable_gender"] = get_gender(pull["user"]["login"])

        stats["state"] = pull["state"]
        stats.update(get_number_of_comments(pull["comments_url"], pull["user"]["login"]))
        for field in TOP_LEVEL_FIELDS_TO_IMPORT:
            stats[field] = pull[field]

        stat_arr.append(stats)

    if len(stat_arr) is not 0:
        with open(out_csv_location, 'wb') as f:
            writer = csv.DictWriter(f, fieldnames=stat_arr[0].keys())
            writer.writeheader()
            writer.writerows(stat_arr)

def get_gender(login):
    # TODO: batch these by 10 to avoid getting rate limited
    r = requests.get("https://api.github.com/users/" + login)
    user_info = r.json()

    if user_info["name"] is None:
        return None

    if " " in user_info["name"]:
        name_to_check = user_info["name"].split()[0]
    else:
        name_to_check = user_info["name"]

    gender_request = requests.get("https://api.genderize.io/?name=" + name_to_check)

    return gender_request.json()["gender"]

# returns {"comments_by_self": X, "comments_by_others": Y}
def get_number_of_comments(url, author):
    # TODO(add a different kind of auth so that other people can use my package)
    r = requests.get(url, auth=('lisunshiny', os.environ.get('GITHUB_SECRET_KEY')))
    comments_info = r.json()
    data = {"comments_by_self": 0, "comments_by_others": 0}

    for comment in comments_info:
        if author is comment["user"]["login"]:
            data["comments_by_self"] += 1
        else:
            data["comments_by_self"] += 1

    return data
