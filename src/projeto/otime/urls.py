from django.urls import path
from .views import  index, salas, reservarHorario, professores, disciplinas, atualizar_professor, deletar_professor, criar_professor, atualizar_disciplina, deletar_disciplina, criar_disciplina
urlpatterns = [
    path("", index, name = "index"),
    path("salas", salas, name = "salas"),
    path("reservarHorario", reservarHorario, name = "reservarHorario"),
    path("professores", professores, name = "professores"),
    path("disciplinas", disciplinas, name = "disciplinas"),
    path('update/<int:id>/', atualizar_professor, name='atualizar_professor'),
  	path('delete/<int:id>/', deletar_professor, name='deletar_professor'),
   	path('criar_professor', criar_professor, name='criar_professores'),
    path('update/disciplina/<int:id>/', atualizar_disciplina, name='atualizar_disciplina'),
  	path('delete/disciplina/<int:id>/', deletar_disciplina, name='deletar_disciplina'),
    path('criar_disciplina', criar_disciplina, name='criar_disciplinas'),
]
