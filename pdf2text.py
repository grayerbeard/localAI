'''This program does the following:

1. It uses `pdfminer` to extract text from PDF files.
2. It includes a `clean_text` function to remove extra whitespace, page numbers, and potential headers/footers. You may need to adjust this function based on the specific format of your documents.
3. It processes all PDF files in the specified directory, converts them to text, cleans the text, and writes the content to a single Markdown file.
4. Each document's content is preceded by a Markdown header with the filename and followed by a horizontal rule for separation.

To use this program:

1. Install the required library: `pip install pdfminer.six`
2. Replace `'path/to/your/pdf/directory'` with the actual path to your directory containing PDF files.
3. Run the script.

This approach should help in extracting mostly useful text content from your PDF files. However, please note:

- The effectiveness of text extraction can vary depending on how the PDFs were created. Some PDFs might not extract well if they're image-based or have complex layouts.
- You might need to fine-tune the `clean_text` function based on the specific format of your documents.
- Large files might take some time to process.

After running this script, you'll have a single Markdown file containing the text content from all your PDFs, which you can then feed into an AI model with a large context window for analysis.

Changes were made based on these recomende changes:
Based on the error message you received, it appears that some of the PDF documents you're trying to process have restrictions on text extraction. This is a common security feature used in some PDFs to prevent unauthorized copying or extraction of content. Unfortunately, there's no straightforward way to bypass this restriction while respecting copyright and legal considerations. However, here are a few approaches you could consider:

1. OCR (Optical Character Recognition):
   Instead of directly extracting text, you could convert the PDF to images and then use OCR to extract the text. This method works around the text extraction restriction but may introduce some inaccuracies.

   You could use a library like `pytesseract` along with `pdf2image` to implement this. Here's a basic example:

   ```python
   from pdf2image import convert_from_path
   import pytesseract
   from PIL import Image
   import io

   def pdf_to_text_ocr(pdf_path):
       images = convert_from_path(pdf_path)
       text = ""
       for image in images:
           text += pytesseract.image_to_string(image)
       return text

   # Replace the convert_pdf_to_text method with this new method
   ```

2. Manual review:
   For the documents that can't be processed automatically, you might need to manually review and input the relevant information.

3. Request unprotected versions:
   If these are your own insurance documents, you could contact the insurance company and request versions of the documents without copy protection.

4. Use commercial PDF processing tools:
   Some commercial PDF processing tools claim to be able to remove copy protection from PDFs. However, the legality and effectiveness of these tools can vary, so use caution with this approach.

5. Hybrid approach:
   Modify your script to use the text extraction method for unprotected PDFs and the OCR method for protected ones. This way, you get the best of both worlds - accurate extraction where possible, and a fallback for protected documents.

   Here's how you might modify your `convert_pdf_to_text` method:

   ```python
   def convert_pdf_to_text(self, path):
       try:
           # Try the original method first
           text = self.original_convert_pdf_to_text(path)
       except PDFTextExtractionNotAllowed:
           # If text extraction is not allowed, fall back to OCR
           print(f"Text extraction not allowed for {path}. Falling back to OCR.")
           text = self.pdf_to_text_ocr(path)
       return text

   def original_convert_pdf_to_text(self, path):
       # Your original conversion method here
       ...

   def pdf_to_text_ocr(self, pdf_path):
       # OCR method as described above
       ...
   ```

Remember that while OCR can help you extract text from protected PDFs, it may not be as accurate as direct text extraction, and it might not preserve formatting or layout information. Also, ensure that you have the right to extract and use the content from these documents, even if they're your own insurance policies.



'''

import os
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

from pdf2image import convert_from_path
import pytesseract
from PIL import Image

class class_pdf2text():
    '''def __init__():
     nothing needed here yet'''

    def direct_convert_pdf_to_text(self,path):
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

    def pdf_to_text_ocr(self,pdf_path):
        images = convert_from_path(pdf_path)
        text = ""
        for image in images:
           text += pytesseract.image_to_string(image)
        return text
    
    def convert_pdf_to_text(self, path):
        try:
            # Try the original method first
            text = self.direct_convert_pdf_to_text(path)
        except:
            # If text extraction is not allowed, fall back to OCR
            print(f"Text extraction not allowed for {path}. Falling back to OCR.")
            text = self.pdf_to_text_ocr(path)
        return text
    


    def clean_text(self,text):
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove page numbers
        text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
        # Remove headers and footers (adjust as needed)
        text = re.sub(r'^.{0,50}$', '', text, flags=re.MULTILINE)
        return text.strip()

    def convert_pdfs_to_markdown(self,input_dir, output_file):
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filename in os.listdir(input_dir):
                if filename.endswith('.pdf'):
                    filepath = os.path.join(input_dir, filename)
                    print(f"Processing {filename}...")
                    
                    # Extract text from PDF
                    raw_text = self.convert_pdf_to_text(filepath)
                    
                    # Clean the extracted text
                    cleaned_text = self.clean_text(raw_text)
                    
                    # Write to Markdown file
                    outfile.write(f"# {filename}\n\n")
                    outfile.write(cleaned_text)
                    outfile.write("\n\n---\n\n")  # Separator between documents
       

if __name__ == '__main__':
        input_dir = "input"
        output_file = 'output.md'
        pdf2text = class_pdf2text()
        pdf2text.convert_pdfs_to_markdown(input_dir,output_file)
        print(f"Conversion complete. Output saved to {output_file}")

