from fpdf import FPDF

class PDFReport(FPDF):
    pass

def create_pdf_report(patient_data, risk_data, ldl_history):
    pdf = PDFReport()
    return pdf.output(dest='S').encode('latin1')