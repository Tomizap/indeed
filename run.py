from indeed import *

from users import users


class AutoApply:

    def __init__(self, s):
        super(AutoApply, self).__init__()
        self.indeed = Indeed(s)

    def start(self):
        self.indeed.application_loop()

    def end(self):
        pass


user_id = 8
user = next((x for x in users if x['ID'] == user_id), None)
config = {
    "inputs": {
        "keywords": ['alternance commerce', 'alternance communication', 'alternance marketing'],
        "localization": "Clichy (92)",
        "excluded_keywords": ['stag'],
        "included_keywords": [],
        "contract_type": [],
        "remote": False,
        "minium_salary": 0
    },
    "options": {
        "hide_jobs": False,
        "message_to_recruiter": False,
        "DEBUG": True,
        "headless": False,
        "infinite": True,
        "safe_mode": False
    },
    "presets": {
        "phone": user['phone'],
        "name": user['firstname'],
        "nom": user['firstname'],
        "pays": "fr",
        "mail": user['email'],
        "linkedin": user['linkedin'],
        "internet": user['website'],
        "civilité": ["homme", "m."]
    },
    "user": user
}
AutoApply(config).start()
