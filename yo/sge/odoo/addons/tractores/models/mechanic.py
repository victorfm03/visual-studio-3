# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mechanic(models.Model):
    _name= 'tractores.mechanic'
    _description= 'mecanico'

    name = fields.Char(string= "Nombre", required=True)
    email= fields.Char(string= "Email", required=True)
    employee_id= fields.Char(string= "numero de empleado", required=True)
    phone= fields.Char(string= "Telefono")
    photo= fields.Binary(string="fotografia")
    
    
    status = fields.Selection(
        string='estado',
        selection=[('valor1', 'valor1'), ('valor2', 'valor2')]
    )
    
    
    num_repairs = fields.Integer(
        compute='_compute_num_repairs',
    )

    
    repair_ids = fields.One2many(
        string='reparaciones',
        comodel_name='tractores.repair_order',
        inverse_name='mechanic_id',
    )
    
    
    @api.depends('repair_ids')
    def _compute_num_repairs(self):
        for record in self:
            record.num_repairs=len(record.repair_ids)
    

    