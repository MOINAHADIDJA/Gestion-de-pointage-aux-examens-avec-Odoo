from odoo import models,fields

class element(models.Model):
    __name__ = "element"
    __description = " "
    id_element = fields.Integer("Id element",required=True)
    code = fields.Char("code",required=True)
    designation = fields.Char("Designation")
    module_id = fields.Many2one("module",string="Module")
    module = fields.Char(related='module_id.designation',string="module")

  