from threading import Thread
from redirect import Execute

people = [
    {
        "name": "Enrico",
        "colleges": [
            "admission@gatech.edu",
            "undergrad-admissions@ncsu.edu",
            "ug-admission@northwestern.edu",
            "admissions@psu.edu",
            "admissions@purdue.edu",
            "askabuckeye@osu.edu",
            "admissions@illinois.edu",
            "unchelp@admissions.unc.edu",
            "onwisconsin@admissions.wisc.edu",
            "admissions@vt.edu",
            "admissions@austin.utexas.edu"
        ],
        "other bad emails": [
            "english-personalized-digest@quora.com",
            "noreply@redditmail.com",
            "no-reply@marketing.espnmail.com",
            "NFL@email.nfl.com",
            "uber@uber.com",
            "nordstromrack@eml.nordstromrack.com"
        ],
        "email": "enricofpersico@gmail.com",
        "app password": "zyedfkgazhjrrfpl"
    },
    # {
    #     "name": "Justin",
    #     "colleges": [
    #         "admission@gatech.edu",
    #         "admissions@purdue.edu",
    #         "admissions@illinois.edu",
    #         "onwisconsin@admissions.wisc.edu",
    #         "be-a-hawkeye@uiowa.edu",
    #         "applicants@admissions.upenn.edu",
    #         "help@admissions.ufl.edu",
    #         "app.enquiries@monash.edu"
    #     ],
    #     "other bad emails": [

    #     ],
    #     "email": "jbcrasko@gmail.com",
    #     "app password": ""
    # },
    # {
    #     "name": "Allison", 
    #     "email": "allison012345@gmail.com",
    #     "colleges": [
    #         uc 
    #         vanderbilt
    #         umich
    #         uof i
    #     ]
    #     "other bad emails": [],

    # }
]

def main():
    for person in people:
        Thread(target=Execute(
            my_college_emails = person['colleges'], 
            my_email = person['email'], 
            app_password = person['app password'], 
            other_bad_emails = person['other bad emails'],
            person = person["name"]
        )).start()

if __name__ == "__main__":
    main()
