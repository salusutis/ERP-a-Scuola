from odoo import models, fields

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'

    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')
"""""
    @api.multi
    def open_student_votes(self):
        return {
            'name': _('Voti'),
            'domain': [('alunno_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'scuola.voti',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }