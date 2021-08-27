def removeAccents(input_text):
    # Convert raw UNICODE to polish chars
    input_text = input_text.encode('raw_unicode_escape').decode('utf-8')
    strange='ąćęłńóśźżĄĆĘŁŃÓŚŹŻ' 
    ascii_replacements='acelnoszzACELNOSZZ'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)
#