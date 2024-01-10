import pyttsx3,PyPDF2

#insert the name of the pdf file
pdfreader = PyPDF2.PdfReader(open('nameofyourfile.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

    
#insert the name of the mp3 file
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()