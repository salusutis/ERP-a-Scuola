from odoo import models, fields, api, _

class scuola_classi(models.Model):
    _name= 'scuola.classi'
    _description= 'Classi Record'
    _rec_name = 'nome_classe'

    classe_id= fields.One2many('scuola.alunno','classe_alunno', string='Classe')
    nome_classe= fields.Char(string='Nome Classe', required= True)
