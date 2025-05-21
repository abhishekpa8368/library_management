from odoo import models, fields, api
from datetime import datetime, timedelta

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'
    
    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('library.member', string='Member', required=True)
    loan_date = fields.Date(string='Loan Date', default=fields.Date.today)
    return_date = fields.Date(string='Due Date', 
                            default=lambda self: fields.Date.to_string(
                                datetime.now() + timedelta(days=14)))
    actual_return_date = fields.Date(string='Actual Return Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('loaned', 'Loaned'),
        ('returned', 'Returned'),
        ('late', 'Late')],
        string='Status', default='draft', readonly=True)
    
    def action_loan(self):
        for record in self:
            record.write({
                'state': 'loaned',
            })
            record.book_id.write({'available': False})
    
    def action_return(self):
        for record in self:
            record.write({
                'state': 'returned',
                'actual_return_date': fields.Date.today(),
            })
            record.book_id.write({'available': True})
    
    @api.model
    def check_late_loans(self):
        loans = self.search([('state', '=', 'loaned')])
        today = fields.Date.today()
        for loan in loans:
            if loan.return_date < today:
                loan.state = 'late'