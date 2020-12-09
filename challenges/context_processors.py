from .views import First_Challenge_Users, Second_Challenge_Users

# Creating the Context processor That will serve Challenges Users - Mudsair Ali
def Challenge_User(req):
    return {'first_challenge_users': First_Challenge_Users, 'second_challenge_users': Second_Challenge_Users}
