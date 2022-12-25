from odoo import models,fields

class etablissement(models.Model):
    __name__ = "etablissement"
    __description = " "
    # id_etab = fields.Integer("Id etablissement",required=True)
    code = fields.Char("Code",required=True)
    nom = fields.Char("Nom")
    _rec_name='short_name'
    short_name = fields.Char("Abreviation")
    email = fields.Char("E-mail")
    tel = fields.Char("Tel")
    fax = fields.Char("Fax")
    adresse = fields.Char("Adresse")
    ville = fields.Char("Ville")
    code_postal = fields.Date("code postal")
    logo = fields.Binary("Logo")
    
   
    
   


