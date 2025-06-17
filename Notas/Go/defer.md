defer em golang coloca a execução de uma função ou codigo na pilha de execucao para ser chamada ao final da funçao em andamento  

na pratica defer está atrasando a execução de algum codigo para ser executado ao final, semelhante ao finally de outras linguagens mas sem a necessidade de um controle de fluxo com blocos try catch  

creio que surge justamente para manter a simplicidade de golang, ao inves de criar toda estrutura de tratamento de erros comum a outras linguages, go mantem os erros apenas como valores e coloca defer como uma forma simples de fechar/encerrar conexões ou acessos a recursos