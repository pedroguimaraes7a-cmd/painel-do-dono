import re, json, shutil, os
from PIL import Image
import numpy as np, colorsys
SRC="/home/claude/painel_src/src.html"; OLD="/home/claude/painel"
src=open(SRC,encoding="utf-8").read()
ED={"basico":dict(title="Meu Painel do Dono",short="Meu Painel",theme="#a8322a",v="painel-basico-v1"),
    "avancado":dict(title="Meu Painel do Dono Avançado",short="Painel Av.",theme="#1f3a68",v="painel-avancado-v1")}
def tint(im):
    a=np.array(im.convert("RGBA")).astype(float)
    rgb=a[...,:3]/255
    mx=rgb.max(-1); mn=rgb.min(-1); d=mx-mn
    r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
    red=(r>=g)&(r>=b)&(d>0.25)&(g<0.45)   # fundo vermelho; moeda dourada tem g alto
    out=a.copy()
    # vermelho -> azul marinho (troca canais r<->b e escurece um pouco)
    nr=b[red]*255*0+ (rgb[...,2][red]*0.6+ rgb[...,0][red]*0.15)*255
    out[...,0][red]=rgb[...,0][red]*255*0.22
    out[...,1][red]=rgb[...,0][red]*255*0.36
    out[...,2][red]=rgb[...,0][red]*255*0.66
    return Image.fromarray(out.clip(0,255).astype("uint8"),"RGBA")
for ed,c in ED.items():
    d=f"{OLD}/{ed}"; os.makedirs(d,exist_ok=True)
    h=src.replace('var EDICAO = "basico";',f'var EDICAO = "{ed}";',1)
    h=h.replace("<title>Meu Painel do Dono</title>",f"<title>{c['title']}</title>",1)
    h=h.replace('content="Painel">',f'content="{c["short"]}">',1)
    h=h.replace("#a8322a",c["theme"]) if ed=="avancado" and False else h
    open(f"{d}/index.html","w",encoding="utf-8").write(h)
    m=json.load(open(f"{OLD}/manifest.webmanifest"))
    m["name"]=c["title"]; m["short_name"]=c["short"]; m["theme_color"]=c["theme"]
    if ed=="avancado": m["description"]="Controle de caixa, lucro, preços, contas a pagar e receber e metas do seu negócio."
    json.dump(m,open(f"{d}/manifest.webmanifest","w"),ensure_ascii=False,indent=2)
    sw=open(f"{OLD}/sw.js").read().replace('"painel-v1"',f'"{c["v"]}"')
    open(f"{d}/sw.js","w").write(sw)
    for f in ["icon-192.png","icon-512.png","icon-maskable-512.png","apple-touch-icon.png"]:
        im=Image.open(f"{OLD}/{f}")
        (tint(im) if ed=="avancado" else im.convert("RGBA")).save(f"{d}/{f}")
print("ok")
