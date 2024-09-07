
class GetUser():
    
    def getuser(self,username,create_conexao):

        conexao = create_conexao.connection()

        cursor = conexao.cursor()

        cursor.execute(f"""
            select username,password  from auth_user where UPPER(username) = UPPER('{username}') 
        """)

        dados = cursor.fetchall()

        return dados

class Sincronizacao():

    def helloWorld(self,create_conexao):


        try:
            conexao = create_conexao.connection()
          
            return {'online':True,'bd':'on'}
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincronizarRegional(self,create_conexao):

        try:
        
            conexao = create_conexao.connection()

            cursor = conexao.cursor()

            cursor.execute("""
                select idregional, nomeregional  from regional r
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincronizarProfissao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idprof,deprofissao,idregional,situacao  from profissao p
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincronizarMotivoNaoEstudar(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idmotivo,demotivo,idregional,situacao  from motivonaoestudar m 
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincronizarEscolaridade(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idescolar,deescolaridade,idregional,situacao  from escolaridade e
            """)

            dados = cursor.fetchall()
            return dados
           
        except Exception as error:
            raise Exception('bd offline', error)

    def sincParentesco(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idparente, deparente, idregional,situacao  from parentesco p
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincAsistparto(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idassisente,deassistente,idregional,situacao  from assistparto a
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)

    def sincLocalatendimento(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idtipoatend,detipoatendimento, idregional, situacao  from localatendimento
            """)

            dados = cursor.fetchall()
            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincTratamentoAgua(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select
                    idtrat,
                    detratamento,
                    idregional,
                    situacao
                from
                    tratamentoagua
            """)

            dados = cursor.fetchall()
            return dados
        except Exception as error:
            raise Exception('bd offline', error)

        
        
    
    def sincLocalpesquisa(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idlocalpesq, momelocal, idregional, situacao  from localpesquisa
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    
    def sincCidade(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idcidade,nomecidade, idestado, idregional, situacao  from cidade order by idcidade asc
            """)

            dados = cursor.fetchall()

            return dados
           
        except Exception as error:
            raise Exception('bd offline', error)

    def sincAtividade(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idatividade,nomeatividade,idregional,situacao  from atividade a 
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincTipoacessoterra(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idtipoacesso,detipoacesso,idregional,situacao  from tipoacessoterra t
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)

    def sincMeiotransporte(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idmeiotransp, demeiotransp  from meiotransporte m
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincEstado(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select idestado,nomeestado,idregional,situacao  from estado
            """)
            
            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincVigencia(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select  idvig,
                        devigencia,
                        dtinicio,
                        dtfim,
                        observacao,
                        valorterra,
                        diaria,
                        idregional,
                        situacao 
                from vigencia v
            """)
            
            dados = cursor.fetchall()

            return dados
          
        except Exception as error:
            raise Exception('bd offline', error)

    def sincProcessamento(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select  idproc,
                        idlocalpesq,
                        idvig,
                        idcidade,
                        dtproc,
                        sistema,
                        anobase,
                        quest,
                        observacao
                from processamento p
            """)

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)



    def sincProjetoDePesquisa(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute("""
                select 
                    idprojeto,
                    anobase,
                    nome,
                    idlocalpesq,
                    idregional,
                    dtabertura,
                    dtfechamento,
                    pesquisafinalizada,
                    idvig,
                    idproc,
                    situacao,
                    tipoprojeto
                from projetodepesquisa p where pesquisafinalizada <> 'S'
            """)
            dados = cursor.fetchall()

            return dados
          
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincTipoDeficiencia(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select  
                        iddeficiencia,
                        dedeficiencia,
                        idregional,
                        situacao
                from tipodeficiencia t order by dedeficiencia  asc

           
            ''')

            dados = cursor.fetchall()

            return dados
           
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincPeriodoVida(self,create_conexao):

        try:
            #select idperiodo,deperiodo,idregional,situacao  from periodovida p

            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select  idperiodo,
                        deperiodo,
                        idregional,
                        situacao
                from periodovida p order by idperiodo asc 
            ''')

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincTipoDoenca(self,create_conexao):

        try:
            #select idperiodo,deperiodo,idregional,situacao  from periodovida p

            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select 
                        idtipodoenca,
                        detipodoenca,
                        idregional, 
                        situacao
                from tipodoenca t 
            ''')

            dados = cursor.fetchall()

            return dados
            
        except Exception as error:
            raise Exception('bd offline', error)
    
    
    def sincTipoAssistencia(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select  idtipoassist,
                        detipoassist,
                        idregional,
                        situacao
                from tipoassistencia t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincAreacapacitcao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select idareacapac,deareacapac,idregional, situacao  from areacapacitcao a
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincProdutos(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idprod,
                    deproduto,
                    id_cat,
                    idunid,
                    vidautil,
                    pesoembalagem,
                    idtipolixo,
                    idregional,
                    situacao
                from
                    produtos p
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincFormauso(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idforma,
                    deforma,
                    idregional,
                    situacao
                from
                    formauso f
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
  
    def sincLinhaexploracao(self,create_conexao):

        try:
        
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdlinha,
                    delinha,
                    cdtipolinha,
                    situacao,
                    idregional
                from
                    linhaexploracao l
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincTipoLinhaExploracao(self,create_conexao):

        try:
        
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdtipolinha,
                    detipolinha,
                    idregional,
                    situacao
                from
                    tipolinha t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincUnidadeMedida(self,create_conexao):

        try:
        
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idunid,
                    descunidade,
                    idregional,
                    situacao
                from
                    unidademedida u
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    
    def sincPabenfeitorias(self,create_conexao):

        try:

            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idquest,
                    cdtipobenf,
                    qde ,
                    cdestagio
                from
                    pabemfeitorias p
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincTipoBenfeitoria(self,create_conexao):

        try:

            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdtipobenf,
                    detipobenf,
                    vidautilext,
                    vidautilagri,
                    vidautilagrof,
                    vidautilfuturaext,
                    vidautilfuturaagri,
                    vidautilfuturaagrof,
                    idregional,
                    situacao
                from
                    tipobenfeitoria t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincEstagioprodutocao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdestagio,
                    deestagio,
                    idregional,
                    situacao
                from
                    estagioproducao e
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincMateriasconstrucao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idconstrucao,
                    idprod,
                    qtde,
                    idquest
                from
                    pamateriaisconstrucao p
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincConstrucoes(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idconstrucao,
                    idquest,
                    cdtipobenf,
                    tempoconstruir,
                    npessoaconstruir,
                    tamanho,
                    comodos,
                    privada,
                    valor
                from
                    paconstrucoes p
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincTipoDivida(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdtipodivida,
                    detipodivida,
                    idregional,
                    situacao
                from
                    tipodivida t 
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincLinhaCredito(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    cdlinhacred,
                    delinmahcred,
                    idregional,
                    situacao
                from
                    linhacredito l
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincPeriodo(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idperiodo,
                    deperiodo,
                    idregional,
                    situacao
                from
                    periodo p
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincServicos(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idserv,
                    deservico,
                    idcatservpag,
                    idregional,
                    situacao
                from
                    servicos 
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincOperacao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idoperacao,
                    idtipooper,
                    deoperacao,
                    idregional,
                    situacao
                from
                    operacao o

            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincLocalreuniao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idlocal,
                    delocalreuniao,
                    idregional,
                    situacao
                from
                    localreuniao l

            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincTipoTaxa(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idtipotaxa,
                    detipotaxa,
                    idregional,
                    situacao
                from
                    tipotaxa t

            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincTipobeneficio(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                idtipoben,
                detipobeneficio,
                idregional,
                situacao
            from
                tipobeneficio t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincTipoOrigemAgua(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                idtipoorig,
                detipoorigem,
                idregional,
                situacao
            from
                tipoorigemagua t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincTipoDestino(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                iddest,
                detipodest,
                idregional,
                situacao
            from
                tipodestinores t
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)


    def sincDestino(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                iddestino,
                dedestino,
                idregional,
                situacao
            from
                destino d 
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincResiduo(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select 
                    idresiduo,
                    deresiduo,
                    idtipores,
                    idresiduo,
                    situacao  
                from 
                    residuos r
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincFonteEnergia(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idfonte,
                    defonte,
                    idregional,
                    situacao
                from
                    fonteenergia f
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)


    def sincCompetitividade(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select 
                    idresp,
                    deresp,
                    idregional,
                    situacao
                from 
                    competitivo c 
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincItensCompetitividade(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    iditem,
                    deitemcomp,
                    idregional,
                    situacao
                from
                    itenscompetividade i 
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincItensVantagens(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    iditemvant,
                    deitemvant,
                    idregional,
                    situacao
                from
                    itensvantagem i
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincVantagens(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idvant,
                    devantagem
                from
                    vantagem v
            ''')

            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincItensAmbiente(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    iditemamb,
                    deitemamb,
                    idregional,
                    situacao
                from
                    itensambiente i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)


    def sincConceitoAmbiente(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idconc,
                    deconc,
                    idregional,
                    situacao
                from
                    conceitoambiente c
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincSituacaoVendas(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idconc,
                    deconc,
                    idregional,
                    situacao
                from
                    conceitoambiente c
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincSituacaoVendas(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idsituacao,
                    desituacao,
                    idregional,
                    situacao
                from
                    situacaovendas c
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    def sincPercentual(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idperc,
                    depercentual,
                    idregional,
                    situacao
                from
                    percentual p
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    # IMS
    
    def sincIMS(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select 
                    idims,
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
                    emailentrevistador,
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
                    questionario,
                    horafim,
                    horainicio
                from ims i 
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)

    
    def sincImsCategoriaIndicador(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idcatindicador,
                    descricao,
                    situacao,
                    idregional
                from
                    imscategoriaindicador i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincImsIndicador(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idindicador,
                    sigla,
                    descricao,
                    situacao,
                    idcatindicador,
                    idregional
                from
                    imsindicador i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
        
    
    def sincIMSpergunta(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idpergunta,
                    descricao,
                    situacao,
                    idindicador,
                    idregional,
                    idcatindicador
                from
                    imspergunta i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincIMSresposta(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idresposta,
                    opcao,
                    valor,
                    situacao,
                    idpergunta,
                    idregional
                from
                    imsresposta i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    
    def sincIMSIndicadoresResposta(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idrespostaindicador,
                    situacao,
                    idims,
                    idregional,
                    idpergunta,
                    idresposta
                from
                    imsindicadoresresposta i
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
        
    def sincIMSProdutosProduzidos(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idprodproduzido,
                    qtdproduzida,
                    situacao,
                    idims,
                    idprod,
                    idregional
                from
                    imsprodutosproduzidos
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
        
    
    def sincTipoCaracterizacao(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
                select
                    idcaracterizacao,
                    descricao,
                    situacao,
                    idregional
                from
                    tipocaracterizacao t
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincTipoCaracterizacaoTerritorio(self,create_conexao):

        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                idterritor,
                descricao,
                situacao,
                idregional
            from
                tipocaracterizacaoterritor t 
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
    

    def sincSistemaProducao(self,create_conexao):
        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                idsistema,
                descricao,
                situacao,
                idregional
            from
                sistemaproducao s 
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)
        
    
    def sincTipoResponsavel(self,create_conexao):
        try:
            conexao = create_conexao.connection()
            cursor = conexao.cursor()

            cursor.execute('''
            select
                idresponsavel,
                descricao,
                situacao,
                idregional
            from
                tiporesponsavel
            ''')


            dados = cursor.fetchall()

            return dados
        except Exception as error:
            raise Exception('bd offline', error)


create_sincronizacao = Sincronizacao()

get_user = GetUser()