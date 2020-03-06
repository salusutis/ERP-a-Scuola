from odoo import models, fields, api, _
from datetime import datetime

class scuola_voti(models.Model):
    _name= 'scuola.voti'
    _description= 'Voti Record'

    voto_alunno = fields.Float(digits=(2,2), string='Voto', required= True)
    voto_materia = fields.Selection([
        ('informatica', 'Informatica'),
        ('ec.aziendale', 'Ec.Aziendale'),
        ('storia', 'Storia'),
        ('italiano', 'Italiano'),
        ('dirito', 'Diritto'),
        ('ec.politica', 'Ec.Politica'),
        ('religione', 'Religione'),
        ('ed.fisica', 'Ed.Fisica'),
    ], string='Materia', required= True)
    voto_data = fields.Date(string='Data voto', required= True, default=datetime.today())
    alunno_id = fields.Many2one('scuola.alunno', string="Alunni")




