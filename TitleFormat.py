def get_file_title(text):
    etext = ""
    for znak in text:
        if znak.isalnum() or znak.isspace():
            etext += znak
    exit = etext[:20] if len(etext) > 20 else etext
    return("C:\\\\Users\\\\Piotr\\\\Downloads\\\\"+exit+".mp3")

