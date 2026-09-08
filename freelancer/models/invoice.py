from ..utils.helper_functions import commission_rate


class Invoice:

    def __init__(self, invoice_id, project_id, amount):
        self.invoice_id = invoice_id
        self.project_id = project_id
        self.amount = int(amount)
        self.status = "unpaid"

        calculate_commission = commission_rate(amount)

        self.platform_commission = calculate_commission()
        self.freelancer_earnings = (amount - self.platform_commission)

    def display_invoice(self):
        print(f"Invoice ID: {self.invoice_id}")
        print(f"Project ID: {self.project_id}")
        print(f"Total Amount: ${self.amount:.2f}")
        print(f"Status: {self.status}")
        print(f"Platform commission: ${self.platform_commission:.2f}")
        print(f"Freelancer earnings: ${self.freelancer_earnings:.2f}")

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "project_id": self.project_id,
            "amount": self.amount,
            "status": self.status,
            "platform_commission": self.platform_commission,
            "freelancer_earnings": self.freelancer_earnings
        }

    @classmethod
    def from_dict(cls, invoice_data):

        invoice = cls(
            invoice_data["invoice_id"],
            invoice_data["project_id"],
            invoice_data["amount"]
        )

        invoice.status = invoice_data.get(
            "status",
            "unpaid"
        )

        return invoice