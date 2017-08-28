import requests
import csv
import os
import api_route_manager
from api_route_manager import ApiRouteManger

class StatPuller(object):
    top_level_fields_to_import = ["state", "url", "created_at", "updated_at", "closed_at", "merged_at"]
    pull_level_fields_to_import =  ["comments", "commits", "additions", "deletions"]

    # @param repo String the respository to scrape, in the format of AccountName/respository-name
    # @param csv_location String path to put the csv, e.g. mystats.csv
    # @param github_username String your GitHub username (for API credentials)
    # @param github_secret_key String your GitHub secret key (for API credentials)
    def __init__(self, repo, csv_location, github_username, github_secret_key):
        # TODO remove hardcode in working stuff
        github_username = "lisunshiny"
        github_secret_key = os.environ.get('GITHUB_SECRET_KEY')
        # END remove

        self.csv_location = csv_location
        self.route_manager = ApiRouteManger(repo, (github_username, github_secret_key))

    def pull_stats(self):
        return self.route_manager.get_pulls()


    def write_to_csv(self):
        print("writing to csv")
'''
import stat_puller
from stat_puller import StatPuller
puller = StatPuller("Appboy/platform", "lol.csv", "lisunshiny", "will_be_replaced")
puller.pull_stats()
'''
