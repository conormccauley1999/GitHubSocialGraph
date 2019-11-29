use ghsocialgraph;
drop view if exists CommitChart_Values;

create view CommitChart_Values as
    select c.RepositoryId, year(c.`Timestamp`) `Year`, month(c.`Timestamp`) `Month`, count(c.Id) Commits
    from `Commit` c
    join RepositoryInformation r on r.RepositoryId = c.RepositoryId
    where not r.IsFork
    group by c.RepositoryId, year(c.`Timestamp`), month(c.`Timestamp`)
;
