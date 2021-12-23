
def char_replace(te_xt):
    return te_xt.replace(",", " ").replace("."," ").replace(";", " ").replace("?", " ").replace("!"," ")

def count_freq(wordlist):
    wordfreq = []
    for word in wordlist:
        wordfreq.append(wordlist.count(word))
    return wordfreq

def freq_dict(wordlist):
    wordfreq = [wordlist.count(pair) for pair in wordlist]
    return dict(list(zip(wordlist, wordfreq)))

def sort_dict(freqdict):
    dict_s = [(freqdict[key], key) for key in freqdict]
    dict_s.sort()
    dict_s.reverse()
    return dict_s