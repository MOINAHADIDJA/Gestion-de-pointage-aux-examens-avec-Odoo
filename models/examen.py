from odoo import models,fields

class examen(models.Model):
    __name__ = "examen"
    __description = " "
    id_examen = fields.Integer("Id examen",required=True)
    type_id = fields.Many2one("type_examen",string="Type")
    type = fields.Char(related='type_id.libelle',string="type")
    date = fields.Datetime("Date examen")
    employe_id = fields.One2many("employe","examens",string='Surveillants')
    element_id = fields.Many2one("element",string="Element" )
    element = fields.Char(related='element_id.designation',string="element")

    local_id = fields.Many2one("local" , string="Local")
    local = fields.Char(related='local_id.nom',string="local")

    session = fields.Selection(
        string='session',
        selection=[('normal', 'Normal'), ('rattrapage', 'Rattrapage')],
        default="normal"
           )
    

    state = fields.Selection(
        string='state',
        selection=[('brouillon', 'Brouillon'), ('en cours', 'En cours'), ('fini', 'Fini')],
        default="brouillon"
           )
    
    
    def make_state1(self):
        self.ensure_one()
        self.state ='brouillon'
    def make_state2(self):
        self.ensure_one()
        self.state='en cours'    
    def make_state3(self):
        self.ensure_one()
        self.state ='fini'