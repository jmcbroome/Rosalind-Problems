#Jakob McBroome
#BME 205

class wordCounter:
    '''Class for counting word numbers in a given string, with space as separator by default. 
    Steps are 
        1. slice it into a list of strings
        2. count the number of occurences of each word in the list
        3. then generate a dictionary associating unique words and their count number.
    There is one primary method. Main() calls the method and and prints the output.'''
    def __init__(self, string, sep=" "):
        self.list = string.split(sep)
        #step 1- split the string
        self.word_dict = {}
        #initialize a dictionary attribute for direct reference after building
    def __unique_words__(self):
        return set(self.list)
        #converting the list to a set object removes duplicates
    def create_count_dict(self):
        self.word_dict = dict.fromkeys(self.unique_words())
        #create a dictionary of keys with None values out of the unique words set, then set each associated value to their count in the full list
        for word in self.unique_words():
            self.word_dict[word] = self.list.count(word)

def main(input_string):
    output = wordCounter(input_string)
    output.create_count_dict()
    print(output.word_dict)
    for key, value in output.word_dict.items():
        print(key, end = ' ')
        print(value)

main("We tried list and we tried dicts also we tried Zen")
main("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")
