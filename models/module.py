from odoo import models,fields

class module(models.Model):
    __name__ = "module"
    __description = " "
    _rec_name = 'designation'
    id_module = fields.Integer("Id module",required=True)
    code = fields.Char("code",required=True)
    designation = fields.Char("Designation")
    element_ids = fields.One2many("element","module_id",string="Elements")
    semestre_id = fields.Many2one("semestre",string="Semestre")
    #semestre = fields.Char(related='semestre_id.designation',string="semestre")
