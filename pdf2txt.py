import os
import re
import pymupdf4llm
from PIL import Image
from pytesseract import image_to_string

class class_pdf2text():

    def convert_pdf_to_text(self, path):
        try:
            return pymupdf4llm.to_markdown(path)
        except:
            print (f"Text extraction not allowed for {path}. Falling back to OCR.")
            # Implement OCR functionality here if needed
            image = Image.open(path)
            return image_to_string(image, lang='eng', config='--psm 6')

    def clean_text(self, text):
        if not isinstance(text, str):
            return ''
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove page numbers
        text = re.sub(r'\n\s*\d+\s*\n', '\n', text, flags=re.MULTILINE)
        # Remove headers and footers (adjust as needed)
        text = re.sub(r'^.{0,50}$', '', text, flags=re.MULTILINE)
        return text.strip()

    def convert_pdfs_to_markdown(self, input_dir, output_file):
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
    pdf2text.convert_pdfs_to_markdown(input_dir, output_file)
    print(f"Conversion complete. Output saved to {output_file}")