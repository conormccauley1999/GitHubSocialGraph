use ghsocialgraph;

create table if not exists MaxDepth (
	Id int auto_increment primary key,
    `Value` int not null,
    DateCreated timestamp not null,
    DateModified timestamp null
);
