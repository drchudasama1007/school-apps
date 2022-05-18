# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OpRoute(models.Model):
    _name = "op.route"
    _description = "Manage Route"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    active = fields.Boolean(default=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    driver_id = fields.Many2one('res.partner', string='Driver')
    supervisor_ids = fields.Many2many('res.partner', string='Supervisor(s)')
    stop_ids = fields.One2many('op.stop', 'route_id', string='Stops', copy=True)
    # user_id = fields.Many2one('res.users', string='Driver')
    # user_ids = fields.Many2many('res.users', string='Supervisor(s)')

    _sql_constraints = [
        ('unique_facility_code',
         'unique(code)', 'Code should be unique per Route!')]

    @api.onchange('vehicle_id')
    def onchange_vehicle_id(self):
        if self.vehicle_id and self.vehicle_id.driver_id:
            self.driver_id = self.vehicle_id.driver_id.id


class OpStop(models.Model):
    _name = "op.stop"
    _description = "Manage Stops"
    _order = "arrival_time"

    name = fields.Char(string='Name')
    active = fields.Boolean(default=True)
    arrival_time = fields.Float(string='Arrival Time')
    departure_time = fields.Float(string='Departure Time')
    route_id = fields.Many2one('op.route', string='Route')


