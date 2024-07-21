# localAI 

This repository contains Python scripts designed to help you use AI and Large Language Models (LLMs) directly on your laptop, specifically within the Obsidian note-taking app.

## Converting PDFs for AI Analysis in Obsidian

One of the challenges of using LLMs is providing them with enough context to answer your questions effectively. This script addresses this by allowing you to convert a batch of PDF files into a single, AI-ready text file. This file can then be used with the SystemSculpt AI plugin in Obsidian to get insightful answers from your documents.

### How it Works

1. **PDF to Text Conversion:** The script uses the `pymupdf4llm` library to extract text from your PDF files. If this fails, it uses Optical Character Recognition (OCR) as a backup, ensuring all content is captured.

2. **Text Cleaning:**  The extracted text often contains unwanted elements like extra spaces, page numbers, and headers/footers. The script cleans this up, making the text more suitable for AI processing.

3. **Combining into a Single File:** All the cleaned text from your PDFs is combined into a single Markdown file (.md). This file is structured to work seamlessly with the SystemSculpt AI plugin.

4. **Ready for SystemSculpt:** The generated Markdown file includes specific sections that SystemSculpt understands, such as "IDENTITY and PURPOSE," "OUTPUT INSTRUCTIONS," and "Context Material." This helps guide the AI and ensures you get the desired output.

### Using the Script

1. **Installation:** Make sure you have Python installed on your system. You'll also need to install the required libraries. You can do this by running `pip install pymupdf4llm pytesseract pillow`.

2. **Obsidian Vault Setup:** 
    - Ensure you have the SystemSculpt AI plugin installed and configured in your Obsidian vault.
    - The script assumes a specific folder structure within your vault. You will be prompted to provide the location of your Obsidian vault and the names of your attachments folder and the folder containing your PDFs.  The script will create a file called `context.md` within your notes folder.

3. **Running the Script:** 
    - Place all the PDF files you want to analyze in the designated PDF folder within your Obsidian vault.
    - Run the `pdf2text.py` script. 
    - The script will prompt you for some information about your Obsidian vault structure. This helps it find your PDFs and save the output in the correct location.

4. **Using with SystemSculpt:**
    - Open the generated `context.md` file in Obsidian.
    - You'll see your PDF content under the "Context Material" section.
    - Simply type your question at the end of the file under the "Question" heading.
    - Use the SystemSculpt hotkey to send the entire file to the AI.
    - ALTERNATIVLEY you can add the context.md file as context in a chat. Click the "C" button at the bottom of the screen then click the "Context Files +" button and enter "context".  Then enter your questions.

### Benefits

- **Easy Context Loading:**  No more manually copying and pasting from multiple PDFs.
- **Improved AI Accuracy:**  Clean and structured text helps the AI understand your documents better.
- **Seamless Obsidian Integration:** Designed to work directly within your Obsidian workflow.

This script simplifies the process of preparing your PDF documents for analysis with AI, making it easier than ever to extract valuable insights from your data. 
