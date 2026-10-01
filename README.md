# Bumerân · Meu Painel do Dono

- `index.html` – página inicial da Bumerân
- `financas/` – página de vendas do Meu Painel do Dono e seus aplicativos
- `financas/basico/` e `financas/avancado/` – os dois aplicativos (gerados de `fonte-painel.html` por `build.py`)
- `financas/calculadora/` – calculadora grátis de lucro da pizza
- `Relatorio_Painel_do_Dono.md` – resumo do projeto e decisões


## Licença e ativação (desde 30/09/2026)
- Cada compra recebe um link pessoal `.../financas/<edicao>/#k=<codigo>` (código assinado ECDSA P-256). Sem ele o app mostra a tela de ativação.
- A chave **privada** fica só com o dono (pasta `privado/`, fora do repositório). No repositório há só a chave pública (embutida no app no build).
- Revogação: incluir o id da licença em `revogados.json` (`{"ids":["abc123"]}`). O app confere ao abrir com internet e passa a mostrar "Licença desativada" (com opção de baixar backup).
- Garantia de 7 dias: ao devolver o dinheiro, revogar a licença.

## Endereço oficial
https://somosbumeran.com.br (GitHub Pages, DNS no Registro.br, HTTPS ativo). Domínio registrado em 30/09/2026, válido até 30/09/2028.
