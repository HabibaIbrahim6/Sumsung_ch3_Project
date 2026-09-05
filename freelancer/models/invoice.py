class Invoice:
    def __init__(self, invoice_id, project_id, amount, status):
        self.invoice_id = invoice_id
        self.project_id = project_id
        self.amount = amount
        self.status = status  

    def display_invoice(self):
        print(f"Invoice ID: {self.invoice_id}")
        print(f"Project ID: {self.project_id}")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Status: {self.status}")