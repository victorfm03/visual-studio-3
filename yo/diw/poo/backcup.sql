
create table genero(
    idgenero integer primary key,
    genero varchar2(30)
);

create table libro(
    idlibro integer primary key,
    idgenero integer,
    titulo varchar2(100),
    autor varchar2(100),
    descripcion varchar2(200),
    imagen varchar2(150)
);