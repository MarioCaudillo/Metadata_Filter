from tika import parser

def extract_metadata_tika(file_path):
    parsed = parser.from_file(file_path)
    return parsed["metadata"]

docx_file = "documento.docx"
xlsx_file = "documento.xlsx"
pdf_file = "documento.pdf"


print("Metadatos de DOCX:")
print(extract_metadata_tika(docx_file))

print("\nMetadatos de XLSX:")
print(extract_metadata_tika(xlsx_file))

print("\nMetadatos de PDF:")
print(extract_metadata_tika(pdf_file))
