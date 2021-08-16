#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/18 下午12:54
# software: PyCharm
# project: dongtai-models
from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from dongtai.utils.customfields import trans_char_field
from typing import Any


class Talent(models.Model):
    talent_name = models.CharField(
        unique=True,
        verbose_name=_('talent'),
        max_length=255,
        blank=True,
        error_messages={
            'unique': _("A talent with that talent name already exists."),
        },
    )
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'),
    )

    class Meta:
        verbose_name = _('talent')
        managed = True if os.getenv('environment', None) == 'TEST' else False
        db_table = 'auth_talent'

    def get_talent_name(self):
        return self.talent_name

    @trans_char_field('talent_name', ["默认租户"])
    def __getattribute__(self, name) -> Any:
        return super().__getattribute__(name)
