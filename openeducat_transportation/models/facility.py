# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields


class OpFacility(models.Model):
    _name = "op.facility"
    _description = "Manage Facility"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    active = fields.Boolean(default=True)
    user_id = fields.Many2one('res.users', string='Resposible')
    task_ids = fields.One2many('op.facility.task', 'facility_id', string='Facility Task', copy=True)

    _sql_constraints = [
        ('unique_facility_code',
         'unique(code)', 'Code should be unique per facility!')]


class OpFacilityTask(models.Model):
    _name = "op.facility.task"
    _description = "Manage Facility Task"

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    user_id = fields.Many2one('res.users', string='Resposible')
    facility_id = fields.Many2one('op.facility', string='Facility')
    type = fields.Selection([('hourly', 'Hourly'),('daily', 'Daily'),('weekly', 'Weekly'),('monthly', 'Monthly'),('quarterly', 'Quarterly'),
        ('semi-annually', 'Semi-annually'),
        ('annually', 'Annually'),],string='Task Type',default='hourly')
    start_date = fields.Datetime(string='Start Task')
    excepted_date = fields.Datetime(string='Excepted End Task')
    end_date = fields.Datetime(string='Actual End Task')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'),('close','Close')],string='Status',default='draft')
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')

    def action_open_task(self):
        self.write({
            'state':'open'
        })
        return True

    def action_close_task(self):
        self.write({
            'state':'close'
        })
        return True