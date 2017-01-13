-- Lab. 5
use Trivia;

--=================================================================
-- I. Functions
--=================================================================
go

if OBJECT_ID('lab5_validate_email', 'FN') is not null
	drop function lab5_validate_email;
go

create function lab5_validate_email(@email varchar(50))
returns bit
as
begin
	declare @result bit;

	set @result = 0;

	if @email is not null
	begin
		set @email = lower(@email);
		
		if	@email like '[a-z]%[a-z0-9_.]%[a-z0-9]@[a-z]%[a-z0-9_.]%[a-z].[a-z]%[a-z]'
			and @email not like '%@%@%'
			and charindex('..', @email) = 0
			and charindex('__', @email) = 0
			and @email not like '%[^a-z0-9@_.]%'
		begin
			set @result = 1
		end
	end

	return @result;
end
go

-- testing
/*
if	dbo.lab5_validate_email('aaie0000@scs.ubbcluj.ro') = 1
	and dbo.lab5_validate_email('ana@gmail.com') = 1
	and dbo.lab5_validate_email('ana2007@gmail.com') = 1
	and dbo.lab5_validate_email('a.n.a@gmail.com') = 1
	and dbo.lab5_validate_email('a_n_a@gmail.com') = 1
	and dbo.lab5_validate_email('_ana@gmail.com') = 0
	and dbo.lab5_validate_email('.ana@gmail.com') = 0
	and dbo.lab5_validate_email('ana__1996@gmail.com') = 0
	and dbo.lab5_validate_email('ana..1996@gmail.com') = 0
	and dbo.lab5_validate_email('ana@ana@ana.com') = 0
	and dbo.lab5_validate_email('2ana@gmail.com') = 0
	and dbo.lab5_validate_email('ana!ana@gmail.com') = 0
	and dbo.lab5_validate_email('ana#ana@gmail.com') = 0
select 1
else select 0;
*/

--=================================================================
-- I. dbo.Users
--=================================================================

if OBJECT_ID('lab5_create_Users', 'P') is not null
	drop procedure lab5_create_Users
go
create procedure lab5_create_Users
	@username	varchar(30),
	@email		varchar(50),
	@passwd		varchar(50),
	@return		bit output
as
begin
	begin transaction;
	begin try
		if @username is null
			raiserror('Error: username is null', 16, 1);

		if exists(select username from Users where username = @username)
			raiserror('Error: duplicate username', 16, 1);

		if dbo.lab5_validate_email(@email) = 0
			raiserror('Error: invalid email', 16, 1);

		insert into dbo.Users(username, email, passwd)
		values(
			@username,
			@email,
			lower(convert(varchar(50), HashBytes('MD5', @passwd), 2))
		)

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
if @ret = 1
	print 'User "test1" inserted successfully';
else
	print 'Failed to insert user "test1"';
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
if @ret = 0
	print 'Double insert case - success';
else
	print 'Double insert case - failure';
delete from Users where Users.username = 'test1';
*/


if OBJECT_ID('lab5_read_Users', 'P') is not null
	drop procedure lab5_read_Users;
go
create procedure lab5_read_Users
@username	varchar(50),
@return		bit output
as
begin
	declare @cmd	varchar(MAX);

	set @cmd = 'select * from dbo.Users';
	if @username is not null
		set @cmd += ' where username = ''' + @username + '''';

	begin transaction;
	begin try
		--print (@cmd);
		exec (@cmd);

		set @return = 1;

		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
declare @ret bit;
exec lab5_read_Users NULL, @ret output;
print cast(@ret as varchar(2));
exec lab5_read_Users 'admin', @ret output;
print cast(@ret as varchar(2));
*/

if OBJECT_ID('lab5_update_Users', 'P') is not null
	drop procedure lab5_update_Users;
go
create procedure lab5_update_Users
	@username	varchar(30),
	@email		varchar(50),
	@passwd		varchar(50),
	@return		bit output
as
begin
	begin transaction;
	begin try
		if @username is null
			raiserror('Error: username is null', 16, 1);

		if @email is null
			set @email = (select email from Users where username = @username);

		if dbo.lab5_validate_email(@email) = 0
			raiserror('Error: invalid email', 16, 1);

		if @passwd is null
			set @passwd = (select passwd from Users where username = @username);
		else
			set @passwd = lower(convert(varchar(50), HashBytes('MD5', @passwd), 2));

		update Users
		set email = @email, passwd = @passwd
		where username = @username;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
if @ret = 1
	print 'User "test1" inserted successfully';
else
	print 'Failed to insert user "test1"';
exec lab5_update_Users 'test1', 'test1@email.ro', NULL, @ret output;
if @ret = 1
	and (select email from Users where username = 'test1') = 'test1@email.ro'
	and (select passwd from Users where username = 'test1')
		= lower(convert(varchar(50), HashBytes('MD5', 'parola123'), 2))
	print 'Update - success';
else
	print 'Update - failed';
delete from Users where Users.username = 'test1';
exec lab5_update_Users 'sdgbhububdagubauf', NULL, NULL, @ret output;
if @ret = 0
	print 'Update (inexistent case) - correct';
else
	print 'Update (inexistent case) - failed';
exec lab5_update_Users NULL, NULL, NULL, @ret output;
if @ret = 0
	print 'Update (null case) - correct';
else
	print 'Update (null case) - failed';
*/

if OBJECT_ID('lab5_delete_Users', 'P') is not null
	drop procedure lab5_delete_Users;
go
create procedure lab5_delete_Users
@username	varchar(50),
@return		bit output
as
begin
	begin transaction;
	begin try
		if @username is null
			raiserror ('Error: username is null', 16, 1);

		if not(exists(select username from Users where username = @username))
			raiserror ('Error: username not found', 16, 1);

		delete from Users where username = @username;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
if @ret = 1
	print 'User "test1" inserted successfully';
else
	print 'Failed to insert user "test1"';
exec lab5_delete_Users 'test1', @ret output;
if @ret = 1
	print 'Delete existent user - correct';
else
	print 'Delete existent user - failed';
exec lab5_delete_Users 'test1', @ret output;
if @ret = 0
	print 'Delete inexistent user - correct';
else
	print 'Delete inexistent user - failed';
exec lab5_delete_Users NULL, @ret output;
if @ret = 0
	print 'Delete null user - correct';
else
	print 'Delete null user - failed';
delete from Users where Users.username = 'test1';
*/

--=================================================================
-- II. dbo.Players
--=================================================================

if OBJECT_ID('lab5_create_Players', 'P') is not null
	drop procedure lab5_create_Players
go
create procedure lab5_create_Players
	@username		varchar(30),
	@level			int,
	@score			int,
	@title_id		int,
	@profile_pic	varchar(40),
	@location		varchar(50),
	@gender			varchar(15),
	@return			bit output
as
begin
	begin transaction;
	begin try
		-- validare
		if @username is null
			raiserror('Error: username is null', 16, 1);

		if not(exists(select username from Users where username = @username))
			raiserror('Error: there is no user having that username', 16, 1);

		if exists(select username from Players where username = @username)
			raiserror('Error: there already is a player binded to that username', 16, 1);

		if lower(@gender) not in ('male', 'female', 'unspecified')
			raiserror('Error: invalid gender', 16, 1);

		if not(exists(select id from Titles where id = @title_id))
			raiserror('Error: invalid title id', 16, 1);

		-- pune valori implicite (daca unele campuri sunt null)
		if @level is null
			set @level = 0;

		if @score is null
			set @score = 0;

		if @profile_pic is null
			set @profile_pic = 'default_avatar.png';

		if @location is null
			set @location = 'Romania';

		insert into dbo.Players(username, [level], score, title_id, profile_picture, [location], gender)
		values(@username, @level, @score, @title_id, @profile_pic, @location, @gender);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
exec lab5_create_Players 'test1', 0, 0, 1, NULL, NULL, 'Unspecified', @ret output;
if @ret = 1
	print 'Player "test1" inserted successfully';
else
	print 'Failed to insert player "test1"';
delete from Players where Players.username = 'test1';
delete from Users where Users.username = 'test1';
*/


if OBJECT_ID('lab5_read_Players', 'P') is not null
	drop procedure lab5_read_Players;
go
create procedure lab5_read_Players
@username	varchar(50),
@return		bit output
as
begin
	declare @cmd	varchar(MAX);

	set @cmd = 'select * from dbo.Players';
	if @username is not null
		set @cmd += ' where username = ''' + @username + '''';

	begin transaction;
	begin try
		--print (@cmd);
		exec (@cmd);

		set @return = 1;

		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
declare @ret bit;
exec lab5_read_Players NULL, @ret output;
print cast(@ret as varchar(2));
exec lab5_read_Players 'admin', @ret output;
print cast(@ret as varchar(2));
*/

if OBJECT_ID('lab5_update_Players', 'P') is not null
	drop procedure lab5_update_Players;
go
create procedure lab5_update_Players
	@username		varchar(30),
	@level			int,
	@score			int,
	@title_id		int,
	@profile_pic	varchar(40),
	@location		varchar(50),
	@gender			varchar(15),
	@return			bit output
as
begin
	begin transaction;
	begin try
		if @username is null
			raiserror('Error: username is null', 16, 1);

		if @level is null
			set @level = (select [level] from Players where username = @username);

		if @score is null
			set @score = (select score from Players where username = @username);

		if @title_id is null
			set @title_id = (select title_id from Players where username = @username);

		if not(exists(select id from Titles where id = @title_id))
			raiserror('Error: invalid title id', 16, 1);

		if @profile_pic is null
			set @profile_pic = (select profile_picture from Players where username = @username);

		if @location is null
			set @location = (select [location] from Players where username = @username);

		if @gender is null
			set @gender = (select gender from Players where username = @username);

		if lower(@gender) not in ('male', 'female', 'unspecified')
			raiserror('Error: invalid gender', 16, 1);

		update Players
		set [level] = @level, score = @score, title_id = @title_id, profile_picture = @profile_pic,
			[location] = @location, gender = @gender
		where username = @username;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Players where Players.username = 'test1';
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
exec lab5_create_Players 'test1', 0, 0, 1, NULL, NULL, 'Unspecified', @ret output;
exec lab5_update_Players 'test1', 4, 100, 1, NULL, NULL, 'Unspecified', @ret output;
if @ret = 1
	and (select [level] from Players where username = 'test1') = 4
	and (select score from Players where username = 'test1') = 100
	print 'Update - success';
else
	print 'Update - failed';
delete from Players where Players.username = 'test1';
delete from Users where Users.username = 'test1';
*/

if OBJECT_ID('lab5_delete_Players', 'P') is not null
	drop procedure lab5_delete_Players;
go
create procedure lab5_delete_Players
@username	varchar(50),
@return		bit output
as
begin
	begin transaction;
	begin try
		if @username is null
			raiserror ('Error: username is null', 16, 1);

		if not(exists(select username from Players where username = @username))
			raiserror ('Error: username not found', 16, 1);

		delete from Players where username = @username;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Players where Players.username = 'test1';
delete from Users where Users.username = 'test1';
declare @ret bit;
exec lab5_create_Users 'test1', 'test1@email.com', 'parola123', @ret output;
exec lab5_create_Players 'test1', 0, 0, 1, NULL, NULL, 'Unspecified', @ret output;
exec lab5_delete_Players 'test1', @ret output;
if @ret = 1
	print 'Delete - correct';
else
	print 'Delete - failed';
delete from Players where Players.username = 'test1';
delete from Users where Users.username = 'test1';
*/

--=================================================================
-- III. dbo.Achievements
--=================================================================

if OBJECT_ID('lab5_create_Achievements', 'P') is not null
	drop procedure lab5_create_Achievements
go
create procedure lab5_create_Achievements
	@name			varchar(30),
	@description	varchar(255),
	@icon_url		varchar(50),
	@return			bit output
as
begin
	begin transaction;
	begin try
		-- validare
		if @name is null
			raiserror('Error: achievement name is null', 16, 1);

		if exists(select achievement_name from Achievements where achievement_name = @name)
			raiserror('Error: duplicate achievement name', 16, 1);

		if @description is null
			raiserror('Error: description cannot be empty', 16, 1);

		-- pune valori implicite (daca unele campuri sunt null)
		if @icon_url is null
			set @icon_url = 'achievement_default.png';

		insert into dbo.Achievements(achievement_name, [description], icon_url)
		values(@name, @description, @icon_url);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
if @ret = 1
	print 'Achievements - CREATE: success';
else
	print 'Achievements - CREATE: failure';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

if OBJECT_ID('lab5_read_Achievements', 'P') is not null
	drop procedure lab5_read_Achievements;
go
create procedure lab5_read_Achievements
@name	varchar(30),
@return	bit output
as
begin
	declare @cmd	varchar(MAX);

	set @cmd = 'select * from dbo.Achievements';
	if @name is not null
		set @cmd += ' where achievement_name = ''' + @name + '''';

	begin transaction;
	begin try
		--print (@cmd);
		exec (@cmd);

		set @return = 1;

		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
declare @ret bit;
exec lab5_read_Achievements NULL, @ret output;
print cast(@ret as varchar(2));
exec lab5_read_Achievements 'Lemon', @ret output;
print cast(@ret as varchar(2));
*/

if OBJECT_ID('lab5_update_Achievements', 'P') is not null
	drop procedure lab5_update_Achievements;
go
create procedure lab5_update_Achievements
	@name			varchar(30),
	@description	varchar(255),
	@icon_url		varchar(50),
	@return			bit output
as
begin
	begin transaction;
	begin try
		if @name is null
			raiserror('Error: achievement name is null', 16, 1);

		if not(exists(select achievement_name from Achievements where achievement_name = @name))
			raiserror('Error: achievement having that name not found', 16, 1);

		if @description is null
			set @description = (select [description] from Achievements where achievement_name = @name);

		if @icon_url is null
			set @icon_url = (select icon_url from Achievements where achievement_name = @name);

		update Achievements
		set [description] = @description, icon_url = @icon_url
		where achievement_name = @name

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
exec lab5_update_Achievements 'test1', 'descr-update', NULL, @ret output;
if @ret = 1
	and (select [description] from Achievements where achievement_name = 'test1') = 'descr-update'
	and (select icon_url from Achievements where achievement_name = 'test1') = 'icon.png'
	print 'Achievements - UPDATE: success';
else
	print 'Achievements - UPDATE: failure';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

if OBJECT_ID('lab5_delete_Achievements', 'P') is not null
	drop procedure lab5_delete_Achievements;
go
create procedure lab5_delete_Achievements
@name	varchar(30),
@return	bit output
as
begin
	begin transaction;
	begin try
		if @name is null
			raiserror ('Error: achievement name is null', 16, 1);

		if not(exists(select achievement_name from Achievements where achievement_name = @name))
			raiserror ('Error: achievement with that name not found', 16, 1);

		delete from Achievements where achievement_name = @name;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
exec lab5_delete_Achievements 'test1', @ret output;
if @ret = 1
	print 'Achievements - DELETE: success';
else
	print 'Achievements - DELETE: failure';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

--=================================================================
-- IV. dbo.AchievementHistory
--=================================================================

if OBJECT_ID('lab5_create_AchievementHistory', 'P') is not null
	drop procedure lab5_create_AchievementHistory
go
create procedure lab5_create_AchievementHistory
	@ach_name		varchar(30),
	@username		varchar(50),
	@return			bit output
as
begin
	declare @time_achieved	datetime;
	declare @achievement_id	int;

	begin transaction;
	begin try
		-- validare
		if @ach_name is null or @username is null
			raiserror('Error: at least one parameter is null', 16, 1);

		if not(exists(select achievement_name from Achievements where achievement_name = @ach_name))
			raiserror('Error: invalid achievement name', 16, 1);

		if not(exists(select username from Players where username = @username))
			raiserror('Error: invalid username', 16, 1);

		-- initializare
		set @achievement_id = (select id from Achievements where achievement_name = @ach_name);
		set @time_achieved = GetDate();

		insert into dbo.AchievementHistory(achievement_id, username, time_achieved)
		values (@achievement_id, @username, @time_achieved);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from AchievementHistory where AchievementHistory.username = 'test_player'
	and AchievementHistory.achievement_id = (select id from Achievements where achievement_name = 'test1');
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
exec lab5_create_Users 'test_player', 'test@test.com', 'pass', @ret output;
exec lab5_create_Players 'test_player', 0, 0, 1, NULL, NULL, 'Female', @ret output;
exec lab5_create_AchievementHistory 'test1', 'test_player', @ret output;
if @ret = 1
	print 'AchievementHistory - CREATE: success';
else
	print 'AchievementHistory - CREATE: failure';
delete from AchievementHistory where AchievementHistory.username = 'test_player'
	and AchievementHistory.achievement_id = (select id from Achievements where achievement_name = 'test1');
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

if OBJECT_ID('lab5_read_AchievementHistory', 'P') is not null
	drop procedure lab5_read_AchievementHistory;
go
create procedure lab5_read_AchievementHistory
@ach_name	varchar(30),
@username	varchar(50),
@return		bit output
as
begin
	declare @cmd	varchar(MAX);

	set @cmd = 'select * from dbo.AchievementHistory where ';
	if @ach_name is not null
		set @cmd += 'achievement_name = ''' + @ach_name + ''' and ';
	if @username is not null
		set @cmd += 'username = ''' + @username + ''' and ';
	set @cmd += '1 = 1';

	begin transaction;
	begin try
		print (@cmd);
		exec (@cmd);

		set @return = 1;

		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
declare @ret bit;
exec lab5_read_AchievementHistory NULL, NULL, @ret output;
print cast(@ret as varchar(2));
exec lab5_read_AchievementHistory NULL, 'helen', @ret output;
print cast(@ret as varchar(2));
*/

if OBJECT_ID('lab5_update_AchievementHistory', 'P') is not null
	drop procedure lab5_update_AchievementHistory;
go
create procedure lab5_update_AchievementHistory
	@ach_name_old	varchar(30),
	@ach_name_new	varchar(30),
	@username		varchar(50),
	@return			bit output
as
begin
	begin transaction;
	begin try
		if @ach_name_old is null or @username is null
			raiserror('Error: old achievement name OR username is null', 16, 1);

		if not(exists(select id from AchievementHistory where AchievementHistory.username = @username and
			AchievementHistory.achievement_id = (select id from Achievements where achievement_name = @ach_name_old)))
			raiserror('Error: there is no such entry in AchievementHistory', 16, 1);

		if not(exists(select achievement_name from Achievements where achievement_name = @ach_name_new))
			raiserror('Error: new achievement name is invalid', 16, 1);

		update AchievementHistory
		set achievement_id = (select id from Achievements where achievement_name = @ach_name_new)
		where username = @username
			and achievement_id = (select id from Achievements where achievement_name = @ach_name_old);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from AchievementHistory where AchievementHistory.username = 'test_player';
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test2';
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
exec lab5_create_Achievements 'test2', 'test2 - description', 'icon.png', @ret output;
exec lab5_create_Users 'test_player', 'test@test.com', 'pass', @ret output;
exec lab5_create_Players 'test_player', 0, 0, 1, NULL, NULL, 'Female', @ret output;
exec lab5_create_AchievementHistory 'test1', 'test_player', @ret output;
exec lab5_update_AchievementHistory 'test1', 'test2', 'test_player', @ret output;
if @ret = 1
	and (select achievement_id from AchievementHistory where AchievementHistory.username = 'test_player'
			and achievement_id = (select id from Achievements where achievement_name = 'test2')) is not null
	print 'AchievementHistory - UPDATE: success';
else
	print 'AchievementHistory - UPDATE: failure';
delete from AchievementHistory where AchievementHistory.username = 'test_player';
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test2';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

if OBJECT_ID('lab5_delete_AchievementHistory', 'P') is not null
	drop procedure lab5_delete_AchievementHistory;
go
create procedure lab5_delete_AchievementHistory
@ach_name	varchar(30),
@username	varchar(50),
@return		bit output
as
begin
	begin transaction;
	begin try
		if @ach_name is null or @username is null
			raiserror ('Error: at least one parameter is null', 16, 1);

		if not(exists(select id from AchievementHistory where AchievementHistory.username = @username and
			AchievementHistory.achievement_id = (select id from Achievements where achievement_name = @ach_name)))
			raiserror('Error: there is no such entry in AchievementHistory', 16, 1);

		delete from AchievementHistory where username = @username and
			achievement_id = (select id from Achievements where achievement_name = @ach_name);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from AchievementHistory where AchievementHistory.username = 'test_player'
	and AchievementHistory.achievement_id = (select id from Achievements where achievement_name = 'test1');
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test1';
declare @ret bit;
exec lab5_create_Achievements 'test1', 'test1 - description', 'icon.png', @ret output;
exec lab5_create_Users 'test_player', 'test@test.com', 'pass', @ret output;
exec lab5_create_Players 'test_player', 0, 0, 1, NULL, NULL, 'Female', @ret output;
exec lab5_create_AchievementHistory 'test1', 'test_player', @ret output;
exec lab5_delete_AchievementHistory 'test1', 'test_player', @ret output;
if @ret = 1
	print 'AchievementHistory - DELETE: success';
else
	print 'AchievementHistory - DELETE: failure';
delete from AchievementHistory where AchievementHistory.username = 'test_player'
	and AchievementHistory.achievement_id = (select id from Achievements where achievement_name = 'test1');
delete from Players where Players.username = 'test_player';
delete from Users where Users.username = 'test_player';
delete from Achievements where Achievements.achievement_name = 'test1';
*/

--=================================================================
-- V. dbo.Cathegories
--=================================================================

if OBJECT_ID('lab5_create_Cathegories', 'P') is not null
	drop procedure lab5_create_Cathegories
go
create procedure lab5_create_Cathegories
	@name			varchar(30),
	@description	text,
	@return			bit output
as
begin
	begin transaction;
	begin try
		-- validare
		if @name is null
			raiserror('Error: cathegory name is null', 16, 1);

		if exists(select cathegory_name from Cathegories where cathegory_name = @name)
			raiserror('Error: duplicate cathegory name', 16, 1);

		if @description is null
			raiserror('Error: description cannot be empty', 16, 1);

		insert into dbo.Cathegories(cathegory_name, [description])
		values(@name, @description);

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Cathegories where Cathegories.cathegory_name = 'test1';
declare @ret bit;
exec lab5_create_Cathegories 'test1', 'test1 - description', @ret output;
if @ret = 1
	print 'Cathegories - CREATE: success';
else
	print 'Cathegories - CREATE: failure';
delete from Cathegories where Cathegories.cathegory_name = 'test1';
*/

if OBJECT_ID('lab5_read_Cathegories', 'P') is not null
	drop procedure lab5_read_Cathegories;
go
create procedure lab5_read_Cathegories
@name	varchar(30),
@return	bit output
as
begin
	declare @cmd	varchar(MAX);

	set @cmd = 'select * from dbo.Cathegories';
	if @name is not null
		set @cmd += ' where cathegory_name = ''' + @name + '''';

	begin transaction;
	begin try
		--print (@cmd);
		exec (@cmd);

		set @return = 1;

		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
declare @ret bit;
exec lab5_read_Cathegories NULL, @ret output;
print cast(@ret as varchar(2));
exec lab5_read_Cathegories 'Biology', @ret output;
print cast(@ret as varchar(2));
*/

if OBJECT_ID('lab5_update_Cathegories', 'P') is not null
	drop procedure lab5_update_Cathegories;
go
create procedure lab5_update_Cathegories
	@name			varchar(30),
	@description	text,
	@return			bit output
as
begin
	begin transaction;
	begin try
		if @name is null
			raiserror('Error: cathegory name is null', 16, 1);

		if not(exists(select cathegory_name from Cathegories where cathegory_name = @name))
			raiserror('Error: cathegory having that name not found', 16, 1);

		if @description is null
			set @description = cast((select [description] from Cathegories where cathegory_name = @name) as text);

		update Cathegories
		set [description] = @description
		where cathegory_name = @name

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Cathegories where Cathegories.cathegory_name = 'test1';
declare @ret bit;
exec lab5_create_Cathegories 'test1', 'test1 - description', @ret output;
exec lab5_update_Cathegories 'test1', 'descr-update', @ret output;
if @ret = 1
	and (select [description] from Cathegories where cathegory_name = 'test1') like 'descr-update'
	print 'Cathegories - UPDATE: success';
else
	print 'Cathegories - UPDATE: failure';
delete from Cathegories where Cathegories.cathegory_name = 'test1';
*/

if OBJECT_ID('lab5_delete_Cathegories', 'P') is not null
	drop procedure lab5_delete_Cathegories;
go
create procedure lab5_delete_Cathegories
@name	varchar(30),
@return	bit output
as
begin
	begin transaction;
	begin try
		if @name is null
			raiserror ('Error: cathegory name is null', 16, 1);

		if not(exists(select cathegory_name from Cathegories where cathegory_name = @name))
			raiserror ('Error: cathegory with that name not found', 16, 1);

		delete from Cathegories where cathegory_name = @name;

		set @return = 1;
		if @@TRANCOUNT > 0
			commit;
	end try
	begin catch
		print ERROR_MESSAGE();
		if @@TRANCOUNT > 0
			rollback;
		set @return = 0;
	end catch
end
go

-- testing
/*
delete from Cathegories where Cathegories.cathegory_name = 'test1';
declare @ret bit;
exec lab5_create_Cathegories 'test1', 'test1 - description', @ret output;
exec lab5_delete_Cathegories 'test1', @ret output;
if @ret = 1
	print 'Cathegories - DELETE: success';
else
	print 'Cathegories - DELETE: failure';
delete from Cathegories where Cathegories.cathegory_name = 'test1';
*/

--=================================================================
-- VI. Views
--=================================================================

if OBJECT_ID('lab5_users_players_view', 'V') is not null
	drop view lab5_users_players_view;
go
create view lab5_users_players_view
as
	select Users.username, email, [level], score, [location], gender, profile_picture as [profile picture]
	from Users
	inner join Players
	on Users.username = Players.username;
go

if OBJECT_ID('lab5_achievement_history_view', 'V') is not null
	drop view lab5_achievement_history_view
go
create view lab5_achievement_history_view
as
	select username, achievement_name as achievement, [description], time_achieved as [date and time]
	from AchievementHistory
	inner join Achievements
	on AchievementHistory.achievement_id = Achievements.id;
go

-- testing
/*
select * from lab5_users_players_view order by [level] desc;
select * from lab5_achievement_history_view order by username;
*/
