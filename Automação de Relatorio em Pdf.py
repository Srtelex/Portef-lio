from fpdf import FPDF
import datetime

def gerar_relatorio(dados, nome_arquivo="relatorio.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    
    pdf.cell(200, 10, f"Relatório - {datetime.datetime.now().strftime('%d/%m/%Y')}", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Resumo dos Dados", ln=True)
    
    pdf.set_font("Arial", "", 10)
    for key, value in dados.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)
    
    pdf.ln(10)
    pdf.cell(0, 10, "Detalhes do Relatório", ln=True)
    
    for i in range(1, 11):
        pdf.cell(0, 10, f"Entrada {i}: Este é um exemplo de dado detalhado.", ln=True)
    
    pdf.output(nome_arquivo)

dados_exemplo = {
    "Total de Vendas": "R$ 10.000,00",
    "Clientes Atendidos": "150",
    "Produtos Vendidos": "200",
    "Custo Médio por Cliente": "R$ 66,67"
}

gerar_relatorio(dados_exemplo)
