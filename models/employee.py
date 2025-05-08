from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee'

    name = fields.Char(string='Employee Name', required=True)
    job_title = fields.Char(string='Job Title')
    department_id = fields.Many2one('hr.department', string='Department')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    hire_date = fields.Date(string='Hire Date')
    # أضف المزيد من الحقول حسب الحاجة
