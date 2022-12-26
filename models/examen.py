from odoo import models,fields
from odoo import api
class examen(models.Model):
    __name__ = "examen"
    __description = " "

    id_examen = fields.Integer("Id examen",required=True)
    _rec_name="designation_exam"
    type_id = fields.Many2one("type_examen",string="Type")
    #date = fields.Datetime("Date examen")
    date = fields.Date("Date examen")
    employe_id = fields.Many2many("employe",string='Surveillants')
    element_id = fields.Many2one("element",string="Element" )
    local_id = fields.Many2one("local" , string="Local")
    session = fields.Selection(
        string='session',
        selection=[('normal', 'Normal'), ('rattrapage', 'Rattrapage')],
        default="normal"
           )
    duree = fields.Float("Duree")

    state = fields.Selection(
        string='state',
        selection=[('brouillon', 'Brouillon'), ('en cours', 'En cours'), ('fini', 'Fini')],
        default="brouillon"
           )
    #pointage_id = fields.One2many("pointage","examen_id",string="pointer")


    designation_exam = fields.Char(compute='_compute_name', store="True")
    @api.depends('type_id','element_id')
    def _compute_name(self):    
        for record in self:      
            record.designation_exam = str(record.type_id.libelle) +' '+ str(record.element_id.designation)
    
    def make_state1(self):
        self.ensure_one()
        self.state ='brouillon'
    def make_state2(self):
        self.ensure_one()
        self.state='en cours'    
    def make_state3(self):
        self.ensure_one()
        self.state ='fini'