use ghsocialgraph;

create table if not exists Repository (
	Id int auto_increment primary key,
    UserId int,
    IsExplored bool not null default false,
	`Name` varchar(255) not null,
    LastCrawled timestamp null,
    DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_Repository_User foreign key (UserId) references `User`(Id),
    unique(UserId, `Name`)
);
