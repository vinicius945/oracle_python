CREATE TABLE mensagem (
    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    assunto VARCHAR2(255),
    destinatario VARCHAR2(255),
    remetente VARCHAR2(255),
    conteudo CLOB
);