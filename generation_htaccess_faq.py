import csv

page = []
other_page = []
redirection_faq = []
redirection= []
delimiter = ";"
with open('liens_redirections_VDN.csv', 'r') as csvfile:
 lecteur = csv.DictReader(csvfile, delimiter = ";")
 for ligne in lecteur:
  if ligne['Redirections'] == 'https://abonnement.lavoixdunord.fr/faq':
   redirection_faq.append(ligne['Redirections'])
   page.append(ligne['Page'])
  else:
   other_page.append(ligne['Page'])
   redirection.append(ligne['Redirections'])


with open('rewrite_rules.txt', 'w', encoding='utf-8') as sortie:
    sortie.write("=========Fichier pour la FAQ=========\n")
    for url,redir in zip(page, redirection_faq):
        if url.startswith('espace-abonnement.lavoixdunord.fr/'):
            url = url[len('espace-abonnement.lavoixdunord.fr/'):]
        sortie.write(f"RewriteRule ^{url}$ {redir} [R=307,QSA,L]\n")


    sortie.write(f'=========Fichier pour les redirection classique=========\n')
    for url,redir in zip(other_page, redirection):
        if url.startswith('espace-abonnement.lavoixdunord.fr/'):
            url = url[len('espace-abonnement.lavoixdunord.fr/'):]
        sortie.write(f"RewriteRule ^{url}$ {redir} [R=307,QSA,L]\n")


