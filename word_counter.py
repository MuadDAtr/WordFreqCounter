from modules import char_replace, count_freq, freq_dict, sort_dict

def main():
    text_init = input('Please insert the text: ')
    print("\n")
    print(text_init)

    text_l= text_init.lower()

    text = char_replace(text_l)

    wordlist = text.split()

    count_freq(wordlist)
    print("...............")
    print("\n")
    print("\n")
    print("This is the frequency of words in the text: \n")

    freqdict = freq_dict(wordlist)

    print(sort_dict(freqdict))

if __name__ == "__main__":
    main()