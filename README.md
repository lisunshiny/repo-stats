# Repo Stats

This project is meant to make it easier for people to pull statistics on pull requests on specific repositories.

It was motivated by these studies, which seem to suggest that women are scrutinized more than men in their
peer-reviewed work (e.g. academic papers, pull requests).

https://peerj.com/preprints/1733/
http://www.erinhengel.com/research/publishing_female.pdf

When I heard about these papers, I became interested in polling statistics to see if there are any differences
in how pull requests are reviewed between different marginalized groups in tech. While this is just a POC,
I'm hoping that it provides a baseline for people to pull stats on their organizations to facilitate data-driven
discussions.

## Usage (not working for others rn)

```bash
$ repostats AccountName/repo-name location.csv
Success! Printed results as a CSV to location.csv
```

### Current CSV fields
______________
`author`

`predicted_gender` (this is predicted by the API provided by genderize.io)

`url`

`commits`

`additions`

`deletions`

`comments_by_self`

`comments_by_others`

`created_at`

`updated_at`

`comments`

`merged_at`

`closed_at`

`state`


## TODO (in order of importance)
- [ ] Figure out some kind of way for people to authenticate with the GitHub API with their own creds in a way that lets them query repos from private organizations that enforce SSO SAML. This is extra important since a key use case is people to be able to pull statistics on their own companies' private repositories, and without some way to authenticate, that isn't possible.
- [ ] Make more performant -- currently it does 3 HTTP requests per pull request, which is v v slow and just :(
- [ ] Less awful janky argument passing
- [ ] Batch gender API calls by 10, also figure out how to increase the limit on this (currently 1000/day, which is nothing)
- [ ] Clean up `__init__.py` since its gross
- [ ] Clean up these docs
- [ ] Add an option for either CSV or JSON.
- [ ] and more!
