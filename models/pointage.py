from odoo import models,fields

class pointage(models.Model):
    __name__ = "pointage"
    __description = " Classe de pointage dans les  examens "
    etudiant_id = fields.Many2many("etudiant",string="Etudiants")
    examen_id = fields.Many2many("examen",string="Examens" )
    state = fields.Selection(
        string='state',
        selection=[('absent', 'Absent'), ('present', 'Present')],
        default='Absent'
           )
    #state = fields.Char("state")

 
    