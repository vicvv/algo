import unittest
import threading
import re

for thread in threading.enumerate(): 
    print(thread.name)

class WordCounter:
    def __init__(self):
        #aquaring datastracture
        self.lock = threading.Lock()
        self.words_count = {}
        
    def process_text(self, text):
        words = text.split(" ")
        for word in words:
            self._increment_words_count(word)

    def get_word_count(self, word):
        #count = len(re.findall(r'\b'+ word + r'\b', self.text))
        self.lock.acquire()
        count = self.words_count.get(word,0)
        self.lock.release()
        return count

    def _increment_words_count(self,word):
        self.lock.acquire()
        self.words_count[word]= self.words_count.get(word, 0) + 1
        self.lock.release()




TEST_TEXT_1 = """
The Ares Program. Mankind reaching out to Mars to send people 
to another planet for the very first time and expand the horizons 
of humanity blah, blah, blah. The Ares 1 crew did their thing and 
came back heroes. They got the parades and fame and love of the world.

Ares 2 did the same thing, in a different location on Mars. They got 
a firm handshake and a hot cup of coffee when they got home.

Ares 3. Well, that was my mission. Okay, not mine per se. Commander 
Lewis was in charge. I was just one of her crew. Actually, I was the 
very lowest ranked member of the crew. I would only be “in command” of 
the mission if I were the only remaining person.
""".strip()

TEST_TEXT_2 = " ".join(["dog"] * 50000)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        wc = WordCounter()
        wc.process_text("the cat is in the bag")
        self.assertEqual(2, wc.get_word_count("the"))
        self.assertEqual(1, wc.get_word_count("bag"))
        self.assertEqual(0, wc.get_word_count("dog"))

    def test_case_2(self):
        wc = WordCounter()
        wc.process_text(TEST_TEXT_1)
        self.assertEqual(8, wc.get_word_count("the"))
        self.assertEqual(4, wc.get_word_count("I"))
        self.assertEqual(5, wc.get_word_count("and"))

    def test_case_3(self):
        wc = WordCounter()

        threads = []
        for _ in range(10):
            thread = threading.Thread(target=wc.process_text, args=(TEST_TEXT_1,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(80, wc.get_word_count("the"))
        self.assertEqual(40, wc.get_word_count("I"))
        self.assertEqual(50, wc.get_word_count("and"))

    def test_case_4(self):
        wc = WordCounter()

        threads = []
        for _ in range(4):
            thread = threading.Thread(target=wc.process_text, args=(TEST_TEXT_2,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(4 * 50000, wc.get_word_count("dog"))

if __name__ == '__main__':
    unittest.main()
