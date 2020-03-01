from odoo import models, fields, api, _

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'


    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')
    combination = fields.Char(string='Combination', compute='fields_combination')
    voti_ids = fields.One2many('scuola.voti', 'voti_id', string='Journal voti',)

    @api.multi
    def name_get(self):
        risultato=[]
        for alunno in self:
            nome= alunno.nome_alunno + ' ' + alunno.cognome_alunno  + ' ' + str(alunno.id)
            risultato.append((alunno.id, nome))
        return risultato


    @api.multi
    def alunno_voti(self):
        return {
            'name': _('votes'),
            'domain': [('alunno_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'scuola.voti',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    @api.multi
    def action_post(self):
        if self.mapped('anni_alunno'):
            pass
        return {}
