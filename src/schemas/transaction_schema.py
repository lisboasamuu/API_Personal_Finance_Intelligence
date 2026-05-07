#O schema é uma estrutura que define como os dados são organizados 
from datetime import datetime

def validate_transaction(data, partial=False):
    erros = []
    #partial parte do pressuposto que toda data está preenchida, ela é definidia a partir das condicionais dentro da condicional que valida data sendo totalmente preenchida
    if not partial:
        if not data.get('description'):
            erros.append('Descrição é obrigatória')
        if not data.get('amount'):
            erros.append('Valor é obrigatória')
        if not data.get('date'):
            erros.append('Data é obrigatória')
    #tratar a conversão do valor para float
    if 'amount' in data and data['amount'] is not None:
        try:
            float(data['amount'])
        except (ValueError, TypeError):
            erros.append("Valor deve ser numérico")
    #tratando a data
    if 'date' in data and data['date'] is not None:
        try:
            datetime.strptime(data['date'], '%Y-%m-%d')
        except (ValueError, TypeError):
            erros.append("Data deve ser no formato YYYY-MM-DD")    
    return erros