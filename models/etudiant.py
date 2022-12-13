from odoo import models,fields

class etudiant(models.Model):
    __name__ = "etudiant"
    __description = " "
    id_etudiant = fields.Integer("Id etudiant",required=True)
    cne = fields.Char("CNE",required=True)
    nom = fields.Char("Nom")
    prenom = fields.Char('Prenom')
    email = fields.Char("Email")
    tel = fields.Char("Tel")
    adresse = fields.Char("Adresse")
    date_naissance = fields.Date("Date Naissance")
    lieu_naissance = fields.Char("Lieu Naissance")
    
    etablissement_id = fields.Many2one(
        string='Etablissement',
        comodel_name='etablissement'
        
    )
    etablissement = fields.Char(related='etablissement_id.short_name',string = "ecole")
    
    
    
   


