import cups

def list_printers():
    conn = cups.Connection()
    printers = conn.getPrinters()
    
    print("List of Printers:")
    for printer in printers:
        print(printer, printers[printer]["device-uri"])

if __name__ == "__main__":
    list_printers()
