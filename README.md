# localAI
Python code to use with AI on my Laptop

# Convert a Batch of PDF Files in a Directory into a Single Text File for Feeding to an LLM.

The pdf2txt.py can be used to convert a whole director full of files into a single markdown file. This is the first version of a PDF to text script that worked OK.

psdf2text.py was then modified by first copying the text into an Obsidian Note requesting Anthropic Claude 3.5 Sonnet to make changes. See 
[Building make4LLM.py.md](Building%20make4LLM.py.md)

This can be fed to an AI as part of a single prompt with the question added at the end of the file.

For example I had a batch of Insurance documents for a charities insurance and some pdf files with guidance on what sort of insurance that type of charity should have.

So at the end of the note containing the converted pdf files I added a brief explanation of the context and asking for a report comparing the insurance policy details with the guidance documents.

The total size of the original pdf files was 6.8MBytes and that gave a 550KB md text file file fed to Googlle Gemini Pro 1.5 using the systemsculpt AI plug in for Obsidian and then clicking the "Generate" hot key.

Then the required report text was copied to a new note and output as a PDF file using Obsidian's built in 
