import json
import traceback

class IMS():
    

    def salvarAspf(self,dados,conexao):
        try:
            # print(dados.formulario)

            dados = json.dumps(dados.formulario)

            dados = json.loads(dados)


    
            idpesquisa = dados['idpesquisa']
            idprojeto = dados['idprojeto']
            usuario = dados['usuario']
            pesquisa = dados['pesquisas']

            # print(idpesquisa,idprojeto,usuario)

            pesquisa = json.loads(pesquisa)

            dadosPesquisa = json.loads(pesquisa['IMS']['data'])

            produtos = pesquisa['IMS']['produtos']
            
            listagem = list(dadosPesquisa.keys())
           
            data = list(filter(lambda x: x[:9] == 'indicador',listagem))

            
            
            connect = conexao.connection()

            cursor = connect.cursor()

            try:

                cursor.execute(f'''
                    select id,username,first_name,last_name,email  from auth_user au where UPPER(username) = upper('{usuario}') 
                ''')
                
                dadosUser = cursor.fetchone()

                

                cursor.execute(f'''
                    select max(questionario) from ims i 
                ''')

                numForm = cursor.fetchone()

                cursor.execute(f'''

                    insert
                    into
                    ims (
                        dtmov,
                        nomeentrevistador,
                        profissao,
                        cellentrevistador,
                        temwhatsentrevistador,
                        emailentrevistador,
                        nomeprodutor,
                        nomepropriedade,
                        localizacaogps,
                        enderecoprodutor,
                        telfixoprodutor,
                        celprodutor,
                        temwhatsprodutor,
                        emailprodutor,
                        areatotal,
                        areacultivo,
                        areapastagens,
                        areapreservada,
                        id,
                        idescolar,
                        idestado,
                        idsistema,
                        idcaracterizacao,
                        idterritor,
                        idresponsavel,
                        idprojeto,
                        idregional,
                        situacao,
                        questionario
                       
                    )
                    values 
                    (
                        current_date,
                        '{dadosUser[1]}',
                        '{dadosPesquisa['profissao']}',
                        '{dadosPesquisa['celularEntrevistador']}',
                        '{'S' if dadosPesquisa['temwhatsEntrevistador'] == 'sim' else 'N'}',
                        '{dadosPesquisa['emailEntrevistador']}',
                        '{dadosPesquisa['produtor']}',
                        '{dadosPesquisa['nomePropriedade']}',
                        '{dadosPesquisa['localizacaoGps']}',
                        '{dadosPesquisa['enderecoProdutor']}',
                        '{dadosPesquisa['telefoneFixoProdutor']}',
                        '{dadosPesquisa['celularProdutor']}',
                        '{dadosPesquisa['temwhatsProdutor']}',
                        '{dadosPesquisa['emailProdutor']}',
                        {dadosPesquisa['areaTotal']},
                        {dadosPesquisa['areaCultivo']},
                        {dadosPesquisa['areaPastagens']},
                        {dadosPesquisa['areaPreservada']},
                        {dadosUser[0]},
                        {str(dadosPesquisa['escolaridadeinput']).split('-')[0]},
                        '{str(dadosPesquisa['estado']).split('-')[0]}',
                        {str(dadosPesquisa['sistemaProducaoInput']).split('-')[0]},
                        {str(dadosPesquisa['tipocaracterizacaoInput']).split('-')[0]},
                        {str(dadosPesquisa['tipocaracterizacaoterritorioInput']).split('-')[0]},
                        {(dadosPesquisa['tipoResponsavel']).split('-')[0]},
                        {idprojeto},
                        {str(dadosPesquisa['regiao']).split('-')[0]},
                        'S',
                        {numForm[0]+1}
                        
                    )
                    RETURNING idims;
                ''')

                

                dados = cursor.fetchall()[0]

                for produto in produtos:

                    # print(str(produto['produto']).split('-')[0],produto['quantidade'],dados,str(dadosPesquisa['regiao']).split('-')[0])

                    cursor.execute(f'''
                        insert
                            into
                            imsprodutosproduzidos 
                            (
                                qtdproduzida,
                                situacao,
                                idims,
                                idprod,
                                idregional
                            )
                        values 
                            (
                                {produto['quantidade']},
                                'S',
                                {dados[0]},
                                {str(produto['produto']).split('-')[0]},
                                {str(dadosPesquisa['regiao']).split('-')[0]}
                            )
                    ''')

                

                for indicador in data:
         
                
                
                    cursor.execute(f'''
                        insert
                        into
                        imsindicadoresresposta 
                        (
                            situacao,
                            idims,
                            idregional,
                            idpergunta,
                            idresposta
                        ) 
                        values
                        (
                            'S',
                            {dados[0]},
                            {str(dadosPesquisa['regiao']).split('-')[0]},
                            {str(indicador).split('-')[3]},
                            {dadosPesquisa[indicador]}

                                       
                        )
                    ''')

                connect.commit()


                return dados[0]
            
            except Exception as error:
               
                connect.rollback()
                raise Exception(error)
        except Exception as error:
           
            dados = False
            return dados
        
        #ims = cursor.fetchall()


ims = IMS()