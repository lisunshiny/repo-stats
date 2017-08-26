import requests
import csv
import os

github_

class StatPuller(object):
    top_level_fields_to_import = ["state", "url", "created_at", "updated_at", "closed_at", "merged_at"]
    pull_level_fields_to_import =  ["comments", "commits", "additions", "deletions"]

    # @param repo String the respository to scrape, in the format of AccountName/respository-name
    # @param csv_location String path to put the csv, e.g. mystats.csv
    # @param github_username String your GitHub username (for API credentials)
    # @param github_secret_key String your GitHub secret key (for API credentials)
    def __init__(self, repo, csv_location, github_username, github_secret_key):
        self.validate_credentials(repo, github_username, github_secret_key)

        self.url = url
        self.csv_location = csv_location
        self.api_creds = (github_username, github_secret_key)

    def validate_credentials(self, repo, github_username, github_secret_key):
        post

    def get_stats(self):
        print("asdfasdf")
