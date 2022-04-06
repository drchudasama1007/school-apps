# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Users(models.Model):
    _inherit = 'res.users'

    menu_ids = fields.Many2many('ir.ui.menu', 'user_menu_rel', 'uid', 'menu_id', string='Menu To Hide', help='Select Menus To Hide From This User')
    report_ids = fields.Many2many('ir.actions.report', 'user_report_rel', 'user_id', 'report_id', 'Report To Hide',
                                  help='Select Report To Hide From This User')


class ResGroups(models.Model):
    _inherit = 'res.groups'

    menu_ids = fields.Many2many('ir.ui.menu', 'group_menu_rel', 'group_id', 'menu_id', string='Menu To Hide')
    report_ids = fields.Many2many('ir.actions.report', 'group_report_rel', 'group_id', 'report_id', 'Report To Hide',
                                  help='Select Report To Hide From This User')


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    hide_user_ids = fields.Many2many('res.users', 'user_report_rel', 'report_id', 'user_id', string='Hide From Users')
    hide_group_ids = fields.Many2many('res.groups', 'group_report_rel', 'report_id', 'group_id', string='Hide From Groups')


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    hide_group_ids = fields.Many2many('res.groups', 'group_menu_rel', 'menu_id', 'group_id', string='Hide From Groups')
    hide_user_ids = fields.Many2many('res.users', string='Hide From Users')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.user == self.env.ref('base.user_root'):
            return super(IrUiMenu, self).search(args, offset=0, limit=None, order=order, count=False)
        else:
            menus = super(IrUiMenu, self).search(args, offset=0, limit=None, order=order, count=False)
            if menus:
                menu_ids = [menu for menu in self.env.user.menu_ids]
                menu_ids2 = [menu for group in self.env.user.groups_id for menu in group.menu_ids]
                for menu in list(set(menu_ids).union(menu_ids2)):
                    if menu in menus:
                        menus -= menu
                if offset:
                    menus = menus[offset:]
                if limit:
                    menus = menus[:limit]
            return len(menus) if count else menus

