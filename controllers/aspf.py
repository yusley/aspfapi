import json
import traceback

def filterOptions(mudancasForm):

    mudancas = {
        'ULTIMA': '',
        'PENULTIMA': '',
        'ANTEPENULTIMA':''
    }

    def criarEstrutura(element):
            
        mudancas[element['orderMudanca']] = element

        return element

    list(map(criarEstrutura,mudancasForm))


    return mudancas


class ASPF():

    def salvarAspf(self,dados,conexao):

        try:


            pesquisas = json.loads(dados.formulario['pesquisas'])

            with open('./teste.txt', 'w') as arquivo:
                arquivo.write(str(pesquisas))

                arquivo.close()

            idprojeto = dados.formulario['idprojeto']
            
            
            
            dgfamilia = pesquisas['dgfamilia']
            
            patrimonios = pesquisas['patrimonio']

            culturasProducao = pesquisas['culturasProducao']

            autoconsumo = pesquisas['autoconsumo']

            assalariamento = pesquisas['indiceAssalariamento']

            transferenciaRenda = pesquisas['transferenciasRenda']

            condicoes = pesquisas['condicoesHabitacionais']

            avaliacao = pesquisas['avaliacaoEstrategica']



            mudancas = filterOptions(dgfamilia['mudanca'])
            
            
            
            
            
            

            connect = conexao.connection()

            cursor = connect.cursor()

            try:
                cursor.execute(f'''
                    insert
                    into 
                    unidadepesquisada
                    (
                        questionario,
                        anobase,
                        idlocalpesq,
                        sistema,
                        
                        dtpesquisa,
                        cidadepesquisada,
                        
                        nomeentevistado,
                        apelido,
                        chefefamilia,
                        naturalidade,
                        tempomoradia,
                        ultmudanca,
                        anoultmud,
                        ativultmud,
                        penultimamud,
                        anopenmud,
                        ativpenultmud,
                        antepenultimamud,
                        anoantepenmud,
                        ativantepenmud,
                        latitude,
                        longitude,
                        ramal,
                        lote,
                        tamanholote,
                        
                        estradasseringa,
                        estradascortadas,
                        farmaceutico,
                        fitoterapico,
                        filhosnolugar,
                        temfilhosmorandofora,
                        filhosmorandofora,
                        tipoacessoterra,
                        pagouservico,
                        
                        trabassallinha,
                        trabassalunidade,
                        distanciario,
                        distnciabr,
                        cidademaisprox,
                        transpcidadeprox,
                        cidadeqcomerc,
                        transpcidadecomerc,
                        dinheirocaixa,
                        tempogasto,
                        fezemprestimo,
                        quantodinheirocaixa,
                        possuiadivida,
                        
                        contasreceber,
                        diasgastoscomerc,
                        diasgastosfinanc,
                        diasgastoscompras,
                        pagouitr,
                        valoritr,
                        
                        valorpagotransporte,
                    
                        idregional,
                        idprojeto,
                        situacao
                    )
                    values
                    (
                        {dados.formulario['idpesquisa']},
                        '{str(dados.formulario['data']).split('/')[2]}',
                        {dados.formulario['localpesquisa']},
                        '{json.loads(dgfamilia['data'])['sistema']}',
                        '{str(dados.formulario['data']).split('/')[2]}-{str(dados.formulario['data']).split('/')[1]}-{str(dados.formulario['data']).split('/')[0]}',
                        {str(json.loads(dgfamilia['data'])['cidadeatual']).split('-')[0]},
                    
                        '{json.loads(dgfamilia['data'])['entrevistado']}',
                        '{json.loads(dgfamilia['data'])['apelido']}',
                        '{json.loads(dgfamilia['data'])['chefe']}',
                        '{str(json.loads(dgfamilia['data'])['naturalidade']).split('-')[0]}',
                        {str(json.loads(dgfamilia['data'])['timeLote'])},
                        '{mudancas['ULTIMA']['orderMudanca'] if mudancas['ULTIMA'] != '' else ''}',
                        '{mudancas['ULTIMA']['ano'] if mudancas['ULTIMA'] != '' else ''}',
                        {str(mudancas['ULTIMA']['atividades']).split('-')[0] if mudancas['ULTIMA'] != '' else "null"},
                        '{mudancas['PENULTIMA']['orderMudanca'] if mudancas['PENULTIMA'] != '' else ''}',
                        '{mudancas['PENULTIMA']['ano'] if mudancas['PENULTIMA'] != '' else ''}',
                        {str(mudancas['PENULTIMA']['atividades']).split('-')[0] if mudancas['PENULTIMA'] != '' else "null"},
                        '{mudancas['ANTEPENULTIMA']['orderMudanca'] if mudancas['ANTEPENULTIMA'] != '' else ''}',
                        '{mudancas['ANTEPENULTIMA']['ano'] if mudancas['ANTEPENULTIMA'] != '' else ''}',
                        {str(mudancas['ANTEPENULTIMA']['atividades']).split('-')[0] if mudancas['ANTEPENULTIMA'] != '' else "null"},
                        '{json.loads(dgfamilia['data'])['latitude']}',
                        '{json.loads(dgfamilia['data'])['longitude']}',
                        '{json.loads(dgfamilia['data'])['ramal']}',
                        '{json.loads(dgfamilia['data'])['lote']}',
                        {json.loads(dgfamilia['data'])['tamanhoLote']},
                    
                        {(json.loads(dgfamilia['data'])['seringaTerra'])},
                        {(json.loads(dgfamilia['data'])['seringaCortada'])},
                        '{'TRUE' if json.loads(dgfamilia['data'])['tipomedicamento'] == 'Farmaceutico' else 'FALSE'}',
                        '{'TRUE' if json.loads(dgfamilia['data'])['tipomedicamento'] == 'Fitoterapico' else 'FALSE'}',
                        {json.loads(dgfamilia['data'])['qtFilhosNoLocal']},
                        '{'S' if json.loads(dgfamilia['data'])['qtFilhosForaUPF'] == 'Sim' else 'N'}',
                        {"null" if json.loads(dgfamilia['data'])['simQuantos'] == 0 else json.loads(dgfamilia['data'])['simQuantos']},
                        {str(json.loads(dgfamilia['data'])['acessoTerra']).split('-')[0]},
                        '{'S' if json.loads(culturasProducao['dadosCulturas'])['pagouServicos'] == 'sim' else 'N'}',
                        
                        '{'S' if json.loads(culturasProducao['dadosCulturas'])['forcaTrabAssalaLinha'] == 'sim' else 'N'}',
                        '{'S' if json.loads(culturasProducao['dadosCulturas'])['forcaTrabAssalaConjunto'] == 'sim' else 'N'}',
                        {json.loads(dgfamilia['data'])['distanciaRio']},
                        {json.loads(dgfamilia['data'])['distanciaBr']},
                        '{str(json.loads(dgfamilia['data'])['cidadeProxima']).split('-')[0]}',
                        '{str(json.loads(dgfamilia['data'])['transporteCidade']).split('-')[0]}',
                        '{str(json.loads(dgfamilia['data'])['cidadeComercializa']).split('-')[0]}',
                        '{str(json.loads(dgfamilia['data'])['transporteComercializa']).split('-')[0]}',
                        '{'S' if json.loads(patrimonios['dadosPatrimonio'])['dinheiro'] == 'sim' else 'N'}',
                        {json.loads(dgfamilia['data'])['tempoChegarCidade']},
                        '{'S' if json.loads(patrimonios['dadosPatrimonio'])['emprestimo'] == 'sim' else 'N'}',
                        {json.loads(patrimonios['dadosPatrimonio'])['simDinheiro']},
                        '{'S' if json.loads(culturasProducao['dadosCulturas'])['possuiDivida'] == 'sim' else 'N'}',
                    
                        '{'S' if json.loads(patrimonios['dadosPatrimonio'])['contasaReceber'] == 'sim' else 'N'}',
                        {json.loads(culturasProducao['dadosCulturas'])['qtDiasUteisGastouProducao']},
                        {json.loads(culturasProducao['dadosCulturas'])['qtDiasUteisGastouFinanciamento']},
                        {json.loads(culturasProducao['dadosCulturas'])['qtDiasGastouCompras']},
                        '{'S' if float(json.loads(culturasProducao['dadosCulturas'])['pagouItr']) > 0 else 'N'}',
                        {json.loads(culturasProducao['dadosCulturas'])['pagouItr'] if float(json.loads(culturasProducao['dadosCulturas'])['pagouItr']) > 0 else ''},
                        
                        {json.loads(culturasProducao['dadosCulturas'])['pagouTransportes']},
                        
                        {(json.loads(dgfamilia['data'])['regiao'])},
                        {idprojeto},
                        'S'

                    )
                    RETURNING idquest;


                ''')
                # idform = [0]
                idform = cursor.fetchall()[0]

                contador = 0
                infofamilia = dgfamilia['infoFamilia'] if 'infoFamilia' in dgfamilia else []
                infofamiliaContinuacao = dgfamilia['infoFamiliaContinuacaoState'] if 'infoFamiliaContinuacaoState' in dgfamilia else []
                acessoEscola = dgfamilia['acessoEscola'] if 'acessoEscola' in dgfamilia else []

                if dgfamilia.get('infoFamilia') != 'None' and dgfamilia.get('infoFamiliaContinuacaoState') != 'None' and dgfamilia.get('acessoEscola') != 'None':
                    
                    for familia,continuacao,acesso in zip(infofamilia,infofamiliaContinuacao,acessoEscola):
                        
                        # 

                        cursor.execute(f'''
                            insert 
                            into 
                            dgfamilia (
                                idquest,
                                idprof,
                                idmotivo,
                                idescolar,
                                idperiodo,
                                iddeficiencia,
                                idparente,
                                nome,
                                idade,
                                sexo,
                                cor,
                                diasproducao,
                                horasdia,
                                gestante,
                                prenatal,
                                idassisente,
                                amamentou,
                                deficiente,
                                incapaztrabalhar,
                                maefalecida,
                                paimaeausente,
                                quemseausentou,
                                algumfilhomorreu,
                                quantosfilhosmor,
                                adoeceu,
                                anosestudo,
                                aindaestuda,
                                profissao,
                                trabalhanaarea,
                                temcapacitacoes,
                                qtostreinamentos,
                                gestantelocalatend
                            ) VALUES (
                                {idform[0]},
                                {str(familia['atividade']).split('-')[0]},
                                {str(acesso['seNaoPorque']).split('-')[0]},
                                {str(acesso['escolaridade']).split('-')[0]},
                                {str(continuacao['periodoMorteFilhos']).split('-')[0]},
                                {(str(continuacao['deficiente']).split('-')[0]).split('.')[0]},
                                {str(familia['grau']).split('-')[0]},
                                '{str(familia['nome'])}',
                                {str(familia['idade'])},
                                '{"M" if str(familia['sexo']).upper() != 'FEMININO' else 'F'}',
                                '{str(familia['cor'])}',
                                {str(familia['qtDiasSemanaProducao'])},
                                {str(familia['qtHorasDiasProducao'])},
                                '{'S' if str(familia['gestante']) == 'sim' else 'N'}',
                                '{'N' if str(familia['prenatal']) == 'nao' else 'S'}',
                                {str(familia['assistencia']).split('-')[0]},
                                '{'N' if str(familia['amamentou']) == 'nao' else 'S'}',
                                '{'N' if str(continuacao['deficiente'] ) == 'nao' else 'S'}',
                                '{'N' if str(continuacao['incapazTrabalhar'])  == 'nao' else 'S'}',
                                '{'N' if str(continuacao['maeFalecida'])  == 'nao' else 'S'}',
                                '{'N' if str(continuacao['paisAusentes'])  == '0' else 'S'}',
                                {'null' if str(continuacao['paisAusentes'])  == '0' else str(continuacao['paisAusentes'])},
                                '{'N' if str(continuacao['filhoMorreuLocal'])  == 'nao' else 'S'}',
                                {'null' if str(continuacao['filhoMorreuLocal'])  == 'nao' else str(continuacao['qtMortesFilhos']) if str(continuacao['qtMortesFilhos']) else 0},
                                '{'N' if str(continuacao['adoeceuUltimoAno'])  == '0' else 'S'}',
                                '{str(acesso['qtAnosEstudo'])}',
                                '{'N' if str(acesso['aindaEstuda'])  == 'Nao' else 'S'}',
                                '{'S' if str(acesso['algumaProfissao'])  == 'sim' else 'N'}',
                                '{'S' if str(acesso['trabalhaNaArea'])  == 'sim' else 'N'}',
                                '{'S' if str(acesso['treinamentos'])  == 'sim' else 'N'}',
                                {str(acesso['quantos'])},
                                {str(continuacao['localAtendimento']).split('-')[0]}
                                
                            )
                        ''')

                        contador += 1


                if dgfamilia.get('criacoesVedida') != 'None':
                
                    for criacoes in dgfamilia['criacoesVedida']:

                        

                        cursor.execute(f'''
                            insert
                            into
                            dgcriacoesvendidas 
                            (
                                idquest,
                                idprod,
                                areapastoocup,
                                areapastonaoocup,
                                qtdevendida,
                                valor,
                                unidade,
                                codlinha
                            )
                            values 
                            (
                                {idform[0]},
                                {str(criacoes['especificacao']).split('-')[0]},
                                {criacoes['areapastoocup']},
                                '{criacoes['areapastonaoocup']}',
                                {criacoes['qtvendida']},
                                '{criacoes['valor']}',
                                {str(criacoes['unidade']).split('-')[0]},
                                {str(criacoes['codlinha']).split('-')[0]}
                            )
                        ''')

                
                if dgfamilia.get('condicoesTerra') != 'None':

                    for criacoes in dgfamilia['condicoesTerra']:

                        

                        cursor.execute(f'''
                            insert 
                            into
                            dgusoterra
                            (
                                idquest,
                                idforma,
                                area,
                                qtdeareaabriu
                            )
                            values 
                            (
                                {idform[0]},
                                {str(criacoes['formauso']).split('-')[0]},
                                {criacoes['area']},
                                {criacoes['quantoAreaPeriodo']}
                                
                            )
                                
                        ''')


                if dgfamilia.get('culturas') != 'None':

                    for culturas in dgfamilia['culturas']:
                        
                        cursor.execute(f'''
                        insert 
                        into
                        dgculturasproduzidas
                        (
                            idquest,
                            vendsign,
                            cdlinha,
                            idprod,
                            jan,
                            fev,
                            mar,
                            abr,
                            mai,
                            jun,
                            jul,
                            ago,
                            set,
                            out,
                            nov,
                            dez,
                            area,
                            idunid,
                            qtde,
                            precounit,
                            consorcio,
                            cicloprodutivo
                        )
                        values
                        (
                            {idform[0]},
                            '{'S' if str(culturas['vendsign']) == 'sim' else 'N' }',
                            {str(culturas['codlinha']).split('-')[0]},
                            {str(culturas['especificacao']).split('-')[0]},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Janeiro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Fevereiro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Março',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Abril',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Maio',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Junho',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Julho',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Agosto',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Setembro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Outubro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Novembro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {'false' if str(list(filter(lambda x : x['mes'] == 'Dezembro',(culturas['cicloMeses'])))[0]['valor']) == 'False' else 'true'},
                            {str(culturas['area'])},
                            {str(culturas['unidade']).split('-')[0]},
                            {str(culturas['quantidade'])},
                            {str(culturas['preco'])},
                            {str(culturas['consorcio']).split('-')[0]},
                            {len(list(filter(lambda x : str(x['valor']) == 'True',(culturas['cicloMeses']))))}

                        )
                        ''')


                

                if patrimonios.get('benfeitorias') != 'None':

                    for benfeitoria in patrimonios['benfeitorias']:

                        

                        cursor.execute(f'''
                            insert
                            into
                            pabemfeitorias 
                            (
                            idquest,
                            cdtipobenf,
                            qde,
                            cdestagio
                            )
                            values
                            (
                                {idform[0]},
                                {str(benfeitoria['especificacao']).split('-')[0]},
                                {str(benfeitoria['quantidade'])},
                                {str(benfeitoria['estagio']).split('-')[0]}
                            )
                        ''')


                # 
                idconstrucao = 0
                counter = 0

                if patrimonios.get('construcao') != 'None':

                    for construcao in patrimonios['construcao']:

                        cursor.execute(f'''
                            insert 
                            into
                            paconstrucoes
                            (
                                
                                idquest,
                                cdtipobenf,
                                tempoconstruir,
                                npessoaconstruir,
                                tamanho,
                                comodos,
                                privada,
                                valor
                            )
                            values
                            (
                                {idform[0]},
                                {str(construcao['Benfeitorias']).split('-')[0]},
                                {construcao['tempoConstruir']},
                                {construcao['npessoaconstruir']},
                                {construcao['tamanho']},
                                {construcao['comodos']},
                                '{construcao['privada']}',
                                {construcao['valor']}

                            )
                            RETURNING idconstrucao;

                        ''')

                        if counter == 0:
                            idconstrucao = cursor.fetchone()

                        counter += 1

                        if(construcao['prods']):

                            for prod in json.loads(construcao['prods']):
                                
                                
                                cursor.execute(f'''
                                    
                                    insert
                                    into 
                                    pamateriaisconstrucao
                                    (
                                        idconstrucao,
                                        idprod,
                                        qtde,
                                        idquest
                                    ) 
                                    VALUES 
                                    (
                                        {idconstrucao[0]},
                                        {str(prod['produto']).split("-")[0]},
                                        {str(prod['quantidade']).split("-")[0]},
                                        {idform[0]}
                                    )

                                ''')

                if patrimonios.get('maquina') != 'None':

                    for maquina in patrimonios['maquina']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            pamaquinas
                            (
                                idprod,
                                idquest,
                                cdlinha,
                                qtde
                            ) 
                            VALUES 
                            (
                                
                                {str(maquina['especificacao']).split("-")[0]},
                                {idform[0]},
                                {str(maquina['linha']).split("-")[0]},
                                {str(maquina['quantidade'])}
                            )

                        ''')
                
                if patrimonios.get('animaisTrabalho') != 'None':

                    for animaisTrabalho in patrimonios['animaisTrabalho']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            paanimaistabalho
                            (
                                idprod,
                                idquest,
                                cdlinha,
                                qtde
                            ) 
                            VALUES 
                            (
                                
                                {str(animaisTrabalho['especificacao']).split("-")[0]},
                                {idform[0]},
                                {str(animaisTrabalho['linha']).split("-")[0]},
                                {str(animaisTrabalho['quantidade'])}
                            )

                        ''')

                
                
                if patrimonios.get('animaisProducao') != 'None':

                    for animaisProducao in patrimonios['animaisProducao']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            paanimaisproducao
                            (
                                idprod,
                                idquest,
                                qtde
                            ) 
                            VALUES 
                            (
                                
                                {str(animaisProducao['especificacao']).split("-")[0]},
                                {idform[0]},
                                {str(animaisProducao['quantidade'])}
                            )

                        ''')

        

                if patrimonios.get('culturasTemporarias') != 'None':

                    for culturasTemp in patrimonios['culturasTemporarias']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            paculturastemporarias
                            (
                                idquest,
                                unidprodcolhida,
                                area,
                                qde,
                                linhaexploracao
                            )
                            VALUES 
                            (
                                
                                {idform[0]},
                                {str(culturasTemp['unidade']).split("-")[0]},
                                {str(culturasTemp['area'])},
                                {str(culturasTemp['qde'])},
                                {str(culturasTemp['especificacao']).split("-")[0]}
                            )

                        ''')



                if patrimonios.get('produtosEstoque') != 'None':

                    for produtosEstoque in patrimonios['produtosEstoque']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            paprodutosestoque
                            (
                                idquest,
                                idprod,
                                qtde
                            )
                            VALUES 
                            (
                                
                                {idform[0]},
                                {str(produtosEstoque['especificacao']).split("-")[0]},
                                {str(produtosEstoque['quantidade'])}
                                
                            )

                        ''')

                if patrimonios.get('insumoEstoque') != 'None':

                    for insumo in patrimonios['insumoEstoque']:

                        cursor.execute(f'''
                                    
                            insert
                            into 
                            painsumosestoque
                            (
                                idquest,
                                idprod,
                                qtde
                            )
                            VALUES 
                            (
                                
                                {idform[0]},
                                {str(insumo['especificacao']).split("-")[0]},
                                {str(insumo['quantidade'])}
                            )

                        ''')

                #

                if patrimonios.get('divida') != 'None':

                    for divida in patrimonios['divida']:

                        cursor.execute(f'''
                            insert 
                            into 
                            padividas
                            (
                                idquest,
                                cdtipodivida,
                                idprod,
                                juropago,
                                cdlinha,
                                outros,
                                reais,
                                qtde
                            )
                            values
                            (
                                {idform[0]},
                                {str(divida['especificacao']).split("-")[0]},
                                {str(divida['produto']).split("-")[0]},
                                {str(divida['juropagos'])},
                                {str(divida['linha']).split('-')[0]},
                                '{str(divida['outros'])}',
                                {str(divida['reais'])},
                                {str(divida['quantidade'])}
                            )
                        ''')


                if patrimonios.get('emprestimoCusteio') != 'None':

                    for custeio in patrimonios['emprestimoCusteio']:

                        cursor.execute(f'''

                            insert 
                            into
                            paemprestimocusteio
                            (
                                idquest,
                                cdlinhacred,
                                cdlinha,
                                ano,
                                valor,
                                taxajurus,
                                carencia,
                                prazo,
                                valorpago 
                            ) 
                            VALUES
                            (
                                {idform[0]},
                                {str(custeio['especificacao']).split("-")[0]},
                                {str(custeio['linha']).split("-")[0]},
                                {str(custeio['ano'])},
                                {str(custeio['valor'])},
                                {str(custeio['taxajuros'])},
                                {str(custeio['carencia'])},
                                {str(custeio['prazo'])},
                                {str(custeio['valorpago'])}
                                
                            )

                        ''')

                

                if patrimonios.get('emprestimosInvestimentos') != 'None':

                    for investimentos in patrimonios['emprestimosInvestimentos']:

                        cursor.execute(f'''

                            insert 
                            into
                            paemprestimoinvestimento
                            (
                                idquest,
                                cdlinhacred,
                                cdlinha,
                                ano,
                                valor,
                                taxajurus,
                                carencia,
                                prazo,
                                valorpago 
                            ) 
                            VALUES
                            (
                                {idform[0]},
                                {str(investimentos['especificacao']).split("-")[0]},
                                {str(investimentos['linha']).split("-")[0]},
                                {str(investimentos['ano'])},
                                {str(investimentos['valor'])},
                                {str(investimentos['taxajuros'])},
                                {str(investimentos['carencia'])},
                                {str(investimentos['prazo'])},
                                {str(investimentos['valorpago'])}
                                
                            )

                        ''')

                

                if patrimonios.get('contasReceber') != 'None':

                    for contas in patrimonios['contasReceber']:

                        cursor.execute(f'''
                            insert 
                            into
                            pacontasreceber
                            (
                                idquest,
                                idprod,
                                decontav,
                                qtde,
                                valor
                            )
                            values
                            (
                                {idform[0]},
                                {str(contas['produto']).split("-")[0]},
                                '{str(contas['descricaoConta'])}',
                                {str(contas['quantidade'])},
                                {str(contas['valor'])}

                            )
                        ''')



                if culturasProducao.get('insumosMateriais'):
                    

                    for insumoMateriais in culturasProducao['insumosMateriais']:
                        cursor.execute(f'''
                            insert 
                            into
                            cpinsumos
                            (
                                idquest,
                                idprod,
                                qtde
                            )
                            values
                            (
                                {idform[0]},
                                {str(insumoMateriais['especificacao']).split("-")[0]},
                                {str(insumoMateriais['quantidade'])}
                                

                            )
                        ''')
                        


                if culturasProducao.get('maquinasAlugados') != 'None':

                    for maquinas in culturasProducao['maquinasAlugados']:


                        cursor.execute(f'''
                            insert
                            into
                            cpmaqimpalugados
                            (
                                idquest,
                                qtdehoras,
                                valorpago,
                                idprod,
                                qtdeproduto,
                                cdlinha,
                                maqimp
                            )
                            VALUES
                            (
                                {idform[0]},
                                {maquinas['qtdHoras']},
                                {maquinas['valorPago']},
                                {str(maquinas['produto']).split('-')[0]},
                                {str(maquinas['quantidade'])},
                                {str(maquinas['linhaexploracao']).split('-')[0]},
                                {str(maquinas['produto']).split('-')[0]}

                            )
                        ''')


                if culturasProducao.get('mercadoriasFamilia') != 'None':

                    for mercadorias in culturasProducao['mercadoriasFamilia']:

                        

                        cursor.execute(f'''

                            insert
                            into
                            cpmercadoriascompradas
                            (
                                idquest,
                                idperiodo,
                                idprod,
                                qtde
                            ) 
                            VALUES
                            (
                                {idform[0]},
                                {str(mercadorias['periodo']).split('-')[0]},
                                {str(mercadorias['produto']).split('-')[0]},
                                {str(mercadorias['quantidade'])}
                            )

                        ''')


                if culturasProducao.get('servicosPagos') != 'None':

                    for servicos in culturasProducao['servicosPagos']:

                        

                        cursor.execute(f'''

                            insert
                            into
                            cpservicospagos
                            (
                                idquest,
                                idserv,
                                valor,
                                periodo
                            ) 
                            VALUES
                            (
                                {idform[0]},
                                {str(servicos['servico']).split('-')[0]},
                                {str(servicos['valorpago'])},
                                {str(servicos['periodo']).split('-')[0]}
                            )

                        ''')
                
                if culturasProducao.get('forcaTrabalho') != 'None':

                    for forca in culturasProducao['forcaTrabalho']:

                    
                        cursor.execute(f'''
                            insert
                            into
                            cpforcatrabfam
                            (
                                idquest,
                                idoperacao,
                                cdlinha,
                                hd,
                                hh
                                
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(forca['operacao']).split('-')[0]},
                                {str(forca['linhaexploracao']).split('-')[0]},
                                {str(forca['hd'])},
                                {str(forca['hh'])}
                            )
                        ''')


                if culturasProducao.get('forcaTrabalho2') != 'None':

                    for forca2 in culturasProducao['forcaTrabalho2']:

                        
                        cursor.execute(f'''
                            insert
                            into
                            cpforcatrabfam2
                            (
                                idquest,
                                cdlinha,
                                idoperacao,
                                diasduracao,
                                quantaspessoas,
                                horaspordia
                                
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(forca2['linhaexploracao']).split('-')[0]},
                                {str(forca2['operacao']).split('-')[0]},
                                {str(forca2['diasduracao'])},
                                {str(forca2['qtdpessoas'])},
                                {str(forca2['horaspordia'])}
                            )
                        ''')


                
                
                if culturasProducao.get('trabalhoContratou') != 'None':

                    for contratou in culturasProducao['trabalhoContratou']:
            
                        
                        cursor.execute(f'''
                            insert
                            into
                            cpforcatrabcontratada
                            (
                                idquest,
                                idoperacao,
                                cdlinha,
                                hd,
                                valorpago,
                                idprod,
                                qtdprod
                                
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(contratou['operacao']).split('-')[0]},
                                {str(contratou['linhaexploracao']).split('-')[0]},
                                {str(contratou['qtdHoras'])},
                                {str(contratou['valorPago'])},
                                {str(contratou['produto']).split('-')[0]},
                                {str(contratou['quantidade'])}
                            )
                        ''')


                if culturasProducao.get('forcaTrabAssalaLinha') != 'None':

                    for trabAssala in culturasProducao['forcaTrabAssalaLinha']:
                
                        
                        cursor.execute(f'''
                            insert
                            into
                            cptrabassalpermlinha
                            (
                                idquest,
                                cdlinha,
                                numtrab,
                                salariomes,
                                salarioano
                                
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(trabAssala['linha']).split('-')[0]},
                                {str(trabAssala['ntrabalhadores'])},
                                {str(trabAssala['salariomes'])},
                                {str(trabAssala['salarioano'])}
                            )
                        ''')

                
                if culturasProducao.get('forcaTrabAssalaConjunt') != 'None':

                    for assalaConjunt in culturasProducao['forcaTrabAssalaConjunt']:
                    
                        
                        cursor.execute(f'''
                            insert
                            into
                            cptrabassalpermunid
                            (
                                idquest,
                                cdlinha,
                                numtrab,
                                salariomes,
                                salarioano
                                
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(assalaConjunt['linha']).split('-')[0]},
                                {str(assalaConjunt['ntrabalhadores'])},
                                {str(assalaConjunt['salariomes'])},
                                {str(assalaConjunt['salarioano'])}
                            )
                        ''')
                    
                if culturasProducao.get('produtoTransportou') != 'None':

                    for transportou in culturasProducao['produtoTransportou']:
                    
                        
                        cursor.execute(f'''
                            insert
                            into
                            cpprodutostransp
                            (
                                cdlinha,
                                unidade,
                                qtde,
                                valorpago,
                                idprod,
                                qtdeprod,
                                idquest
                            ) VALUES 
                            (
                                
                                {str(transportou['linha']).split('-')[0]},
                                {str(transportou['unidade']).split('-')[0]},
                                {str(transportou['quantidade'])},
                                {str(transportou['valorpago'])},
                                {str(transportou['produto']).split('-')[0]},
                                {str(transportou['quantidadeprodu'])},
                                {idform[0]}
                            )
                        ''')


                if culturasProducao.get('beneficiamentoProduto') != 'None':

                    for beneficiamento in culturasProducao['beneficiamentoProduto']:
                        
                        
                        cursor.execute(f'''
                            insert
                            into
                            cppagbenefprod
                            (
                                idquest,
                                cdlinha,
                                unidade,
                                qtde,
                                valorpago,
                                idprod,
                                qtdeprod
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(beneficiamento['linha']).split('-')[0]},
                                {str(beneficiamento['unidade']).split('-')[0]},
                                {str(beneficiamento['quantidade'])},
                                {str(beneficiamento['valorpago'])},
                                {str(beneficiamento['produto']).split('-')[0]},
                                {str(beneficiamento['quantidadeprodu'])}
                                
                            )
                        ''')

                
                if culturasProducao.get('pagouServicosLinhasVendidas') != 'None':

                    for pagouServ in culturasProducao['pagouServicosLinhasVendidas']:
                        
                        
                        cursor.execute(f'''
                            insert
                            into
                            cpoutrosservicos
                            (
                                idquest,
                                idserv,
                                cdlinha,
                                idunid,
                                qtde,
                                valorpago,
                                idprod,
                                qtdeprod 
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(pagouServ['servico']).split('-')[0]},
                                {str(pagouServ['linha']).split('-')[0]},
                                {str(pagouServ['unidade']).split('-')[0]},
                                {str(pagouServ['quantidade'])},
                                {str(pagouServ['valorpago'])},
                                {str(pagouServ['produto']).split('-')[0]},
                                {str(pagouServ['quantidadeprodu'])}
                                
                            )
                        ''')


                if culturasProducao.get('diasReuniao') != 'None':

                    for reuniao in culturasProducao['diasReuniao']:
                        
                        
                        cursor.execute(f'''
                            insert
                            into
                            cpdiasgastosreunioes
                            (
                                idquest,
                                idlocal,
                                qtdedias
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(reuniao['localreuniao']).split('-')[0]},
                                {str(reuniao['qtdDias'])}
                                
                            )
                        ''')


                if culturasProducao.get('pagouTaxa') != 'None':

                    for taxa in culturasProducao['pagouTaxa']:
                    
                        
                        cursor.execute(f'''
                            insert
                            into
                            cptaxaspagas
                            (
                                idquest,
                                idtipotaxa,
                                valorpago,
                                idprod,
                                qtdeprod,
                                valorprod
                            ) VALUES 
                            (
                                {idform[0]},
                                {str(taxa['tipotaxa']).split('-')[0]},
                                {str(taxa['valorpago'])},
                                {str(taxa['produto']).split('-')[0]},
                                {str(taxa['qtdProd'])},
                                {str(taxa['valorProd'])}
                                
                            )
                        ''')

                
                if culturasProducao.get('outrasDespesas') != 'None':

                    for despesas in culturasProducao['outrasDespesas']:
                        
                        
                        cursor.execute(f'''
                            insert
                            into
                            cpoutrasdespesas
                            (
                                descricao,
                                idquest,
                                valorpago,
                                idprod,
                                qtdeprod
                            ) VALUES 
                            (
                                
                                '{str(despesas['despesa']).split('-')[0]}',
                                {idform[0]},
                                {str(despesas['valorpago'])},
                                {str(despesas['produto']).split('-')[0]},
                                {str(despesas['qtdProd'])}
                                
                                
                            )
                        ''')

                
                
                if autoconsumo.get('dadosAutoconsumo') != 'None':

                    for autoCons in autoconsumo['dadosAutoconsumo']:
                        
                        cursor.execute(f'''
                            insert
                            into
                            autoconsumo
                            (
                                idquest,
                                idperiodo,
                                qtde,
                                idprod
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(autoCons['periodo']).split('-')[0]},
                                {str(autoCons['produto']).split('-')[0]},
                                {str(autoCons['quantidade'])}
                                
                                
                            )
                        ''')


                if assalariamento.get('dadosAssalariamento') != 'None':
                    
                    for indiceAssa in assalariamento['dadosAssalariamento']:
                        
                        cursor.execute(f'''
                            insert
                            into
                            assalariamento
                            (
                                idquest,
                                membro,
                                horadia,
                                valor,
                                idprod,
                                qtde
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                '{str(indiceAssa['membro'])}',
                                {str(indiceAssa['horadia'])},
                                {str(indiceAssa['valor'])},
                                {str(indiceAssa['produto']).split('-')[0]},
                                {str(indiceAssa['qtdProd'])}
                                
                                
                            )
                        ''')

            
                if transferenciaRenda.get('dadosTransferencias') != "None":

                    for renda in transferenciaRenda['dadosTransferencias']:
                    
                        cursor.execute(f'''
                            insert
                            into
                            beneficio
                            (
                                nomeben,
                                meses,
                                valormensal,
                                valoranual,
                                idquest,
                                idtipoben
                            ) VALUES 
                            (
                                
                                
                                '{str(renda['nomeben'])}',
                                {str(renda['quantidademeses'])},
                                {str(renda['valormensal'])},
                                {str(renda['valoranual'])},
                                {idform[0]},
                                {str(renda['tipobeneficio']).split('-')[0]}

                                
                            )
                        ''')


                if condicoes.get('recursosHidricos') != 'None':

                    for recursos in condicoes['recursosHidricos']:
                        
                    
                        cursor.execute(f'''
                            insert
                            into
                            chrecursoshid
                            (
                                idquest,
                                idtipoorig,
                                qtde
                            ) VALUES 
                            (

                                {idform[0]},
                                {str(recursos['Discriminacao']).split('-')[0]},
                                {str(recursos['quantidade'])}
                                
                                
                            )
                        ''')

                if condicoes.get('origemAbastecimento') != 'None':

                    for origem in condicoes['origemAbastecimento']:
                        
                    
                        cursor.execute(f'''
                            insert
                            into
                            chorigemabast
                            (
                                idquest,
                                idtipoorig
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(origem['Discriminacao']).split('-')[0]}
                            
                                
                                
                            )
                        ''')

                if condicoes.get('qualidadeAgua') != 'None':

                    for qualidade in condicoes['qualidadeAgua']:

                

                        cursor.execute(f'''
                            insert
                            into
                            chqualidadeagua
                            (
                                idquest,
                                beber,
                                cozinhar,
                                lavar,
                                banho,
                                idtipoorig
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                '{'S' if str(qualidade['boabeber']) == 'sim' else 'N'}',
                                '{'S' if str(qualidade['boacozinha']) != 'nao' else 'N'}',
                                '{'S' if str(qualidade['boalavarroupa']) != 'nao' else 'N'}',
                                '{'S' if str(qualidade['boatomarbanho']) == 'sim' else 'N'}',
                                {str(qualidade['Discriminacao']).split('-')[0]}
                            
                                
                                
                            )
                        ''')
                    
                if condicoes.get('aguaConsumida') != 'None':

                    for agua in condicoes['aguaConsumida']:
                
                        cursor.execute(f'''
                            insert
                            into
                            chaguaconsumida
                            (
                                idquest,
                                idtrat
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(agua['Discriminacao']).split('-')[0]}
                            
                                
                                
                            )
                        ''')


                if condicoes.get('destinoAgua') != 'None':

                    for destino in condicoes['destinoAgua']:
                        
                        cursor.execute(f'''
                            insert
                            into
                            chdestinogua
                            (
                                idquest,
                                iddest
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(destino['Discriminacao']).split('-')[0]}
                            
                                
                                
                            )
                        ''')
                
                if condicoes.get('destinoEsgoto') != 'None':

                    for destinoEsg in condicoes['destinoEsgoto']:
                
                        cursor.execute(f'''
                            insert
                            into
                            chdestesgoto
                            (
                                idquest,
                                iddest
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(destinoEsg['Discriminacao']).split('-')[0]}
                            
                                
                                
                            )
                        ''')


                if condicoes.get('lixo') != 'None':

                    for lixo in condicoes['lixo']:
                        
                        cursor.execute(f'''
                            insert
                            into
                            chlixo
                            (
                                idquest,
                                idresiduo,
                                idunid,
                                qtde,
                                periodo,
                                idacond,
                                iddestino
                                
                            ) VALUES 
                            (
                                
                                {idform[0]},
                                {str(lixo['residuos']).split('-')[0]},
                                {str(lixo['unidades']).split('-')[0]},
                                {str(lixo['quantidade'])},
                                {str(lixo['periodos']).split('-')[0]},
                                {str(lixo['acondiciona'])},
                                {str(lixo['destinos']).split('-')[0]}
                                
                                
                            )
                        ''')
                

                if condicoes.get('origemEnergia') != 'None':

                    for energia in condicoes['origemEnergia']:

                        cursor.execute(f'''
                            insert
                            into
                            chfonteenergia
                            (
                                idfonte,
                                idquest
                                
                            ) VALUES
                            (
                                    
                                {str(energia['fonteEnerg']).split('-')[0]},
                                {idform[0]}

                            )
                        ''')


                if condicoes.get('bensconsDuraveis') != 'None':

                    for bens in condicoes['bensconsDuraveis']:
                        
                        cursor.execute(f'''
                            insert
                            into
                            chbensconsduraveis
                            (
                                idquest,
                                idprod,
                                qtde
                            ) VALUES
                            (
                                    
                                {idform[0]},
                                {str(bens['bens']).split('-')[0]},
                                {str(bens['quantidade'])}
                            )
                        ''')

                
                if avaliacao.get('competitividade') != 'None':

                    for comp in avaliacao['competitividade']:
                        

                        cursor.execute(f'''
                            insert
                            into
                            aecompetividade
                            (
                                idquest,
                                idresp,
                                iditem
                            ) VALUES
                            (
                                    
                                {idform[0]},
                                {str(comp['competitividadesOpcoes']).split('-')[0]},
                                {str(comp['itenscompetitividadesValue']).split('-')[0]}
                            )
                        ''')


                if avaliacao.get('vantagens') != 'None':

                    for vantagens in avaliacao['vantagens']:

                        cursor.execute(f'''
                            insert
                            into
                            aevantagem
                            (
                                idquest,
                                iditemvant,
                                idvant,
                                acesso
                            ) VALUES
                            (  
                                {idform[0]},
                                {str(vantagens['itensVantagens']).split('-')[0]},
                                {str(vantagens['vantagens']).split('-')[0]},
                                '{'S' if str(vantagens['acesso']) == 'sim' else 'N'}'
                            )
                        ''')

                
                if avaliacao.get('ambienteCompetitivo') != 'None':

                    for ambiente in avaliacao['ambienteCompetitivo']:
                        
            

                        cursor.execute(f'''
                            insert
                            into
                            aeambientecomp
                            (
                                idquest,
                                iditemamb,
                                idconc
                            ) VALUES
                            (  
                                {idform[0]},
                                {str(ambiente['itensAmbientes']).split('-')[0]},
                                {str(ambiente['conceitoambientes']).split('-')[0]}
                                
                            )
                        ''')


                if avaliacao.get('situacaoVendas') != 'None':

                    for ambienteComp in avaliacao['situacaoVendas']:
                        

                        cursor.execute(f'''
                            insert
                            into
                            aesituacaovendas
                            (
                                idsituacao,
                                idperc,
                                idquest,
                                idprod
                                    
                            ) VALUES
                            (
                                
                                {str(ambienteComp['situacao']).split('-')[0]},
                                {str(ambienteComp['percentual']).split('-')[0]},
                                {idform[0]},
                                {str(ambienteComp['produto']).split('-')[0]}
                            )
                        ''')

                
                connect.commit()

                return {'validacao':True, 'idoform':idform[0]}
            
            except Exception as error:
                
                
                
                connect.rollback()
                # raise Exception(error)
        

        except Exception as error:
            erro = type(error).__name__
            return {'validacao':False, 'erro':str(erro)+ f': {error} '}

aspf = ASPF()