import PyPDF2
import sys

def extract_pdf_text(pdf_path, output_path=None):
    """
    Extract text from a PDF file and either print it or save it to a file.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_path (str, optional): Path to save the extracted text. If None, prints to console.
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get the number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Processing {num_pages} pages...")
            
            # Extract text from all pages
            text = ""
            for page_num in range(num_pages):
                # Get the page
                page = pdf_reader.pages[page_num]
                # Extract text from page
                text += page.extract_text() + "\n\n"
            
            # Either save to file or print to console
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(text)
                print(f"Text has been saved to {output_path}")
            else:
                print(text)
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_reader.py <pdf_path> [output_path]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    extract_pdf_text(pdf_path, output_path) 