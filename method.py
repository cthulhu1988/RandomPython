def main():
    # open appropriate files for reading/writing
    input_handle = open("mail.dat","r")
    output_file = open("addresses.dat","w")
    # priming read
    line = input_handle.readline()
    
    # start loop
    while line != '':
        tokens = line.split()
        line = input_handle.readline()
        for word in tokens:
            if "@" in word:
                cleaned = clean_address(word)
                output_file.write(cleaned+"\n")

    input_handle.close()
    output_file.close()

# function strips email addresses of excess chars.
def clean_address(word):
    word = word.strip()
    word = word.rstrip(",>")# I know stripping these was not specified
    word = word.lstrip("<")# but they bothered me. 
    return word

# invoke main   
main()
