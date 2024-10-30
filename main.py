from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
data = pd.read_csv("topics.csv")

def add_footer(height):
    pdf.ln(height)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R",ln=1)

def add_lines():
    for i in range(20,298,10):
        pdf.line(10,i,200,i)

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
    add_footer(265)
    add_lines()

    for page in range(row["Pages"]-1):
        pdf.add_page()
        add_footer(277)
        add_lines()

pdf.output("output.pdf")