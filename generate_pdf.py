# Script to generate pdf from md file.

from md2pdf.core import md2pdf

pdf = "AI-Concept-paper-Nepal-en.pdf"
md_file = "./AI-paper-en.md"

md2pdf(pdf_file_path=pdf,
       md_file_path=md_file,
       base_url="./"
       )
