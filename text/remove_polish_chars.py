def removeAccents(input_text):
    strange='ąćęłńóśź' 
    ascii_replacements='acelnosz'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)
#