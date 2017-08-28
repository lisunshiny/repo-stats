import requests

class ApiRouteManger(object):
    base_url = "https://api.github.com/"

    # @param repo String in the form of "AccountName/repo-name"
    # @param credentials Tuple in the form of (github_username, github_secret_key)
    def __init__(self, repo, credentials):
        self.repo = repo
        self.credentials = credentials
        # Will raise an error if they're not valid.
        self.validate_credentials()

    def validate_credentials(self):
        # using GET /pulls as a proxy for valid credentials
        url = self.get_pulls_url()
        r = self.get(url, {})

        if r.status_code is not requests.codes.ok:
            raise ValueError("Your credentials are invalid and/or your repository does not exist.")

    def get_pulls(self):
        url = self.get_pulls_url()
        r = self.get(url, {})

        return r.json()

    def get(self, url, params = {}):
        url = self.get_pulls_url()
        r = requests.get(url, auth=self.credentials, params=params)

        if r.status_code is 403 and "API rate limited exceeded" in r.json()["message"]:
            raise Exception("You've been rate limited :(")

        return r

    # GET repos/:repo/pulls
    # Documentation: https://developer.github.com/v3/pulls/#list-pull-requests

    # @return String in the form of "https://api.github.com/repos/Owner/repo-name/pulls"
    def get_pulls_url(self):
        return self.base_url + "repos/" + self.repo + "/pulls"

    def get_pulls_opts(self):
        return {"state": "all"}

    # GET /repos/:owner/:repo/pulls/:number/comments
    # Documentation: https://developer.github.com/v3/pulls/#list-pull-requests

    # @param pull_number Number or String the number of the pull
    # @return String in the form of "https://api.github.com/repos/Owner/repo-name/pulls/1234/comments"
    def get_comments_for_pull_url(self, pull_number):
        return get_pulls_url() + str(pull_number) + "/comments"

    def get_comments_opts(self):
        return {}
