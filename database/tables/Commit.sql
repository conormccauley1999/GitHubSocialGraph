use ghsocialgraph;

create table if not exists Commit (
	Id int auto_increment primary key,
    RepositoryId int,
    `Timestamp` timestamp not null,
	DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_Commit_Repository foreign key (RepositoryId) references Repository(Id)
);
