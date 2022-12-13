from odoo import models,fields

class semestre(models.Model):
    __name__ = "semestre"
    __description = " "
    id_semestre = fields.Integer("Id semestre",required=True)
    designation = fields.Char("designation")
    module_ids = fields.One2many("module","semestre",string="Modules")
    filiere_id = fields.Many2one("filiere",string="Filiere" )
    filiere = fields.Char(related='filiere_id.short_name',string="filiere")
    

