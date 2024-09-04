cursos = {
    'Curso': '',
    'Duração do Curso (horas)': '',
    'Período do Dia': '',
    'Quantidade de Vagas': '',
}

cursos['Curso'] = input('Informe nome do curso a ser cadastrado: ')
cursos['Duração do Curso (horas)'] = input('Informe tempo de duração do curso (hrs): ')
cursos['Período do Dia'] = input('Informe pedíodo em que será ministrado o curso: ')
cursos['Quantidade de Vagas'] = input('Informe quantidade de vagas para o curso: ')


print(cursos.get('Curso'))
print(cursos.get('Duração do Curso (horas)'))
print(cursos.get('Período do Dia'))
print(cursos.get('Quantidade de Vagas')) 