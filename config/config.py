# This value will determine how many surveys are completed every hour.
# if surveys are completed t6o quickly McDonald's won't believe that a human did
# them, and in this case they'd be right.
# To be safe, for now, this shouldn't exceed 60, but more testing will be done
# to find out exactly where the line lies.
SURVEYS_PER_HOUR = 59

# Setting this to True will force the bot to work in the background in practice
# it seems as if this causes failures to happen more often. However, it has a
# major upside of allowing you to do other things on your computer while the bot
# is running.
IS_HIDDEN_BROWSER = True

# This setting causes the bot to use fake codes that dont go to any stores.
# This is only for debugging and development purposes
IS_TEST_MODE = False


# The comments that are generated by this program are chosen randomly you can
# add/change/delete options from these lists.

# you can test out how the comments will look by pressing the play button on
# line 13 of "generate_survey_responses.py" or right-clicking that file in the
# file explorer and selecting run

# Part one should be a descriptive word or phrase. probably a positive one, but
# negative sounding reviews don't change your VOICE score.
RESPONSE_PART_ONE = [
    "Great",
    "Good",
    "Legendary",
    "Adequate",
    "Surprisingly good",
    "Wonderfully adequate",
    "On par with wendy's",
    "Almost as good as my wife's",
    "Better than my wife's",
    "god-tier",
    ]

# Part Two should start with the thing part one is describing, then maybe add
# some flavor after that.
RESPONSE_PART_TWO = [
    "food, loved my visit today!",
    "food this time.",
    "food, great service, I even got a smile.",
    "people, love to serve you with a smile!",
    "atmosphere, makes you feel welcome.",
    "service and food!",
    "food, the person who took my order was very friendly.",
    "food, McDonalds is definitely getting better!",
    "food.",
    "visit, legendary nuggets! and the big mac is to die for!",
    ]

# Part three doesnt have to flow into anything else so there really arent many
# rules here, but I tended to have them talking about wanting to return.
RESPONSE_PART_THREE = [
    "might come back soon!",
    "thinking of returning.",
    "thinking of coming back.",
    "definitely gonna come back to get me summa that food!",
    "I'll be back.",
    "I might return this week",
    "thinking of returning soon.",
    "might return soon.",
    "I'll definitely come back soon.",
    "heck, I might come back later today!!",
    "Aleena was supercalifragilisticexpialidocious! I might come back today!!",
    ]

# This is placed at the end of every survey, it is not decided randomly but
# rather cycled through in order. These are useful for if you are trying a new
# setting on the bot, but they lead to highly suspect comments.
RESPONSE_SIGNATURE = [
    "",
    ]
