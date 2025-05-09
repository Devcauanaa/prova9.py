import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Formulário de Contato"

    campo_nome = ft.TextField(label="Nome", width=400)
    campo_email = ft.TextField(label="E-mail", width=400)
    campo_mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=3, max_lines=5, width=400)

    texto_confirmacao = ft.Text("", color="green")

    def enviar_formulario(e):
        if campo_nome.value and campo_email.value and campo_mensagem.value:
            texto_confirmacao.value = "Formulário enviado com sucesso!"
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
        else:
            texto_confirmacao.value = "Por favor, preencha todos os campos."
        pagina.update()

    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    pagina.add(
        campo_nome,
        campo_email,
        campo_mensagem,
        botao_enviar,
        texto_confirmacao
    )

ft.app(target=main)
