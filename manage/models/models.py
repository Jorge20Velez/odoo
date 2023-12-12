# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
     _name = 'manage.task'
     _description = 'manage.task'


     code=fields.Char(compute="_get_code")
     name = fields.Char(string="Nombre")
     description=fields.Text()
     creation_date=fields.Date()
     start_date=fields.Datetime()
     end_date=fields.Datetime()
     is_paused=fields.Boolean()
     sprint=fields.Many2one("manage.sprint", ondelete="set null", help="Sprint relacionado")
     technology=fields.Many2many(comodel="manage.technology", relation_name="technology_task",
                                 column1="task_id",
                                 column2="technology_id")
     
     #@api.one
     def _get_code(self):
          for task in self:
               if len(task.sprint) == 0:
                   task.code="TSK_"+str(task.id)
               else:
                   task.code=str(task.sprint.name).upper()+"_"+str(task.id)



class sprint(models.Model):
     _name = 'manage.sprint'
     _description = 'manage.sprint'

     name = fields.Char(string="Nombre")
     description=fields.Text()
     start_date=fields.Datetime()
     end_date=fields.Datetime()
     task=fields.One2many(string="Tareas", comodel_name="manage.task" , inverse_name="sprint")


class technology(models.Model):
     _name = 'manage.technology'
     _description = 'manage.technology'

     name = fields.Char(string="Nombre")
     description=fields.Text()

     photo=fields.Image(max_width=200, max_height=200)
     task=fields.Many2many(comodel_name="manage.task",
                           relation_name="technology_task",
                           column1="technology_id",
                           column2="task_id")