use ghsocialgraph;

create table if not exists RepositoryInformation (
	Id int auto_increment primary key,
    RepositoryId int,
    FullName varchar(255) null,
    Url varchar(255) null,
    IsFork bool null,
    Description text null,
    ForkCount int null,
    StarCount int null,
    WatcherCount int null,
    CommitCount int null,
    Size int null,
    DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_RepositoryInformation_Repository foreign key (RepositoryId) references Repository(Id),
    unique(RepositoryId)
);
