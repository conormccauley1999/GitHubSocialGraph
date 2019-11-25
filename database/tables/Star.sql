use ghsocialgraph;

create table if not exists Star (
	Id int auto_increment primary key,
    UserId int,
    RepositoryId int,
	DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_Star_User foreign key (UserId) references `User`(Id),
    constraint FK_Star_Repository foreign key (RepositoryId) references Repository(Id),
    unique(UserId, RepositoryId)
);
