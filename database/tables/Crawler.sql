use ghsocialgraph;

create table if not exists Crawler (
	Id int auto_increment primary key,
    StartTime timestamp not null,
    EndTime timestamp not null,
    QueriesMade int not null,
    UsersAdded int not null,
    UsersUpdated int not null,
    RepositoriesAdded int not null,
    RepositoriesUpdated int not null
);
