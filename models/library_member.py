from odoo import models, fields, api

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    membership_date = fields.Date(string='Membership Date', default=fields.Date.today)
    membership_type = fields.Selection([
        ('regular', 'Regular'),
        ('premium', 'Premium'),
    ], string='Membership Type', default='regular')
    
    # Relational fields
    book_ids = fields.One2many('library.book', 'member_id', string='Borrowed Books')