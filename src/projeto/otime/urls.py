from django.urls import path
from .views import  index, salas, buscas, reservarHorario, exibeSlotTurma, exibeSlotDisciplina, exibeSlotSala, exibeSlotProfessor, filtroTurma, filtroProfessor, filtroSala, filtroDisciplina, professores, turmas, disciplinas, seletor_turmas, atualizar_professor, atualizar_disciplina, atualizar_sala, atualizar_turma
urlpatterns = [
    path("", index, name = "index"),
    path("salas", salas, name = "salas"),
    path("buscas", buscas, name = "buscas"),
    path("filtroSala", filtroSala, name = "filtroSala"),
    path("filtroProfessor", filtroProfessor, name = "filtroProfessor"),
    path("filtroTurma", filtroTurma, name = "filtroTurma"),
    path("filtroDisciplina", filtroDisciplina, name = "filtroDisciplina"),
    path("reservarHorario/<int:id>", reservarHorario, name = "reservarHorario"),
    path("exibeSlotDisciplina/<int:id>", exibeSlotDisciplina, name = "exibeSlotDisciplina"),
    path("exibeSlotTurma/<int:id>", exibeSlotTurma, name = "exibeSlotTurma"),
    path("exibeSlotProfessor/<int:id>", exibeSlotProfessor, name = "exibeSlotProfessor"),
    path("exibeSlotSala/<int:id>", exibeSlotSala, name = "exibeSlotSala"),
    path("professores", professores, name = "professores"),
    path("seletor_turmas", seletor_turmas, name = "seletor_turmas"),
    path("turmas", turmas, name = "turmas"),
    path("disciplinas", disciplinas, name = "disciplinas"),
    path('update/professor/<int:id>/', atualizar_professor, name='atualizar_professor'),
    path('update/disciplina/<int:id>/', atualizar_disciplina, name='atualizar_disciplina'),
    path('update/sala/<int:id>/', atualizar_sala, name='atualizar_sala'),
    path('update/turma/<int:id>/', atualizar_turma, name='atualizar_turma')
]
