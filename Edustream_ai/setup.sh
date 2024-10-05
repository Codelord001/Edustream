#!/bin/bash

# Download NLTK data
python -m nltk.downloader universal_tagset


python -m spacy download en_core_web_sm

# Download and extract Sense2Vec model
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
tar -xvf s2v_reddit_2015_md.tar.gz -C Edustream_ai/


