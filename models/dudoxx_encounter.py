from odoo import models, fields

class Encounter(models.Model):
    _name = 'dudoxx.encounter'
    _description = 'Patient-Doctor Encounter'

    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    doctor_id = fields.Many2one('res.partner', string='Doctor', required=True)
    date = fields.Datetime(string='Date', required=True)
    notes = fields.Text(string='Notes')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

class EncounterLine(models.Model):
    _name = 'dudoxx.encounter.line'
    _description = 'Encounter Line'

    encounter_id = fields.Many2one('dudoxx.encounter', string='Encounter', required=True)
    description = fields.Text(string='Description')
    date = fields.Datetime(string='Date', required=True)
