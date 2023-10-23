'''
Project 4 - Text Analysis - Fall 2020
Author: Alex Vidal alexv20

The program will read and analyze file of English text and output the results

I have neither given or received unauthorized assistance on this assignment.
Signed:  Alex Vidal
'''

def read_text(file_name):
    raw_text=''
    with open(file_name) as file:
        raw_text=str(file.read())
    return raw_text

def clean_text(raw_text):
    remove=[',',';',':','.','?','!','[',']','*','(',')','-','\'','\"']
    clean_text=raw_text.lower()
    for x in clean_text:
        if x in remove:
            clean_text =clean_text.replace(x,'')
    return clean_text

def get_word_frequencies(cleaned_text):
    word_freq={}
    for word in cleaned_text:
        if word not in word_freq:
            word_freq[word] =1
        else:
            word_freq[word]+=1
    return word_freq

def count_syllables(word):
    ''' Estimates and returns the number of syllables in
    the specified word. '''
    syllables = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            syllables += 1
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le'):
        syllables += 1
    if syllables == 0: 
        syllables = 1
    return syllables

def count_all_syllables(cleaned_text):
    count=0
    for x in cleaned_text:
        count+=count_syllables(x)
    return count

def get_flesch_reading_score(raw_text):
    clean =clean_text(raw_text)
    score = 206.835-1.015*float(len(clean)/count_sentences(raw_text))-84.6*float(count_all_syllables(clean)/len(clean))
    return score

def school_level_score(flesch_score):
    if flesch_score>=90:
        return '5th'
    if flesch_score<90 and flesch_score>=80:
        return '6th'
    if flesch_score<80 and flesch_score>=70:
        return '7th'
    if flesch_score<70 and flesch_score>=60:
        return '8th and 9th'
    if flesch_score<60 and flesch_score>=50:
        return '10th to 12th'
    if flesch_score<50 and flesch_score>=30:
        return 'College'
    if flesch_score<30 and flesch_score>=10:
        return 'College Graduate'
    else:
        return 'Professional'
    

def count_sentences(raw_text):
    punct=['.','?','!']
    count=0
    for x in punct:
        count+=raw_text.count(x)
    return count

def dict_sort(dictionary):
    sorted_dict=sorted(dictionary.items(), key = lambda kv:(kv[1]), reverse=True)
    return sorted_dict
    
    

def main():
   file_name=input('Name of file to analyze? ')
   raw_text = read_text(file_name)
   sentences=count_sentences(raw_text)
   print('\nNumber of sentences: '+str(sentences))
   word_list = clean_text(raw_text).split()
   print('Number of words: '+str(len(word_list)))
   word_dict= get_word_frequencies(word_list)
   all_syll=count_all_syllables(word_list)
   print('Number of unique words: '+str(len(word_dict)))
   print('Average words per sentence: '+str(round(len(word_list)/sentences,1)))
   print('Average syllables per word: '+str(round(all_syll/len(word_list),1)))
   score = get_flesch_reading_score(raw_text)
   print('\nReading-ease score: '+str(round(score,1)))
   print('U.S. grade level: '+str(school_level_score(score)))
   print('The 20 most common words:')
   sorted_dict =dict_sort(word_dict)
   for x,i in zip(sorted_dict, range(20)):
       print(str(x[1])+' '+x[0])
    
   

if __name__ == '__main__':
    main()