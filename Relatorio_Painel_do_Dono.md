# Relatório do projeto Meu Painel do Dono (para revisão por outra IA)

Data: 30/09/2026 · Dono: Pedro Guimarães (Itaquaquecetuba) · Marca: Bumerân

## Objetivo
Gerar renda online independente (meta inicial R$ 5.000/mês) vendendo aplicativos de controle financeiro para pequenos comércios locais (pizzaria, barbearia, lanchonete, salão, padaria, loja de roupa, lava-rápido, pet shop, autônomos). Prospecção manual de desconhecidos pelo WhatsApp Business, com Google Maps para achar leads. O Instagram Bumerân Edu continua focado em educação, sem vendas.

## Produto (dois apps separados, pagamento único)
- **Básico**: lançar entradas/saídas, caixa x lucro (retirada não conta como custo), categorias prontas por nicho + próprias, histórico, gráficos, backup JSON e CSV.
- **Avançado**: tudo do Básico + Preços (precificação com taxas e margem), Contas a pagar e a receber (inclui fiado, gera lançamento ao pagar), Meta do mês, ponto de equilíbrio, relatório mensal em PDF.
- Tecnologia: HTML único, JavaScript puro, PWA instalável por QR/link, funciona offline. Dados só no celular do cliente (localStorage). Sem servidor, sem custo de infraestrutura, sem suporte de dados (LGPD simples).
- Testes: 42 testes de lógica novos (+69 do app anterior), testes de navegador em 360/390 px, fluxo contas→caixa, backup entre versões.

## Site
Página de vendas com os dois planos, demos (`/basico/#demo`, `/avancado/#demo`), botão de WhatsApp e calculadora grátis de lucro da pizza (isca para prospecção). Arquivo: `painel-do-dono.zip`.

## Decisões em aberto (opinião bem-vinda)
1. **Preço**: hipótese atual Básico R$ 47 / Avançado R$ 97, com preço "de" mais alto como âncora. Página está com R$ 27/R$ 67 de lançamento (Pedro acha barato).
2. **Cobrança**: Hotmart (checkout com cartão e Pix, entrega do link por e-mail) x Pix direto no WhatsApp.
3. **Repositório**: público (GitHub Pages grátis) x privado (Cloudflare Pages/Netlify). Um app estático sempre pode ser copiado por quem tem o link; a proteção real é distribuir o link só a compradores e, depois da primeira venda, código de ativação.
4. **Receita recorrente**: ideias: revisão financeira mensal (o cliente manda o backup, Pedro devolve 3 pontos de atenção), implantação paga (configurar categorias e produtos), pacote de precificação de cardápio.
5. **Endereço final**: os dados ficam presos ao endereço do site; precisa ser definitivo antes da primeira venda.

## Cuidados
Aviso de que não é contabilidade; direito de arrependimento de 7 dias em venda online; MEI/Pix PF a confirmar com contador; abordagem fria manual e em baixo volume (WhatsApp bloqueia disparo em massa).

## Atualização 30/09/2026: licença, garantia e antifraude de reembolso
- "Teste grátis" removido do site. Garantia de 7 dias para compras online (CDC art. 49).
- Cada comprador recebe link pessoal de ativação (código assinado ECDSA P-256, verificado no próprio app, sem servidor). Sem o código o app não abre.
- Reembolso/estorno: o dono coloca o id da licença em `revogados.json` no site; o app confere ao abrir com internet e passa a exibir "Licença desativada", com opção de baixar backup dos próprios dados. Limitação: offline o app segue até a primeira checagem online; quem nunca abre com internet escapa (risco baixo, dado o público).
- Chave privada só com o dono (fora do repositório). Gerador local `gerador-de-licencas.html` cria licenças e o arquivo de revogação.
- Preços: exemplos do formulário seguem o nicho escolhido (ex.: pizzaria = "Pizza de mussarela grande"; salão = "Unha em gel"; geral = exemplos genéricos).
- Próximo: automatizar entrega/revogação via webhook da Hotmart (Cloudflare Worker) após as primeiras vendas.
