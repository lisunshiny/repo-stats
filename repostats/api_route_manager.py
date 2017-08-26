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
        url = self.get_pulls_url()
        r = requests.get(url, auth=self.credentials)

        if r.status_code is not requests.codes.ok:
            raise ValueError("Your credentials are invalid and/or your repository does not exist.")

    # GET /pulls
    # Documentation: https://developer.github.com/v3/pulls/#list-pull-requests

    # @return String in the form of "https://api.github.com/AccountNAme/repo-name/pulls"
    def get_pulls_url(self):
        return self.base_url + "repos/" + self.repo + "/pulls"

    def get_pulls_opts(self):
        return {"state": "all"}
