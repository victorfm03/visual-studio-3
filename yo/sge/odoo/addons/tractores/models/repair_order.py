# -*- coding: utf-8 -*-

from odoo import models, fields, api

class repair_order(models.Model):
    _name= 'tractores.repair_order'
    _description= 'Orden de reparacion'

    name = fields.Char(string= "ID orden de rep", required=True)
    vehicle_plate= fields.Char(string= "matricula", required=True)
    client_name= fields.Char(string= "nombre del cliente", required=True)
    repair_date = fields.Datetime(
        string='fecha de reparacion',
        default=fields.Datetime.now,
    )

    const = field_name = fields.Float(
        string='Coste estimado',
    )

    mechanic_id = fields.Many2one(
        string='Mecanico',
        comodel_name='tractores.mechanic',
        ondelete='restrict',
    )
    
    
    @api.depends('repair_ids')
    def _compute_num_repairs(self):
        for record in self:
            record.num_repairs=len(record.repair_ids)
    