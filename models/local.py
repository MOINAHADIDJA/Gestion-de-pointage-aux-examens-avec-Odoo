from odoo import api
from odoo import models,fields

class local(models.Model):
    __name__ = "local"
    __description = " "
    _rec_name = 'nom'
    id_local = fields.Integer("Id local",required=True)
    code = fields.Char("code",required=True)
    nom = fields.Char("Nom")
    examen_ids = fields.One2many("examen","local_id",string="Examens")
    
    etablissement_id = fields.Many2one(
        string='etablissement',
        comodel_name='etablissement',
        ondelete='restrict'
    )
    
    designation = fields.Char(compute='_compute_local', store="True")
    @api.depends('nom', 'etablissement_id')
    def _compute_local(self):    
        for local in self:        
            local.designation = local.nom +' '+ str(local.etablissement_id.short_name)

