use ghsocialgraph;

create table if not exists Crawler (
	Id int auto_increment primary key,
    StartTime timestamp not null,
    EndTime timestamp not null,
    QueriesMade int not null
);
