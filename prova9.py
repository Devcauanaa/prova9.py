import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    tarefas = ft.Column()  # Container para exibir as tarefas

    campo_tarefa = ft.TextField(label="Digite uma tarefa", expand=True)

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            tarefas.controls.append(ft.Text(campo_tarefa.value))
            campo_tarefa.value = ""
            page.update()

    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        tarefas
    )

ft.app(target=main)

