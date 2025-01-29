from langchain.prompts import ChatPromptTemplate
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Configuração da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Função para processar a resposta do bot
def resposta_bot(mensagens):
    # Criar histórico no formato correto
    mensagem_modelo = [SystemMessage(content='Você é um assistente amigável e parceiro chamado Zikzin')]
    
    for remetente, conteudo in mensagens:
        if remetente == 'user':
            mensagem_modelo.append(HumanMessage(content=conteudo))
        elif remetente == 'assistant':
            mensagem_modelo.append(AIMessage(content=conteudo))

    # Criar template com as mensagens corretamente formatadas
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat

    # Obter resposta do modelo
    resposta = chain.invoke({'input': mensagens[-1][1]})  # Apenas última entrada do usuário

    return resposta  # Já retorna o objeto correto

# Loop de interação com o usuário
historico = []
while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    
    historico.append(('user', pergunta))  # Adicionando pergunta do usuário
    resposta = resposta_bot(historico)
    historico.append(('assistant', resposta.content))  # Correção: acessa apenas o conteúdo da resposta

    print(f'Bot: {resposta.content}')  # Exibe corretamente a resposta

print(historico)
print('Muito obrigado por usar o nosso bot!')
