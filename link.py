import re

def links(text):
    # Remplace les hashtags trouvés dans la chaîne de caractères par des lien de recherche sur facebook
    def remp(match):
        hashtag = match.group()
        link = f'<a href="https://facebook.com/search?q={hashtag[1:]}">{hashtag}</a>'
        return link

    return re.sub(r'#\w+', remp, text)

text = "here an #exemple of a #text havings some  #hashtags"
result = links(text)
print(result)