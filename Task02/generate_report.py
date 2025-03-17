import pandas as pd
from fpdf import FPDF

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Perform Data Analysis
total_sales = (df["Quantity"] * df["Price"]).sum()
top_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
total_quantity = df["Quantity"].sum()

# Define PDF class with header and footer
class PDF(FPDF):
    def header(self):
        # Add Company Logo
        self.image("logo.png", 10, 8, 30)  # (File, X, Y, Width)
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Sales Report", ln=True, align="C")
        self.ln(10)  # Line break

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Report Summary
pdf.cell(200, 10, "Summary of Sales Data", ln=True, align="C")
pdf.ln(10)
pdf.cell(200, 10, f"Total Sales: Rs. {total_sales}", ln=True)
pdf.cell(200, 10, f"Top Selling Product: {top_selling_product}", ln=True)
pdf.cell(200, 10, f"Total Quantity Sold: {total_quantity}", ln=True)
pdf.ln(10)  # Line break before table

# Table Headers
pdf.set_font("Arial", "B", 12)
col_widths = [40, 40, 40, 40]  # Width for each column
headers = ["Date", "Product", "Quantity", "Price"]
for col, width in zip(headers, col_widths):
    pdf.cell(width, 10, col, border=1, align="C")
pdf.ln()  # New line after headers

# Table Data (Loop through DataFrame rows)
pdf.set_font("Arial", size=12)
for _, row in df.iterrows():
    pdf.cell(col_widths[0], 10, row["Date"], border=1, align="C")
    pdf.cell(col_widths[1], 10, row["Product"], border=1, align="C")
    pdf.cell(col_widths[2], 10, str(row["Quantity"]), border=1, align="C")
    pdf.cell(col_widths[3], 10, f"Rs. {row['Price']}", border=1, align="C")
    pdf.ln()  # Move to next row

# Save PDF
pdf.output("sales_report.pdf")

print("✅ Report with company logo generated successfully as 'sales_report.pdf'")
