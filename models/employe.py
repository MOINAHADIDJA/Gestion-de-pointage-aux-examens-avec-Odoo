from odoo import models,fields

class employe(models.Model):
    __name__ = "employe"
    __description = " "
    id_employe = fields.Integer("Id employe",required=True)
    matricule = fields.Char("Matricule",required=True)
    nom = fields.Char("Nom")
    prenom = fields.Char('Prenom')
    email = fields.Char("Email")
    tel = fields.Char("Tel")
    role = fields.Selection(
        string='Role',
        selection=[('enseignant', 'Enseignant'), ('responsable filiere', 'Responsable filiere'), ('administratif', 'Administratif')],
        default="enseignant"
           )
    examens = fields.Many2one("examen",string= "examen à surveiller")
       
    etablissement_id = fields.Many2one(
        string='Etablissement',
        comodel_name='etablissement'
        
    )
    examen_id = fields.Many2many(
        string='examen',
        comodel_name='examen'
        
    )
    
