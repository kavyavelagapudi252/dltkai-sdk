import dltkai as dl

print(dl.NaturalLanguage.pos_tagger('My name is Nagesh. I like to play basketball. I live in Lucknow'))
print(dl.NaturalLanguage.ner_tagger('Delhi is a capital of India. Google and Microsoft are rivals. Facebook was founded by Mark Zukerberg.'))
print(dl.NaturalLanguage.dependency_parser('I prefer the morning flight through Denver'))
print(dl.NaturalLanguage.sentiment_detect('Though it is android TV comes with pre-installed PRIME VIDEO and other Video apps, Prime video and other apps are getting crashed. i have raised complaint to Amazon to troubleshoot the issue and their technician has reported that TV has issues without showing-up to my house . i have also contacted VU customer service, they said this model has issue. i really had bad experience with amazon service. the lesson i learnt is buy it from your local shops around you, instead of going through this hardship. Zero Star for their valuable service. i do not thing Amazon will post my review.'))
print(dl.NaturalLanguage.sarcasm_detect('oh! i never knew  that'))
print(dl.NaturalLanguage.toxic_comment_detect('I hate my wife and I hate all women'))
print(dl.NaturalLanguage.detect_tonality('Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entr...'))
print(dl.NaturalLanguage.detect_tonality('FreeMsg Hey there darling it\'s been 3 week\'s now and no word back! I\'d like some fun you up for it s...'))
