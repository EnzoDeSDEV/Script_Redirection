import csv

with open('../csv/test.csv', 'r') as csvfile:
    page = []
    redirection= []
    delimiter = ";"
    lecteur = csv.DictReader(csvfile, delimiter = ";")
    for ligne in lecteur:
           page.append(ligne['Page'])
           redirection.append(ligne['Redirections'])
    with open('../csv/rewrite_rules.csv', 'w', encoding='utf-8') as sortie:
        for url,redir in zip(page, redirection):
                    if url.startswith('espace-abonnement.lavoixdunord.fr/'):
                          url = url[len('espace-abonnement.lavoixdunord.fr'):]
                          sortie.write(f"RewriteRule ^{url}$ {redir} [R=307,QSA,L]\n")