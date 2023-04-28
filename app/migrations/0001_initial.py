# Generated by Django 4.2 on 2023-04-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CAPEXModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("empresa", models.CharField(db_column="Empresa", max_length=255)),
                ("codigo", models.CharField(db_column="Código", max_length=255)),
                ("programa", models.CharField(db_column="Programa", max_length=255)),
                (
                    "status",
                    models.CharField(db_column="Status da Obra", max_length=255),
                ),
                ("nome", models.CharField(db_column="Nome da Obra", max_length=255)),
                ("descricao", models.CharField(db_column="Descrição", max_length=255)),
                ("regiao", models.CharField(db_column="Região", max_length=255)),
                (
                    "criterio",
                    models.CharField(
                        db_column="Critério de Planejamento", max_length=255
                    ),
                ),
                (
                    "classificacao",
                    models.CharField(db_column="Classificação", max_length=255),
                ),
                (
                    "tipo_obra",
                    models.CharField(db_column="Tipo de Obra", max_length=255),
                ),
                ("ano_pese", models.CharField(db_column="Ano PESE", max_length=255)),
                (
                    "regiao_eletrica",
                    models.CharField(db_column="Região Elétrica", max_length=255),
                ),
                (
                    "tipo_projeto",
                    models.CharField(db_column="Tipo do Projeto", max_length=255),
                ),
                (
                    "subtipo_projeto",
                    models.CharField(db_column="Subtipo", max_length=255),
                ),
                (
                    "qtd_fisica",
                    models.CharField(db_column="Qtd. Física", max_length=255),
                ),
                ("unidade", models.CharField(db_column="Unidade", max_length=255)),
                (
                    "valor_previsto_unitizacao",
                    models.DecimalField(
                        db_column="Valor Previsto de Unitização",
                        decimal_places=2,
                        max_digits=20,
                    ),
                ),
                (
                    "data_unitizacao",
                    models.DateTimeField(db_column="Data Prevista de Unitização"),
                ),
                (
                    "responsavel",
                    models.CharField(
                        db_column="Responsável Planejamento", max_length=255
                    ),
                ),
                (
                    "orcamento_total",
                    models.DecimalField(
                        db_column="Orçamento Total", decimal_places=2, max_digits=20
                    ),
                ),
            ],
        ),
    ]