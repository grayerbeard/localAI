import pymupdf4llm
md_text = pymupdf4llm.to_markdown("input/Guidance - Trustee-Indemnity-Insurance doc by UKMSA.pdf")

# write markdown string to some file
output = open("out-markdown.md", "w")
output.write(md_text)
output.close()
print(f"Converted text {md_text}")