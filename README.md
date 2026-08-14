# Little Text Comparator

### What does it do ?
Using Python and NLTK, this program analyzes and compares two different texts. It then generates graphs for better data visualization with Plotly and Matplotlib.

### Why this project ?
This project was a way to start learning NLP basics, while doing some data visualization.

### Demo and features
Analysis includes:
- number of words,
- number of sentences,
- average number of letters per word,
- average number of words per sentence,
- lexical diversity,
- POS tagging.

Tables:
![alt text](examples/tables5.png)
A green box means a higher value compared to the other text.

Pie charts:
![alt text](<examples/POS tagging.png>)
### What I learned
I learned the basics of NLP:
- file preprocessing,
- simple tokenization and POS tagging,
- counting words and sentences.

More generally:
- working with multiple classes,
- simple error handling,
- imports,
- creating pie charts and tables.

I refactored the project before publishing it.

### How to use
##### Installation and setup
1. Create a virtual environment: 
    `python -m venv .venv`

2. Activate it: 
    macOS / Linux: `source .venv/bin/activate`
    Windows: `.venv\Scripts\Activate.ps1`

3. Install dependencies: `pip install -r requirements.txt`

##### Running the program
Please place your texts in the `Texts` folder as `.txt` files. Your texts must not be empty or corrupted.
Then, run `python main.py` and follow the instructions. When asked, enter the exact filename. For example: `Steam, Its Generation and Use` or `Computers-the machines we think with` without the `.txt` extension.

The program includes four texts from Project Gutenberg as examples.

### Possible improvements
Adding more NLP features and improving existing ones. Currently, the separation between words and punctuation can still be improved.

Better error handling and a more user-friendly interface.

### Credits
Natural Language Processing with Python, by Steven Bird, Ewan Klein, and Edward Loper. Copyright 2009 Steven Bird,
Ewan Klein, and Edward Loper, 978-0-596-51649-9.

Project Gutenberg — Source for the four example texts included with the project.

### License
This project is under the MIT license.
