create or replace function ufoffice.leaderboard_update() returns trigger
language plpgsql
    as $$
    begin
        if new.task_status = 2 
        then
            update ufoffice.leaderboard
            set user_rating = user_rating + new.user_rating
            where user_id = (
                select distinct
                    user_id
                from
                    ufoffice.user_tasks t
                where
                    t.task_id = new.task_id
                );
        end if;
    end $$

create trigger leaderboard
after update on ufoffice.task_status
for each row execute function ufoffice.leaderboard_update();
