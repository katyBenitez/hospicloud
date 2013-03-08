# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2013 Carlos Flores <cafg10@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url
from emergency.views import (PersonaEmergenciaCreateView, EmergenciaDetailView,
                             EmergenciaCreateView, RemisionInternaCreateView,
                             TratamientoCreateView, RemisionExternaCreateView,
                             EmergenciaUpdateView, EmergenciaListView,
                             CobroCreateView,  HallazgoCreateView,
                             EmergenciaPreCreateView)

urlpatterns = patterns('',
    
    url(r'^$',
        EmergenciaListView.as_view(),
        name='emergency-index'),
    
    url(r'^ingresar$',
        EmergenciaPreCreateView.as_view(),
        name='emergency-ingresar'),

    url(r'^persona/ingresar$',
        PersonaEmergenciaCreateView.as_view(),
        name='emergency-persona-create'),

    url(r'^persona/(?P<persona>\d+)$',
        EmergenciaCreateView.as_view(),
        name='emergency-create'),

    url(r'^(?P<pk>\d+)$',
        EmergenciaDetailView.as_view(),
        name='emergency-view-id'),
    
    url(r'^(?P<emergencia>\d+)/tratamiento/agregar$',
        TratamientoCreateView.as_view(),
        name='emergencia-tratamiento-agregar'),
    
    url(r'^(?P<emergencia>\d+)/hallazgo/agregar$',
        HallazgoCreateView.as_view(),
        name='emergencia-hallazgo-agregar'),
    
    url(r'^(?P<emergencia>\d+)/remision/interna/agregar$',
        RemisionInternaCreateView.as_view(),
        name='emergencia-remision-interna-agregar'),

    url(r'^(?P<emergencia>\d+)/cobro/agregar$',
        CobroCreateView.as_view(),
        name='emergencia-cobro-agregar'),
    
    url(r'^(?P<emergencia>\d+)/remision/externa/agregar$',
        RemisionExternaCreateView.as_view(),
        name='emergencia-remision-externa-agregar'),
)