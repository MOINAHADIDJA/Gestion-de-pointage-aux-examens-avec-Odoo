from odoo import api
from odoo import models,fields

class local(models.Model):
    __name__ = "local"
    __description = " "
    _rec_name = 'designation'
    id_local = fields.Integer("Id local",required=True)
    code = fields.Char("code",required=True)
    nom = fields.Char("Nom")
    examen_ids = fields.One2many("examen","local_id",string="Examens")
    
    etablissement_id = fields.Many2one(
        string='etablissement',
        comodel_name='etablissement',
        ondelete='restrict'
    )
    
    designation = fields.Char(compute='_compute_name', store="True")
    @api.depends('nom', 'etablissement_id')
    def _compute_name(self):    
        for record in self:        
            record.designation = record.nom +' '+ str(record.etablissement_id.short_name)

