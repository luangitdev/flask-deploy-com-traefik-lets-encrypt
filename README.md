# Flask Deploy com Traefik e Let's Encrypt

Este projeto demonstra como fazer o deploy de uma aplicação Flask utilizando o Traefik como proxy reverso, com suporte a HTTPS automático via Let's Encrypt. O painel do Traefik está protegido por autenticação básica e disponível em um subdomínio.

## Tecnologias Utilizadas
- Python 3.9
- Flask
- Traefik v2.9
- Docker & Docker Compose
- Let's Encrypt (SSL automático)

## Estrutura do Projeto
```
├── acme.json                # Armazena certificados SSL gerados pelo Traefik
├── app.py                   # Aplicação Flask principal
├── docker-compose.yml       # Orquestração dos containers
├── Dockerfile               # Build da aplicação Flask
├── requirements.txt         # Dependências Python
├── traefik.yml              # Configuração estática do Traefik
├── letsencrypt/             # Pasta para certificados (persistência)
```

## Pré-requisitos
- Docker e Docker Compose instalados
- Um domínio registrado e gerenciável (ex: Hostinger, GoDaddy, Hostgator)
- Acesso a uma instância (ex: AWS EC2) com IP público

## Configuração do Domínio
1. Acesse o painel do seu provedor de domínio (No meu caso, Hostinger).
2. Vá em "Domínios" e selecione seu domínio (ex: `startdevops.site`).
3. Clique em "Gerenciar DNS".
4. Crie ou edite um registro do tipo **A**:
   - Nome: `@`
   - Tipo: `A`
   - Valor: [IP público da sua instância EC2]
   - TTL: 300 (ou padrão)
5. (Opcional) Para o painel do Traefik, crie um subdomínio do tipo CNAME com o nome Traefik, para ficar: `traefik.startdevops.site` também apontando para o mesmo IP da instância EC2 ou para startdevops.site.
6. Aguarde a propagação do DNS que pode levar algumas horas ou até 48 horas para propagar (Recomendo usar o TTL 300 para propagar mais rápido).

## Como Executar o Projeto
1. **Clone o repositório na sua instância EC2:**
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd flask-deploy-com-traefik-lets-encrypt
   ```
2. **Dê permissão ao arquivo `acme.json`:**
   ```bash
   chmod 600 acme.json
   ```
3. **Ajuste as configurações se necessário:**
   - No `docker-compose.yml`, confira se os domínios estão corretos nas labels.
   - No `traefik.yml`, ajuste o e-mail e domínios se necessário.
4. **Suba os containers:**
   ```bash
   docker-compose up --build -d
   ```
5. **Acesse a aplicação:**
   - App Flask: https://startdevops.site
   - Painel Traefik: https://traefik.startdevops.site (usuário: `admin`, senha conforme hash no compose gerado pelo htpasswd)

## Segurança
- O painel do Traefik está protegido por autenticação básica.
- Recomenda-se restringir o acesso ao painel por IP ou VPN em produção.
- Nunca exponha o painel sem autenticação.

## Personalização
- Para alterar a senha do painel, gere um novo hash (htpasswd) e substitua no `docker-compose.yml`.
- Para customizar a tela do Flask, edite o arquivo `app.py`.

## Licença
Este projeto é livre para uso educacional e pessoal.
