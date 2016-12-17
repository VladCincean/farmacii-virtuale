use Trivia;

--=================================================================
-- 0. before everything else
--=================================================================

/*
alter table AchievementHistory
drop constraint pk_achievement_history;
alter table AchievementHistory
drop column id;
alter table AchievementHistory
add constraint pk_achievement_history
	primary key(achievement_id, username);
*/

/*
select * into Achievements_backup from Achievements;
select * into GameSessions_backup from GameSessions;
select * into LoginHistory_backup from LoginHistory;
select * into AchievementHistory_backup from AchievementHistory;
select * into Games_backup from Games;
*/

--=================================================================
-- I. insert data procedures
--=================================================================

-- table with 1 PK, no FK
if OBJECT_ID('lab4_insert_data_Achievements', 'P') is not null
	drop procedure lab4_insert_data_Achievements
go
create procedure lab4_insert_data_Achievements
	@n int
as
begin
	declare @i						int;
	declare @new_achievement_name	varchar(30);
	declare @new_description		varchar(255);
	declare	@new_icon_url			varchar(50);
	
	set @i = 1;

	while @i < @n
	begin
		set @new_achievement_name = 'ach_name_' + cast(@i as varchar(7));
		set @new_description = 'description_' + cast(@i as varchar(7));
		set @new_icon_url = 'icon_' + cast(@i as varchar(7)) + '.png';

		insert into dbo.Achievements(achievement_name, [description], icon_url)
		values
			(@new_achievement_name, @new_description, @new_icon_url);

		set @i += 1;
	end
end
go

-- table with 1 PK and >= 1 FK
if OBJECT_ID('lab4_insert_data_GameSessions', 'P') is not null
	drop procedure lab4_insert_data_GameSessions
go
create procedure lab4_insert_data_GameSessions
	@n int
as
begin
	declare @i		int;
	declare @q1		int;
	declare @q2		int;
	declare @q3		int;
	declare @q4		int;
	declare @q5		int;
	declare	@qB		int;
	declare	@start	datetime;

	set @i = 1;
	
	while @i < @n
	begin
		set @q1 = (select top 1 q.id from Questions q order by newid());
		set @q2 = (select top 1 q.id from Questions q order by newid());
		while (@q1 = @q2)
			set @q2 = (select top 1 q.id from Questions q order by newid());
		set @q3 = (select top 1 q.id from Questions q order by newid());
		while (@q1 = @q3 or @q1 = @q2)
			set @q3 = (select top 1 q.id from Questions q order by newid());
		set @q4 = (select top 1 q.id from Questions q order by newid());
		while (@q1 = @q4 or @q2 = @q4 or @q3 = @q4)
			set @q4 = (select top 1 q.id from Questions q order by newid());
		set @q5 = (select top 1 q.id from Questions q order by newid());
		while (@q1 = @q5 or @q2 = @q5 or @q3 = @q5 or @q4 = @q5)
			set @q5 = (select top 1 q.id from Questions q order by newid());
		set @qB = (select top 1 q.id from Questions q order by newid());
		while (@q1 = @qB or @q2 = @qB or @q3 = @qB or @q4 = @qB or @q5 = @qB)
			set @qB = (select top 1 q.id from Questions q order by newid());

		set @start = getdate();

		insert into dbo.GameSessions
		(question1_id, question2_id, question3_id, question4_id, question5_id, questionBonus_id, datetime_start)
		values (@q1, @q2, @q3, @q4, @q5, @qB, @start);

		set @i += 1;
	end
end
go

-- another table with 1 PK, >= 1 FK
if OBJECT_ID('lab4_insert_data_LoginHistory', 'P') is not null
	drop procedure lab4_insert_data_LoginHistory
go
create procedure lab4_insert_data_LoginHistory
	@n int
as
begin
	declare @i			int;
	declare	@uname		varchar(30);
	declare @ip_addr	varchar(30);
	declare	@act_time	int;

	set @i = 1;

	while @i < @n
	begin
		set @uname = (select top 1 u.username from Users u order by newid());
		set @ip_addr =	cast(abs(checksum(newid())) % 256 as varchar(3)) + '.' +
						cast(abs(checksum(newid())) % 256 as varchar(3)) + '.' +
						cast(abs(checksum(newid())) % 256 as varchar(3)) + '.' +
						cast(abs(checksum(newid())) % 256 as varchar(3));
		set @act_time = abs(checksum(newid())) % 120 + 1;
		insert into dbo.LoginHistory(username, browser, ip_address, activity_time)
		values (@uname, 'Chrome', @ip_addr, @act_time);

		set @i += 1;
	end
end
go

-- table with 2 PKs
if OBJECT_ID('lab4_insert_data_AchievementHistory', 'P') is not null
	drop procedure lab4_insert_data_AchievementHistory
go
create procedure lab4_insert_data_AchievementHistory
	@n int
as
begin
	declare	@i					int;
	declare @new_achievement_id	int;
	declare	@new_username		varchar(30);
	declare @new_time			datetime;

	set @i = 1;

	while @i < @n
	begin
		set @new_achievement_id = (select top 1 a.id from Achievements a order by newid());
		set @new_username = (select top 1 u.username from Users u order by newid());
		while exists(select * from AchievementHistory ah where ah.username = @new_username and ah.achievement_id = @new_achievement_id)
		begin
			set @new_achievement_id = (select top 1 a.id from Achievements a order by newid());
			set @new_username = (select top 1 u.username from Users u order by newid());
		end
		set @new_time = getdate();

		insert into AchievementHistory(achievement_id, username, time_achieved)
		values (@new_achievement_id, @new_username, @new_time);

		set @i += 1;
	end
end
go

--=================================================================
-- II. delete data procedures
--=================================================================

if OBJECT_ID('lab4_delete_data_Achievements', 'P') is not null
	drop procedure lab4_delete_data_Achievements
go
create procedure lab4_delete_data_Achievements
	@n int
as
begin
	while @n > 0
	begin
		delete top (1) from Achievements;
		set @n -= 1;
	end
end
go

if OBJECT_ID('lab4_delete_data_GameSessions', 'P') is not null
	drop procedure lab4_delete_data_GameSessions
go
create procedure lab4_delete_data_GameSessions
	@n int
as
begin
	while @n > 0
	begin
		delete top (1) from dbo.GameSessions;
		set @n -= 1;
	end
end
go

if OBJECT_ID('lab4_delete_data_LoginHistory', 'P') is not null
	drop procedure lab4_delete_data_LoginHistory
go
create procedure lab4_delete_data_LoginHistory
	@n int
as
begin
	while @n > 0
	begin
		delete top (1) from dbo.AchievementHistory
		set @n -= 1;
	end
end
go

if OBJECT_ID('lab4_delete_data_AchievementHistory', 'P') is not null
	drop procedure lab4_delete_data_AchievementHistory
go
create procedure lab4_delete_data_AchievementHistory
	@n int
as
begin
	while @n > 0
	begin
		delete top (1) from dbo.AchievementHistory
		set @n -= 1;
	end
end
go

--=================================================================
-- III. views
--=================================================================

-- 1) a view with a SELECT statement working on a single table
if OBJECT_ID('lab4_all_achievements_view', 'V') is not null
	drop view lab4_all_achievements_view
go
create view lab4_all_achievements_view
as
	select * from dbo.Achievements
go

-- 2) a view with a SELECT statement working on at least two tables
if OBJECT_ID('lab4_user_logins_view', 'V') is not null
	drop view lab4_user_logins_view
go
create view lab4_user_logins_view
as
	select lh.username, u.email, lh.activity_time
	from dbo.LoginHistory lh
	inner join Users u
	on lh.username = u.username
go

-- 3) a view witha a SELECT statement working on at least two tables and having a GROUP BY clause
if OBJECT_ID('lab4_bonus_chem_questions_view', 'V') is not null
	drop view lab4_bonus_chem_questions_view
go
create view lab4_bonus_chem_questions_view
as
	select	question_text			as [question],
			min(q.optionA)			as [A],
			min(q.optionB)			as [B],
			min(q.optionC)			as [C],
			min(q.optionD)			as [D],
			min(q.correct_answer)	as [correct answer],
			count(questionBonus_id) as [number of times]
	from Questions	q
	inner join GameSessions	gs
	on q.id = gs.questionBonus_id
	inner join Cathegories	c
	on c.id = q.cathegory_id
	where c.cathegory_name = 'Chemistry'
	group by question_text
go

--=================================================================
-- IV. testing configuration set-up
--=================================================================

delete from dbo.TestViews;
delete from dbo.TestTables;
delete from dbo.Tests;
delete from dbo.Tables;
delete from dbo.Views;

-- 1) 'Tables' table
set identity_insert dbo.Tables on;
insert into dbo.Tables([TableID], [Name])
values
	(1, 'Achievements'),
	(2, 'GameSessions'),
	(3, 'LoginHistory'),
	(4, 'AchievementHistory');
set identity_insert dbo.Tables off;

-- 2) 'Views' table
set identity_insert dbo.Views on;
insert into dbo.Views([ViewID], [Name])
values
	(1, 'lab4_all_achievements_view'),
	(2, 'lab4_user_logins_view'),
	(3, 'lab4_bonus_chem_questions_view');
set identity_insert dbo.Views off;

-- 3) 'Tests' table
set identity_insert dbo.Tests on;
insert into dbo.Tests([TestID], [Name])
values
	(1, 'test_a'),
	(2, 'test_b');
set identity_insert dbo.Tests off;

-- 4) 'TestTables' table
insert into dbo.TestTables([TestID], [TableID], [NoOfRows], [Position])
values
	(1, 1, 1000, 3),
	(1, 2, 1000, 1),
	(1, 3, 1000, 2),
	(1, 4, 1000, 4),
	(2, 1, 10000, 3),
	(2, 2, 10000, 1),
	(2, 3, 10000, 2),
	(2, 4, 10000, 4);

-- 5) 'TestViews' table
insert into dbo.TestViews([TestID], [ViewID])
values
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 1),
	(2, 2),
	(2, 3);

--=================================================================
-- V. run_test procedure
--=================================================================

if OBJECT_ID('lab4_run_test', 'P') is not null
	drop procedure lab4_run_test
go
create procedure lab4_run_test
	@test_name nvarchar(50)
as
begin
	-- 1) declaring variables
	declare	@test_id		int;
	declare @table_id		int;
	declare @view_id		int;
	declare @nr_rows		int;
	declare @table_name		varchar(50);
	declare @view_name		varchar(50);
	declare @start_at		datetime;
	declare @end_at			datetime;

	-- 2) init
	set @test_id = -1;
	select @test_id = [TestID] from dbo.Tests where [Name] = @test_name;
	if @test_id = -1
	begin
		print('Error! There is no test named ' + @test_name + '.');
		return ;
	end
	set identity_insert dbo.TestRuns on;
	insert into dbo.TestRuns([TestRunID], [Description], [StartAt], [EndAt])
	values (@test_id, 'TestRun of ' + @test_name, NULL, NULL);
	set identity_insert dbo.TestRuns off;
	update TestRuns set [StartAt] = getdate() where [TestRunID] = @test_id;

	-- 3) TEST: inserting rows in the table
	declare @cmd_insert	varchar(MAX);
	declare cursor_insert cursor for
		select TableId, NoOfRows from dbo.TestTables
		where [TestId] = @test_id order by [Position]
	for read only;
	
	open cursor_insert;
	fetch cursor_insert into @table_id, @nr_rows;
	while @@FETCH_STATUS = 0
	begin
		set @table_name = (select t.[Name] from dbo.Tables t where t.[TableID] = @table_id);
		set @cmd_insert = 'exec lab4_insert_data_' + @table_name + ' '+ cast(@nr_rows as varchar(8));
		print 'Inserting ' + cast(@nr_rows as varchar(8)) + ' rows into ' + @table_name + '...';
		set @start_at = getdate();
		print 'Start: ' + cast(@start_at as varchar(100));
		exec (@cmd_insert);
		set @end_at = getdate();
		print 'Finished: ' + cast(@end_at as varchar(100));

		insert into TestRunTables([TestRunID], [TableID], [StartAt], [EndAt])
		values (@test_id, @table_id, @start_at, @end_at);

		fetch cursor_insert into @table_id, @nr_rows;
	end

	close cursor_insert;
	deallocate cursor_insert;

	-- 4) TEST: evaluating the views
	declare @cmd_evaluate_view	varchar(MAX);
	declare cursor_views cursor for
		select ViewId from dbo.TestViews
		where [TestId] = @test_id
	for read only;
	
	open cursor_views;
	fetch cursor_views into @view_id;
	while @@FETCH_STATUS = 0
	begin
		set @view_name = (select v.[Name] from dbo.Views v where v.[ViewID] = @view_id);
		set @cmd_evaluate_view = 'select * from ' + @view_name;
		print 'Evaluating view "' + @view_name + '"...';
		set @start_at = getdate();
		print 'Start: ' + cast(@start_at as varchar(100));
		exec (@cmd_evaluate_view);
		set @end_at = getdate();
		print 'Finished: ' + cast(@end_at as varchar(100));

		insert into TestRunViews([TestRunID], [ViewID], [StartAt], [EndAt])
		values (@test_id, @view_id, @start_at, @end_at);

		fetch cursor_views into @view_id;
	end

	close cursor_views;
	deallocate cursor_views;

	-- 5) TEST: deleting the information from the tables
	declare @cmd_delete	varchar(MAX);
	declare cursor_delete cursor for
		select TableId, NoOfRows from dbo.TestTables
		where [TestId] = @test_id order by [Position] desc
	for read only;
	
	open cursor_delete;
	fetch cursor_delete into @table_id, @nr_rows;
	while @@FETCH_STATUS = 0
	begin
		set @table_name = (select t.[Name] from dbo.Tables t where t.[TableID] = @table_id);
		set @cmd_delete = 'exec lab4_delete_data_' + @table_name + ' '+ cast(@nr_rows as varchar(8));
		print 'Deleting ' + cast(@nr_rows as varchar(8)) + ' rows from ' + @table_name + '...';
		set @start_at = getdate();
		print 'Start: ' + cast(@start_at as varchar(100));
		exec (@cmd_delete);
		set @end_at = getdate();
		print 'Finished: ' + cast(@end_at as varchar(100));

		insert into TestRunTables([TestRunID], [TableID], [StartAt], [EndAt])
		values (@test_id, @table_id, @start_at, @end_at);

		fetch cursor_delete into @table_id, @nr_rows;
	end

	close cursor_delete;
	deallocate cursor_delete;

	-- 6) finish
	update TestRuns set [EndAt] = getdate() where [TestRunID] = @test_id;
end
go

--=================================================================
-- VI. test
--=================================================================

delete from TestRunTables;
delete from TestRunViews;
delete from TestRuns;

delete from AchievementHistory;
delete from Achievements;
delete from LoginHistory;
delete from Games;
delete from GameSessions;

exec lab4_run_test 'test_a';

select * from TestRuns;
select * from TestRunTables;
select * from TestRunViews;

select * from Achievements;