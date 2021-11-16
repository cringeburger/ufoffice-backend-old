create schema chat;


create sequence chat.chat_num start 1;


-- информация о пользователях
create or replace view chat.users_info as
select
	us.user_id,
	cast(lower(us.username) as varchar(100)) username,
	us.user_role_id
from
	ufoffice.users us
join ufoffice.user_roles usr
	on usr.user_role_id = us.user_role_id;

-- история чата
create table chat.chat_hist (
	log_id bigserial primary key,
	log_dttm timestamp default now(),
	team_channel_id int default -1,
	user_from int,
	user_to int,
	message varchar(5000)
);

-- кАналы команды
create table chat.team_channels(
	team_channel_id serial primary key,
	team_channel_name varchar(100) default 'chat_no_'||nextval('chat.chat_num'),
	created_dttm timestamp default now()
);

-- участники
create table chat.team_channel_members(
	team_channel_member_id serial primary key,
	team_channel_id int,
	user_id int
);
