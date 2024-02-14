
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
#import nltk
#nltk.download('stopwords')
#from nltk.corpus import stopwords

# Read your README.md content (modify the path as needed)
readme_path = 'README.md'

def read_readme():
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        return readme_file.read()

def extract_text_from_markdown(markdown_content):
    soup = BeautifulSoup(markdown_content, 'html.parser')
    cleaned_text = ' '.join(soup.stripped_strings)
#    print(cleaned_text)
    # Remove stopwords
#    stop_words = set(stopwords.words('english'))
    words = cleaned_text.split()
#    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Exclude specific words (e.g., your name)
    excluded_words = ['ralucan', 'RalucaN', 'github', 'repo', 'https', 'keywords', 'key steps']
    filtered_words = [word for word in words if word.lower()  not in excluded_words]
#    print(filtered_words)

    return ' '.join(filtered_words)

markdown_content = read_readme()
cleaned_content = extract_text_from_markdown(markdown_content)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_content)

# Save the word cloud image
wordcloud.to_file('wordcloud.png')
