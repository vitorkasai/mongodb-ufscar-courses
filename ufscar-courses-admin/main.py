#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import find_all_cursos

cursos = find_all_cursos()

for curso in cursos:
    print(curso)
