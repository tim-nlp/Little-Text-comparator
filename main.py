from text_reader import TextReader
from analyse import Analyser
from visualisation import Visualisation
from pathlib import Path

print("""
▀▛▘     ▐                         ▐        
 ▌▞▀▖▚▗▘▜▀  ▞▀▖▞▀▖▛▚▀▖▛▀▖▝▀▖▙▀▖▝▀▖▜▀ ▞▀▖▙▀▖
 ▌▛▀ ▗▚ ▐ ▖ ▌ ▖▌ ▌▌▐ ▌▙▄▘▞▀▌▌  ▞▀▌▐ ▖▌ ▌▌  
 ▘▝▀▘▘ ▘ ▀  ▝▀ ▝▀ ▘▝ ▘▌  ▝▀▘▘  ▝▀▘ ▀ ▝▀ ▘  
""")


class UserInterface:
    def __init__(self):
        pass

    def greet(self):
        """Greets user."""
        greet = "Welocome to this little text comparator !"
        print(greet)


    def read_texts(self):
        """Read both texts"""
        # Reading text 1
        try:
            reader1 = TextReader(Path(f"Texts/{self.name_text1}.txt"))
            self.text1 = reader1.read_text()
        except FileNotFoundError:
            print(f"File not found : {self.name_text1}.txt")
            pass
        else:
            print(f"\nReading {self.name_text1}...")

        # Reading text 2
        try:
            reader2 = TextReader(Path(f"Texts/{self.name_text2}.txt"))
            self.text2 = reader2.read_text()
        except FileNotFoundError:
            print(f"File not found : {self.name_text2}.txt")
            pass
        else:
            print(f"Reading {self.name_text2}...")


    def analyse_texts(self):
        """Analyses both texts"""
        # Analyse text 1
        try:
            self.analyse1 = Analyser(self.text1)
        except (ValueError, AttributeError) as e:
            print(f"Analysis error: {e}")
        else:
            self.analyse1.pre_traitement()
            self.analyse1.number_of_words()
            self.analyse1.letters_per_words()
            self.analyse1.number_of_sentences()
            self.analyse1.words_per_sentences()
            self.analyse1.lexical_diversity()
            self.analyse1.pos_tagging()

        # Analyse text 2
        try:
            self.analyse2 = Analyser(self.text2)
        except (ValueError, AttributeError) as e:
            print(f"Analysis error: {e}")
        else:
            self.analyse2.pre_traitement()
            self.analyse2.number_of_words()
            self.analyse2.letters_per_words()
            self.analyse2.number_of_sentences()
            self.analyse2.words_per_sentences()
            self.analyse2.lexical_diversity()
            self.analyse2.pos_tagging()

            print("\nStarting analysis...")


    def visualisations(self):
        """Create data visualisations"""
        try:
            visualisation = Visualisation(self.analyse1, self.analyse2,
                                        self.name_text1, self.name_text2)

            visualisation.compare_values()
            visualisation.make_table()
            visualisation.create_pies()
        except AttributeError as e:
            print(f"Visualisation error: {e}")
        else:
            print("\nDone!")


    def input_user(self):
        """Ask for user input"""
        while True:
            awnser = input("\nType 'h' for help, 's' to start, and 'q' to quit. ").strip().lower()
            print(awnser)

            help_user = """
Please place texts in the 'Texts' folder as .txt files.
When asked, enter the exact filename. Ex: "Steam, Its Generation and Use" or "Computers-the machines we think with".
The texts must not be empty or corrupted.
            """

            if awnser == 'h':
                print(help_user)
            elif awnser == 'q':
                print("\nThanks for using me!")
                break

            elif awnser == 's':
            # Start program
                self.name_text1 = input("\nEnter name text 1: ").strip()
                self.name_text2 = input("Enter name text 2: ").strip()

                self.read_texts()
                self.analyse_texts()
                self.visualisations()

            else:
                print("\nPlease enter a valid input.")


user = UserInterface()
user.greet()
user.input_user()
