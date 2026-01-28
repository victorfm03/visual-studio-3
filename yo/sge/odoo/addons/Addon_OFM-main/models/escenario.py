from odoo import models, fields, api

class Escenario(models.Model):
    _name = "fiesta.escenario"
    _description = "Escenario de la fiesta"

    name = fields.Text(
        string='Nombre del escenario',
        required=True, unique=True
    )
    
    num_Sala= fields.Integer(
        string='Número de sala',
        required=True
    )


    ubicacion = fields.Text(string="Ubicación del escenario")

    escenarios_ids = fields.One2many(
    comodel_name="fiesta.actuacion",
    inverse_name="escenario_id",
    string="Actuaciones"
)

    numero_de_actuaciones = fields.Integer(string="Cantidad de actuaciones", compute="_compute_cant_actuaciones", store=True)

    @api.depends('escenarios_ids')
    def _compute_cant_actuaciones(self):
        for record in self:
            record.numero_de_actuaciones = len(record.escenarios_ids)