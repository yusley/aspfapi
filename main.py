from fastapi import FastAPI, HTTPException,Depends,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials
from typing import Annotated
import sys
import os
from django.contrib.auth.hashers import check_password
import django
from pydantic import BaseModel
from models.aspfModel import ItemAspf
from models.imsModel import ItemIMS
from controllers.ims import ims
from controllers.aspf import aspf
from bd.postgres import create_conexao
from fastapi.middleware.cors import CORSMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
print(current_dir)

from bd.sincronizacoes.sincronizacao import create_sincronizacao,get_user

app = FastAPI()

# Defina as origens permitidas (você pode usar "*" para permitir todas)
origins = [
    "http://172.19.6.75:9001",  # IP da API
    "http://localhost",
    "http://127.0.0.1",
    "http://seu-ip-do-dispositivo",
    "*"  # para permitir todas as origens (em desenvolvimento)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os headers
)

security = HTTPBasic()

def validadorSenha(credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    user = get_user.getuser(username=credentials.username,create_conexao=create_conexao)
    
    if user:
        print('passando...')
        valid = check_password(str(credentials.password),str(user[0][1]))
        print(valid)

        if valid == True:
            return credentials.username
        else:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        print('rejeitado...')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )



@app.get('/helloworld')
async def helloworld():
    try:
        dados = create_sincronizacao.helloWorld(create_conexao)
        
        if dados['online'] == True:
            return dados
        else:
            return {'online':True,'bd':'off'}

    except Exception as error:
        print(error)
        return {'online':True, 'bd':'off'}
    

@app.get("/users/me/")
async def read_users_me(username: Annotated[str,Depends(validadorSenha)]):
    return {"username":username}

@app.get('/sincregional')
async def sincRegional():

    # print(conexao)
    try:
        dados = create_sincronizacao.sincronizarRegional(create_conexao)
        return {'regional':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/sincprofissao')
async def sincProfissao():

    try:
        dados = create_sincronizacao.sincronizarProfissao(create_conexao)
        return {'profissao': dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sincmotivonaoestudar')
async def sincProfissao():

    try:
        dados = create_sincronizacao.sincronizarMotivoNaoEstudar(create_conexao)
        return {'motivos': dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sincescolaridade')
async def sincEscolaridade():
    try:
        dados = create_sincronizacao.sincronizarEscolaridade(create_conexao)
        return {'escolaridade': dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sincparentesco')
async def sincParentesco():
    try:
        dados = create_sincronizacao.sincParentesco(create_conexao)
        return {'parentesco':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sincassistparto')
async def sincAssistparto():
    try:
        dados = create_sincronizacao.sincAsistparto(create_conexao)
        return {'assistparto': dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


##select idtipoatend,detipoatendimento, idregional, situacao  from localatendimento
@app.get('/sinclocalatendimento')
async def sincLocalatendimento():
    try:
        dados = create_sincronizacao.sincLocalatendimento(create_conexao)
        return {'localatendimento':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sinclocalpesquisa')
async def sincLocalpesquisa():
    try:
        dados = create_sincronizacao.sincLocalpesquisa(create_conexao)
        return {'localpesquisa':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sinccidade')
async def sincCidade():
    try:
        dados = create_sincronizacao.sincCidade(create_conexao)
        return {'cidade':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sincatividade')
async def sincAtividade():
    try:
        dados = create_sincronizacao.sincAtividade(create_conexao)
        return {'atividade':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sinctipoacessoterra')
async def sincTipoacessoterra():
    try:
        dados = create_sincronizacao.sincTipoacessoterra(create_conexao)
        return {'tipoacessoterra':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sincmeiotransporte')
async def sincMeiotransp():
    try:
        dados = create_sincronizacao.sincMeiotransporte(create_conexao)
        return {'meiotransporte':dados}
    except:
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sincestado')
async def sincestado():
    try:
        dados = create_sincronizacao.sincEstado(create_conexao)
        return {'estados':dados}
    except Exception as error:
      
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/sincvigencia')
async def sincvigencia():
    try:
        dados = create_sincronizacao.sincVigencia(create_conexao)
        return {'vigencia':dados}
    except Exception as error:
        
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    

@app.get('/sincprocessamento')
async def sincprocessamento():
    try:
        dados = create_sincronizacao.sincProcessamento(create_conexao)
        return {'processamento':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/projetodepesquisa')
async def sincProjetoDePesquisa():
    try:
        dados = create_sincronizacao.sincProjetoDePesquisa(create_conexao)
        return {'projetodepesquisa':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    
@app.get('/tipodeficiencia')
async def sincTipoDeficiencia():
    try:
        dados = create_sincronizacao.sincTipoDeficiencia(create_conexao)
        return {'tipodeficiencia':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    
@app.get('/periodovida')
async def sincPeriodoVida():
    try:
        dados = create_sincronizacao.sincPeriodoVida(create_conexao)
        return {'periodovida':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/tipodoenca')
async def sincTipoDoenca():
    try:
        dados = create_sincronizacao.sincTipoDoenca(create_conexao)
        return {'tipodoenca':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    
@app.get('/tipoassistencia')
async def sincTipoAssistencia():
    try:
        dados = create_sincronizacao.sincTipoAssistencia(create_conexao)
        return {'tipoassistencia':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/areacapacitacao')
async def sincAreacapacitacao():
    try:
        dados = create_sincronizacao.sincAreacapacitcao(create_conexao)
        return {'capacitacao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/produtos')
async def sincprodutos():
    try:
        dados = create_sincronizacao.sincProdutos(create_conexao)
        return {'produtos':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/formauso')
async def sincformauso():
    try:
        dados = create_sincronizacao.sincFormauso(create_conexao)
        return {'formauso':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/linhaexploracao')
async def sincLinhaExploracao():
    try:
        dados = create_sincronizacao.sincLinhaexploracao(create_conexao)
        return {'linhaexploracao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/tipolinhaexploracao')
async def sincTipoLinhaExploracao():
    try:
        dados = create_sincronizacao.sincTipoLinhaExploracao(create_conexao)
        return {'tipolinha':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/unidademedida')
async def sincUnidadeMedida():
    try:
        dados = create_sincronizacao.sincUnidadeMedida(create_conexao)
        return {'unidademedida':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/pabenfeitorias')
async def sincPabenfeitorias():
    try:
        dados = create_sincronizacao.sincPabenfeitorias(create_conexao)
        return {'benfeitorias':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/tipobenfeitoria')
async def sincTipobenfeitorias():
    try:
        dados = create_sincronizacao.sincTipoBenfeitoria(create_conexao)
        return {'tipobenfeitorias':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")



@app.get('/estagioproducao')
async def sincEstagioproducao():
    try:
        dados = create_sincronizacao.sincEstagioprodutocao(create_conexao)
        return {'estagioproducao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/materiaisconstrucao')
async def sincmateriasconstrucao():
    try:
        dados = create_sincronizacao.sincMateriasconstrucao(create_conexao)
        return {'materiaisconstrucao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/construcao')
async def sincconstrucao():
    try:
        dados = create_sincronizacao.sincConstrucoes(create_conexao)
        return {'construcao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/tipodivida')
async def sinctipodivida():
    try:
        dados = create_sincronizacao.sincTipoDivida(create_conexao)
        return {'tipodivida':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/linhacredito')
async def sincLinhacredito():
    try:
        dados = create_sincronizacao.sincLinhaCredito(create_conexao)
        return {'linhacredito':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/periodo')
async def sincperiodo():
    try:
        dados = create_sincronizacao.sincPeriodo(create_conexao)
        return {'periodo':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/servicos')
async def sincservicos():
    try:
        dados = create_sincronizacao.sincServicos(create_conexao)
        return {'servicos':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/operacao')
async def sincoperacao():
    try:
        dados = create_sincronizacao.sincOperacao(create_conexao)
        return {'operacao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/localreuniao')
async def sinclocalreuniao():
    try:
        dados = create_sincronizacao.sincLocalreuniao(create_conexao)
        return {'localreuniao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/tipotaxa')
async def sinctipotaxa():
    try:
        dados = create_sincronizacao.sincTipoTaxa(create_conexao)
        return {'tipotaxa':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")

@app.get('/tipobeneficio')
async def sinctipobeneficio():
    try:
        dados = create_sincronizacao.sincTipobeneficio(create_conexao)
        return {'tipobeneficio':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/tipoorigemagua')
async def sinctipoorigemagua():
    try:
        dados = create_sincronizacao.sincTipoOrigemAgua(create_conexao)
        return {'tipoorigemagua':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/tipodestino')
async def sinctipodestino():
    try:
        dados = create_sincronizacao.sincTipoDestino(create_conexao)
        return {'tipodestino':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/destino')
async def sincdestino():
    try:
        dados = create_sincronizacao.sincDestino(create_conexao)
        return {'destino':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/residuo')
async def sincresiduo():
    try:
        dados = create_sincronizacao.sincResiduo(create_conexao)
        return {'residuo':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/fonteenergia')
async def sincfonteenergia():
    try:
        dados = create_sincronizacao.sincFonteEnergia(create_conexao)
        return {'fonteenergia':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/competitividade')
async def sinccompetitividade():
    try:
        dados = create_sincronizacao.sincCompetitividade(create_conexao)
        return {'competitividade':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/itenscompetitividade')
async def sincitenscompetitividade():
    try:
        dados = create_sincronizacao.sincItensCompetitividade(create_conexao)
        return {'itenscompetitividade':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/itensvantagens')
async def sincitensvantagens():
    try:
        dados = create_sincronizacao.sincItensVantagens(create_conexao)
        return {'itensvantagens':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/vantagens')
async def sincvantagens():
    try:
        dados = create_sincronizacao.sincVantagens(create_conexao)
        return {'vantagens':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/itensambiente')
async def sincitensambiente():
    try:
        dados = create_sincronizacao.sincItensAmbiente(create_conexao)
        return {'itensambiente':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/conceitoambiente')
async def sincconceitoambiente():
    try:
        dados = create_sincronizacao.sincConceitoAmbiente(create_conexao)
        return {'conceitoambiente':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/situacaovendas')
async def sincsituacaovendas():
    try:
        dados = create_sincronizacao.sincSituacaoVendas(create_conexao)
        return {'situacaovendas':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/percentual')
async def sincpercentual():
    try:
        dados = create_sincronizacao.sincPercentual(create_conexao)
        return {'percentual':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")
    
@app.get('/tratamentoagua')
async def sinctratamentoagua():
    try:
        dados = create_sincronizacao.sincTratamentoAgua(create_conexao)
        return {'tratamento':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


# IMS

@app.get('/ims')
async def sincronizarIMS():
    try:
        dados = create_sincronizacao.sincIMS(create_conexao)
        return {'ims':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/imscategoriaindicador')
async def sincImscategoriaindicador():
    try:
        dados = create_sincronizacao.sincImsCategoriaIndicador(create_conexao)
        return {'imscategoriaindicador':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/imsindicador')
async def sincIMSindicador():
    try:
        dados = create_sincronizacao.sincImsIndicador(create_conexao)
        return {'imsindicador':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/imspergunta')
async def sincimspergunta():
    try:
        dados = create_sincronizacao.sincIMSpergunta(create_conexao)
        return {'imspergunta':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")



@app.get('/imsresposta')
async def sincimsresposta():
    try:
        dados = create_sincronizacao.sincIMSresposta(create_conexao)
        return {'imsresposta':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")



@app.get('/imsindicadoresresposta')
async def sincimsindicadoresresposta():
    try:
        dados = create_sincronizacao.sincIMSIndicadoresResposta(create_conexao)
        return {'imsindicadoresresposta':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/imsprodutosproduzidos')
async def sincIMSprodutosproduzidos():
    try:
        dados = create_sincronizacao.sincIMSProdutosProduzidos(create_conexao)
        return {'imsprodutosproduzidos':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")



@app.get('/sinctipocaracterizacao')
async def sinctipocaracterizacao():
    try:
        dados = create_sincronizacao.sincTipoCaracterizacao(create_conexao)
        return {'sinctipocaracterizacao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sinctipocaracterizacaoterritorio')
async def sinctipocaracterizacaoterritorio():
    try:
        dados = create_sincronizacao.sincTipoCaracterizacaoTerritorio(create_conexao)
        return {'sinctipocaracterizacao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")



@app.get('/sincsistemaproducao')
async def sincSistemaProducao():
    try:
        dados = create_sincronizacao.sincSistemaProducao(create_conexao)
        return {'sistemaproducao':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")


@app.get('/sinctiporesponsavel')
async def sinctiporesponsavel():
    try:
        dados = create_sincronizacao.sincTipoResponsavel(create_conexao)
        return {'tiporesponsavel':dados}
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, details="Erro ao consultar dados no banco!")




@app.post('/aspf')
async def sincAspf(item:ItemAspf,username: Annotated[str,Depends(validadorSenha)]):

    dadosResponse = aspf.salvarAspf(item,create_conexao)

    print('dados =>',dadosResponse)

    return {'dadosResponse':dadosResponse}



@app.post('/ims')
async def sincIms(item:ItemIMS,username: Annotated[str,Depends(validadorSenha)]):

    dadosResponse = ims.salvarAspf(item,create_conexao)
    
    print('dados =>',dadosResponse)

    return {'dadosResponse':dadosResponse}