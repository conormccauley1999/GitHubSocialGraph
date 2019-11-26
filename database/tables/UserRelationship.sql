use ghsocialgraph;

create table if not exists UserRelationship (
	Id int auto_increment primary key,
    UserId int,
	ParentUserId int,
    CurrentDepth int null,
    DateCreated timestamp not null,
    DateModified timestamp null,
    constraint FK_UserRelationship_User_1 foreign key (UserId) references `User`(Id),
    constraint FK_UserRelationship_User_2 foreign key (ParentUserId) references `User`(Id),
    constraint CR_UserRelationship_UsersDiffer check (UserId != ParentUserId),
    unique(UserId, ParentUserId)
);
