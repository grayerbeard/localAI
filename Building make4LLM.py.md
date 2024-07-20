Project::  local AI 
#python/obsidian

This is the note used to get "Anthropic Claude 3.5 Sonnet" to make "make4LLM.py" from "pdf2txt.py",  See  [Github - grayerbeard - localAI : github.com/grayerbeard/localAI)](https://github.com/grayerbeard/localAI)

# This is the tested pdf2txt.py script: 
```python
import os
import re
import pymupdf4llm
from io import BytesIO
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
                    outfile.write("\n\n---\n\n")  # Separator between documents

if __name__ == '__main__':
    input_dir = "input"
    output_file = 'output.md'
    pdf2text = class_pdf2text()
    pdf2text.convert_pdfs_to_markdown(input_dir, output_file)
    print(f"Conversion complete. Output saved to {output_file}")
```
## This is the prompt

The above is a python program that is working.  It is used to convert as set of PDF files in a directory into a single Text file that can be fed to an AI as part of a prompt to allow questions to be asked about the set of PDF documents.
The question ids put using the SystemSculpt AI plug in in Obsidian.
The procedure requires that the output of this program ends up as a note file in the obsidian vault.  The pdf file start out in a folder in the "attachments" folder of the obsidian vault.    e.g.  "D:\Obsidian Vaults\Second Brain\attachments\pdf_inputs" and the note output is put in  "D:\Obsidian Vaults\Second Brain\notes\ouput.md".
So to make this process as smooth as possible to code needs to be modified so that it asks for the location of the obsidian vault and the needed folders.
Please rewrite making the following changes.

1. Make it interactive so that it requests input of the following rather than requireing them to be added to the code;
	(a) "Input_dir" and 
	(b) "Output_file" 
	 (c) Vault Location
	 (d) Notes folder
2. Fully comment the code to explain it in details.

## Here is the result

Here's the modified and fully commented version of the code that incorporates the requested changes:

```python
import os
import re
import pymupdf4llm
from io import BytesIO
from PIL import Image
from pytesseract import image_to_string

class class_pdf2text():
    def convert_pdf_to_text(self, path):
        """
        Converts a PDF file to text using pymupdf4llm or OCR as fallback.
        
        Args:
            path (str): Path to the PDF file.
        
        Returns:
            str: Extracted text from the PDF.
        """
        try:
            # Attempt to extract text using pymupdf4llm
            return pymupdf4llm.to_markdown(path)
        except:
            print(f"Text extraction not allowed for {path}. Falling back to OCR.")
            # Use OCR as a fallback method
            image = Image.open(path)
            return image_to_string(image, lang='eng', config='--psm 6')

    def clean_text(self, text):
        """
        Cleans the extracted text by removing extra whitespace, page numbers, and headers/footers.
        
        Args:
            text (str): Raw text extracted from PDF.
        
        Returns:
            str: Cleaned text.
        """
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
        """
        Converts all PDF files in the input directory to a single Markdown file.
        
        Args:
            input_dir (str): Path to the directory containing PDF files.
            output_file (str): Path to the output Markdown file.
        """
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

def get_user_input():
    """
    Prompts the user for necessary input paths.
    
    Returns:
        tuple: Contains vault_location, input_dir, output_file, and notes_folder.
    """
    vault_location = input("Enter the location of your Obsidian vault: ")
    attachments_folder = input("Enter the name of your attachments folder (default: attachments): ") or "attachments"
    notes_folder = input("Enter the name of your notes folder (default: notes): ") or "notes"
    pdf_folder = input("Enter the name of the folder containing PDFs (default: pdf_inputs): ") or "pdf_inputs"
    
    input_dir = os.path.join(vault_location, attachments_folder, pdf_folder)
    output_file = os.path.join(vault_location, notes_folder, "output.md")
    
    return vault_location, input_dir, output_file, notes_folder

if __name__ == '__main__':
    # Get user input for paths
    vault_location, input_dir, output_file, notes_folder = get_user_input()
    
    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: The input directory {input_dir} does not exist.")
        exit(1)
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize the PDF to text converter
    pdf2text = class_pdf2text()
    
    # Convert PDFs to Markdown
    pdf2text.convert_pdfs_to_markdown(input_dir, output_file)
    
    print(f"Conversion complete. Output saved to {output_file}")
```

This modified version of the code includes the following changes and additions:

1. A new function `get_user_input()` has been added to interactively prompt the user for:
   a. The location of the Obsidian vault
   b. The name of the attachments folder (with a default value)
   c. The name of the notes folder (with a default value)
   d. The name of the folder containing PDFs (with a default value)

2. The `input_dir` and `output_file` paths are now constructed based on the user's input.

3. The code now checks if the input directory exists and creates the output directory if it doesn't exist.

4. Detailed comments have been added throughout the code to explain each function and significant code block.

5. The main execution flow has been updated to use the new `get_user_input()` function and perform necessary checks before proceeding with the conversion.

This version of the code provides a more user-friendly and flexible approach, allowing users to specify their Obsidian vault structure without modifying the code directly. It also includes error checking to ensure the input directory exists and creates the output directory if needed.