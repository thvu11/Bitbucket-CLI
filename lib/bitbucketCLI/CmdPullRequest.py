from .UserAgent import UserAgent

import pprint

class CmdPullRequest:
    def __init__(self, config_obj):
        self.pull_request_endpoint = config_obj.base_url + '/pullrequests'
        self.pp = pprint.PrettyPrinter(indent=4)
        self.ua = UserAgent()
        self.branch_dict = config_obj.branch_dict

    def view(self, pr_id):
        # view the detail of a chosen pull request
        endpoint = self.pull_request_endpoint + '/' + str(pr_id)

        pr = self.ua.get(endpoint)
        print("title: {}\n".format(pr['title']))
        print("summary:\n{}\n".format(pr['summary']['raw']))
        return 1

    def create(self, details={}):
        # create a PR using the current branch you're on
        #NOTE mock post data
        dest_branch = 'master'
        if 'branch' in details:
            if details['branch'] in self.branch_dict['available_branch']:
                dest_branch = details['branch']
            else:
                print("Unknown branch " + details['branch'])
                return 0


        data = {
            "title": details['title'],
            "source": {
                "branch": {
                    "name": self.branch_dict['my_branch']
                    #"name": "update-readme"
                }
            },
            "destination": {
                "branch": {
                    "name": dest_branch
                }
            },
            "description": details['description']
        }

        new_pr = self.ua.post(self.pull_request_endpoint, data)
        print("Pull request (id={}) is created successfully\n".format(new_pr['id']))

        return 1

    def status(self, pr_id):
        # get activity log for the pr
        endpoint = self.pull_request_endpoint + '/' + str(pr_id)

        pr = self.ua.get(endpoint)
        print("title: {}".format(pr['title']))
        print("state: {}".format(pr['state']))

        # get activity log for the pr
        activity_endpoint = self.pull_request_endpoint + '/' + str(pr_id) + '/activity'

        pr = self.ua.get(activity_endpoint)
        for activity in pr['values']:
            if activity['update']['changes']:
                self.pp.pprint(activity['update']['changes'])
        return 1

    def close(self, pr_id, action="decline"):
        endpoint = self.pull_request_endpoint + '/' + str(pr_id) + '/' + action
        self.ua.post(endpoint)
        print("Pull request (ID={}) is {}".format(str(pr_id), action))
        return 1

    def list(self, id):
        # list all open pr
        pull_requests = self.ua.get(self.pull_request_endpoint)

        for pr in pull_requests['values']:
            print("title: {}\n".format(pr['title']))
            print("summary:\n{}\n".format(pr['summary']['raw']))
        return 1
