use ghsocialgraph;

create table if not exists `User` (
	Id int auto_increment primary key,
    IsExplored bool not null default false,
    IsRoot bool not null default false,
    `Ignore` bool not null default false,
	Username varchar(255) not null,
    LastCrawled timestamp null,
    DateCreated timestamp not null,
    DateModified timestamp null
);
