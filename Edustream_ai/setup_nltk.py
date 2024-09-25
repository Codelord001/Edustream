import nltk
# List of NLTK data packages to download
nltk_packages = ['brown', 'stopwords', 'popular','punkt_tab']

# Download each package
for package in nltk_packages:
    nltk.download(package)
