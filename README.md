# simulador_sensor_biomedico
Um sistema de monitoramento de dados biomédicos desenvolvido na cadeira de Sistemas Operacionais do cursos de Informática Biomédica.
Utiliza o conceito de multi-threading para simular sensores biomédicos independentes que enviam dados para uma estrutura compartilhada.
Uma Thread coletora é responsável por retirar esses dados da estrutura compartilhada, sumarizar calculando media,variância,desvio padrão e por fim apresentar esses dados para o usuário.

