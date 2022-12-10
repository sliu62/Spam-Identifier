# [Spam-Identifier](https://github.com/Curseridden/Spam-Identifier)
A python-based input classifier for class assignment that uses random forest algorithm to evaluate its input

**Machine Learning Algorithms were done by:** [@leonardgarcia90](https://github.com/leonardgarcia90)


**UI**:

[tkinter](https://docs.python.org/3/library/tkinter.html) - python standard library

[custom tkinter](https://github.com/TomSchimansky/CustomTkinter) - a more nicer and user friendly version of tkinter that built upon tkinter

**Machine Learning**:

[pickle](https://docs.python.org/3/library/pickle.html) - python object serializing and de-serializing tool (use to save and load the machine learning model)

[sklearn](https://scikit-learn.org/stable/) - python machine learning library

[nltk](https://www.nltk.org/) - python natural language toolkit

**Installation and Configuration:**
1. Check the above libraries (except tkinter and pickle) and install them through pip, anaconda, or any other python platforms you are using
2. Download the code as a zip, unzip to any location you like
3. On terminal/command prompt, change to the directory to where you saved your unzipped files, then run: **python main.py**


**Features:**
1. Simple Graphical User Interface (GUI) that is very straight forward
2. Supporting switching between identifying email and text message input
3. Supporting export evaluation to a .csv file for future evaluation
4. Light weight application that is good for offline
5. Automatically switch between light mode and dark mode based on system setting (featured by custom tkinter)

**Issues/Limitaions:**
1. Limited amount of training data and testing data, only able to identify old fashion spam messages
2. Limited features

**Future works (if possible):**
1. Find a more robust dataset to train the model to give a more modern result
2. Support more exporting file types
3. Cache the configuration and export it to a .cfg file so user will no longer need to re-configure the app every time they start the app
4. Support more font types (and maybe font sizes) for better visualization for different groups of people
5. Manually switch between light mode and dark mode of the application
6. Export the program into a stand alone software for different platform, no more libraries installation will be required
7. Support internal model training to help improve the software locally
8. Support opening up customized training model based on what the user expected

**Resources**:

[Text Message Training Python Notebook](https://colab.research.google.com/drive/1o8qf9L3Ppcf1rnJpIoAF034VZPjIa3sc)

[Email Training Python Notebook](https://colab.research.google.com/drive/1Mbrbx0IJ0whav2u7OrcBbCOIo5RrCS4e)
