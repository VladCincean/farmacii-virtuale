use [Trivia];
go
-- 1. Modify the type of a column
-- Players.profile_picture from varchar(50) not null to varchar(40)

create procedure modify_column_type
as
begin
	if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'Players')
		if exists(select * from INFORMATION_SCHEMA.COLUMNS
		where TABLE_NAME = 'Players' and COLUMN_NAME = 'profile_picture')
			begin
				alter table [Players]
				alter column [profile_picture] varchar(40) null;
				print 'Column Players.profile_picture changed type to varchar(40) null';
			end
		else
			print 'Error! Cannot find column Players.profile_picture.';
	else
		print 'Error! Cannot find table Players.';
end

go
-- ~1. Modify the type of a column (reverse)
-- Players.profile_picture from varchar(40) to varchar(50) not null

create procedure modify_column_type_rev
as
begin
	if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'Players')
		if exists(select * from INFORMATION_SCHEMA.COLUMNS
		where TABLE_NAME = 'Players' and COLUMN_NAME = 'profile_picture')
			begin
				alter table [Players]
				alter column [profile_picture] varchar(50) not null;
				print 'Column Players.profile_picture changed type to varchar(50) not null';
			end
		else
			print 'Error! Cannot find column Players.profile_picture.';
	else
		print 'Error! Cannot find table Players.';
end

go
-- 2. Add a default constraint
-- Player.location -> 'Romania'

create procedure add_default_constraint_location
as
begin
	if not exists(select * from sys.default_constraints where name = 'dc_location')
	begin
		if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'Players')
			if exists(select * from INFORMATION_SCHEMA.COLUMNS
			where TABLE_NAME = 'Players' and COLUMN_NAME = 'location')
				begin
					alter table [Players]
					add constraint dc_location default 'Romania' for [location];
					print 'Default constraint "Romania" for Players.location successfully added.';
				end
			else
				print 'Error! Cannot find column Players.location.';
		else
			print 'Error! Cannot find table Players.';
	end
	else
		print 'Error! Default constraint dc_location already exists.';
end

go
-- ~2. Add a default constraint (reverse)
-- Player.location -> 'Romania'

create procedure remove_default_constraint_location
as
begin
	if exists(select * from sys.default_constraints where name = 'dc_location')
	begin
		if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'Players')
			if exists(select * from INFORMATION_SCHEMA.COLUMNS
			where TABLE_NAME = 'Players' and COLUMN_NAME = 'location')
				begin
					alter table [Players]
					drop constraint dc_location;
					print 'Default constraint "Romania" for Players.location successfully dropped.';
				end
			else
				print 'Error! Cannot find column Players.location.';
		else
			print 'Error! Cannot find table Players.';
	end
	else
		print 'Error! Default constraint dc_location does not exist.';
end

go
-- 3. Create a new table
-- LoginHistory

create procedure create_table_login_history
as
begin
	if not exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'LoginHistory')
	begin
		create table [LoginHistory]
		(
			lh_id		int identity(1, 1)	not null,
			username	varchar(30)			not null,
			browser		varchar(30)			not null,
			ip_address	varchar(30)			not null,

			constraint	pk_login_history	primary key(lh_id)
		);
		print 'Table LoginHistory successfully created.';
	end
	else
		print 'Error! Table LoginHistory already exists.';
end

go
-- ~3. Remove a table (3. reverse)
-- LoginHistory

create procedure drop_table_login_history
as
begin
	if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'LoginHistory')
	begin
		drop table [LoginHistory];
		print 'Table LoginHistory successfully dropped.';
	end
	else
		print 'Error! Table LoginHistory not found.';
end

go
-- 4. Add a column
-- LoginHistory.activity_time

create procedure add_column_activity_time
as
begin
	if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'LoginHistory')
	begin
		if not exists(select * from INFORMATION_SCHEMA.COLUMNS where
		TABLE_NAME = 'LoginHistory' and COLUMN_NAME = 'activity_time')
		begin
			alter table [LoginHistory]
			add [activity_time] int not null constraint dc_activity_time default 0;
			print 'Column LoginHistory.activity_time successfully added.';
		end
		else
			print 'Error! Column LoginHistory.activity_time already exists.';
	end
	else
		print 'Error! Table LoginHistory not found.';
end

go
-- ~4. Remove a column (4. reverse)
-- LoginHistory.activity_time

create procedure drop_column_activity_time
as
begin
	if exists(select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME = 'LoginHistory')
	begin
		if exists(select * from INFORMATION_SCHEMA.COLUMNS where
		TABLE_NAME = 'LoginHistory' and COLUMN_NAME = 'activity_time')
		begin
			alter table [LoginHistory]
			drop constraint [dc_activity_time];
			alter table [LoginHistory]
			drop column [activity_time];
			print 'Column LoginHistory.activity_time successfully dropped.';
		end
		else
			print 'Error! Column LoginHistory.activity_time not found.';
	end
	else
		print 'Error! Table LoginHistory not found.';
end

go
-- 5. Create a foreign key constraint
-- LoginHistory.username references Users.username

create procedure add_fk_constraint_lh_username
as
begin
	if not exists(select * from sys.foreign_keys where name = 'fk_lh_username')
	begin
		alter table [LoginHistory]
		add constraint [fk_lh_username] foreign key (username)
			references Users(username);
		print 'Foreign key constraint fk_lh_username successfully created.';
	end
	else
		print 'Error! Foreign key fk_lh_username already exists.';
end

go
-- ~5. Create a foreign key constraint (reverse)
-- LoginHistory.username references Users.username

create procedure drop_fk_constraint_lh_username
as
begin
	if exists(select * from sys.foreign_keys where name = 'fk_lh_username')
	begin
		alter table [LoginHistory]
		drop constraint [fk_lh_username];
		print 'Foreign key constraint fk_lh_username successfully removed.';
	end
	else
		print 'Error! Foreign key fk_lh_username does not exist.';
end

go
-- Version control
/*
   1      2      3      4      5
  --->   --->   --->   --->   --->
1      2      3      4      5      6
  <---   <---   <---   <---   <---
   ~1      ~2    ~3     ~4     ~5
*/

create procedure change_version
	@version int
as
begin
	declare @current_version int;
	set @current_version = (select top(1) VersionDB.current_version from VersionDB
		where VersionDB.id = 1);
	print 'Current version   = ' + cast(@current_version as varchar(20));
	print 'Changing to version ' + cast(@version as varchar(20));
	
	if (@version < 1 or @version > 6)
		print 'Error! Invalid version.';
	else if (@current_version < @version)
	begin -- upgrade
		while (@current_version < @version)
		begin
			if (@current_version = 1)					-- 1 -> 2
				exec modify_column_type;				-- 1.
			else if (@current_version = 2)				-- 2 -> 3
				exec add_default_constraint_location;	-- 2.
			else if (@current_version = 3)				-- 3 -> 4
				exec create_table_login_history;		-- 3.
			else if (@current_version = 4)				-- 4 -> 5
				exec add_column_activity_time;			-- 4.
			else if (@current_version = 5)				-- 5 -> 6
				exec add_fk_constraint_lh_username;		-- 5.
			set @current_version = @current_version + 1;
			update VersionDB set current_version = @current_version where id = 1;
		end
		print 'Now, version = ' + cast(@current_version as varchar(20)) + '.';
	end
	else if (@current_version > @version)
	begin -- downgrade
		while (@current_version > @version)
		begin
			if (@current_version = 6)					-- 6 -> 5
				exec drop_fk_constraint_lh_username;	-- ~5.
			else if (@current_version = 5)				-- 5 -> 4
				exec drop_column_activity_time;			-- ~4.
			else if (@current_version = 4)				-- 4 -> 3
				exec drop_table_login_history;			-- ~3.
			else if (@current_version = 3)				-- 3 -> 2
				exec remove_default_constraint_location;-- ~2.
			else if (@current_version = 2)				-- 2 -> 1
				exec modify_column_type_rev;			-- ~1
			set @current_version = @current_version - 1;
			update VersionDB set current_version = @current_version where id = 1;
		end
		print 'Now, version = ' + cast(@current_version as varchar(20)) + '.';
	end
	else -- if @current_version = @version
		print 'Already at version ' + cast(@current_version as varchar(20)) + '.';
end