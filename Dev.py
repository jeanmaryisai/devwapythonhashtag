import re

def hashtags_to_links(text):
    # Remplace les hashtags trouvés dans la chaîne de caractères par des lien de recherche sur twitter
    def replace_hashtag(match):
        hashtag = match.group()
        link = f'<a href="https://twitter.com/search?q={hashtag}">{hashtag}</a>'
        return link
    
    return re.sub(r'#\w+', replace_hashtag, text)

text = "Voici un #exemple de #texte contenant des #hashtags"
result = hashtags_to_links(text)
print(result)

