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