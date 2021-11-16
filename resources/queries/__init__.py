from resources.queries.skills import skills_info
from resources.queries.login import check_user_login
from resources.queries.registration_add_user import registration
from resources.queries.tasks import (
    get_user_tasks,
    task_crt,
    task_status_upd
)
from resources.queries.team_info import (
    team_list,
    get_team_name
)
from resources.queries.leaderboard import (
    get_leaderboard,
    get_leaderboard_place
)
from resources.queries.notes_info import (
    user_notes,
    create_note,
    delete_note,
    update_note
)
