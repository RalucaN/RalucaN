from wordcloud import WordCloud
from bs4 import BeautifulSoup
import string
import re
from PIL import Image
import numpy as np

readme_path = 'README.md'

def read_readme():
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        return readme_file.read()

def extract_text_from_markdown(markdown_content):
    soup = BeautifulSoup(markdown_content, 'html.parser')
    cleaned_text = ' '.join(soup.stripped_strings)
    
    cleaned_text = re.sub(r'http\S+|www.\S+', '', cleaned_text, flags=re.MULTILINE)
    
    stop_words = set(['the', 'and', 'to', 'of', 'a', 'in', 'is', 'that', 'for', 'on', 'it', 'with', 'as', 'was', 'at', 'by', 'an', 'be', 'this', 'which', 'or', 'from', 'are', 'we', 'have', 'not', 'has', 'your', 'will', 'more', 'can', 'also', 'but', 'about', 'up', 'what', 'there', 'out', 'all', 'their', 'who', 'they', 'so', 'her', 'would', 'if', 'when', 'she', 'him', 'you', 'could', 'no', 'my', 'than', 'he', 'its', 'may', 'into', 'only', 'other', 'new', 'these', 'some', 'two', 'may', 'then', 'do', 'first', 'any', 'its', 'now', 'our', 'even', 'most', 'me', 'made', 'over', 'did', 'down', 'were', 'just'])
    words = cleaned_text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]

    excluded_words = ['RalucaN', 'Raluca', 'github', 'repo', 'using', 'Keywords', 'Key steps']
    filtered_words = [word for word in filtered_words if word.lower() not in excluded_words]

    filtered_words = [''.join(c for c in w if c not in string.punctuation) for w in filtered_words]
    filtered_words = [word for word in filtered_words if word]

    return ' '.join(filtered_words)

markdown_content = read_readme()
cleaned_content = extract_text_from_markdown(markdown_content)

bubble_mask = np.array(Image.open("gears.png"))

wordcloud = WordCloud(width=800, height=400, background_color='black', contour_color='steelblue', contour_width=3, collocations=False, mask=bubble_mask).generate(cleaned_content)
wordcloud.to_file('wordcloud.png')
