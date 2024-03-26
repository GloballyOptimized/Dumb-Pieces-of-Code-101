from PyPDF2 import PdfReader
from docx import Document
import os 

#...........................................................................................................
cv_directory_path = 'D:\\abc\\xyz' #Replace and Insert your path here 

#...........................................................................................................
keyword = ['Django','HTML','CSS','Selenium']  # Enter your keywods here ...
keywords = {} 
for i in keywords:
    keywords[i] = i
#............................................................................................................

def filter(file,final,keywords:dict,target = 70): # the function takes in different mentioned parameters & sortes the CV to respective folder
    counter = 0 
    for word in final: # iterate over the extracted text to filter out keywords 
        if word in keywords:
            counter+=1  # counting total keywords
            keywords.pop(word) # removing the existing found keyword to avoid duplication 

    percentage = (counter*100)/len(keyword)  # counting CV percentage match to keywords 
    base_location = os.path.join(cv_directory_path,file) # inital location of all CV's

    if percentage >= target: 
        qualified_path = 'D:\\abc\Qualified' # path to qualified resume folder 
        final_qualified_path = os.path.join(qualified_path,file)
        os.rename(base_location,final_qualified_path) # moving file from exsiting to desired location 

    else:
        disqualified_path = 'D:\\abc\Disqualified'
        final_disqualified_path = os.path.join(disqualified_path,file)
        os.rename(base_location,final_disqualified_path)

#.............................................................................................................

for file in os.listdir(cv_directory_path):  # iteratijng over all the CV's in the folder 
    if file.endswith('docx'):  # this code filters DOCX files and reads the data to filter ... 
        docx_file_path = str(os.path.join(cv_directory_path,file))
        document = Document(docx_file_path)
        final_docx = []
        for para in document.paragraphs:
            final_docx.append(para.text)

        filter(file,final_docx,keywords) # filter if the final output qualifies for CV match
    #.........................................................................................................

    elif file.endswith('pdf'): # this code filters PDF files and reads the data to filter ... 
        pdf_file_path = os.path.join(cv_directory_path,file)
        cv_pdf = open(pdf_file_path,mode='rb')
        pdf = PdfReader(cv_pdf)
        number_of_pages = len(pdf.pages)
        i = 0 
        final_pdf = []
        while i < number_of_pages:
            page = pdf.pages[i]
            final_pdf.append((page.extract_text()))
            i+=1

        filter(file,final_pdf,keywords) # filter if the final output qualifies for CV match

#...........................................................................................................