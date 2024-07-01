# usada para verificar se algum valor NÃO está na lista

# em um site veja se a pessoa está banida de realizar comentários

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user}, você pode comentar se você quiser')
