from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    invoice_information = fields.Char(
        string="Facturas relacionadas", compute="_compute_invoice_information"
    )
    bills_information = fields.Char(
        string="Facturas relacionadas", compute="_compute_bills_information"
    )

    def _compute_invoice_information(self):
        for payment in self:
            invoices = payment.mapped("reconciled_invoice_ids")
            if invoices:
                payment.invoice_information = ", ".join(invoices.mapped("name"))
            else:
                payment.invoice_information = False

    def _compute_bills_information(self):
        for payment in self:
            bills = payment.mapped("reconciled_bill_ids")
            if bills:
                payment.bills_information = ", ".join(bills.mapped("name"))
            else:
                payment.bills_information = False
