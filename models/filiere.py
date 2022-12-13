from odoo import models,fields

class filiere(models.Model):
    __name__ = "filiere"
    __description = " "
    id_filiere = fields.Integer("Id filiere",required=True)
    code = fields.Char("code",required=True)
    name = fields.Char("nom")
    short_name = fields.Char("Abreviation")
    semestre_ids = fields.One2many('semestre','filiere_id',string="Semestre")   

    
