#a service é responsável pela regra de negócio e lógicas
def classify_category(description):
    desc_lower = description.lower()
    keywords = {
        'transporte': ['uber', '99', 'taxi', 'onibus', 'metrô', 'combustivel', 'viagem'],
        'alimentacao': ['restaurante', 'supermercado', 'mercado', 'feira', 'comida', 'lanche', 'pizza'],
        'moradia': ['aluguel', 'condominio', 'agua', 'luz', 'internet'],
        'lazer': ['cinema', 'teatro', 'show', 'netflix', 'spotify'],
        'saude': ['farmacia', 'medico', 'consulta', 'exame']
    }        
    for category, words in keywords.items():
        if any(word in desc_lower for word in words):
            return category
    return 'outros'
