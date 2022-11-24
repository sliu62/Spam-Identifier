import pickle
import sklearn
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
import nltk
nltk.load('./nltk_data/tokenizers/punkt/english.pickle')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from tkinter import messagebox as msg


class Identifier():

    def __init__(self):

        self.__textModel = None
        self.__textVectorizer = None

        self.__emailModel = None
        self.__emailVectorizer = None

        self.__loadIdentifier()

    # load the model files
    def __loadIdentifier(self):

        with open("./models/textModel/model_pkl", "rb") as file:
            self.__textModel = pickle.load(file)
        
        with open("./models/textModel/vectorizer_pkl", "rb") as file:
            self.__textVectorizer = pickle.load(file)

        with open("./models/emailModel/model_pkl", "rb") as file:
            self.__emailModel = pickle.load(file)
        
        with open("./models/emailModel/vectorizer_pkl", "rb") as file:
            self.__emailVectorizer = pickle.load(file)

    # evaluate based on the model
    def evaluate(self, inputMessage, type):

        processedInput = self.__processInput(inputMessage)

        if (type == "Email"):
            vectorizedMsg = self.__emailVectorizer.transform([processedInput])
            prediction = self.__emailModel.predict(vectorizedMsg[0])

        elif (type == "Text Message"):
            vectorizedMsg = self.__textVectorizer.transform([processedInput])
            prediction = self.__textModel.predict(vectorizedMsg[0])

        else:
            msg.showerror("Error", "System Error")

        if prediction == 0:
            return "Normal"

        else:
            return "Suspicious"

    def __processInput(self, inputMsg):
        inputMsg =  inputMsg.lower()
        inputMsg =  inputMsg.translate(str.maketrans('', '', string.punctuation))
        inputMsg =  inputMsg.replace(r'[^\w\s]+', '')
        inputMsg =  inputMsg.replace('_', '')
        inputMsg =  inputMsg.replace('\d+', '')
        inputMsg =  inputMsg.replace('\n', '')
        words_to_remove = ['com', 'e', 'cc', 'j', 'subject','å', 'http']
        pat = r'\b(?:{})\b'.format('|'.join(words_to_remove))
        inputMsg =  inputMsg.replace(pat, '')
        text_tokens = word_tokenize(inputMsg)
        inputMsg = [word for word in text_tokens if not word in stopwords.words()]
        stemmer = PorterStemmer()
        inputMsg = [stemmer.stem(w) for w in inputMsg]
        inputMsg = (" ").join(inputMsg)
        return inputMsg
