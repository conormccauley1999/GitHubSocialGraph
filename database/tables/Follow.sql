use ghsocialgraph;

create table if not exists Follow (
	Id int auto_increment primary key,
    FollowerUserId int,
    FollowingUserId int,
	DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_Follow_User_1 foreign key (FollowerUserId) references `User`(Id),
    constraint FK_Follow_User_2 foreign key (FollowingUserId) references `User`(Id),
    constraint CR_Follow_UsersDiffer check (FollowerUserId != FollowingUserId),
    unique(FollowerUserId, FollowingUserId)
);
