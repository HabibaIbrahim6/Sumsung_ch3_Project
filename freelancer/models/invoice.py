from ..utils.helper_functions import commission_rate


class Invoice:
    def __init__(self, invoice_id, project_id, amount):
        self.invoice_id = invoice_id
        self.project_id = project_id
        self.amount = amount
        self.status = "unpaid"

        calculate_commission = commission_rate(amount)
        self.commission = calculate_commission()
        self.freelancer_earnings = amount - self.commission

    def display_invoice(self):
        print(f"Invoice ID: {self.invoice_id}")
        print(f"Project ID: {self.project_id}")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Status: {self.status}")
        print(f"Commission: ${self.commission:.2f}")
        print(f"Freelancer earnings: ${self.freelancer_earnings:.2f}")