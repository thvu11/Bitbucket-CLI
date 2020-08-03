import os
import json

class Config:
    def __init__(self):
        #TODO: make this dynamic, use a config file or something
        with open(os.environ['CREDENTIAL']) as cred_json:
            data = json.load(cred_json)
            self.user = data['user']
            self.password = data['password']
            self.workspace = data['workspace']
            self.repo_slug = data['repo_slug']
        self.url = 'https://api.bitbucket.org/2.0/repositories'
        self.base_url = self.url + '/' + self.workspace + '/' + self.repo_slug

    def get_config(self):
        return {
            'user': self.user,
            'password': self.password,
            'workspace': self.workspace,
            'repo': self.repo_slug,
            'api': self.url
        }
