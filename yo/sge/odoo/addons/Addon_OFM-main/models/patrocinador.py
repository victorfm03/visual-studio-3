from odoo import models, fields, api

class Patrocinador(models.Model):
    _name = "fiesta.patrocinador"
    _description = "patrocinador de la fiesta"

    dni = fields.Text(
        string='DNI del patrocinador',
    )
    

    name = fields.Char(
        string='Nombre del patrocinador',
        required=True, unique=True
    )

    empresa_asociada = fields.Text(
        string='Nombre de la empresa asociada',
        required=True
    )

    edad = fields.Integer(string="Edad", required=True, readonly=True, compute="_compute_edad")


    ubicacion = fields.Text(string="Ubicación del patrocinador")

    patrocinadores_ids = fields.One2many(
    comodel_name="fiesta.artista",
    inverse_name="patrocinador_id",
    string="Artistas"
)

    @api.depends('patrocinadores_ids')
    def _compute_cant_actuaciones(self):
        for record in self:
            record.numero_de_actuaciones = len(record.patrocinadors_ids)