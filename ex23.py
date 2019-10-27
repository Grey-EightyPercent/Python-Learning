# 2019/10/26
# What does that mean?
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline () # Read encoded content

    if line: # What is this ?
        print_line(line, encoding, errors) # Run "print_line" function, assigning it line/utf-8/errors
        return main(language_file, encoding, errors) # Return the result.

def print_line(line, encoding, errors):
    next_lang = line.strip() # WHat does .strip mean?
    raw_bytes = next_lang.encode(encoding, errors=errors) #define raw_bytes,encoded
    cooked_string = raw_bytes.decode(encoding, errors=errors) #define cooked_string, decoded

    print(raw_bytes, "<===>", cooked_string)


# Use open() to open the file and encode it with utf-8
# Assigning the conten above to the variable.
languages = open("languages.txt", encoding="utf-8") # the usage of open ()

# Run the "main" function, assign 3 args: opened and encoded languages.txt/utf-8/strict
main(languages, input_encoding, error)  # What does main mean?
