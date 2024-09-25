from pprint import pprint
import nltk
from Questgen import main
qe= main.BoolQGen()

payload = {
    "input_text": "Kwame Nkrumah University of Science and Technology (KNUST) was established in 1952 as the Kumasi College of Technology. It became a full university in 1961, named after Ghana's first President, Dr. Kwame Nkrumah. Initially focused on engineering, agriculture, and science, KNUST has expanded to include faculties like medicine, law, and business. It is renowned for its academic excellence, research, and contributions to Ghana's development.",
    "max_questions": 5
}


qg = main.QGen()
output = qg.predict_mcq(payload)
pprint (output)
    