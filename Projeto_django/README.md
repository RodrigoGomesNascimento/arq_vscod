Este projeto consiste no aprendizado da utilização de django
O código aqui desenvolvido foi baseado nas aulas de Rafael, segue abaixo o link para as aulas no 
youtube.
https://www.youtube.com/watch?v=RrSLLDC3ys0&t=665s
========================================================================================

Anotações sobre a criação.
Foram criadas as pastas dentro do git para tentar atualizar e trabalhar em vários pcs, pois não tenho um fixo
comandos utilizados django-admin startproject (nome do projeto) cria a pasta onde ficará o projeto e o manage.py responsável por startar o projeto.
Para criar as tabelas na base de dados rodorar manage.py migrate dado o comando irá criar as tabelas no sqlite
mas ainda não tem usuario.
rodando o comando python manage.py runserver e acessando o /admin vc vera o servidor 
mas tem que criar um user com python manage.py createuser
Entrar no model para criar as tabelas.
depois de criar as tabelas e antes colocar a pastas criada do app no caso a 'core' no settings do projeto e depois rodar o comando python manage.py makemigrations core. vai criar um arquivo no migrate 
Apos rodar o comando python manage.py migrate core 0001(nome do arquivo onde esta o bd ou tb q ira subir  para o gerenciador do bd) se for um bd de produção e quiser ver o slq antes de subir rodar o comando 
python manage.py sqlmigrate core 0001
para aparecer no admin tem que registrar no admin.py
para criar a pagina e interação tem que ir no urls.py
pasta templetes.
Tem que colocar o caminho no settings.py na TEMPLATES DIR[]
foi encontrado o erro era o caminho if user is not None:
            login(request, user)
            return redirect('/')# tinha que ser assim sem o resto do end 
também foi criado o logout e necessario a importação de outras biblitecas, bem como a criação do metodo
outro detalhe foi o decoretor para não deixar acessar direto o index.
@login_required(login_url='/login')#tem que importar e para segurança se nao fica logado sem logar
Uma das vantagens do django é criar os templates em camadas, onde as mais estaticas são feitas uma unica vez e reaproveitadas para outras, no caso do footer, header.
