#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from repository import find_cursos_by_campus

cursosFiltrados = find_cursos_by_campus("Sorocaba")

for curso in cursosFiltrados:
    print(curso)
