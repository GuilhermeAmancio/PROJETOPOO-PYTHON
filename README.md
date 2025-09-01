# POOprojeto

Dupla: Pietro Oliveira Lima e Guilherme Ferreira Amâncio

*Nota
Como durante o desenvolvimento do projeto utilizamos uma pasta de teste separada do github, quando finalizamos notamos que quando tentávamos executar a aplicação python na pasta do github, esta dava erros que não conseguíamos resolver, mas quando resolvemos testar criando um repositório separado só para a aplicação python, funcionou. Então resolvemos deixar como 2 repositórios separados para garantir o funcionamento de ambos. O ReadMe de ambos os repositórios contém todas as informações, então qualquer um pode ser lido para compreender

links dos repositórios:
Repositório Java:
https://github.com/PietroLima04/POOprojeto

Repositório Python:
https://github.com/GuilhermeAmancio/PROJETOPOO-PYTHON

O conceito do projeto era analisar os dados da covid no estado de Sergipe. Para isso, criamos apps em java e python que possuem o mesmo conceito, que por meio de uma lista das cidades, ao escolher uma delas, abre-se uma nova aba com as informações relevantes quanto ao covid naquela cidade. Devido as diferenças nas linguagens, conseguimos implementar em python todas as cidades, mas para manter um projeto mais conciso e organizado com java, decidimos utilizar as 10 cidades mais populosas nesta versão, mas em compensação, conseguimos tranquilamente implementar os gráficos na aplicação java por meio do scenebuilder, enquanto que, devido a uma certa dificuldade, não os implementamos na aplicação python.

A fonte utilizada foi: dados tabulados pelo pesquisador Wesley Cota, da UFV, com base em números das secretarias estaduais da Saúde coletados pelo Brasil.IO. O projeto 'Modelagem matemática da disseminação geográfica da Covid-19' faz parte do Programa de Combate a Epidemias da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (Capes). A base também é usada pela universidade Johns Hopkins, referência mundial no acompanhamento dos dados da pandemia.

# Instalação e Uso

Para instalar a aplicação Java, primeiro tenha em mente que este projeto foi feito no Eclipse, então estas instruções são feitas com base nas configurações básicas da IDE para qualquer projeto do tipo. Acesse o arquivo pelo diretório do github, e observe se as bibliotecas corretas estão implementadas, caso não estejam, é necessário implementá-las. As bibliotecas são "JavaFX(Uma criada pelo próprio usuário com os arquivos da lib do javafx)", "JavaFX SDK" e "JRE System Library (o seu workspace deve estar de acordo com a versão do java instalada em sua máquina)". Agora para certificar que a aplicação rode corretamente, clique com o botão direito no projeto, vá para Run as->Run Configurations, na janela que abre, certifique-se a Main Class seja application.Main, e o campo Project deve estar de acordo. agora na aba arguments, em VM arguments, é preciso colar isso aqui :
--module-path "lib*" --add-modules javafx.controls,javafx.fxml
--enable-native-access=javafx.graphics

Este lib* é o campo que você substituirá com o caminho da pasta onde a lib de seu jdk se localiza.

Agora que as configurações básicas de um projeto JavaFX foi estabelecido, para conectá-lo com o SceneBuilder, o caminho é Window->Preferences->JavaFX->SceneBuilderExecutable, onde conectará o executável do SceneBuilder da máquina.

Após tudo configurado corretamente, é apenas rodar o projeto com a configuração criada.

Para instalar a aplicação Python, tenha em mente que o PROJETOPOO-PYTHON foi testado na IDE VS Code. Basta executar o arquivo main.py.

# Discussão da orientação a objetos na segunda linguagem

Vindo de uma linguagem como Java, a transição para a Orientação a Objetos em Python foi mais fluida e intuitiva, sentindo-se mais natural e direta. No entanto, o verdadeiro desafio surgiu ao integrar esses conceitos na construção da interface gráfica. Embora a lógica de classes e objetos para o processamento de dados fosse clara e fácil de implementar, a criação das janelas e a organização dos elementos visuais no PyQt apresentaram uma curva de aprendizado mais íngreme, exigindo experimentação e paciência para alinhar cada componente e garantir que a aplicação funcionasse exatamente como o planejado.
