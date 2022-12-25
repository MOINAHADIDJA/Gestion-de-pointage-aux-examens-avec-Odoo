from odoo import models,fields

class type_examen(models.Model):
    __name__ = "type_examen"
    __description = " "
    _rec_name = 'libelle'
    id_type_examen = fields.Integer("Id type examen",required=True)
    libelle = fields.Char("libelle",required=True)
    examen_ids = fields.One2many("examen","type_id",string="Examens")
    
  