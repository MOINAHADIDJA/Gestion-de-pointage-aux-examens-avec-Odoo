from odoo import models,fields
from odoo import api

class pointage(models.Model):
    __name__ = "pointage"
    __description = " Classe de pointage dans les  examens "
    etudiant_id = fields.Many2one("etudiant",string="Etudiants",required=True)
    examen_id = fields.Many2one("examen",string="Examens",required=True)
    state = fields.Selection(
        string='state',
        selection=[('absent', 'Absent'), ('present', 'Present')],
        default='Absent'
           )
    
    verification= fields.Integer("Etat", default=1, compute='_computer_name')
    @api.depends('examen_id')
    def _computer_name(self):    
        for record in self:        
            record.verification = (1) if record.examen_id.state in ('brouillon', 'Brouillon','fini', 'Fini') else (0)

    
  
    