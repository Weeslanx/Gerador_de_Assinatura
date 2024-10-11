# Gerador de Imagem para Assinatura de E-mail

Este projeto utiliza **Flask** e uma página **HTML** para gerar imagens personalizadas de assinaturas de e-mail, com dados de funcionários obtidos através da API **Microsoft Graph**. A imagem é criada utilizando a biblioteca `PIL` (Python Imaging Library), com campos posicionados de acordo com coordenadas configuradas previamente.

## :star2: Funcionalidades

- **Integração com a API Microsoft Graph**: Obtém automaticamente informações de funcionários, como nome, e-mail e setor.
- **Interface de configuração web**: Permite que os usuários carreguem uma imagem de fundo e ajustem a posição dos campos (nome, e-mail, etc.) diretamente na interface.
- **Geração de imagem automática**: A imagem é gerada com os dados dos funcionários, utilizando as coordenadas configuradas para posicionamento dos campos.
- **Armazenamento de coordenadas**: As posições configuradas são salvas para gerar imagens futuras com os mesmos parâmetros.

## :gear: Tecnologias Utilizadas

- **Flask** (backend)
- **React** (frontend para a configuração)
- **Microsoft Graph API** (integração para obter dados dos funcionários)
- **PIL** (Python Imaging Library para manipulação de imagens)
- **HTML/CSS/JavaScript** (interface web)

## :hammer_and_wrench: Como Funciona

1. A aplicação se conecta à **API Microsoft Graph** para obter as informações do funcionário (nome, e-mail, etc.).
2. O usuário pode acessar uma interface web onde é possível:
   - Carregar uma imagem de fundo.
   - Definir as coordenadas dos campos (nome, e-mail, setor, etc.) na imagem.
3. O sistema utiliza a biblioteca **PIL** para gerar uma imagem personalizada com base nos dados e coordenadas fornecidos.
4. As coordenadas configuradas são salvas para que possam ser reutilizadas na geração de novas imagens com diferentes dados.

## :rocket: Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Weeslanx/Gerador_de_Assinatura
