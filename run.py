from indeed import *


class AutoApply:

    def __init__(self, s):
        super(AutoApply, self).__init__()
        self.indeed = Indeed(s, name="indeed")

    def start(self):
        self.indeed.application_loop()

    def end(self):
        pass


config = {
    "inputs": {
        "keywords": ['seo', 'webmarketing', 'wordpress', 'e-commerce'],
        "localization": "Ile-de-France",
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
        "phone": "0665774180",
        "name": "Tom",
        "nom": "Tom",
        "pays": "fr",
        "mail": "zaptom.pro@gmail.com",
        "twitter": "https://twitter.com/tom_zapico",
        "linkedin": "https://www.linkedin.com/in/tom-zapico/",
        "internet": "https://tom-zapico.com",
        "civilité": ["m", "homme"]
    },
    "user": {
        "email": "t.zapico@ldeclic.fr",
        "password": "Tom01032000",
        "phone": "0665774180"
    }
}
AutoApply(config).start()
