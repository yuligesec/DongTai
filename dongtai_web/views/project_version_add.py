#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:sjh
# software: PyCharm
# project: lingzhi-webapi
import logging

from dongtai_common.endpoint import R
from dongtai_common.endpoint import UserEndPoint

from dongtai_web.base.project_version import version_modify, VersionModifySerializer
from django.utils.translation import gettext_lazy as _
from dongtai_web.utils import extend_schema_with_envcheck, get_response_serializer

logger = logging.getLogger("django")

_ResponseSerializer = get_response_serializer(status_msg_keypair=(
    ((202, _('Parameter error')), ''),
    ((201, _('Created success')), ''),
))


class ProjectVersionAdd(UserEndPoint):
    name = "api-v1-project-version-add"
    description = _("New application version information")

    @extend_schema_with_envcheck(
        request=VersionModifySerializer,
        tags=[_('Project')],
        summary=_('Projects Version Add'),
        description=_("""Add project version information according to the given conditions;
            if the version id is specified, the corresponding version information is updated according to the given conditions."""
                      ),
        response_schema=_ResponseSerializer,
    )
    def post(self, request):
        try:
            # auth_users = self.get_auth_users(request.user)
            department = request.user.get_relative_department()
            result = version_modify(request.user, department, request.data)
            if result.get("status", "202") == "202":
                return R.failure(status=202,
                                 msg=result.get("msg", _("Parameter error")))
            else:
                return R.success(msg=_('Created success'), data=result.get("data", {}))

        except Exception as e:
            logger.error(e, exc_info=True)
            return R.failure(status=202, msg=_("Parameter error"))
