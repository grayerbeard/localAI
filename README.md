# localAI
Python scripts to use for AI/LLM related tasks on my Laptop

# Convert a Batch of PDF Files in a Directory into a Single Text File for Feeding to an LLM.

The pdf2txt.py can be used to convert a whole director full of files into a single markdown file. This is the first version of a PDF to text script that worked OK.

psdf2text.py was then modified by first copying the text into an Obsidian Note requesting Anthropic Claude 3.5 Sonnet to make changes. See 
[Building make4LLM.py.md](Building%20make4LLM.py.md)

I have tried using the text file output in two different ways.
I am using the SystemSculpt AI plug in in Obsidian.

* Just put a question at the end and then use a hot key to send whole file to AI
* Add in the file using the "Context Files +" button in chat then enter the question.

  In both cases its important to select and LLM able to take in such a large prompt.
  Note that the python code adds what is iin effect a prompt template at the start of the file.

For example I had a batch of Insurance documents for a charities insurance and some pdf files with guidance on what sort of insurance that type of charity should have.

The total size of the original pdf files was 6.8MBytes and that gave a 550KB md text file file fed to Googlle Gemini Pro 1.5 using the systemsculpt AI plug in for Obsidian and then clicking the "Generate" hot key.
