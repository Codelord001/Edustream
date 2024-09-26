#!/bin/bash

# Download NLTK data
python -m nltk.downloader universal_tagset

# Download spaCy English model
python -m spacy download en
python -m spacy download en_core_web_sm

# Download and extract Sense2Vec model
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
tar -xvf s2v_reddit_2015_md.tar.gz -C Edustream_ai/

# Move Sense2Vec model to the appropriate directory
# Create the s2v_old directory inside Edustream_ai if it doesn't exist
mkdir -p Edustream_ai/s2v_old
mv s2v_reddit_2015_md/* Edustream_ai/s2v_old/

