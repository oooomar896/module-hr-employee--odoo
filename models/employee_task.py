from odoo import models, fields

class EmployeeTask(models.Model):
    _name = 'employee.task'
    _description = 'Employee Task'

    name = fields.Char(string='Task Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Assigned Employee')
    due_date = fields.Date(string='Due Date')
    # أضف المزيد من الحقول حسب الحاجة
