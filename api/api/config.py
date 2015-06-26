"""
CTF API Configuration File

Note this is just a python script. It does config things.
"""

import api
import datetime

import api.app

HOST = "146.148.82.223"
LOCAL = "127.0.0.1"

""" FLASK """

api.app.session_cookie_domain = HOST
api.app.session_cookie_path = "/"
api.app.session_cookie_name = "flask"

# KEEP THIS SECRET
api.app.secret_key = "5XVbne3AjPH35eEH8yQI"

""" SECURITY """

api.common.allowed_protocols = ["https", "http"]
api.common.allowed_ports = [8080]

""" MONGO """

api.common.mongo_db_name = "pico"
api.common.mongo_addr = LOCAL
api.common.mongo_port = 27017

""" TESTING """

testing_mongo_db_name = "ctf_test"
testing_mongo_addr = LOCAL
testing_mongo_port = 27017

""" CTF SETTINGS """

enable_teachers = True
enable_feedback = True

competition_name = "picoCTF"
competition_urls = [HOST]

# Max users on any given team
api.team.max_team_users = 5

# Teams to display on scoreboard graph
api.stats.top_teams = 5

# start and end times!
class EST(datetime.tzinfo):
    def __init__(self, utc_offset):
        self.utc_offset = utc_offset

    def utcoffset(self, dt):
      return datetime.timedelta(hours=-self.utc_offset)

    def dst(self, dt):
        return datetime.timedelta(0)

start_time = datetime.datetime(2014, 7, 25, 9, 0, 0, tzinfo=EST(4))
end_time = datetime.datetime(2015, 7, 26, 14, 59, 59, tzinfo=EST(5))

# Root directory of all problem graders
api.problem.grader_base_path = "./graders"

""" ACHIEVEMENTS """

enable_achievements = True

api.achievement.processor_base_path = "./achievements"

""" SHELL SERVER """

enable_shell = False

shell_host = HOST
shell_username = "pico"
shell_password = "pico"
shell_port = 22

shell_user_prefixes  = list("abcdefghijklmnopqrstuvwxyz")
shell_password_length = 4
shell_free_acounts = 10
shell_max_accounts = 9999

shell_user_creation = "sudo useradd -m {username} -p {password}"

""" EMAIL (SMTP) """

api.utilities.enable_email = False
api.utilities.smtp_url = ""
api.utilities.email_username = ""
api.utilities.email_password = ""
api.utilities.from_addr = ""
api.utilities.from_name = ""

""" CAPTCHA """
enable_captcha = False
captcha_url = "http://www.google.com/recaptcha/api/verify"
reCAPTCHA_private_key = ""


""" AUTOGENERATED PROBLEMS """

api.autogen.seed = "0413688f8ef14e96b0afe25e2f662fef"

""" LOGGING """

# Will be emailed any severe internal exceptions!
# Requires email block to be setup.
api.logger.admin_emails = ["paullj1@gmail.com", "joe@example.com"]
api.logger.critical_error_timeout = 600
