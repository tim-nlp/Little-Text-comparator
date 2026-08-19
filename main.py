from text_reader import TextReader
from get_api import TextReaderAPI
from analyse import Analyser
from visualisation import Visualisation
from pathlib import Path

print("""
▀▛▘     ▐                         ▐        
 ▌▞▀▖▚▗▘▜▀  ▞▀▖▞▀▖▛▚▀▖▛▀▖▝▀▖▙▀▖▝▀▖▜▀ ▞▀▖▙▀▖
 ▌▛▀ ▗▚ ▐ ▖ ▌ ▖▌ ▌▌▐ ▌▙▄▘▞▀▌▌  ▞▀▌▐ ▖▌ ▌▌  
 ▘▝▀▘▘ ▘ ▀  ▝▀ ▝▀ ▘▝ ▘▌  ▝▀▘▘  ▝▀▘ ▀ ▝▀ ▘  
""")


class WorkWithTexts:
    """Does evertyhing when given texts by user"""
    def __init__(self):
        pass


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

        return self.text1, self.text2


    def visualisations(self, analyse1, analyse2):
        """Create data visualisations"""
        try:
            visualisation = Visualisation(analyse1, analyse2,
                                        self.name_text1, self.name_text2)

            visualisation.compare_values()
            visualisation.make_table()
            visualisation.create_pies()
        except AttributeError as e:
            print(f"Visualisation error: {e}")
        else:
            print("\nDone!")


class WorkWithAPITexts:
    """Does everything with APIs texts"""
    def __init__(self):
        pass

    def get_api(self):
        """Gets APIs at Gutendex"""
        self.first_text = TextReaderAPI()
        self.second_text = TextReaderAPI()

        # Gets two differents APIs
        while True:
            self.first_text.get_id()
            self.second_text.get_id()
            if self.first_text != self.second_text:
                break
            else:
               continue


    def get_api_texts(self):
        # Reading texts
        self.text1 = self.first_text.get_text()
        self.text2 = self.second_text.get_text()

        print("\nReading texts...")


    def get_api_books_infos(self):
        """Gets APIs book's informations"""
        self.name_text1 = self.first_text.get_book_title()
        self.author1 = self.first_text.get_book_author()

        self.name_text2 = self.second_text.get_book_title()
        self.author2 = self.second_text.get_book_author()


    def visualisations_api(self, analyse1, analyse2):
        try:
            visualisation = Visualisation(analyse1, analyse2,
                                        self.name_text1, self.name_text2,
                                        self.author1, self.author2)

            visualisation.compare_values()
            visualisation.make_table_api()
            visualisation.create_pies_api()
        except AttributeError as e:
            print(f"Visualisation error: {e}")
        else:
            print("\nDone!")


class DoTheAnalyse:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2


    def analyse_texts(self):
        """Analyses both texts"""
        # Analyse text 1
        try:
            self.analyse1 = Analyser(self.text1)
            self.analyse1.analyse()
        except (ValueError, AttributeError) as e:
            print(f"Analysis error: {e}")
        else:
            pass

        # Analyse text 2
        try:
            self.analyse2 = Analyser(self.text2)
            self.analyse2.analyse()
        except (ValueError, AttributeError) as e:
            print(f"Analysis error: {e}")
        else:
            pass

        print("\nStarting analysis...")

        return self.analyse1, self.analyse2



class UserInterface:
    def __init__(self):
        pass

    def greet(self):
        """Greets user."""
        greet = "Welocome to this little text comparator !"
        print(greet)


    def input_user(self):
        """Ask for user input"""
        while True:
            awnser = input("\nType 'h' for help, 's' to start, and 'q' to quit. ").strip().lower()
            print(awnser)

            help_user = """
    Texts:
Please place texts in the 'Texts' folder as .txt files.
After pressing `s` to start, please enter `custom` and follow the instructions. 
When asked, enter the exact filename. For example: `Steam, Its Generation and Use` or `Computers-the machines we think with` without the `.txt` extension.

    APIS:
After pressing `s` to start, please enter `random` to work with random texts.
This part of the program sends two API requests to Gutendex.com, and then gets two random texts to work with. 
Some texts may not contain all the information required by the program, which can cause an error.
For example, a text may have no author or may be in an unsupported format. 
            """

            if awnser == 'h':
                print(help_user)
            elif awnser == 'q':
                print("\nThanks for using me!")
                break

            elif awnser == 's':
                api_or_not = input("""
Do you want to use your own texts or random ones? [random/custom] """).strip().lower()

                if api_or_not == "custom":
                # Start program with texts given by user
                    texts = WorkWithTexts()

                    texts.name_text1 = input("\nEnter name text 1: ").strip()
                    texts.name_text2 = input("Enter name text 2: ").strip()

                    texts.read_texts()

                    analyse = DoTheAnalyse(texts.text1, texts.text2)
                    analyse.analyse_texts()

                    texts.visualisations(analyse.analyse1, analyse.analyse2)

                elif api_or_not == "random":
                # Start program with APIs requests
                    texts = WorkWithAPITexts()

                    texts.get_api()
                    texts.get_api_texts()
                    texts.get_api_books_infos()

                    analyse = DoTheAnalyse(texts.text1, texts.text2)
                    analyse.analyse_texts()

                    texts.visualisations_api(analyse.analyse1, analyse.analyse2)

                else:
                    print("Please enter a valid input.")

            else:
                print("\nPlease enter a valid input.")


user = UserInterface()
user.greet()
user.input_user()
