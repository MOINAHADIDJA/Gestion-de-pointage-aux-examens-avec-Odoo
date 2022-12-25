from odoo import api
from odoo import models,fields

class etudiant(models.Model):
    __name__ = "etudiant"
    __description = " "
    _rec_name="name"
    id_etudiant = fields.Integer("Id etudiant",required=True)
    cne = fields.Char("CNE",required=True)
    nom = fields.Char("Nom")
    prenom = fields.Char('Prenom')
    email = fields.Char("Email")
    tel = fields.Char("Tel")
    adresse = fields.Char("Adresse")
    date_naissance = fields.Date("Date Naissance")
    lieu_naissance = fields.Char("Lieu Naissance")
    semestre_id = fields.Many2one("semestre",string="Niveau")
    etablissement_id = fields.Many2one(
        string='Etablissement',
        comodel_name='etablissement'
        
    )
    #pointage_id = fields.One2many("pointage","etudiant_id",string="pointer")
    
    
    name = fields.Char(compute='_compute_name', store="True")
    @api.depends('nom', 'prenom')
    def _compute_name(self):    
        for record in self:        
            record.name = record.nom +' '+ record.prenom
        
   


