from django.db import models

# Create your models here.


class CAPEXModels(models.Model):
    empresa = models.CharField(max_length=255, db_column='Empresa')
    codigo = models.CharField(max_length=255, db_column='Código')
    programa = models.CharField(max_length=255, db_column='Programa')
    status = models.CharField(max_length=255, db_column='Status da Obra')
    nome = models.CharField(max_length=255, db_column='Nome da Obra')
    descricao = models.CharField(max_length=255, db_column='Descrição')
    regiao = models.CharField(max_length=255, db_column='Região')
    criterio = models.CharField(max_length=255, db_column='Critério de Planejamento')
    classificacao = models.CharField(max_length=255, db_column='Classificação')
    tipo_obra = models.CharField(max_length=255, db_column='Tipo de Obra')
    ano_pese = models.CharField(max_length=255, db_column='Ano PESE')
    regiao_eletrica = models.CharField(max_length=255, db_column='Região Elétrica')
    tipo_projeto = models.CharField(max_length=255, db_column='Tipo do Projeto')
    subtipo_projeto = models.CharField(max_length=255, db_column='Subtipo')
    qtd_fisica = models.CharField(max_length=255, db_column='Qtd. Física')
    unidade = models.CharField(max_length=255, db_column='Unidade')
    valor_previsto_unitizacao = models.DecimalField(max_digits=20, decimal_places=2, db_column='Valor Previsto de Unitização')
    data_unitizacao = models.DateTimeField(db_column='Data Prevista de Unitização')
    responsavel = models.CharField(max_length=255, db_column='Responsável Planejamento')
    orcamento_total = models.DecimalField(max_digits=20, decimal_places=2, db_column='Orçamento Total')
