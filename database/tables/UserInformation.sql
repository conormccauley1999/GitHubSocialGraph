use ghsocialgraph;

create table if not exists UserInformation (
	Id int auto_increment primary key,
    UserId int,
    `Name` varchar(255) null,
    AvatarUrl varchar(255) null,
    Company varchar(255) null,
    Location varchar(255) null,
    Email varchar(255) null,
    Bio text null,
    RepositoryCount int null,
    FollowerCount int null,
    FollowingCount int null,
    DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_UserInformation_User foreign key (UserId) references `User`(Id),
    unique(UserId)
);
