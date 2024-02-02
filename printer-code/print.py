import cups

def print_pdf(file_path, printer_name, job_title="Print Job"):
    conn = cups.Connection()

    # Get the printer attributes, including the default options
    printer_info = conn.getPrinterAttributes(printer_name)

    # Set print options, in this case, A4 paper size
    print_options = {
        "media": "A4",
        # Add more options as needed, for example, duplexing, color mode, etc.
    }

    # Submit the print job
    job_id = conn.printFile(printer_name, file_path, job_title, print_options)

    print(f"Print job submitted successfully. Job ID: {job_id}")

if __name__ == "__main__":
    pdf_file_path = "example.pdf"
    printer_name = "Your_Printer_Name"  # Replace with your actual printer name
    print_title = "Print Job Title"  # Optional, replace with your desired job title

    print_pdf(pdf_file_path, printer_name, print_title)