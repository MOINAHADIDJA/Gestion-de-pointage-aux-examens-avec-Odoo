from odoo import models,fields

class element(models.Model):
    __name__ = "element"
    __description = " "
    _rec_name = 'designation'
    id_element = fields.Integer("Id element",required=True)
    code = fields.Char("code",required=True)
    designation = fields.Char("Designation")
    module_id = fields.Many2one("module",string="Module")
    examens_id = fields.One2many("examen","element_id",string='Examens')

  