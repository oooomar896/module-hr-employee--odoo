from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee'

    name = fields.Char(string='Employee Name', required=True)
    job_title = fields.Char(string='Job Title')
    department_id = fields.Many2one('hr.department', string='Department')
    color = fields.Integer(string='Color')
    # أضف المزيد من الحقول حسب الحاجة
