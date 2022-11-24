# Spam-Identifier
A python-based input classifier for class assignment

UI:

tkinter - python standard library

custom tkinter - a more nicer and user friendly version of tkinter that built upon tkinter - https://github.com/TomSchimansky/CustomTkinter

Machine Learning:

sklearn - python machine learning library - https://scikit-learn.org/stable/

nltk - python natural language toolkit - https://www.nltk.org/


Features:
1. Simple Graphical User Interface (GUI) that is very straight forward
2. Supporting switching between identifying email and text message input
3. Supporting export evaluation to a .csv file for future evaluation
4. Light weight application that is good for offline
5. Automatically switch between light mode and dark mode based on system setting (featured by custom tkinter)

Issues/Limitaions:
1. Limited amount of training data and testing data, only able to identify old fashion spam messages
2. Limited features

Future work (if possible):
1. Find a more robust dataset to train the model to give a more modern result
2. Support more exporting file types
3. Cache the configuration and export it to a .cfg file so user will no longer need to re-configure the app everytime they start the app
4. Support more font types (and maybe font sizes) for better visualization for different groups
5. Manaully switch between light mode and dark mode of the application
