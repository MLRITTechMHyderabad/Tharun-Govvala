import re

def Hash_Tags(text):
    
    matching = r"#\w+"
    hashtags_matches = re.findall(matching, text)
    
    return hashtags_matches

text = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

valid_hash_tags = Hash_Tags(text)
print(valid_hash_tags)
