# -*- coding: utf-8 -*-

from djangorestframework.mixins import InstanceMixin, ReadModelMixin
from djangorestframework.views import ModelView


class ReadModelView(InstanceMixin, ReadModelMixin, ModelView):
    """A view which provides default operations for read, against a model in the database."""

    _suffix = 'Instance'
