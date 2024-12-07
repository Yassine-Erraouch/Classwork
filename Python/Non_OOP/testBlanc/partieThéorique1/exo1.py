
def analyze_text (s):
    #replace spaces with #
    def replaceSpacesWithHash (s):
        return s.replace(" ", "#")
    #get word count
    def wordCount (s):
        return len(s.split())

    #get most repeated word
    def mostRepeatedWord (s):
        words = s.split()
        return max(words, key=words.count)  


    print(f'there are {wordCount(s)} words in the sentence')
    print(f'the most repeated word is:  {mostRepeatedWord(s)}')
    print(f'the sentence without spaces is:  {replaceSpacesWithHash(s)}')
    
s = input("Entrez une phrase: ")
analyze_text(s)
