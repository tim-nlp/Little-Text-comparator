import plotly.graph_objects as go
import matplotlib.pyplot as plt

class Visualisation:
    """Create data visualisation"""
    def __init__(self, analyse1, analyse2, name_text1, name_text2,
                 author1=None, author2=None):
        self.analyse1 = analyse1
        self.analyse2 = analyse2
        self.name_text1 = name_text1
        self.name_text2 = name_text2
        self.author1 = author1
        self.author2 = author2


    def compare_values(self):
        """Creates table comparing Text 1 and 2."""
        # Establish color lists
        self.couleurs_text1 = []
        self.couleurs_text2 = []
        # Construct lists of attributes
        self.attributes1 = [self.analyse1.num_tokens, self.analyse1.num_words,
                            self.analyse1.num_sentences, self.analyse1.letters_words,
                            self.analyse1.words_sentences, self.analyse1.lex_div]
        self.attributes2 = [self.analyse2.num_tokens, self.analyse2.num_words,
                            self.analyse2.num_sentences, self.analyse2.letters_words,
                            self.analyse2.words_sentences, self.analyse2.lex_div]
        # Compare values with zip()
        for self.element1, self.element2 in zip(self.attributes1, self.attributes2):
            if self.element1 > self.element2:
                self.couleurs_text1.append('#a6e3a1')
                self.couleurs_text2.append('#f38ba8')
            elif self.element1 < self.element2:
                self.couleurs_text1.append('#f38ba8')
                self.couleurs_text2.append('#a6e3a1')
            else:
                self.couleurs_text1.append('#89b4fa')
                self.couleurs_text2.append('#89b4fa')

# deux formats différents :
# 1 avec auteurs, l'autre sans

    def make_table(self):
        # Make table
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Attributes',
                                f'{self.name_text1} by {self.author1}',
                                f'{self.name_text2} by {self.author2}'],
                        line_color='darkslategray',
                        height=30, 
                        font=dict(color='#cdd6f4', size=14,),
                        fill_color='royalblue'),
            cells=dict(values=[
                ['Number of tokens', 'Number of words', 'Number of sentences',
                'Average number of letters per word',
                'Average number of words per sentence', 'Lexical diversity'],
                [self.analyse1.num_tokens, self.analyse1.num_words,
                self.analyse1.num_sentences,
                f"{self.analyse1.letters_words:.2f}",
                f"{self.analyse1.words_sentences:.2f}",
                f"{self.analyse1.lex_div:.2f}"],
                [self.analyse2.num_tokens, self.analyse2.num_words,
                self.analyse2.num_sentences,
                f"{self.analyse2.letters_words:.2f}",
                f"{self.analyse2.words_sentences:.2f}",
                f"{self.analyse2.lex_div:.2f}"]],
                            height = 30,
                            line_color='darkslategray',
                            font=dict(color='#313244', size=14,),
                            fill=dict(color=['#bac2de', self.couleurs_text1, 
                                            self.couleurs_text2])))])
        fig.update_layout(title = "Comparing two texts",
                        title_font=dict(size=36, color='#313244'))
        fig.show()


    def make_table_api(self):
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Attributes',
                                f'{self.name_text1.title()} by {self.author1}',
                                f'{self.name_text2.title()} by {self.author2}'],
                        line_color='darkslategray',
                        height=30, 
                        font=dict(color='#cdd6f4', size=14,),
                        fill_color='royalblue'),
            cells=dict(values=[
                ['Number of tokens', 'Number of words', 'Number of sentences',
                'Average number of letters per word',
                'Average number of words per sentence',
                'Lexical diversity'],
                [self.analyse1.num_tokens, self.analyse1.num_words,
                self.analyse1.num_sentences,
                f"{self.analyse1.letters_words:.2f}",
                f"{self.analyse1.words_sentences:.2f}",
                f"{self.analyse1.lex_div:.2f}"],
                [self.analyse2.num_tokens, self.analyse2.num_words,
                self.analyse2.num_sentences,
                f"{self.analyse2.letters_words:.2f}",
                f"{self.analyse2.words_sentences:.2f}",
                f"{self.analyse2.lex_div:.2f}"]],
                            height = 30,
                            line_color='darkslategray',
                            font=dict(color='#313244', size=14,),
                            fill=dict(color=['#bac2de', self.couleurs_text1, 
                                            self.couleurs_text2])))])
        fig.update_layout(title = "Comparing two texts",
                            title_font=dict(size=36, color='#313244'))
        # fig.write_html("comparaison.html") -> enregistrer en tant que html interactif
        fig.show()


    def create_pies(self):
        """Creating a pie to visualize POS tagging"""
        labels = list(self.analyse1.data.keys())
        values1 = list(self.analyse1.data.values())
        values2 = list(self.analyse2.data.values())

        _, (ax1, ax2) = plt.subplots(1, 2) # _ équivaut à fig (jamais utilisé donc ignoré)

        colors = plt.cm.tab20(range(len(labels)))

        ax1.pie(values1,
                labels=labels,
                autopct='%1.1f%%',
                textprops={'fontsize': 8, 'color': 'black'}, 
                pctdistance=0.8,
                colors=colors)
        ax1.set_title(f"POS tagging in {self.name_text1.title()}", fontsize=16)

        ax2.pie(values2,
                labels=labels,
                autopct='%1.1f%%',
                textprops={'fontsize': 8, 'color': 'black'},
                pctdistance=0.8,
                colors=colors)
        ax2.set_title(f"POS tagging in {self.name_text2.title()}", fontsize=16)
        plt.show()

    def create_pies_api(self):
        """Creating a pie to visualize POS tagging"""
        labels = list(self.analyse1.data.keys())
        values1 = list(self.analyse1.data.values())
        values2 = list(self.analyse2.data.values())

        _, (ax1, ax2) = plt.subplots(1, 2) # _ équivaut à fig (jamais utilisé donc ignoré)

        colors = plt.cm.tab20(range(len(labels)))

        ax1.pie(values1,
                labels=labels,
                autopct='%1.1f%%',
                textprops={'fontsize': 8, 'color': 'black'}, 
                pctdistance=0.8,
                colors=colors)
        ax1.set_title(f"POS tagging in {self.name_text1.title()} by\n{self.author1}", fontsize=16)

        ax2.pie(values2,
                labels=labels,
                autopct='%1.1f%%',
                textprops={'fontsize': 8, 'color': 'black'},
                pctdistance=0.8,
                colors=colors)
        ax2.set_title(f"POS tagging in {self.name_text2.title()} by\n{self.author2}", fontsize=16)
        plt.show()