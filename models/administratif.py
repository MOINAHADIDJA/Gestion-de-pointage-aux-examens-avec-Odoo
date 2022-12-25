from odoo import models,fields

class administratif(models.Model):
    __name__ = "administratif"
    __description = " "
    matricule = fields.Char("Matricule",required=True)
    nom = fields.Char("Nom")
    prenom = fields.Char('Prenom')
    email = fields.Char("Email")
    tel = fields.Char("Tel")
    role = fields.Selection(
        string='Role',
        selection=[('enseignant', 'Enseignant'), ('responsable filiere', 'Responsable filiere'), ('administration', 'Administration')],
        default="enseignant"
           )
 
    
    #etablissement_id = fields
