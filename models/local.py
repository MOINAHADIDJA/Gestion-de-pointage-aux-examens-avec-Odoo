from odoo import models,fields

class local(models.Model):
    __name__ = "local"
    __description = " "
    id_local = fields.Integer("Id local",required=True)
    code = fields.Char("code",required=True)
    nom = fields.Char("Nom")
    examen_ids = fields.One2many("examen","local",string="Examens")
    
    etablissement_id = fields.Many2one(
        string='etablissement',
        comodel_name='etablissement',
        ondelete='restrict'
    )
    etab = fields.Char(related='etablissement_id.short_name',string="etablissement")
