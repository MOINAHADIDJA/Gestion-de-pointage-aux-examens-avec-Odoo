from odoo import models,fields
from odoo import api

class semestre(models.Model):
    __name__ = "semestre"
    __description = " "
    _rec_name = 'name'
    id_semestre = fields.Integer("Id semestre",required=True)
    designation = fields.Char("designation")
    module_ids = fields.One2many("module","semestre_id",string="Modules")
    filiere_id = fields.Many2one("filiere",string="Filiere" )
    etudiant_id = fields.One2many("etudiant","semestre_id",string="Etudiant")
    
    name = fields.Char(compute='_compute_name', store="True")
    @api.depends('designation', 'filiere_id')
    def _compute_name(self):    
        for record in self:        
            record.name = record.designation +' '+ str(record.filiere_id.short_name)
    

