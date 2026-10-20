E-commerce Growth Intelligence
Documento Mestre do Projeto — Contexto, Arquitetura e Roadmap

Versão: 1.0
Última atualização: 20/10/2026
Status: Planejamento inicial
Objetivo: Construir um projeto de portfólio profissional que demonstre competências em desenvolvimento de software, engenharia e análise de dados, Business Intelligence, e-commerce e marketing analytics.

1. CONTEXTO DO PROJETO
Perfil profissional

O desenvolvedor responsável pelo projeto possui:

Graduação em Análise e Desenvolvimento de Sistemas (ADS), no Brasil.
Pós-graduação em Inteligência Artificial.
Aproximadamente cinco anos de experiência profissional em desenvolvimento de sistemas.
Experiência principal com Python e FastAPI.
Experiência com Flutter.
Experiência adicional com Next.js e Node.js.
Residência atual na Espanha.
Previsão de início de um Master em Marketing e E-commerce em Madrid no início de 2027.
Objetivo de carreira

Conseguir uma oportunidade profissional na Espanha ou em outro mercado europeu, aproveitando a experiência prévia em desenvolvimento e expandindo a atuação para áreas como:

Data Analytics.
Analytics Engineering.
Business Intelligence.
Data Engineering.
Marketing Analytics.
E-commerce Analytics.
Marketing Technology (MarTech).
Desenvolvimento de soluções de dados e IA.

O projeto deve ajudar a demonstrar competências relevantes para recrutadores europeus, sem posicionar o desenvolvedor como um profissional iniciante em tecnologia.

Estratégia

Construir uma aplicação funcional que integre desenvolvimento de software, tratamento de dados, SQL, dashboards e análise de negócio.

A prioridade é desenvolver um MVP simples, bem documentado, publicamente acessível e tecnicamente sólido, evitando funcionalidades desnecessárias.

2. VISÃO DO PRODUTO
Nome

E-commerce Growth Intelligence

Descrição

Uma plataforma de analytics para e-commerce que transforma dados operacionais de vendas e comportamento dos consumidores em indicadores, análises e recomendações para melhorar o desempenho comercial.

A aplicação simula uma ferramenta de apoio à decisão utilizada por uma equipe de e-commerce, marketing ou gestão comercial.

Problema que o produto resolve

Empresas de comércio eletrônico acumulam dados de pedidos, produtos, clientes e pagamentos, mas precisam transformá-los em informações úteis para responder a perguntas como:

Como estão evoluindo as vendas?
Quais categorias e produtos apresentam melhor desempenho?
Qual é o ticket médio?
Como estão os prazos de entrega e a satisfação dos clientes?
Quais clientes compram com frequência?
Quais segmentos de clientes precisam de campanhas de reativação?
Quais canais de marketing merecem maior investimento?
Quais ações podem melhorar os resultados comerciais?

O projeto deverá responder às perguntas sustentadas pelos dados disponíveis e identificar explicitamente quando não houver dados suficientes para uma conclusão.

Público-alvo
Recrutadores de tecnologia e dados.
Empresas de e-commerce.
Marketplaces.
SaaS.
Consultorias de dados.
Agências de marketing digital.
Equipes de BI, CRM, Growth e MarTech.
Diferencial

O projeto não será apenas um conjunto de gráficos.

Deverá demonstrar um fluxo completo:

Dados brutos → transformação → modelagem → indicadores → visualização → insights → recomendações de negócio.

3. ESCOPO DO MVP
Funcionalidades obrigatórias
3.1. Dashboard executivo

Apresentar indicadores como:

Receita de vendas.
Quantidade de pedidos.
Ticket médio.
Evolução mensal da receita.
Distribuição das vendas por categoria.
Distribuição geográfica dos pedidos.
Indicadores de entrega.
Avaliações dos clientes, quando disponíveis.
3.2. Análise de produtos e vendas

Permitir identificar:

Categorias com maior volume de vendas.
Produtos com melhor desempenho.
Evolução das vendas ao longo do tempo.
Distribuição do valor dos pedidos.
Diferenças entre regiões.

É necessário documentar as definições utilizadas para receita, pedidos e ticket médio, incluindo o tratamento de cancelamentos, reembolsos e pedidos incompletos, conforme as informações disponíveis no dataset.

3.3. Customer Intelligence

Implementar segmentação de clientes utilizando RFM:

Recency: tempo desde a última compra.
Frequency: frequência de compras.
Monetary: valor monetário das compras.

Criar segmentos interpretáveis, como clientes recentes, recorrentes, de alto valor e potencialmente inativos.

Os nomes, limites e regras de cada segmento deverão ser documentados. Não apresentar uma classificação heurística como se fosse um modelo preditivo validado.

3.4. Insights de negócio

Criar uma seção de análises que explique:

O que foi observado.
Qual indicador sustenta a conclusão.
Qual período foi analisado.
Quais são as limitações.
Qual ação poderia ser testada pelo negócio.

As recomendações devem derivar de análises reproduzíveis, não de resultados inventados.

Funcionalidades opcionais

Implementar somente depois que o MVP estiver funcional:

Análise de campanhas de marketing.
CAC, ROAS e LTV.
Funil de conversão.
Retenção e coortes.
Previsão de vendas.
Assistente de IA para gerar resumos executivos.
Autenticação de usuários.
Integração com APIs externas.
Testes de hipóteses ou experimentos de marketing.

Essas funcionalidades não devem atrasar a primeira entrega.

4. FONTES DE DADOS
Dataset principal

Brazilian E-Commerce Public Dataset by Olist.

Link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Motivo da escolha

O dataset oferece dados relacionais de e-commerce e permite explorar:

Clientes.
Pedidos.
Itens dos pedidos.
Produtos.
Pagamentos.
Avaliações.
Vendedores.
Localização e dados geográficos.
Datas de compra, aprovação e entrega.

Isso possibilita demonstrar SQL, modelagem relacional, transformação de dados, indicadores e análise comercial sem precisar construir um sistema de coleta de dados do zero.

Cuidados com os dados
Verificar os termos de uso e a licença antes da publicação.
Documentar a origem dos dados.
Não tratar os dados como dados reais de uma empresa contratante.
Não presumir que existam custos de campanhas de marketing.
Não calcular CAC ou ROAS sem os dados necessários.
Identificar claramente quaisquer dados sintéticos adicionados.
Documentar limitações, valores ausentes e regras de limpeza.
Dados adicionais de marketing

Se necessário, criar um pequeno dataset sintético contendo:

Data.
Canal de aquisição.
Investimento publicitário.
Impressões.
Cliques.
Conversões atribuídas.
Receita atribuída.

Os dados devem ser marcados como simulados e utilizados apenas para demonstrar a lógica dos indicadores.

Os resultados sintéticos não poderão ser apresentados como evidências reais do dataset Olist.

5. STACK TECNOLÓGICA
Backend
Python.
FastAPI.
Pydantic.
SQLAlchemy, se adequado à implementação.
pytest.

Responsabilidades:

Expor os indicadores através de endpoints.
Validar parâmetros e filtros.
Centralizar a lógica de negócio.
Consultar a camada analítica.
Documentar a API com OpenAPI.
Disponibilizar mensagens de erro consistentes.
Banco de dados
PostgreSQL.

Responsabilidades:

Armazenar dados preparados.
Disponibilizar tabelas analíticas.
Executar consultas SQL.
Sustentar os indicadores do dashboard.
Processamento de dados
Python.
pandas.
SQL.

Responsabilidades:

Ler os arquivos originais.
Validar e limpar os dados.
Tratar datas, valores ausentes e duplicidades.
Criar tabelas de preparação.
Produzir tabelas analíticas reproduzíveis.
Frontend
Next.js.
TypeScript.
Uma biblioteca de gráficos, como Recharts.
Uma solução de estilização consistente, como Tailwind CSS.

Responsabilidades:

Apresentar o dashboard.
Implementar filtros.
Consumir a API FastAPI.
Exibir indicadores, gráficos e insights.
Oferecer uma interface responsiva.
Infraestrutura e qualidade
Git e GitHub.
Docker e Docker Compose.
pytest.
Testes de integração.
Variáveis de ambiente.
CI com GitHub Actions, se viável.
Deploy público do frontend e backend.
Decisões de escopo
Não utilizar Flutter na primeira versão, pois o foco é um dashboard web.
Não introduzir Node.js como backend adicional.
Não implementar microsserviços.
Não adicionar autenticação sem uma necessidade concreta.
Não introduzir Airflow, Kafka ou infraestrutura distribuída no MVP.
Não adicionar IA antes de validar os indicadores e a qualidade dos dados.

O objetivo é demonstrar capacidade técnica e julgamento de engenharia, não acumular tecnologias no currículo.

6. ARQUITETURA PROPOSTA

Fluxo principal:

Os arquivos CSV originais são obtidos a partir do dataset.
Um pipeline Python valida, limpa e transforma os dados.
Os dados preparados são carregados no PostgreSQL.
A camada analítica disponibiliza tabelas e consultas para os indicadores.
O backend FastAPI expõe os indicadores por endpoints REST.
O frontend Next.js consulta a API.
O usuário aplica filtros e visualiza os resultados.
A seção de insights apresenta interpretações fundamentadas nos dados.

A primeira versão pode utilizar uma arquitetura simples, com um único backend, um único frontend e um banco PostgreSQL.

Modelagem de dados

A modelagem analítica deve ser definida depois de inspecionar as tabelas originais.

Uma estrutura candidata é:

fact_orders: dados de pedidos e valores agregados.
fact_order_items: itens de cada pedido.
dim_customers: informações dos clientes.
dim_products: informações dos produtos.
dim_sellers: informações dos vendedores.
dim_date: calendário analítico.
fact_marketing_campaigns: dados sintéticos opcionais de campanhas.

A estrutura definitiva dependerá das regras de negócio e dos dados efetivamente disponíveis.

É importante evitar duplicação de valores: por exemplo, associar um pedido a vários itens e depois somar repetidamente o total do pedido pode inflar a receita.

Os indicadores devem respeitar o nível de granularidade de cada tabela.

7. ESTRUTURA INICIAL DO REPOSITÓRIO

Estrutura proposta para um monorepo:

ecommerce-growth-intelligence/
├── README.md
├── docker-compose.yml
├── .env.example
├── .gitignore
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── ROADMAP.md
│   ├── DATA_DICTIONARY.md
│   ├── BUSINESS_METRICS.md
│   ├── ARCHITECTURE.md
│   └── DECISIONS.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   └── load_data.py
├── sql/
│   ├── staging/
│   ├── marts/
│   └── analysis/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── repositories/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
└── .github/
    └── workflows/


Essa estrutura é uma proposta inicial, não uma obrigação de criar todos os diretórios no primeiro dia.

O repositório deverá evoluir de acordo com as necessidades reais. Não criar arquivos vazios ou camadas arquiteturais sem propósito.

Os dados brutos não devem ser enviados ao GitHub sem verificar tamanho, licença e necessidade. O arquivo .gitignore deverá impedir a publicação acidental de datasets e segredos.

8. API: PRIMEIROS ENDPOINTS PROPOSTOS

A API poderá começar com os seguintes endpoints:

GET /health

Verifica se o serviço está operacional.

GET /api/v1/overview

Retorna os principais KPIs.

GET /api/v1/sales/trends

Retorna a evolução das vendas por período.

GET /api/v1/sales/categories

Retorna indicadores por categoria de produto.

GET /api/v1/customers/segments

Retorna a distribuição de clientes por segmento RFM.

GET /api/v1/orders/delivery

Retorna indicadores de entrega.

GET /api/v1/insights

Retorna os insights de negócio calculados.

Os parâmetros de filtro poderão incluir datas, categoria e região, quando forem relevantes para o endpoint.

As respostas devem ter contratos documentados, tipos definidos e testes.

Os endpoints são candidatos iniciais e poderão ser ajustados durante o desenvolvimento.

9. MÉTRICAS E DEFINIÇÕES DE NEGÓCIO

Criar um documento BUSINESS_METRICS.md com as definições exatas.

Exemplos:

Receita de vendas: valor definido a partir dos dados disponíveis, com regras documentadas para cancelamentos, pagamentos e reembolsos.

Quantidade de pedidos: número distinto de pedidos elegíveis para a análise.

Ticket médio: receita elegível dividida pela quantidade de pedidos elegíveis, respeitando o mesmo período e universo de pedidos.

Atraso de entrega: diferença entre a data estimada e a data efetiva de entrega, quando ambas estiverem disponíveis.

RFM: segmentação por recência, frequência e valor monetário, calculados para uma data de referência definida.

CAC: investimento de aquisição dividido pela quantidade de novos clientes atribuídos à aquisição, quando houver dados suficientes.

ROAS: receita atribuída à publicidade dividida pelo investimento publicitário correspondente.

LTV: valor de cliente ao longo do relacionamento, cuja definição dependerá do horizonte temporal e do método de cálculo.

Não assumir que faturamento, valor de pedidos, pagamentos recebidos e receita líquida são conceitos equivalentes.

10. ROADMAP E TIMELINE
Fase 0 — Planejamento

Status: EM ANDAMENTO.

Definir o objetivo profissional.
Definir o conceito do produto.
Escolher o dataset inicial.
Propor a stack tecnológica.
Definir o escopo preliminar.
Criar o documento mestre.
Confirmar o ambiente de desenvolvimento.
Criar o repositório GitHub.
Fase 1 — Exploração dos dados

Previsão: dias 1–2.

Baixar e inspecionar o dataset.
Documentar as tabelas e colunas.
Identificar chaves primárias e relacionamentos.
Investigar valores ausentes e duplicidades.
Definir as regras iniciais de negócio.
Produzir o dicionário de dados.

Critério de conclusão: compreender as tabelas e documentar as principais limitações dos dados.

Fase 2 — Banco de dados e pipeline

Previsão: dias 3–4.

Criar o ambiente PostgreSQL.
Implementar o carregamento dos dados.
Criar as transformações necessárias.
Definir a modelagem analítica.
Implementar validações.
Documentar as métricas.

Critério de conclusão: pipeline reproduzível e dados disponíveis para consulta SQL.

Fase 3 — Análises SQL

Previsão: dias 5–6.

Consultas de receita e pedidos.
Evolução temporal.
Desempenho por categoria.
Análise de entrega e avaliações.
Segmentação RFM.
Identificação de pelo menos três insights sustentados pelos dados.

Critério de conclusão: indicadores reproduzíveis e resultados documentados.

Fase 4 — Backend

Previsão: dias 7–8.

Criar aplicação FastAPI.
Implementar endpoints.
Criar schemas de resposta.
Implementar filtros.
Adicionar testes.
Documentar a API.

Critério de conclusão: endpoints funcionais e testados.

Fase 5 — Frontend e dashboard

Previsão: dias 9–11.

Criar aplicação Next.js.
Implementar layout.
Criar cards de KPIs.
Criar gráficos.
Conectar o frontend à API.
Implementar filtros.
Tratar carregamento e erros.
Validar a experiência em dispositivos diferentes.

Critério de conclusão: dashboard funcional utilizando dados reais do dataset.

Fase 6 — Qualidade e publicação

Previsão: dias 12–14.

Revisar testes.
Configurar Docker Compose.
Configurar variáveis de ambiente.
Revisar o README em inglês.
Criar capturas de tela.
Publicar frontend e backend.
Gravar uma demonstração curta.
Adicionar o projeto ao currículo e ao LinkedIn.

Critério de conclusão: outra pessoa consegue compreender o projeto, executá-lo seguindo a documentação e experimentar a aplicação publicada.

Fase 7 — Evolução estratégica

Executar depois do MVP.

Adicionar um conjunto sintético de campanhas.
Demonstrar CAC e ROAS com ressalvas documentadas.
Desenvolver análises de coorte e retenção.
Adicionar uma camada opcional de BI.
Avaliar dbt para transformação e testes SQL.
Adicionar geração de resumos com IA.
Melhorar a infraestrutura conforme necessário.
Observação sobre a timeline

Os prazos são estimativas. O objetivo é entregar um MVP em aproximadamente duas semanas de trabalho focado, não cumprir datas artificialmente.

Se alguma fase exigir mais tempo, atualizar o status e a previsão, sem comprometer a qualidade dos dados ou a clareza das métricas.

11. PADRÕES DE DESENVOLVIMENTO
Implementar uma etapa de cada vez.
Priorizar entregas pequenas e funcionais.
Explicar decisões arquiteturais relevantes.
Não criar funcionalidades antes de validar sua necessidade.
Escrever testes para regras de negócio importantes.
Não inventar dados, resultados ou benchmarks.
Não publicar credenciais ou segredos.
Manter o README atualizado.
Usar nomes claros para variáveis, funções, tabelas e endpoints.
Escrever a documentação do projeto em inglês, visando recrutadores internacionais.
Manter as explicações e o planejamento em português, salvo solicitação contrária.
Atualizar este documento quando houver mudanças relevantes na arquitetura, no escopo ou no status.
Critério para considerar uma tarefa concluída

Uma tarefa só deve ser marcada como concluída quando:

A implementação estiver pronta.
Os testes pertinentes passarem.
A validação dos resultados estiver feita.
A documentação necessária estiver atualizada.

Se uma etapa não tiver sido executada no ambiente real, ela deve permanecer pendente, mesmo que o código tenha sido sugerido ou escrito em uma conversa.

12. CONTROLE DE PROGRESSO ENTRE CONVERSAS

Este documento é a fonte principal de contexto do projeto.

Ao iniciar uma nova conversa, o desenvolvedor deverá enviar este documento e, se possível, o estado atual do repositório, os arquivos relevantes e a saída dos últimos testes.

O assistente deverá:

Ler o documento antes de sugerir mudanças.
Identificar a última fase concluída.
Verificar as tarefas pendentes.
Continuar a partir da próxima tarefa concreta.
Evitar repetir etapas já concluídas.
Respeitar as tecnologias e decisões existentes.
Sugerir alterações no documento mestre quando necessário.
Atualizar a timeline somente com informações confirmadas.
Não afirmar que comandos foram executados ou testes passaram sem evidências.
Preferir mudanças pequenas e verificáveis.
Registro de sessões

Ao final de cada sessão de desenvolvimento, registrar:

Data.
Objetivo da sessão.
Arquivos criados ou modificados.
Decisões técnicas tomadas.
Comandos executados.
Testes realizados e resultados.
Problemas encontrados.
Próxima tarefa recomendada.
13. ESTADO ATUAL DO PROJETO

Última atualização: 20/10/2026.

Fase atual: Fase 0 — Planejamento.

Status de implementação: ainda não confirmado.

Repositório GitHub: não informado.

Ambiente de desenvolvimento: não informado.

Banco de dados: não configurado ou ainda não confirmado.

Dataset: escolhido, mas download e inspeção ainda não confirmados.

Backend: não implementado ou ainda não confirmado.

Frontend: não implementado ou ainda não confirmado.

Deploy: não iniciado ou ainda não confirmado.

Próxima ação recomendada: verificar o ambiente disponível, criar o repositório e iniciar a inspeção do dataset antes de definir a modelagem definitiva.

14. INSTRUÇÃO PARA CONTINUAR O PROJETO EM OUTRO CHAT

Estamos desenvolvendo o E-commerce Growth Intelligence, um projeto de portfólio profissional para demonstrar competências em Python, FastAPI, SQL, PostgreSQL, Next.js, análise de dados, BI, e-commerce e marketing analytics.

Leia este documento integralmente e use-o como contexto principal.

Antes de propor qualquer implementação:

Identifique a fase atual na seção 13.
Consulte a timeline na seção 10.
Considere apenas tarefas comprovadamente concluídas.
Proponha a próxima tarefa de forma incremental.
Explique o objetivo, os arquivos envolvidos e os critérios de validação.
Quando houver código, forneça instruções executáveis e explique como verificar o resultado.
Ao final da sessão, apresente um resumo atualizado do progresso e as mudanças necessárias neste documento.

Não recomece o projeto do zero. Não assuma que arquivos, bancos de dados, ambientes ou serviços foram criados se isso não estiver documentado.

Objetivo imediato: sair do planejamento e começar a implementar o projeto, começando pelo ambiente de desenvolvimento e pela exploração dos dados.